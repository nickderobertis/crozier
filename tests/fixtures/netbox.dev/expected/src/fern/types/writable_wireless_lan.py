

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_wireless_lan_auth_cipher import WritableWirelessLanAuthCipher
from .writable_wireless_lan_auth_type import WritableWirelessLanAuthType
from .writable_wireless_lan_status import WritableWirelessLanStatus


class WritableWirelessLan(UniversalBaseModel):
    auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = None
    auth_psk: typing.Optional[str] = None
    auth_type: typing.Optional[WritableWirelessLanAuthType] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    group: typing.Optional[int] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    ssid: str
    status: typing.Optional[WritableWirelessLanStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vlan: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
