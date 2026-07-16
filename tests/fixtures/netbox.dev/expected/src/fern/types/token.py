

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_network import IpNetwork
from .nested_user import NestedUser


class Token(UniversalBaseModel):
    allowed_ips: typing.Optional[typing.List[IpNetwork]] = None
    created: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    expires: typing.Optional[dt.datetime] = None
    id: typing.Optional[int] = None
    key: typing.Optional[str] = None
    last_used: typing.Optional[dt.datetime] = None
    url: typing.Optional[str] = None
    user: NestedUser
    write_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Permit create/update/delete operations using this key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
