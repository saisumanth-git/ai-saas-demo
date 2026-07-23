from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI SaaS Demo Backend</h1>
    <h3>Application is Running Successfully!</h3>
    <p>Welcome to the AI SaaS Demo deployed using AWS Elastic Beanstalk.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
