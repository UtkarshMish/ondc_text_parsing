from os import environ

from dotenv import load_dotenv

from app import create_app

load_dotenv(".env")


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(
        host=environ.get("HOST") or "127.0.0.1",
        port=environ.get("PORT") or 8000,
        debug=environ.get("DEBUG") or False,
    )
