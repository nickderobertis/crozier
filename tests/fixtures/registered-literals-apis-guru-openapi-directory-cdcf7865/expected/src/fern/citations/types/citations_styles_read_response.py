

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citations_styles_read_response_attributes import CitationsStylesReadResponseAttributes


class CitationsStylesReadResponse(UniversalBaseModel):
    attributes: typing.Optional[CitationsStylesReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the citation style entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the citation style, e.g. APA.
    """

    links: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the citation style entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the citation style entity (`citation-styles`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
