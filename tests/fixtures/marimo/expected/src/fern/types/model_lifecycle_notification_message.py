

import typing

from .model_close import ModelClose
from .model_custom import ModelCustom
from .model_open import ModelOpen
from .model_update import ModelUpdate

ModelLifecycleNotificationMessage = typing.Union[ModelOpen, ModelUpdate, ModelCustom, ModelClose]
