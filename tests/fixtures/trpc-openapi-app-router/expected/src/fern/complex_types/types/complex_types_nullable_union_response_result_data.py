

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .complex_types_nullable_union_response_result_data_optional_value import (
    ComplexTypesNullableUnionResponseResultDataOptionalValue,
)
from .complex_types_nullable_union_response_result_data_value import ComplexTypesNullableUnionResponseResultDataValue


class ComplexTypesNullableUnionResponseResultData(UniversalBaseModel):
    value: typing.Optional[ComplexTypesNullableUnionResponseResultDataValue] = None
    optional_value: typing_extensions.Annotated[
        typing.Optional[ComplexTypesNullableUnionResponseResultDataOptionalValue],
        FieldMetadata(alias="optionalValue"),
        pydantic.Field(alias="optionalValue"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
