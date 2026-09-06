

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .function_data_nullish_schema_schema import FunctionDataNullishSchemaSchema
from .function_data_nullish_schema_type import FunctionDataNullishSchemaType


class FunctionDataNullishSchema(UniversalBaseModel):
    type: FunctionDataNullishSchemaType
    data: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The parameters data
    """

    schema_: typing_extensions.Annotated[
        FunctionDataNullishSchemaSchema,
        FieldMetadata(alias="__schema"),
        pydantic.Field(alias="__schema", description="JSON Schema format for parameters"),
    ]
    """
    JSON Schema format for parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
