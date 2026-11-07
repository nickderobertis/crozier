

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FieldConfigDto(UniversalBaseModel):
    field_name: typing_extensions.Annotated[str, FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")]
    field_key: typing_extensions.Annotated[str, FieldMetadata(alias="fieldKey"), pydantic.Field(alias="fieldKey")]
    field_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="fieldCategory"), pydantic.Field(alias="fieldCategory")
    ]
    data_type: typing_extensions.Annotated[str, FieldMetadata(alias="dataType"), pydantic.Field(alias="dataType")]
    is_array: typing_extensions.Annotated[bool, FieldMetadata(alias="isArray"), pydantic.Field(alias="isArray")]
    hidden: bool
    flatten: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
