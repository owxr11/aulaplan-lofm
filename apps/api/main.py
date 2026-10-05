from firebase_functions import https_fn
from firebase_admin import initialize_app, get_app
from src.http.app import create_app

try: 
    get_app()
except: 
    initialize_app()


flask_app = create_app()

@https_fn.on_request(
    region="us-central1",
    cors = True
)


def api(req: https_fn.Request) -> https_fn.Response: 
    with flask_app.request_context(req.environ):
        return flask_app.full_dispatch_request()
    