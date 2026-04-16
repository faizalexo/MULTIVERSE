import requests
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.core.cache import cache

# 🔥 HOME / INDEX

def index(request):

    queries = [
        "war",
        "cyber attack",
        "geopolitics",
        "international conflict",
        "military",
        "security breach",
        "india news",
        "global crisis"
    ]

    query = random.choice(queries)

    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=9&apiKey=c49f1ffc9cae4ef6bffb1f05405f798a"
    
    
    """apikey-5ac64b4163c04d26b79cceb5f1416e70"""

    # 🔥 CACHE CHECK
    articles = cache.get('news_cache')

    if not articles:
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            print("API RESPONSE:", data)

            if data.get("status") == "ok":
                articles = data.get("articles", [])[:6]
                cache.set('news_cache', articles, 600)

            else:
               articles = [
    {
        "title": "🌍 Global Conflict Rising",
        "description": "Tensions increasing worldwide",
        "urlToImage": "https://source.unsplash.com/400x300/?war",
        "url": "#"
    },
    {
        "title": "💻 Cyber Attack Alert",
        "description": "Major global cyber threats detected",
        "urlToImage": "https://source.unsplash.com/400x300/?cyber",
        "url": "#"
    },
    {
        "title": "⚠ Security Crisis",
        "description": "Multiple regions on high alert",
        "urlToImage": "https://source.unsplash.com/400x300/?security",
        "url": "#"
    }
]

        except:
            articles = [
                {
                    "title": "⚠ Server Error",
                    "description": "Unable to load news",
                    "urlToImage": "https://source.unsplash.com/400x300/?error",
                    "url": "#"
                }
            ]

    # 🔥 CONFLICTS
    conflicts = [
        {"country": "Ukraine", "reason": "Russia invasion ongoing"},
        {"country": "Israel", "reason": "Gaza conflict escalation"},
        {"country": "Sudan", "reason": "Civil war between army factions"},
        {"country": "Myanmar", "reason": "Military vs resistance groups"},
        {"country": "Yemen", "reason": "Proxy war & humanitarian crisis"},
        {"country": "Ethiopia", "reason": "Internal ethnic conflict"},
        {"country": "Pakistan", "reason": "Border tension & terrorism"},
        {"country": "Syria", "reason": "Ongoing civil war"},
        {"country": "DR Congo", "reason": "Eastern rebel conflict"}
    ]

    return render(request, 'worldmonitor/index.html', {
    'articles': articles,
    'conflicts': conflicts
})
    


def cyberattacks(request):
    attacks = [
        {"country": "USA", "type": "DDoS", "severity": "High"},
        {"country": "India", "type": "Phishing", "severity": "Medium"},
        {"country": "Germany", "type": "Malware", "severity": "Low"},
        
    ]
    return render(request, 'worldmonitor/cyberattacks', {'attacks': attacks})



def geopolitics(request):
    return render(request, 'worldmonitor/geopolitics')
        
        
        
        
        
        
        
        


def country_news(request, country):

    url = f"https://newsapi.org/v2/everything?q={country}&apiKey=c49f1ffc9cae4ef6bffb1f05405f798a"

    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])[:5]
    except:
        articles = []

    return JsonResponse({"articles": articles})  



def get_war_countries():
    url = "https://newsapi.org/v2/everything?q=war OR conflict&apiKey=YOUR_KEY"
    data = requests.get(url).json()

    countries = []

    for article in data.get("articles", []):
        title = article["title"]

        if "Russia" in title:
            countries.append("Russia")
        if "Ukraine" in title:
            countries.append("Ukraine")

    return list(set(countries))
        
        





