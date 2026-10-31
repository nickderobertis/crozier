

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebSearchResult(UniversalBaseModel):
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Page title of the result
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resolved URL for the result
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Extracted text content snippet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
