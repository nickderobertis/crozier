

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card_pin_assignment import CardPinAssignment


class CardBatchReplaceEntry(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    The ID of the card that needs to be replaced.
    """

    name_on_card: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's name as it will be on the card. Check 'card-name' for the available card names for a user.
    """

    pin_code_assignment: typing.Optional[typing.List[CardPinAssignment]] = pydantic.Field(default=None)
    """
    Array of Types, PINs, account IDs assigned to the card.
    """

    second_line: typing.Optional[str] = pydantic.Field(default=None)
    """
    The second line on the card.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
