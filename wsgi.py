"""App entry point."""
from main import create_app

app = create_app()
#test

if __name__ == "__main__":
    app.run(host='localhost', port=5000, threaded=False)
