

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_action import RemoteAction


class RemoteActionsEmbedded(UniversalBaseModel):
    remote_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[RemoteAction]],
        FieldMetadata(alias="remoteActions"),
        pydantic.Field(alias="remoteActions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
