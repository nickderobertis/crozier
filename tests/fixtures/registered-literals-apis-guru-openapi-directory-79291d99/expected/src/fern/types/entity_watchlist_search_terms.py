

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


class EntityWatchlistSearchTerms(UniversalBaseModel):
    """
    Search inputs for creating an entity watchlist screening
    """

    country: typing.Optional[GenericCountryCodeNullable] = None
    document_number: typing.Optional[WatchlistScreeningDocumentValueNullable] = None
    email_address: typing.Optional[EmailAddressNullable] = None
    entity_watchlist_program_id: EntityWatchlistProgramId
    legal_name: EntityWatchlistScreeningName
    phone_number: typing.Optional[WatchlistScreeningPhoneNumberNullable] = None
    url: typing.Optional[UrlNullable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
