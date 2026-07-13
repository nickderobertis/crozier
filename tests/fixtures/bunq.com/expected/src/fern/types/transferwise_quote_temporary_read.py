

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class TransferwiseQuoteTemporaryRead(UniversalBaseModel):
    amount_source: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The source amount.
    """

    amount_target: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The target amount.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the note's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the quote.
    """

    quote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The quote id Transferwise needs. Will always be null for temporary quotes.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expiration timestamp of the quote. Will always be null for temporary quotes.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the note's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
