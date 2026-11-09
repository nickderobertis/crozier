

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Chapter(UniversalBaseModel):
    """
    Chapter of the audio file
    """

    gist: str = pydantic.Field()
    """
    An ultra-short summary (just a few words) of the content spoken in the chapter
    """

    headline: str = pydantic.Field()
    """
    A single sentence summary of the content spoken during the chapter
    """

    summary: str = pydantic.Field()
    """
    A one paragraph summary of the content spoken during the chapter
    """

    start: int = pydantic.Field()
    """
    The starting time, in milliseconds, for the chapter
    """

    end: int = pydantic.Field()
    """
    The starting time, in milliseconds, for the chapter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
