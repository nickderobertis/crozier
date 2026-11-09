

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_country_code import GenericCountryCode
from .iso8601date import Iso8601Date
from .watchlist_program_id import WatchlistProgramId
from .watchlist_screening_document_value import WatchlistScreeningDocumentValue
from .watchlist_screening_individual_name import WatchlistScreeningIndividualName


class UpdateIndividualScreeningRequestSearchTerms(UniversalBaseModel):
    """
    Search terms for editing an individual watchlist screening
    """

    country: typing.Optional[GenericCountryCode] = None
    date_of_birth: typing.Optional[Iso8601Date] = None
    document_number: typing.Optional[WatchlistScreeningDocumentValue] = None
    legal_name: typing.Optional[WatchlistScreeningIndividualName] = None
    watchlist_program_id: typing.Optional[WatchlistProgramId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
