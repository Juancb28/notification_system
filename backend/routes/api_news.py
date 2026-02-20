from fastapi import APIRouter
import httpx
from bs4 import BeautifulSoup
import re
import requests


router = APIRouter()



@router.get("/apple")
async def get_apple_news():
    async with httpx.AsyncClient() as client:
        response = httpx.get("https://www.apple.com/es/newsroom/")

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=False)

    direct_access = [h.get_text(strip=True) for h in soup.find_all("h3")]

    for t in direct_access:
        text = re.sub(re.escape(t), "", text)

    text = re.sub(r"\t", "", text)

    titles = [h.get_text(strip=True) for h in soup.find_all('h7')]

    return {
        "status_code": response.status_code,
        "length": len(response.text),
        "conten_length": response.headers.get("content-length"),
        "titles": titles,
        "content": text,
    }

@router.get('/news')
async def raw_data():
    response = requests.get('https://www.apple.com/es/newsroom/')
    
    return {response.content}