

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OpenapiValidationErrorsErrorsItem(UniversalBaseModel):
    instance_path: typing_extensions.Annotated[
        str, FieldMetadata(alias="instancePath"), pydantic.Field(alias="instancePath")
    ]
    schema_path: typing_extensions.Annotated[str, FieldMetadata(alias="schemaPath"), pydantic.Field(alias="schemaPath")]
    keyword: str
    message: str
    params: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
