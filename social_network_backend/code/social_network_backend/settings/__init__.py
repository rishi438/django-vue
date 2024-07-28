import os
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / "media"

ENVAR_PREFIX_SETTINGS = "CORESETTINGS_"
LOCAL_SETTINGS_PATH = os.getenv(f"{ENVAR_PREFIX_SETTINGS}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = "local/settings.dev.py"

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

include("base.py", "custom.py", optional(LOCAL_SETTINGS_PATH), "env_vars.py")
