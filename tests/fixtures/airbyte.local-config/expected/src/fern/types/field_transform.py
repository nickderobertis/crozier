

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_add import FieldAdd
from .field_name import FieldName
from .field_remove import FieldRemove
from .field_schema_update import FieldSchemaUpdate
from .field_transform_transform_type import FieldTransformTransformType


class FieldTransform(UniversalBaseModel):
    """
    Describes the difference between two Streams.
    """

    add_field: typing_extensions.Annotated[typing.Optional[FieldAdd], FieldMetadata(alias="addField")] = None
    breaking: bool
    field_name: typing_extensions.Annotated[FieldName, FieldMetadata(alias="fieldName")]
    remove_field: typing_extensions.Annotated[typing.Optional[FieldRemove], FieldMetadata(alias="removeField")] = None
    transform_type: typing_extensions.Annotated[FieldTransformTransformType, FieldMetadata(alias="transformType")]
    update_field_schema: typing_extensions.Annotated[
        typing.Optional[FieldSchemaUpdate], FieldMetadata(alias="updateFieldSchema")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
