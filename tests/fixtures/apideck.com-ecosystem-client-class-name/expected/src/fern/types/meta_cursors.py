

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetaCursors(UniversalBaseModel):
    """
    Cursors to navigate to previous or next pages through the API
    """

    current: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to navigate to the current page of results through the API
    """

    next: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to navigate to the next page of results through the API
    """

    previous: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor to navigate to the previous page of results through the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
