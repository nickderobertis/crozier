

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryCompletion(UniversalBaseModel):
    """
    Defines query completion generation for an index.
    """

    max_completion_entries: int = pydantic.Field()
    """
    Maximum number of completions to generate during indexing
    disabled if == 0
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
