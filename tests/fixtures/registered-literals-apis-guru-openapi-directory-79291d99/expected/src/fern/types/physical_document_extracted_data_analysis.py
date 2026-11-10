

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_date_of_birth_match_code import DocumentDateOfBirthMatchCode
from .document_name_match_code import DocumentNameMatchCode
from .expiration_date import ExpirationDate
from .issuing_country import IssuingCountry


class PhysicalDocumentExtractedDataAnalysis(UniversalBaseModel):
    """
    Analysis of the data extracted from the submitted document.
    """

    date_of_birth: DocumentDateOfBirthMatchCode
    expiration_date: ExpirationDate
    issuing_country: IssuingCountry
    name: DocumentNameMatchCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
