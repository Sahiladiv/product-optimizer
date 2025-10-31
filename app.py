from flask import Flask
from routes.home import home_bp
# from routes.category import category_bp
from routes.product import product_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
# app.register_blueprint(category_bp)
app.register_blueprint(product_bp)

@app.route('/sitemap.xml')
def sitemap():
    from utils.sitemap import generate_sitemap
    return generate_sitemap()

if __name__ == '__main__':
    app.run(debug=True)
