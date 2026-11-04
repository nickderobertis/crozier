

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsersPreprintsListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the preprint entity.
    """

    bibliographic_contributors: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the bibliographic contributors that are listed as contributing to this preprint.
    """

    citation: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the citation of the preprint.
    """

    identifiers: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the identifiers associated with the preprint.
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the license that has been applied to the preprint.
    """

    node: str = pydantic.Field()
    """
    A relationship to the node that was created for the preprint, or from which the preprint was created.
    """

    primary_file: str = pydantic.Field()
    """
    A relationship to the file that is designated as the preprint's primary file, or the manuscript of the preprint.
    """

    provider: str = pydantic.Field()
    """
    A relationship to the preprint provider under which the preprint was created (OSF, socarxiv, psyarxiv, etc.).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
