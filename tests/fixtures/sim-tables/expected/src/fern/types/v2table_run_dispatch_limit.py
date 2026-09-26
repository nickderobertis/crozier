

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_run_dispatch_limit_type import V2TableRunDispatchLimitType


class V2TableRunDispatchLimit(UniversalBaseModel):
    type: V2TableRunDispatchLimitType = pydantic.Field()
    """
    Unit the cap counts.
    """

    max: int = pydantic.Field()
    """
    Hard ceiling in units of `type`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
