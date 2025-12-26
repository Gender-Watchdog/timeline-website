import os
from bs4 import BeautifulSoup
import urllib.parse

SITE_DIR = "_site"

def check_links_and_content():
    errors = []
    checked_files = 0
    
    for root, dirs, files in os.walk(SITE_DIR):
        for file in files:
            if file.endswith(".html"):
                checked_files += 1
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, SITE_DIR)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        soup = BeautifulSoup(content, 'html.parser')
                        
                        # Content Checks
                        if "timeline" in file: # Only check timeline pages for specific structure
                            h1 = soup.find('h1')
                            if not h1 or not h1.get_text(strip=True):
                                errors.append(f"[{rel_path}] Missing or empty <h1>")
                            
                            alert = soup.find(class_='alert')
                            if not alert or not alert.get_text(strip=True):
                                errors.append(f"[{rel_path}] Missing or empty alert box")

                        # Link Checks
                        for a in soup.find_all('a', href=True):
                            href = a['href']
                            if href.startswith(('http://', 'https://', 'mailto:', '#')):
                                continue
                            
                            # Resolve path
                            if href.startswith('/'):
                                target_path = os.path.join(SITE_DIR, href.lstrip('/'))
                            else:
                                target_path = os.path.join(os.path.dirname(file_path), href)
                            
                            # Remove anchor
                            if '#' in target_path:
                                target_path = target_path.split('#')[0]
                                
                            # Check existence
                            if not os.path.exists(target_path) and not os.path.exists(target_path + "/index.html"):
                                # Try decoding URL encoding
                                decoded_path = urllib.parse.unquote(target_path)
                                if not os.path.exists(decoded_path):
                                     errors.append(f"[{rel_path}] Broken link: {href} -> {target_path}")

                except Exception as e:
                    errors.append(f"[{rel_path}] Error processing file: {str(e)}")

    print(f"Checked {checked_files} files.")
    if errors:
        print("Found errors:")
        for error in errors:
            print(error)
    else:
        print("No errors found!")

if __name__ == "__main__":
    check_links_and_content()
