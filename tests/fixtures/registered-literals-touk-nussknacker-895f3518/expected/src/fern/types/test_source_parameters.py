

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_parameter_name_expression import MapParameterNameExpression


class TestSourceParameters(UniversalBaseModel):
    source_id: typing_extensions.Annotated[str, FieldMetadata(alias="sourceId"), pydantic.Field(alias="sourceId")]
    parameter_expressions: typing_extensions.Annotated[
        MapParameterNameExpression,
        FieldMetadata(alias="parameterExpressions"),
        pydantic.Field(alias="parameterExpressions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
