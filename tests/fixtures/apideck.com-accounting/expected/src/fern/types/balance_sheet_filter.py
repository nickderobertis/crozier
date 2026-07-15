

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BalanceSheetFilter(UniversalBaseModel):
    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter by end date. If end date is given, start date is required.
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter by start date. If start date is given, end date is required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
