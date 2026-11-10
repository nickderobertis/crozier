

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_screening_hit_documents_items import EntityScreeningHitDocumentsItems
from .entity_screening_hit_emails_items import EntityScreeningHitEmailsItems
from .entity_screening_hit_names_items import EntityScreeningHitNamesItems
from .entity_screening_hit_urls_items import EntityScreeningHitUrlsItems
from .entity_screening_hits_phone_number_items import EntityScreeningHitsPhoneNumberItems
from .generic_screening_hit_location_items import GenericScreeningHitLocationItems


class EntityScreeningHitData(UniversalBaseModel):
    """
    Information associated with the entity watchlist hit
    """

    documents: typing.Optional[typing.List[EntityScreeningHitDocumentsItems]] = pydantic.Field(default=None)
    """
    Documents associated with the watchlist hit
    """

    email_addresses: typing.Optional[typing.List[EntityScreeningHitEmailsItems]] = pydantic.Field(default=None)
    """
    Email addresses associated with the watchlist hit
    """

    locations: typing.Optional[typing.List[GenericScreeningHitLocationItems]] = pydantic.Field(default=None)
    """
    Locations associated with the watchlist hit
    """

    names: typing.Optional[typing.List[EntityScreeningHitNamesItems]] = pydantic.Field(default=None)
    """
    Names associated with the watchlist hit
    """

    phone_numbers: typing.Optional[typing.List[EntityScreeningHitsPhoneNumberItems]] = pydantic.Field(default=None)
    """
    Phone numbers associated with the watchlist hit
    """

    urls: typing.Optional[typing.List[EntityScreeningHitUrlsItems]] = pydantic.Field(default=None)
    """
    URLs associated with the watchlist hit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
