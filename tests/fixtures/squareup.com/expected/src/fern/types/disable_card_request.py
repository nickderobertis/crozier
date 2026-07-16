

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DisableCardRequest(UniversalBaseModel):
    """
    Disables the card, preventing any further updates or charges. Disabling
    an already disabled card is allowed but has no effect. Accessible via
    HTTP requests at POST https://connect.squareup.com/v2/cards/{card_id}/disable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
