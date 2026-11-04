

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming(UniversalBaseModel):
    name: str
    url: str
    slogan: str
    color: str
    color_text: typing_extensions.Annotated[str, FieldMetadata(alias="color-text"), pydantic.Field(alias="color-text")]
    color_element: typing_extensions.Annotated[
        str, FieldMetadata(alias="color-element"), pydantic.Field(alias="color-element")
    ]
    color_element_bright: typing_extensions.Annotated[
        str, FieldMetadata(alias="color-element-bright"), pydantic.Field(alias="color-element-bright")
    ]
    color_element_dark: typing_extensions.Annotated[
        str, FieldMetadata(alias="color-element-dark"), pydantic.Field(alias="color-element-dark")
    ]
    logo: str
    background: str
    background_plain: typing_extensions.Annotated[
        bool, FieldMetadata(alias="background-plain"), pydantic.Field(alias="background-plain")
    ]
    background_default: typing_extensions.Annotated[
        bool, FieldMetadata(alias="background-default"), pydantic.Field(alias="background-default")
    ]
    logoheader: str
    favicon: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
