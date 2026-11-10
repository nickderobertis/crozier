

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_document_type import EntityDocumentType
from .watchlist_screening_document_value import WatchlistScreeningDocumentValue


class EntityDocument(UniversalBaseModel):
    """
    An official document, usually issued by a governing body or institution, with an associated identifier.
    """

    number: WatchlistScreeningDocumentValue
    type: EntityDocumentType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
