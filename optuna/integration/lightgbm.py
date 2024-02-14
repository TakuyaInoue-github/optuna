import os
import sys
from types import ModuleType
from typing import Any

import optuna_integration.lightgbm as lgb


__all__ = [
    "LightGBMPruningCallback",
    "LightGBMTuner",
    "LightGBMTunerCV",
]


class _LightGBMModule(ModuleType):
    """Module class that implements `optuna.integration.lightgbm` package."""

    __all__ = __all__
    __file__ = globals()["__file__"]
    __path__ = [os.path.dirname(__file__)]

    def __getattr__(self, name: str) -> Any:
        return lgb.__dict__[name]


sys.modules[__name__] = _LightGBMModule(__name__)
