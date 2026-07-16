

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prefix_status_label import PrefixStatusLabel
from .prefix_status_value import PrefixStatusValue


class PrefixStatus(UniversalBaseModel):
    label: PrefixStatusLabel
    value: PrefixStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
