FROM python:3.9-slim

WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# 포트 설정
EXPOSE 8000

# 환경 변수 설정 (기본값)
ENV OPENAI_API_KEY=""

# 서버 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]