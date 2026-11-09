

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .security_override import SecurityOverride


class HoldingsOverride(UniversalBaseModel):
    """
    Specify the holdings on the account.
    """

    cost_basis: typing.Optional[float] = pydantic.Field(default=None)
    """
    The average original value of the holding. Multiple cost basis values for the same security purchased at different prices are not supported.
    """

    currency: str = pydantic.Field()
    """
    Either a valid `iso_currency_code` or `unofficial_currency_code`
    """

    institution_price: float = pydantic.Field()
    """
    The last price given by the institution for this security
    """

    institution_price_as_of: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date at which `institution_price` was current. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date.
    """

    quantity: float = pydantic.Field()
    """
    The total quantity of the asset held, as reported by the financial institution.
    """

    security: SecurityOverride

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
