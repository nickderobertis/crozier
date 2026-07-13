

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class InsightListing(UniversalBaseModel):
    amount_total: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount of the transactions in the category.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category.
    """

    category_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The translated category.
    """

    number_of_transactions: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of the transactions in the category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
