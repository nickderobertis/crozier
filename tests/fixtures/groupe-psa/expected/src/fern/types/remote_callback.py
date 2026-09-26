

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callback_status import CallbackStatus
from .remote_callback_id import RemoteCallbackId
from .remote_callback_links import RemoteCallbackLinks
from .remote_callback_subscribe import RemoteCallbackSubscribe


class RemoteCallback(UniversalBaseModel):
    """
    Remote callback state.
    """

    links: typing_extensions.Annotated[
        RemoteCallbackLinks,
        FieldMetadata(alias="_links"),
        pydantic.Field(alias="_links", description="*Note*: ```remotes``` is a templated link."),
    ]
    """
    *Note*: ```remotes``` is a templated link.
    """

    id: RemoteCallbackId
    subscribe: RemoteCallbackSubscribe
    status: CallbackStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
