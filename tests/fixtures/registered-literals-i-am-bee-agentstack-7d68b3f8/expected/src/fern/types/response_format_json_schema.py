

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_schema import JsonSchema
from .response_format_json_schema_type import ResponseFormatJsonSchemaType


class ResponseFormatJsonSchema(UniversalBaseModel):
    """
    JSON Schema response format.

    Used to generate structured JSON responses.
    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).
    """

    json_schema: JsonSchema
    type: ResponseFormatJsonSchemaType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
