

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxCloudTax(UniversalBaseModel):
    amount: float = pydantic.Field()
    """
    The calculated tax amount for the line item, in the transaction currency.
    """

    rate: float = pydantic.Field()
    """
    The combined tax rate applied to the line item, as a decimal fraction (e.g. 0.08125 = 8.125%).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
