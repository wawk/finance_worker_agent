import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
platform_core_root = Path(__file__).resolve().parents[2] / "platform_core"

sys.path.insert(0, str(project_root))
sys.path.insert(0, str(platform_core_root))
