

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037DiagStatisticsTime(UniversalBaseModel):
    """
    Time values
    """

    average: typing.Optional[int] = pydantic.Field(default=None)
    """
    Average time spent processing this RPC type
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time spent processing this RPC type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
