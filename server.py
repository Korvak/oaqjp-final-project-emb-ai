from flask import Flask, render_template, request

app = Flask("My app")

if __name__ == "__main__":
    #we run the server on the specified host and port
    app.run(host="0.0.0.0", port=5000)