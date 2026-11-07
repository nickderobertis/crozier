

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreprintsContributorsListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the contributor entity.
    """

    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the node that was created for the preprint, or from which the preprint was created.
    """

    user: str = pydantic.Field()
    """
    A relationship to the file that is designated as the preprint's primary file, or the manuscript of the preprint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
