

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .acquisition import Acquisition
from .affiliation import Affiliation
from .author import Author
from .base_model import BaseModel
from .description_license import DescriptionLicense
from .docling_core_types_base_identifier import DoclingCoreTypesBaseIdentifier
from .publication import Publication


class DocumentDescription(UniversalBaseModel):
    title: typing.Optional[str] = None
    abstract: typing.Optional[typing.List[str]] = None
    authors: typing.Optional[typing.List[Author]] = None
    affiliations: typing.Optional[typing.List[Affiliation]] = None
    subjects: typing.Optional[typing.List[str]] = None
    keywords: typing.Optional[typing.List[str]] = None
    publication_date: typing.Optional[dt.datetime] = None
    languages: typing.Optional[typing.List[str]] = None
    license: typing.Optional[DescriptionLicense] = None
    publishers: typing.Optional[typing.List[str]] = None
    url_refs: typing.Optional[typing.List[str]] = None
    references: typing.Optional[typing.List[DoclingCoreTypesBaseIdentifier]] = None
    publication: typing.Optional[typing.List[Publication]] = pydantic.Field(default=None)
    """
    List of publication journals or venues.
    """

    reference_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of documents referenced by this document.
    """

    citation_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of citations that this document has received (number of documents in whose bibliography this document appears).
    """

    citation_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last update date of the citation count.
    """

    advanced: typing.Optional[BaseModel] = None
    analytics: typing.Optional[BaseModel] = None
    acquisition: typing.Optional[Acquisition] = pydantic.Field(default=None)
    """
    Information on how the document was obtained, for data governance purposes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
