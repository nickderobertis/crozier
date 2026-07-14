

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .searched_artifact import SearchedArtifact


class ArtifactSearchResults(UniversalBaseModel):
    """
    Describes the response received when searching for artifacts.
    """

    artifacts: typing.List[SearchedArtifact] = pydantic.Field()
    """
    The artifacts returned in the result set.
    """

    count: int = pydantic.Field()
    """
    The total number of artifacts that matched the query that produced the result set (may be 
    more than the number of artifacts in the result set).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
