

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .telegram_qr_login_state import TelegramQrLoginState
from .uuid_ import Uuid


class TelegramQrLoginResponse(UniversalBaseModel):
    flow_id: typing_extensions.Annotated[Uuid, FieldMetadata(alias="flowId"), pydantic.Field(alias="flowId")]
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    state: TelegramQrLoginState
    qr_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="qrUrl"), pydantic.Field(alias="qrUrl")
    ] = None
    qr_expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="qrExpiresAt"), pydantic.Field(alias="qrExpiresAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
