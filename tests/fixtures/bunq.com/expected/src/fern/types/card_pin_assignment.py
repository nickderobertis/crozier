

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardPinAssignment(UniversalBaseModel):
    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the monetary account to assign to this pin for the card.
    """

    pin_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 4 digit PIN to be assigned to this account.
    """

    routing_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Routing type. Can be MANUAL or AUTOMATIC
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    PIN type. Can be PRIMARY, SECONDARY or TERTIARY
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
