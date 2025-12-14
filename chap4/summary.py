from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(file_path: str):
    client = OpenAI(api_key=api_key)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()[:50000]  # Truncate to first 50k characters to avoid RateLimitError
    system_prompt = f'''너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 카메라 조작 계통 관련 내용 중 주요 내용을 요약하라.
    작성해야 하는 포맷은 다음과 같다.
    
    # 제목
    ## 조작 계통의 역할
    ## 주요 기능
    ## 작동 방법

    ==================== 이하 텍스트 ====================
    {text}
    '''
    print(system_prompt)
    print('===========================================')
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": system_prompt}
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    file_path = "./chap4/output/sony-parsing_preprocessed.txt"
    summary = summarize_text(file_path)
    print(summary)

    with open("./chap4/output/sony-parsing_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)