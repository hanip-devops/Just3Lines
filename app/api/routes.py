from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from app.services.openai_service import summarize_text

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Article(BaseModel):
    content: str
    language: Optional[str] = "korean"

class Summary(BaseModel):
    summary: list[str]

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.post("/summarize", response_model=Summary)
async def summarize_article(article: Article):
    try:
        summary_lines = summarize_text(article.content, article.language)
        return Summary(summary=summary_lines)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 