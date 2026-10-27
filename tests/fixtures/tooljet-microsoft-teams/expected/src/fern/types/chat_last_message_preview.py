

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_last_message_preview_body import ChatLastMessagePreviewBody
from .chat_last_message_preview_from import ChatLastMessagePreviewFrom


class ChatLastMessagePreview(UniversalBaseModel):
    odata_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.type"), pydantic.Field(alias="@odata.type")
    ] = None
    body: typing.Optional[ChatLastMessagePreviewBody] = None
    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    from_: typing_extensions.Annotated[
        typing.Optional[ChatLastMessagePreviewFrom], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    id: typing.Optional[str] = None
    is_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")
    ] = None
    message_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageType"), pydantic.Field(alias="messageType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
