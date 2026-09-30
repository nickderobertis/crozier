

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tls_allow_permissions_item import TlsAllowPermissionsItem


class TlsAllow(UniversalBaseModel):
    host: str
    permissions: typing.Optional[typing.List[TlsAllowPermissionsItem]] = None
    suffix: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
