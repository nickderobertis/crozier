

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_action_id import RemoteActionId
from .remote_post_response_links import RemotePostResponseLinks
from .remote_type import RemoteType


class RemotePostResponse(UniversalBaseModel):
    """
    Remote action reference returned when posting a remote action.
    """

    links: typing_extensions.Annotated[
        typing.Optional[RemotePostResponseLinks], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ] = None
    remote_action_id: typing_extensions.Annotated[
        typing.Optional[RemoteActionId], FieldMetadata(alias="remoteActionId"), pydantic.Field(alias="remoteActionId")
    ] = None
    type: typing.Optional[RemoteType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
