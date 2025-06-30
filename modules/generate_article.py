import pandas as pd
import openai
from docx import Document
import os

def generate_articles_from_excel(path):
    df = pd.read_excel(path)
    date_folder = "./output/" + pd.Timestamp.now().strftime('%Y-%m-%d')
    os.makedirs(date_folder, exist_ok=True)

    for _, row in df.iterrows():
        prompt = f"请将以下内容改写为适合公众号发布的中文资讯文章，包含标题、三段正文，总字数控制在500字以内：\n内容：{row['content']}"
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        article = response['choices'][0]['message']['content']
        doc = Document()
        doc.add_paragraph(article)
        doc.save(os.path.join(date_folder, f"{row['platform']}_{row['username'][:10]}.docx"))