

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ArchivalMemorySearchResult(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier of the archival memory passage
    """

    timestamp: str = pydantic.Field()
    """
    Timestamp of when the memory was created, formatted in agent's timezone
    """

    content: str = pydantic.Field()
    """
    Text content of the archival memory passage
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of tags associated with this memory
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
