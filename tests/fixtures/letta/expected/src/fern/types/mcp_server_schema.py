

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class McpServerSchema(UniversalBaseModel):
    """
    MCP server schema for agent files with remapped ID.
    """

    id: str = pydantic.Field()
    """
    Human-readable MCP server ID
    """

    server_type: str
    server_name: str
    server_url: typing.Optional[str] = None
    stdio_config: typing.Optional[typing.Dict[str, typing.Any]] = None
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
