

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paystub_override import PaystubOverride


class IncomeOverride(UniversalBaseModel):
    """
    Specify payroll data on the account.
    """

    paystubs: typing.Optional[typing.List[PaystubOverride]] = pydantic.Field(default=None)
    """
    A list of paystubs associated with the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
