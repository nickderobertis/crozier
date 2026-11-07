

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SatelliteDataUsage(UniversalBaseModel):
    bytes_remaining: int = pydantic.Field()
    """
    Bytes remaining in the plan
    """

    bytes_total: int = pydantic.Field()
    """
    Total bytes included in the plan
    """

    bytes_used: int = pydantic.Field()
    """
    Bytes used to date
    """

    bytes_used_billable: int = pydantic.Field()
    """
    Billable bytes used to date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
