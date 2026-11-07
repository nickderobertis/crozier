

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .static_parameter_editor import StaticParameterEditor


class UiActionParameterConfigDto(UniversalBaseModel):
    default_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ] = None
    editor: StaticParameterEditor
    label: typing.Optional[str] = None
    hint_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hintText"), pydantic.Field(alias="hintText")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
