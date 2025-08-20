from .main import app  # if main.py exposes app
try:
	from ..api import app as legacy_app  # fallback if tests import from api (repo root style)
except Exception:
	legacy_app = None
