

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_input_kind import MessageInputKind
from .part_input import PartInput
from .role import Role


class MessageInput(UniversalBaseModel):
    """
    Represents a single message in the conversation between a user and an agent.
    """

    context_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contextId"), pydantic.Field(alias="contextId")
    ] = None
    extensions: typing.Optional[typing.List[str]] = None
    kind: typing.Optional[MessageInputKind] = None
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    parts: typing.List[PartInput]
    reference_task_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="referenceTaskIds"),
        pydantic.Field(alias="referenceTaskIds"),
    ] = None
    role: Role
    task_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="taskId"), pydantic.Field(alias="taskId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
