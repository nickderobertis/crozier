

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AudioTimestamps(UniversalBaseModel):
    graph_chars: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Grapheme characters
    """

    graph_times: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    Grapheme timestamps [start, end] in seconds
    """

    phon_chars: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Phoneme characters
    """

    phon_times: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    Phoneme timestamps [start, end] in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
