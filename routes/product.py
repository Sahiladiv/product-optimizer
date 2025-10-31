from flask import Blueprint, render_template, jsonify
import json

product_bp = Blueprint('product', __name__)

@product_bp.route('/product/<asin>')
def product_page(asin):
    with open('data/scrapped_data.json') as f:
        data = json.load(f)
    if data['asin'] != asin:
        return "Product not found", 404
    return render_template('product.html', product=data)
