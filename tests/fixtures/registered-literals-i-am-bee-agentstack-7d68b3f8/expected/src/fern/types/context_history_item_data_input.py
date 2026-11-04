

import typing

from .artifact_input import ArtifactInput
from .message_input import MessageInput

ContextHistoryItemDataInput = typing.Union[ArtifactInput, MessageInput]
