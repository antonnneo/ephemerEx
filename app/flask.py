from flask import Flask
from modules import execute, generate_text
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/new', methods=['POST'])
def new_note():
    execute(f"""
    INSERT INTO messages
            ("content")
    VALUES
            ('{generate_text(10_000)}');
    """)
    return {"message": "Text saved successfully"}


if __name__ == '__main__':
    app.run(debug=False, port=5000, host="0.0.0.0")