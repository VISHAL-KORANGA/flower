from flask import Flask, send_from_directory

app = Flask(__name__)


# Route to serve the HTML file
@app.route("/")
def serve_html():
    return send_from_directory(
        ".", "flower.html"
    )  # Ensure "flower.html" is in the same folder as "flower.py"


if __name__ == "__main__":
    app.run(debug=True)
