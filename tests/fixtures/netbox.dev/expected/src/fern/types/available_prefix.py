

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_vrf import NestedVrf


class AvailablePrefix(UniversalBaseModel):
    family: typing.Optional[int] = None
    prefix: typing.Optional[str] = None
    vrf: typing.Optional[NestedVrf] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
