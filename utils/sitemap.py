from flask import Response
from datetime import datetime

def generate_sitemap():
    today = datetime.utcnow().strftime('%Y-%m-%d')
    base_url = "https://product-optimizer.onrender.com/"

    urls = [
        {"loc": "/", "priority": "1.0"},
        {"loc": "/product/B0D1KJ6PKJ", "priority": "0.8"},
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for u in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{base_url}{u['loc']}</loc>")
        xml.append(f"    <lastmod>{today}</lastmod>")
        xml.append("    <changefreq>weekly</changefreq>")
        xml.append(f"    <priority>{u['priority']}</priority>")
        xml.append("  </url>")

    xml.append('</urlset>')
    return Response("\n".join(xml), mimetype='application/xml')
