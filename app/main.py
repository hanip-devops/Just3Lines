from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.core.config import get_settings
import os

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="뉴스 기사를 3줄로 요약해주는 API",
    version=settings.APP_VERSION
)

#정적 파일 설정 (테스트 환경이 아닐 때만)
if not os.getenv("TESTING"):
   app.mount("/static", StaticFiles(directory="static"), name="static")

# 라우터 등록
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 