from openai import OpenAI
from app.core.config import get_settings

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_text(content: str, language: str = "korean") -> list[str]:
    """텍스트를 3줄로 요약합니다."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a professional news article summarizer. Summarize the given article in exactly 3 lines in {language}. Make each line informative and concise."},
            {"role": "user", "content": content}
        ],
        temperature=0.7,
        max_tokens=300
    )
    
    summary_text = response.choices[0].message.content.strip()
    return [line.strip() for line in summary_text.split('\n') if line.strip()][:3] 