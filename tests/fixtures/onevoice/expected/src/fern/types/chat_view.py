

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message import Message
from .pending_approval import PendingApproval


class ChatView(UniversalBaseModel):
    messages: typing.List[Message]
    pending_approvals: typing_extensions.Annotated[
        typing.List[PendingApproval], FieldMetadata(alias="pendingApprovals"), pydantic.Field(alias="pendingApprovals")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
