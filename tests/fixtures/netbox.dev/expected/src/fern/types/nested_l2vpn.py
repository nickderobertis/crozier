

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_l2vpn_type import NestedL2VpnType


class NestedL2Vpn(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    identifier: typing.Optional[int] = None
    name: str
    slug: str
    type: NestedL2VpnType
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
