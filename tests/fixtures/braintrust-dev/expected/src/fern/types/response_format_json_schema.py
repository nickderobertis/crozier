

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .response_format_json_schema_schema import ResponseFormatJsonSchemaSchema


class ResponseFormatJsonSchema(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[ResponseFormatJsonSchemaSchema], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    strict: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
