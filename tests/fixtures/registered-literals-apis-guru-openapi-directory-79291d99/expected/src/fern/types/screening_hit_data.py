

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems
from .screening_hit_date_of_birth_item import ScreeningHitDateOfBirthItem
from .screening_hit_documents_items import ScreeningHitDocumentsItems
from .screening_hit_names_items import ScreeningHitNamesItems


class ScreeningHitData(UniversalBaseModel):
    """
    Information associated with the watchlist hit
    """

    dates_of_birth: typing.Optional[typing.List[ScreeningHitDateOfBirthItem]] = pydantic.Field(default=None)
    """
    Dates of birth associated with the watchlist hit
    """

    documents: typing.Optional[typing.List[ScreeningHitDocumentsItems]] = pydantic.Field(default=None)
    """
    Documents associated with the watchlist hit
    """

    locations: typing.Optional[typing.List[GenericScreeningHitLocationItems]] = pydantic.Field(default=None)
    """
    Locations associated with the watchlist hit
    """

    names: typing.Optional[typing.List[ScreeningHitNamesItems]] = pydantic.Field(default=None)
    """
    Names associated with the watchlist hit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
