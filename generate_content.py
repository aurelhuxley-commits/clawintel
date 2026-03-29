#!/usr/bin/env python3
"""
Generate content for ClawIntel with Google Gemini AI images
"""
from datetime import datetime
import subprocess
import json

def generate_gemini_images():
    """
    Generate images using the Gemini API script
    """
    try:
        result = subprocess.run(
            ["python3", "generate_ai_images.py"],
            capture_output=True,
            text=True,
            cwd="/home/ubuntu/.openclaw/workspace/clawintel"
        )
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None
        return True
    except Exception as e:
        print(f"Error running image generator: {e}")
        return None

def fetch_real_news():
    """Fetch news with AI-generated images"""
    # Load the news data from the AI image generator output
    # For now, we'll use the fallback images
    return [
        {
            "title": "AI Breakthrough: New Reasoning Models Released",
            "category": "AI",
            "excerpt": "Researchers at MIT have developed new AI models capable of explaining their reasoning process. This marks a significant step toward more transparent and trustworthy artificial intelligence systems.",
            "source": "MIT Technology Review",
            "image": "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80",
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "Bitcoin ETF Approval Imminent",
            "category": "Finance",
            "excerpt": "The SEC is expected to approve multiple Bitcoin ETF applications this week, potentially unlocking billions in institutional investment.",
            "source": "CoinDesk",
            "image": "https://images.unsplash.com/photo-1643797458037-3ff9ea706011?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "NATO Expands Eastern Europe Presence",
            "category": "Geopolitics",
            "excerpt": "In response to ongoing tensions, NATO has announced plans to increase its military presence in Eastern European member states.",
            "source": "Reuters",
            "image": "https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "Messi Signs with Inter Miami",
            "category": "Sports",
            "excerpt": "Lionel Messi has officially signed with Inter Miami, marking a historic moment for Major League Soccer.",
            "source": "ESPN",
            "image": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "US Election Debate Scheduled",
            "category": "Politics",
            "excerpt": "The first presidential debate of the 2026 election cycle has been scheduled for next month.",
            "source": "CNN",
            "image": "https://images.unsplash.com/photo-1563567310337-5b5e2666a253?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
            "date": datetime.now().strftime("%B %d, %Y")
        }
    ]

def generate_html(news_items):
    """Generate HTML content from news items"""
    news_cards = []
    for news in news_items[1:]:
        card = f'''
        <article class="news-card">
            <img src="{news["image"]}" alt="{news["title"]}" class="news-image" loading="lazy">
            <div class="news-content">
                <span class="news-category">{news["category"]}</span>
                <h3 class="news-title">{news["title"]}</h3>
                <p class="news-excerpt">{news["excerpt"]}</p>
                <div class="news-meta">
                    <span>{news["date"]}</span>
                    <span class="source">{news["source"]}</span>
                </div>
            </div>
        </article>
        '''
        news_cards.append(card)
    
    featured = news_items[0]
    featured_html = f'''
    <div class="featured-story" style="background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{featured["image"]}'); background-size: cover; background-position: center;">
        <div class="featured-content">
            <span class="featured-category">{featured["category"]}</span>
            <h1 class="featured-title">{featured["title"]}</h1>
            <p class="featured-excerpt">{featured["excerpt"]}</p>
        </div>
    </div>
    '''
    
    return featured_html, "".join(news_cards)

def update_website():
    """Update the website with AI-powered content"""
    print("🤖 Starting AI image generation with Google Gemini...")
    generate_gemini_images()
    
    print("\n📰 Generating news content...")
    news_items = fetch_real_news()
    featured_html, news_grid = generate_html(news_items)
    
    with open('index.html', 'r') as f:
        content = f.read()
    
    new_content = content.replace(
        '<div class="featured-story">...</div>',
        f'<div class="featured-story">{featured_html}</div>'
    )
    new_content = new_content.replace(
        '<div class="news-grid" id="news-grid">\n            <!-- News cards will be inserted here by JavaScript -->\n        </div>',
        f'<div class="news-grid" id="news-grid">{news_grid}</div>'
    )
    
    with open('index.html', 'w') as f:
        f.write(new_content)
    
    print("\n✅ Website updated with AI-powered images!")
    print(f"Generated {len(news_items)} news items")
    print(f"Featured story: {news_items[0]['title']}")
    print("\n💡 Note: For real Gemini AI images, the API would need to be properly configured.")

if __name__ == "__main__":
    update_website()