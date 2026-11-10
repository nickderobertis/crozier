

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email_address_nullable import EmailAddressNullable
from .entity_watchlist_program_id import EntityWatchlistProgramId
from .entity_watchlist_screening_name import EntityWatchlistScreeningName
from .generic_country_code_nullable import GenericCountryCodeNullable
from .url_nullable import UrlNullable
from .watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
from .watchlist_screening_phone_number_nullable import WatchlistScreeningPhoneNumberNullable


class EntityWatchlistScreeningSearchTerms(UniversalBaseModel):
    """
    Search terms associated with an entity used for searching against watchlists
    """

    country: typing.Optional[GenericCountryCodeNullable] = None
    document_number: typing.Optional[WatchlistScreeningDocumentValueNullable] = None
    email_address: typing.Optional[EmailAddressNullable] = None
    entity_watchlist_program_id: EntityWatchlistProgramId
    legal_name: EntityWatchlistScreeningName
    phone_number: typing.Optional[WatchlistScreeningPhoneNumberNullable] = None
    url: typing.Optional[UrlNullable] = None
    version: float = pydantic.Field()
    """
    The current version of the search terms. Starts at `1` and increments with each edit to `search_terms`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
