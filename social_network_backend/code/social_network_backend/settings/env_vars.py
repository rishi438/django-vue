from code.core.utils.collections import deep_update
from code.core.utils.settings import get_settings_from_environment

deep_update(globals(), get_settings_from_environment(ENVAR_PREFIX_SETTINGS))  # type: ignore
