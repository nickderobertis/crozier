

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .passage import Passage


class PassageSearchResult(UniversalBaseModel):
    """
    Result from a passage search operation with scoring details.
    """

    passage: Passage = pydantic.Field()
    """
    The passage object
    """

    score: float = pydantic.Field()
    """
    Relevance score
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Additional metadata about the search result
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
