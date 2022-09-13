from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<html lang="en">
    <head>
<script src="https://unpkg.com/htmx.org@1.8.0" integrity="sha384-cZuAZ+ZbwkNRnrKi05G/fjBX+azI9DNOkNYysZ0I/X5ZFgsmMiBXgDZof30F5ofc" crossorigin="anonymous"></script>
    </head>

    <body hx-boost="true">
      <p>Hello, World!</p><button hx-get="/wrapper_test">test oob</button>
       <ul class="messages" id="messages"  hx-swap-oob="beforeend:#messages">
    </body>
    </html>
    """


@app.route("/wrapper_test")
def wrapper_test():
    return """
<p>foo</p>
<li hx-swap-oob="beforeend:#messages"><div>message</message></li>
"""
