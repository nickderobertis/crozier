

import typing

from .model_custom_message import ModelCustomMessage
from .model_update_message import ModelUpdateMessage

ModelRequestMessage = typing.Union[ModelUpdateMessage, ModelCustomMessage]
