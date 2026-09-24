

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_format_json_schema_json_schema import ResponseFormatJsonSchemaJsonSchema


class ResponseFormatJsonSchema(UniversalBaseModel):
    """
    JSON Schema response format. Extra provider fields are allowed.
    """

    json_schema: ResponseFormatJsonSchemaJsonSchema = pydantic.Field()
    """
    JSON Schema payload. Extra provider fields are allowed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
