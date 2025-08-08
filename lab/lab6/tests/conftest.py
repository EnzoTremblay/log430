import sys
from pathlib import Path

# Add lab6/src to sys.path for imports like `from saga.orchestrator import OrderSaga`
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
