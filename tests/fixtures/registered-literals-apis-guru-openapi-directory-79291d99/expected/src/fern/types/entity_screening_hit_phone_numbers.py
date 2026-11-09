

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .phone_type import PhoneType
from .watchlist_screening_phone_number import WatchlistScreeningPhoneNumber


class EntityScreeningHitPhoneNumbers(UniversalBaseModel):
    """
    Phone number information associated with the entity screening hit
    """

    phone_number: WatchlistScreeningPhoneNumber
    type: PhoneType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
