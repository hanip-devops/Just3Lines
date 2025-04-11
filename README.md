# Just3Lines

긴 텍스트를 3줄로 요약해주는 웹 서비스입니다.

## 기능

- 텍스트를 3줄로 요약
- 한국어/영어 지원
- 웹 인터페이스 제공
- OpenAI GPT-3.5 Turbo 기반 요약

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/hanip-devops/Just3Lines.git
cd Just3Lines
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 환경 변수 설정
`.env` 파일을 생성하고 OpenAI API 키를 설정합니다:
```
OPENAI_API_KEY=your_api_key_here
```

## 실행 방법

```bash
python app.py
```

웹 브라우저에서 http://localhost:8000 으로 접속하여 서비스를 이용할 수 있습니다.

## 기술 스택

- FastAPI
- OpenAI GPT-3.5 Turbo
- Tailwind CSS
- Jinja2 Templates

## 라이선스

MIT License 