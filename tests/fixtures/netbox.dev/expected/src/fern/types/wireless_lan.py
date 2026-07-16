

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_vlan import NestedVlan
from .nested_wireless_lan_group import NestedWirelessLanGroup
from .wireless_lan_auth_cipher import WirelessLanAuthCipher
from .wireless_lan_auth_type import WirelessLanAuthType
from .wireless_lan_status import WirelessLanStatus


class WirelessLan(UniversalBaseModel):
    auth_cipher: typing.Optional[WirelessLanAuthCipher] = None
    auth_psk: typing.Optional[str] = None
    auth_type: typing.Optional[WirelessLanAuthType] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    group: typing.Optional[NestedWirelessLanGroup] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    ssid: str
    status: typing.Optional[WirelessLanStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vlan: typing.Optional[NestedVlan] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
