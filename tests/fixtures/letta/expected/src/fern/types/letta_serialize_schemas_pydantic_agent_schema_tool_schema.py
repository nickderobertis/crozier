

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tool_json_schema import ToolJsonSchema


class LettaSerializeSchemasPydanticAgentSchemaToolSchema(UniversalBaseModel):
    args_json_schema: typing.Optional[typing.Any] = None
    created_at: str
    description: str
    json_schema: ToolJsonSchema
    name: str
    return_char_limit: int
    source_code: typing.Optional[str] = None
    source_type: str
    tags: typing.List[str]
    tool_type: str
    updated_at: str
    metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="metadata_"),
        pydantic.Field(alias="metadata_"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
