

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .docling_core_types_base_identifier import DoclingCoreTypesBaseIdentifier


class Publication(UniversalBaseModel):
    """
    Publication details of a journal or venue.
    """

    identifiers: typing.Optional[typing.List[DoclingCoreTypesBaseIdentifier]] = pydantic.Field(default=None)
    """
    Unique identifiers of a publication venue.
    """

    name: str = pydantic.Field()
    """
    Name of the publication.
    """

    alternate_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Other names or abbreviations of this publication.
    """

    type: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Type of publication (journal article, conference, review,...).
    """

    pages: typing.Optional[str] = pydantic.Field(default=None)
    """
    Page range in the publication.
    """

    issue: typing.Optional[str] = pydantic.Field(default=None)
    """
    Publication issue (issue number).
    """

    volume: typing.Optional[str] = pydantic.Field(default=None)
    """
    Publication volume.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL on the publication site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
