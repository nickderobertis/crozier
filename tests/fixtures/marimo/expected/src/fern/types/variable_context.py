

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VariableContext(UniversalBaseModel):
    name: str
    preview_value: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="previewValue"), pydantic.Field(alias="previewValue")
    ]
    value_type: typing_extensions.Annotated[str, FieldMetadata(alias="valueType"), pydantic.Field(alias="valueType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
