

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fhrp_group_auth_type import FhrpGroupAuthType
from .fhrp_group_protocol import FhrpGroupProtocol
from .nested_ip_address import NestedIpAddress
from .nested_tag import NestedTag


class FhrpGroup(UniversalBaseModel):
    auth_key: typing.Optional[str] = None
    auth_type: typing.Optional[FhrpGroupAuthType] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    group_id: int
    id: typing.Optional[int] = None
    ip_addresses: typing.Optional[typing.List[NestedIpAddress]] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    protocol: FhrpGroupProtocol
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
