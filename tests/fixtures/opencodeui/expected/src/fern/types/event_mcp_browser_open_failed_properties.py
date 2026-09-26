

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EventMcpBrowserOpenFailedProperties(UniversalBaseModel):
    mcp_name: typing_extensions.Annotated[str, FieldMetadata(alias="mcpName"), pydantic.Field(alias="mcpName")]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
