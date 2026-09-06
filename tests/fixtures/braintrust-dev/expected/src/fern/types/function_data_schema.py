

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .function_data_schema_schema import FunctionDataSchemaSchema
from .function_data_schema_type import FunctionDataSchemaType


class FunctionDataSchema(UniversalBaseModel):
    type: FunctionDataSchemaType
    data: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The parameters data
    """

    schema_: typing_extensions.Annotated[
        FunctionDataSchemaSchema,
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
