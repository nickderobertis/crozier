

import typing

from .model_custom_message import ModelCustomMessage
from .model_update_message import ModelUpdateMessage

ModelCommandMessage = typing.Union[ModelUpdateMessage, ModelCustomMessage]
