

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_action_id import RemoteActionId
from .remote_action_status import RemoteActionStatus
from .remote_type import RemoteType


class RemoteRef(UniversalBaseModel):
    remote_action_id: typing_extensions.Annotated[
        typing.Optional[RemoteActionId], FieldMetadata(alias="remoteActionId"), pydantic.Field(alias="remoteActionId")
    ] = None
    status: typing.Optional[RemoteActionStatus] = None
    type: typing.Optional[RemoteType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
