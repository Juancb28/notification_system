from fastapi import APIRouter
import httpx
from bs4 import BeautifulSoup
import re
from tools import format_text
from schemas import pages



router = APIRouter()

@router.get('/news')
async def raw_data():
    async with httpx.AsyncClient() as client:
        for page in pages.link_pages:
            response = httpx.get(page)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.get_text(separator=' ', strip=False)
    
    text = format_text.format_text_tabulator(text)
    
    text = format_text.format_lines_jump(text)
    
    
    return {text}