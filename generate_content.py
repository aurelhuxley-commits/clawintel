#!/usr/bin/env python3
import requests
from datetime import datetime
import json

def fetch_news():
    """Fetch news from various sources"""
    # This is a placeholder - in reality we'd use web_search API
    # For demo purposes, we'll use placeholder data
    return [
        {
            "title": "AI Breakthrough: New Reasoning Models Released",
            "category": "AI",
            "date": datetime.now().strftime("%B %d, %Y"),
            "content": "Researchers at MIT have developed new AI models capable of explaining their reasoning process. This marks a significant step toward more transparent and trustworthy artificial intelligence systems.",
            "source": "MIT Technology Review",
            "image": "https://via.placeholder.com/800x400?text=AI+Research"
        },
        {
            "title": "Bitcoin ETF Approval Imminent",
            "category": "Fintech",
            "date": datetime.now().strftime("%B %d, %Y"),
            "content": "The SEC is expected to approve multiple Bitcoin ETF applications this week, potentially unlocking billions in institutional investment.",
            "source": "CoinDesk",
            "image": "https://via.placeholder.com/800x400?text=Bitcoin+ETF"
        },
        {
            "title": "NATO Expands Eastern Europe Presence",
            "category": "Geopolitics",
            "date": datetime.now().strftime("%B %d, %Y"),
            "content": "In response to ongoing tensions, NATO has announced plans to increase its military presence in Eastern European member states.",
            "source": "Reuters",
            "image": "https://via.placeholder.com/800x400?text=NATO+Meeting"
        }
    ]

def generate_html(posts):
    """Generate HTML content from posts"""
    html_posts = []
    for post in posts:
        html = f'''
        <article class="post">
            <h2 class="post-title">{post["title"]}</h2>
            <div class="post-meta">
                <span class="category">{post["category"]}</span>
                <span>{post["date"]}</span>
            </div>
            <img src="{post["image"]}" alt="{post["title"]}" class="post-image">
            <div class="post-content">
                {post["content"]}
            </div>
            <div class="source">Source: {post["source"]}</div>
        </article>
        '''
        html_posts.append(html)
    
    return "".join(html_posts)

def update_website():
    """Update the website with new content"""
    posts = fetch_news()
    html_content = generate_html(posts)
    
    # Read the template
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Replace the posts section
    new_content = content.replace('<div id="posts"></div>', f'<div id="posts">{html_content}</div>')
    
    # Write back
    with open('index.html', 'w') as f:
        f.write(new_content)
    
    print("Website updated successfully!")
    print(f"Generated {len(posts)} posts")

if __name__ == "__main__":
    update_website()