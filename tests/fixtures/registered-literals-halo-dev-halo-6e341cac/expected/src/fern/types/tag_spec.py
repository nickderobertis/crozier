

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TagSpec(UniversalBaseModel):
    """
    Desired tag display and rendering configuration.
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display color of the tag in 3- or 6-digit hex notation, such as #fff or #ffffff.
    """

    cover: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cover image URL or attachment URI of the tag.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the tag.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the tag."),
    ]
    """
    Display name of the tag.
    """

    slug: str = pydantic.Field()
    """
    URL slug used to build the tag permalink.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
