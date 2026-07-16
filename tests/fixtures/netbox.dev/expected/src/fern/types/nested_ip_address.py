

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NestedIpAddress(UniversalBaseModel):
    address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    display: typing.Optional[str] = None
    family: typing.Optional[int] = None
    id: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
