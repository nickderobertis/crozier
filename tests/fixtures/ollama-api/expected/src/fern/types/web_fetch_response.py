

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WebFetchResponse(UniversalBaseModel):
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the fetched page
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Extracted page content
    """

    links: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Links found on the page
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
