from modules.log_config import setup_logger
logger = setup_logger('gen_digest')
import pandas as pd
import openai
from docx import Document
import os

def generate_hot_post_digest(path):
    df = pd.read_excel(path)
    content_blocks = [f"{i+1}. {row['content']}" for i, row in df.iterrows()]
    prompt = "你是资深新闻整合编辑，请将以下社交平台热门帖文整合成一篇适合发布在华人公众号的中文文章，包含一个吸引人的标题和正文三段，字数控制在500字内：\n\n" + "\n".join(content_blocks)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    article = response['choices'][0]['message']['content']
    date_folder = "./output/" + pd.Timestamp.now().strftime('%Y-%m-%d')
    os.makedirs(date_folder, exist_ok=True)
    doc = Document()
    doc.add_paragraph(article)
    doc.save(os.path.join(date_folder, f"🔥热帖合辑.docx"))