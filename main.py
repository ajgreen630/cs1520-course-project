from flask import Flask, Response, redirect

# Execution:
# 1. gcloud config set project [PROJECT_ID] (for each terminal)
# 2. gcloud app deploy
# 3. dev_appserver.py app.yaml

app = Flask(__name__)

@app.route('/')
def root():
    # Match url in app.yaml handler; ensure app.yaml points to existing static directory.
    return redirect("/static/index/index.html", code=302)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)