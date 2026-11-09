

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .income_summary_field_number import IncomeSummaryFieldNumber


class YtdNetIncomeSummaryFieldNumber(IncomeSummaryFieldNumber):
    """
    Year-to-date earnings after any tax withholdings, benefit payments or deductions, as reported on the paystub.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
