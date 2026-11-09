import sys
from pathlib import Path

platform_core_root = Path(__file__).resolve().parents[2] / "platform_core"

sys.path.insert(0, str(platform_core_root))
