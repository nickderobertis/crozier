

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListMcpServerToolsResponse(UniversalBaseModel):
    data: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    MCP `tools/list` entries, passed through verbatim from the MCP server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
