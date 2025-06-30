# PRContentBot

自动抓取波多黎各新闻 & 社交平台内容，GPT 优选并生成微信公众号文章。

## 快速体验

```bash
git clone <repo>
cd PRContentBot
pip install -r requirements.txt
export OPENAI_API_KEY=sk-xxx
python main_fetch_social.py   # 获取社媒并筛选 30 条
python main_fetch_news.py     # 获取新闻并筛选 30 条
```

完成后在 `output/<date>/` 目录将生成 `social_top30.xlsx` 和 `news_top30.xlsx`。  
手动挑选→保存到 `input/articles_selected.xlsx` 然后

```bash
python main_generate_from_excel.py   # 逐条生成 .docx
python main_generate_hotdigest.py    # 生成热帖合辑
```

## 主要脚本
- `main_fetch_social.py`
- `main_fetch_news.py`
- `main_generate_from_excel.py`
- `main_generate_hotdigest.py`

## 部署到 Replit
- Import from GitHub
- 在 Secrets 中添加 `OPENAI_API_KEY`
- 修改 `.replit` 指定启动脚本