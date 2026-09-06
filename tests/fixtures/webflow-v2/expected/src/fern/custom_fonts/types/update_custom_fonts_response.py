

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_custom_fonts_response_custom_font import UpdateCustomFontsResponseCustomFont


class UpdateCustomFontsResponse(UniversalBaseModel):
    custom_font: typing_extensions.Annotated[
        UpdateCustomFontsResponseCustomFont,
        FieldMetadata(alias="customFont"),
        pydantic.Field(alias="customFont", description="A custom font uploaded to a Webflow site"),
    ]
    """
    A custom font uploaded to a Webflow site
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
