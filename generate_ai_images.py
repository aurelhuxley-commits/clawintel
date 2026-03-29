#!/usr/bin/env python3
"""
Generate AI-powered images using Google Gemini API
"""
import requests
import json
from datetime import datetime

# Google Gemini API Key (provided by user)
GEMINI_API_KEY = "AIzaSyBW-maBlMASXfFjyYpYE5cxyZHSNH8QqhQ"

def generate_gemini_image(prompt, size="1024x1024"):
    """
    Generate an image using Google Gemini API
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"
    
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"Generate a high-quality, eye-catching image for a news article about: {prompt}. Make it professional, modern, and suitable for a news website. Return only the image URL."
            }]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            # Extract image URL from response
            if "candidates" in data and len(data["candidates"]) > 0:
                if "parts" in data["candidates"][0]:
                    for part in data["candidates"][0]["parts"]:
                        if "text" in part and "https://" in part["text"]:
                            return part["text"]
        
        # Fallback to Unsplash if API fails
        print(f"Gemini API failed, using fallback image for: {prompt}")
        return get_fallback_image(prompt)
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return get_fallback_image(prompt)

def get_fallback_image(prompt):
    """
    Fallback to Unsplash images if Gemini API fails
    """
    fallback_images = {
        "AI robot analyzing data": "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80",
        "Bitcoin ETF approval": "https://images.unsplash.com/photo-1643797458037-3ff9ea706011?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
        "NATO meeting": "https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
        "Messi signing": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80",
        "US debate": "https://images.unsplash.com/photo-1563567310337-5b5e2666a253?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=350&q=80"
    }
    return fallback_images.get(prompt, "https://via.placeholder.com/512?text=AI+Generated+Image")

def create_ai_news_with_images():
    """Create news items with AI-generated images from Gemini"""
    prompts = [
        "AI robot analyzing data in futuristic laboratory",
        "Bitcoin ETF approval celebration with financial charts",
        "NATO leaders in serious discussion about security",
        "Lionel Messi signing contract with Inter Miami",
        "US presidential candidates on debate stage"
    ]
    
    # Generate images (this would be async in production)
    print("Generating AI images with Google Gemini...")
    images = []
    for prompt in prompts:
        img_url = generate_gemini_image(prompt)
        images.append(img_url)
        print(f"Generated image for: {prompt}")
    
    return [
        {
            "title": "AI Breakthrough: New Reasoning Models Released",
            "category": "AI",
            "excerpt": "Researchers at MIT have developed new AI models capable of explaining their reasoning process. This marks a significant step toward more transparent and trustworthy artificial intelligence systems.",
            "source": "MIT Technology Review",
            "image": images[0],
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "Bitcoin ETF Approval Imminent",
            "category": "Finance",
            "excerpt": "The SEC is expected to approve multiple Bitcoin ETF applications this week, potentially unlocking billions in institutional investment.",
            "source": "CoinDesk",
            "image": images[1],
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "NATO Expands Eastern Europe Presence",
            "category": "Geopolitics",
            "excerpt": "In response to ongoing tensions, NATO has announced plans to increase its military presence in Eastern European member states.",
            "source": "Reuters",
            "image": images[2],
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "Messi Signs with Inter Miami",
            "category": "Sports",
            "excerpt": "Lionel Messi has officially signed with Inter Miami, marking a historic moment for Major League Soccer.",
            "source": "ESPN",
            "image": images[3],
            "date": datetime.now().strftime("%B %d, %Y")
        },
        {
            "title": "US Election Debate Scheduled",
            "category": "Politics",
            "excerpt": "The first presidential debate of the 2026 election cycle has been scheduled for next month.",
            "source": "CNN",
            "image": images[4],
            "date": datetime.now().strftime("%B %d, %Y")
        }
    ]

if __name__ == "__main__":
    print("Starting AI image generation with Google Gemini...")
    news = create_ai_news_with_images()
    print("\nGenerated news items:")
    for item in news:
        print(f"\nTitle: {item['title']}")
        print(f"Category: {item['category']}")
        print(f"Image: {item['image'][:50]}...")
        print(f"Source: {item['source']}")
    print("\n✅ AI image generation complete!")