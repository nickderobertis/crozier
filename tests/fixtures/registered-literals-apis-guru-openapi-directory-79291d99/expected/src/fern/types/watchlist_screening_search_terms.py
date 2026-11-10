

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_country_code_nullable import GenericCountryCodeNullable
from .iso8601date_nullable import Iso8601DateNullable
from .watchlist_program_id import WatchlistProgramId
from .watchlist_screening_document_value_nullable import WatchlistScreeningDocumentValueNullable
from .watchlist_screening_individual_name import WatchlistScreeningIndividualName


class WatchlistScreeningSearchTerms(UniversalBaseModel):
    """
    Search terms for creating an individual watchlist screening
    """

    country: typing.Optional[GenericCountryCodeNullable] = None
    date_of_birth: typing.Optional[Iso8601DateNullable] = None
    document_number: typing.Optional[WatchlistScreeningDocumentValueNullable] = None
    legal_name: WatchlistScreeningIndividualName
    version: float = pydantic.Field()
    """
    The current version of the search terms. Starts at `1` and increments with each edit to `search_terms`.
    """

    watchlist_program_id: WatchlistProgramId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
