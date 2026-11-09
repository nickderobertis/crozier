

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_country_code import GenericCountryCode
from .iso8601date_nullable import Iso8601DateNullable
from .physical_document_category import PhysicalDocumentCategory
from .physical_document_id_number import PhysicalDocumentIdNumber
from .region_nullable import RegionNullable


class PhysicalDocumentExtractedData(UniversalBaseModel):
    """
    Data extracted from a user-submitted document.
    """

    category: PhysicalDocumentCategory
    expiration_date: typing.Optional[Iso8601DateNullable] = None
    id_number: typing.Optional[PhysicalDocumentIdNumber] = None
    issuing_country: GenericCountryCode
    issuing_region: typing.Optional[RegionNullable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
