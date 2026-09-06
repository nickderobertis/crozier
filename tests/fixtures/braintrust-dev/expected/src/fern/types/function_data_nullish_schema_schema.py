

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .function_data_nullish_schema_schema_type import FunctionDataNullishSchemaSchemaType


class FunctionDataNullishSchemaSchema(UniversalBaseModel):
    """
    JSON Schema format for parameters
    """

    type: FunctionDataNullishSchemaSchemaType
    properties: typing.Dict[str, typing.Dict[str, typing.Any]]
    required: typing.Optional[typing.List[str]] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="additionalProperties"), pydantic.Field(alias="additionalProperties")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
