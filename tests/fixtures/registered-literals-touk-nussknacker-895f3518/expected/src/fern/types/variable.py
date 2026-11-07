

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .expression import Expression
from .field import Field
from .user_defined_additional_node_fields import UserDefinedAdditionalNodeFields
from .variable_operation_schema_type import VariableOperationSchemaType


class Variable(UniversalBaseModel):
    id: str
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    operation: VariableOperationSchemaType
    variables_to_unset: typing_extensions.Annotated[
        typing.Optional[typing.List[Field]],
        FieldMetadata(alias="variablesToUnset"),
        pydantic.Field(alias="variablesToUnset"),
    ] = None
    var_name: typing_extensions.Annotated[str, FieldMetadata(alias="varName"), pydantic.Field(alias="varName")]
    value: Expression

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
