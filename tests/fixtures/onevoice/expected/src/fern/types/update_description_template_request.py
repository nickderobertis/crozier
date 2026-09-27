

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateDescriptionTemplateRequest(UniversalBaseModel):
    description_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="descriptionTemplate"),
        pydantic.Field(
            alias="descriptionTemplate",
            description="Free-text template with single-brace placeholders drawn from the\nallowed set (name, category, address, phone, website, hours,\ndescription). A non-empty value fully replaces the platform\ndescription; an empty string clears the override.",
        ),
    ] = None
    """
    Free-text template with single-brace placeholders drawn from the
    allowed set (name, category, address, phone, website, hours,
    description). A non-empty value fully replaces the platform
    description; an empty string clears the override.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
