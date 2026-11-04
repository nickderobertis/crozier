

import typing

from .artifact_output import ArtifactOutput
from .message_output import MessageOutput

ContextHistoryItemDataOutput = typing.Union[ArtifactOutput, MessageOutput]
