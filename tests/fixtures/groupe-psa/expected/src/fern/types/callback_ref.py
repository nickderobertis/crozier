

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callback_ref_links import CallbackRefLinks
from .callback_status import CallbackStatus
from .remote_callback_id import RemoteCallbackId


class CallbackRef(UniversalBaseModel):
    """
    Remote callback reference returned when posting/getting a remote callback.
    """

    links: typing_extensions.Annotated[
        typing.Optional[CallbackRefLinks], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")
    ] = None
    callback_id: typing_extensions.Annotated[
        typing.Optional[RemoteCallbackId], FieldMetadata(alias="callbackId"), pydantic.Field(alias="callbackId")
    ] = None
    status: typing.Optional[CallbackStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
