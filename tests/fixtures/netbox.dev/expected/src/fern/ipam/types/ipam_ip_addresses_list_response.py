

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ip_address import IpAddress


class IpamIpAddressesListResponse(UniversalBaseModel):
    count: int
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.List[IpAddress]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
