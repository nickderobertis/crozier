

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .searched_version import SearchedVersion


class VersionSearchResults(UniversalBaseModel):
    """
    Describes the response received when searching for artifacts.
    """

    count: int = pydantic.Field()
    """
    The total number of versions that matched the query (may be more than the number of versions
    returned in the result set).
    """

    versions: typing.List[SearchedVersion] = pydantic.Field()
    """
    The collection of artifact versions returned in the result set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
