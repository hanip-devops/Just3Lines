from fastapi.testclient import TestClient
from app import app
import pytest
from unittest.mock import patch

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

@patch('app.client.chat.completions.create')
def test_summarize_korean(mock_create):
    # 모의 응답 설정
    mock_create.return_value.choices = [
        type('obj', (object,), {
            'message': type('obj', (object,), {
                'content': "1. 애플이 5월 7일 'Let Loose' 행사에서 새로운 iPad Pro와 iPad Air를 공개할 예정\n2. M3 칩을 탑재한 iPad Pro와 새로운 Apple Pencil이 공개될 것으로 알려짐\n3. iPadOS 17.5와 함께 새로운 기능들이 소개될 것으로 전망"
            })
        })
    ]
    
    response = client.post(
        "/summarize",
        json={
            "content": "애플이 오는 5월 7일 'Let Loose' 행사를 통해 새로운 iPad Pro와 iPad Air를 공개할 것으로 예상됩니다. 이번 행사에서는 M3 칩을 탑재한 iPad Pro와 새로운 Apple Pencil이 공개될 것으로 알려졌습니다. 또한 iPadOS 17.5와 함께 새로운 기능들이 소개될 것으로 전망됩니다. 애플은 이번 행사를 통해 태블릿 시장에서의 경쟁력을 더욱 강화할 것으로 보입니다.",
            "language": "korean"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert len(data["summary"]) == 3
    
    # API 호출 확인
    mock_create.assert_called_once()

@patch('app.client.chat.completions.create')
def test_summarize_english(mock_create):
    # 모의 응답 설정
    mock_create.return_value.choices = [
        type('obj', (object,), {
            'message': type('obj', (object,), {
                'content': "1. Apple to unveil new iPad Pro and iPad Air at 'Let Loose' event on May 7th\n2. Event will showcase iPad Pro with M3 chip and new Apple Pencil\n3. New features expected alongside iPadOS 17.5"
            })
        })
    ]
    
    response = client.post(
        "/summarize",
        json={
            "content": "Apple is expected to unveil new iPad Pro and iPad Air models at its 'Let Loose' event on May 7th. The event will likely showcase iPad Pro models powered by the M3 chip and a new Apple Pencil. Additionally, new features are expected to be introduced alongside iPadOS 17.5. Apple aims to strengthen its position in the tablet market through this event.",
            "language": "english"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert len(data["summary"]) == 3
    
    # API 호출 확인
    mock_create.assert_called_once() 