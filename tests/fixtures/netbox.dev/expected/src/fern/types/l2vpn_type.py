

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .l2vpn_type_label import L2VpnTypeLabel
from .l2vpn_type_value import L2VpnTypeValue


class L2VpnType(UniversalBaseModel):
    label: L2VpnTypeLabel
    value: L2VpnTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
