

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .complex_types_literal_response_result_data_str_lit import ComplexTypesLiteralResponseResultDataStrLit


class ComplexTypesLiteralResponseResultData(UniversalBaseModel):
    str_lit: typing_extensions.Annotated[
        ComplexTypesLiteralResponseResultDataStrLit, FieldMetadata(alias="strLit"), pydantic.Field(alias="strLit")
    ]
    num_lit: typing_extensions.Annotated[float, FieldMetadata(alias="numLit"), pydantic.Field(alias="numLit")]
    bool_lit: typing_extensions.Annotated[bool, FieldMetadata(alias="boolLit"), pydantic.Field(alias="boolLit")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
