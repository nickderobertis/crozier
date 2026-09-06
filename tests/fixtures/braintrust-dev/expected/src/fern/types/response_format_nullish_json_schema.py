

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_format_json_schema import ResponseFormatJsonSchema
from .response_format_nullish_json_schema_type import ResponseFormatNullishJsonSchemaType


class ResponseFormatNullishJsonSchema(UniversalBaseModel):
    type: ResponseFormatNullishJsonSchemaType
    json_schema: ResponseFormatJsonSchema

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
