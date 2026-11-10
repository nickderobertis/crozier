

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenCreateRequestIncomeVerificationBankIncome(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with Bank Income. This field is required if `income_verification` is included in the `products` array and `bank` is specified in `income_source_types`.
    """

    days_requested: int = pydantic.Field()
    """
    The number of days of data to request for the Bank Income product
    """

    enable_multiple_items: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable multiple Items to be added in the Link session
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
