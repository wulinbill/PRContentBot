# PRContentBot

Python 项目：自动抓取波多黎各新闻、社交媒体内容，通过 GPT 精选并生成微信公众号文章。

## 主要脚本
| 文件 | 功能 |
|------|------|
| **launcher.py** | 菜单入口，选择不同任务 |
| main_fetch_social.py | 抓取 Twitter+Reddit，并 GPT 精选 30 条，导出 Excel |
| main_fetch_news.py | 抓取新闻 RSS，并 GPT 精选 30 条，导出 Excel |
| main_generate_from_excel.py | 读取手动挑选的 Excel，逐条生成公众号文章 `.docx` |
| main_generate_hotdigest.py | 将多条热帖整合生成 1 篇热帖合辑文章 |

## 快速开始
```bash
git clone <repo>
cd PRContentBot
pip install -r requirements.txt
export OPENAI_API_KEY=sk-xxxx

# 启动菜单
python3 launcher.py
```

## Replit 部署
1. Import from GitHub  
2. 在 *Secrets* 添加 `OPENAI_API_KEY`  
3. `.replit` 已设置 `run = "python3 launcher.py"`，点击 ▶️ 选择任务即可。

## 依赖
- openai
- pandas
- python-docx
- snscrape
- feedparser