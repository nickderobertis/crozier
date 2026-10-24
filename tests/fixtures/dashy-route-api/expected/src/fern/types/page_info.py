

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageInfo(UniversalBaseModel):
    """
    Branding shown in the header and footer.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dashboard title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sub-title
    """

    nav_links: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="navLinks"),
        pydantic.Field(alias="navLinks", description="Header navigation links"),
    ] = None
    """
    Header navigation links
    """

    footer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Footer HTML or text
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path or URL to the header logo
    """

    favicon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path or URL to the favicon
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Header text color
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
