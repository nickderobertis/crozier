

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_wireless_link_auth_cipher import WritableWirelessLinkAuthCipher
from .writable_wireless_link_auth_type import WritableWirelessLinkAuthType
from .writable_wireless_link_status import WritableWirelessLinkStatus


class WritableWirelessLink(UniversalBaseModel):
    auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = None
    auth_psk: typing.Optional[str] = None
    auth_type: typing.Optional[WritableWirelessLinkAuthType] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    interface_a: int
    interface_b: int
    last_updated: typing.Optional[dt.datetime] = None
    ssid: typing.Optional[str] = None
    status: typing.Optional[WritableWirelessLinkStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
