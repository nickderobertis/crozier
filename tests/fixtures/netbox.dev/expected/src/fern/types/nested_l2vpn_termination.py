

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_l2vpn import NestedL2Vpn


class NestedL2VpnTermination(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    l2vpn: NestedL2Vpn
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
