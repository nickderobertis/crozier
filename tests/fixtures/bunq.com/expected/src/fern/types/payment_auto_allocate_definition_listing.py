

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .pointer import Pointer


class PaymentAutoAllocateDefinitionListing(UniversalBaseModel):
    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount to allocate.
    """

    counterparty_alias: typing.Optional[Pointer] = pydantic.Field(default=None)
    """
    The alias of the party we are allocating the money to.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocateDefinition was created.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the payment.
    """

    fraction: typing.Optional[int] = pydantic.Field(default=None)
    """
    The percentage of the triggering payment's amount to allocate.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the PaymentAutoAllocateDefinition.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocateDefinition was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
