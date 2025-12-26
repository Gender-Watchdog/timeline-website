import os
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import concurrent.futures
import time

SITE_DIR = "_site"
TIMEOUT = 10  # seconds
USER_AGENT = "Mozilla/5.0 (compatible; GenderWatchdogBot/1.0; +http://genderwatchdog.org)"

def get_external_links():
    """
    Walks through the _site directory and collects all external links.
    Returns a dictionary mapping URL -> list of files where it appears.
    """
    links_map = {}
    
    print(f"Scanning {SITE_DIR} for external links...")
    
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, SITE_DIR)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f.read(), 'html.parser')
                        
                        for a in soup.find_all('a', href=True):
                            href = a['href']
                            if href.startswith(('http://', 'https://')):
                                if href not in links_map:
                                    links_map[href] = []
                                links_map[href].append(rel_path)
                                
                        # Also check data-link attributes in timeline events
                        for div in soup.find_all('div', attrs={'data-link': True}):
                            link = div['data-link']
                            if link.startswith(('http://', 'https://')):
                                if link not in links_map:
                                    links_map[link] = []
                                links_map[link].append(rel_path)
                                
                except Exception as e:
                    print(f"Error reading {rel_path}: {e}")
                    
    return links_map

def check_url(url):
    """
    Checks if a URL is accessible.
    Returns (url, status, error_message)
    """
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': USER_AGENT}
    )
    
    try:
        # Try HEAD request first to save bandwidth
        req.method = 'HEAD'
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            return url, response.status, None
    except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
        # If HEAD fails (some servers don't support it), try GET
        try:
            req.method = 'GET'
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                return url, response.status, None
        except urllib.error.HTTPError as e:
            return url, e.code, str(e)
        except urllib.error.URLError as e:
            return url, 0, str(e.reason)
        except Exception as e:
            return url, 0, str(e)

def main():
    links_map = get_external_links()
    unique_urls = list(links_map.keys())
    
    print(f"Found {len(unique_urls)} unique external links.")
    print("Checking links (this may take a while)...")
    
    broken_links = []
    
    # Use a thread pool to check links in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in unique_urls}
        
        completed = 0
        for future in concurrent.futures.as_completed(future_to_url):
            url, status, error = future.result()
            completed += 1
            
            if completed % 10 == 0:
                print(f"Progress: {completed}/{len(unique_urls)}")
            
            if error or (status >= 400):
                print(f"❌ BROKEN: {url} (Status: {status}, Error: {error})")
                broken_links.append((url, status, error))
            else:
                # Optional: Print success for verbose mode
                # print(f"✅ OK: {url}")
                pass

    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    if broken_links:
        print(f"Found {len(broken_links)} broken links:")
        for url, status, error in broken_links:
            print(f"\n🔗 URL: {url}")
            print(f"   Status: {status} | Error: {error}")
            print(f"   Found in:")
            for source_file in links_map[url]:
                print(f"   - {source_file}")
        exit(1)
    else:
        print("✅ All external links are working!")
        exit(0)

if __name__ == "__main__":
    main()
