

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .counterparty import Counterparty
from .location import Location
from .payment_channel import PaymentChannel
from .personal_finance_category import PersonalFinanceCategory


class Enhancements(UniversalBaseModel):
    """
    A grouping of the Plaid produced transaction enhancement fields.
    """

    category: typing.List[str] = pydantic.Field()
    """
    A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """

    category_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the category to which this transaction belongs. For a full list of categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """

    check_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The check number of the transaction. This field is only populated for check transactions.
    """

    counterparties: typing.Optional[typing.List[Counterparty]] = pydantic.Field(default=None)
    """
    The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description.
    """

    location: Location
    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file.
    """

    merchant_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description.
    """

    payment_channel: PaymentChannel
    personal_finance_category: typing.Optional[PersonalFinanceCategory] = None
    personal_finance_category_icon_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with this transaction, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
