

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenCreateRequestEmploymentBankIncome(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with Bank Employment. This field is required if `employment` is included in the `products` array and `bank` is specified in `employment_source_types`.
    """

    days_requested: int = pydantic.Field()
    """
    The number of days of data to request for the Bank Employment product.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
