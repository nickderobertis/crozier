

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplateDescriptor(UniversalBaseModel):
    """
    Type used to describe custom template page.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of when to use this template.
    """

    file: str = pydantic.Field()
    """
    Template file path relative to the theme templates directory.
    """

    name: str = pydantic.Field()
    """
    Template display name shown to users.
    """

    screenshot: typing.Optional[str] = pydantic.Field(default=None)
    """
    Screenshot URL or attachment URI for previewing the template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
