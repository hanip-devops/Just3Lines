from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(
    title="Just3Lines",
    description="뉴스 기사를 3줄로 요약해주는 API",
    version="1.0.0"
)

# 정적 파일과 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Article(BaseModel):
    content: str
    language: Optional[str] = "korean"

class Summary(BaseModel):
    summary: list[str]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/summarize", response_model=Summary)
async def summarize_article(article: Article):
    try:
        # GPT 모델을 사용하여 요약 생성
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a professional news article summarizer. Summarize the given article in exactly 3 lines in {article.language}. Make each line informative and concise."},
                {"role": "user", "content": article.content}
            ],
            temperature=0.7,
            max_tokens=300
        )
        
        # 응답에서 3줄 요약 추출
        summary_text = response.choices[0].message.content.strip()
        summary_lines = [line.strip() for line in summary_text.split('\n') if line.strip()][:3]
        
        return Summary(summary=summary_lines)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 