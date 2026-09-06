

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BookChapter(UniversalBaseModel):
    """
    A book chapter. Includes the title and timestamps.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the book chapter.
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    When in the book (in seconds) the chapter starts.
    """

    end: typing.Optional[float] = pydantic.Field(default=None)
    """
    When in the book (in seconds) the chapter ends.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chapter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
