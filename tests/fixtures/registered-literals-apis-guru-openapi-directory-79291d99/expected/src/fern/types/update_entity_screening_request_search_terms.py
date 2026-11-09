

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email_address import EmailAddress
from .entity_watchlist_program_id import EntityWatchlistProgramId
from .entity_watchlist_screening_name import EntityWatchlistScreeningName
from .generic_country_code import GenericCountryCode
from .url import Url
from .watchlist_screening_document_value import WatchlistScreeningDocumentValue
from .watchlist_screening_phone_number import WatchlistScreeningPhoneNumber


class UpdateEntityScreeningRequestSearchTerms(UniversalBaseModel):
    """
    Search terms for editing an entity watchlist screening
    """

    country: typing.Optional[GenericCountryCode] = None
    document_number: typing.Optional[WatchlistScreeningDocumentValue] = None
    email_address: typing.Optional[EmailAddress] = None
    entity_watchlist_program_id: EntityWatchlistProgramId
    legal_name: typing.Optional[EntityWatchlistScreeningName] = None
    phone_number: typing.Optional[WatchlistScreeningPhoneNumber] = None
    url: typing.Optional[Url] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
