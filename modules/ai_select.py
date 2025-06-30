import openai
import os

def select_top_posts(posts, top_k=30):
    content_blocks = [f"{i+1}. [{p['platform']}] {p['content'][:200]}" for i, p in enumerate(posts)]
    full_prompt = "请从以下社交平台内容中选出最值得发布在波多黎各华人资讯公众号的30条，只返回编号列表：\n\n" + "\n".join(content_blocks)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是资深公众号编辑"},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2
    )
    selected_indices = [int(s.strip()) - 1 for s in response['choices'][0]['message']['content'].split(",") if s.strip().isdigit()]
    return [posts[i] for i in selected_indices if i < len(posts)]