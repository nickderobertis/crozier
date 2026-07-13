

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class CustomerLimit(UniversalBaseModel):
    limit_amount_monthly: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum amount a user is allowed to spend in a month.
    """

    limit_card_debit_maestro: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit of Maestro cards.
    """

    limit_card_debit_mastercard: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit of MasterCard cards.
    """

    limit_card_debit_wildcard: typing.Optional[int] = pydantic.Field(default=None)
    """
    DEPRECTATED: The limit of wildcards, e.g. Maestro or MasterCard cards.
    """

    limit_card_replacement: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit of free replacement cards.
    """

    limit_card_wildcard: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit of wildcards, e.g. Maestro or MasterCard cards.
    """

    limit_monetary_account: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit of monetary accounts.
    """

    limit_monetary_account_remaining: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of additional monetary accounts you can create.
    """

    spent_amount_monthly: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount the user has spent in the last month.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
