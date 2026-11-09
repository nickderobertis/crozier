

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxPublicTokenCreateRequestIncomeVerificationBankIncome(UniversalBaseModel):
    """
    Specifies options for Bank Income. This field is required if `income_verification` is included in the `initial_products` array and `bank` is specified in `income_source_types`.
    """

    days_requested: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of days of data to request for the Bank Income product
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
