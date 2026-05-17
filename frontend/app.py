from flask import Flask, render_template
import os

# Create an un-breakable relative directory mapping path
current_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__, 
    template_folder=os.path.join(current_dir, "templates"),
    static_folder=os.path.join(current_dir, "static")
)

# Helper function to dynamically grab the Gateway URL or fallback for local testing
def get_gateway_url():
    return os.environ.get("GATEWAY_URL", "http://localhost:5000")

# ----------------- ROUTES -----------------

@app.route("/")
def home():
    return render_template("index.html", gateway_url=get_gateway_url())

@app.route("/login")
def login_page():
    return render_template("login.html", gateway_url=get_gateway_url())

@app.route("/register")
def register_page():
    return render_template("register.html", gateway_url=get_gateway_url())

@app.route("/products")
def products():
    return render_template("products.html", gateway_url=get_gateway_url())

@app.route("/orders")
def orders():
    return render_template("orders.html", gateway_url=get_gateway_url())

@app.route("/payment/<int:order_id>")
def payment(order_id):
    return render_template("payment.html", order_id=order_id, gateway_url=get_gateway_url())

@app.route("/checkout")
def checkout():
    return render_template("checkout.html", gateway_url=get_gateway_url())

@app.route("/success")
def success():
    return render_template("success.html", gateway_url=get_gateway_url())

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
