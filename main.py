if __name__ == "__main__":
    from utils.request_handler import app
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)