import requests
from bs4 import BeautifulSoup
import re

files = {
        "maha.txt" : "https://en.wikipedia.org/wiki/Maharashtra",
        "friends.txt" : "https://en.wikipedia.org/wiki/Friendship",
        "2e.txt" : "https://en.wikipedia.org/wiki/Twice_exceptional"
        }


def extract_text(url:str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9"
    }

    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content , 'html.parser')

        citations = soup.find_all('sup', class_='reference')
        for citation in citations:
            citation.decompose()

        paragraphs = soup.find_all('p')
        if not paragraphs:
            raise ValueError("No Paragraphs found")
        
        para = []
        for p in paragraphs :
            para.append(p.get_text().strip())

        return ' '.join(para)

    except Exception as e:
        print(f"Something went wrong : {e}")
        return "NULL"

if __name__ == '__main__':

    for file,link in files.items():
        
        text = extract_text(link)

        with open(file,'w', encoding='utf-8') as f:
            f.write(text)
            f.close()
        print(f"Files Saved Successfully : {file}")

    print("complete!!!")
