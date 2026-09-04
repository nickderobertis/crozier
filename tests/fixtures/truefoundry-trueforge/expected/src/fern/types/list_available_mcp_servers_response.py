

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .available_mcp_server import AvailableMcpServer
from .token_pagination import TokenPagination


class ListAvailableMcpServersResponse(UniversalBaseModel):
    data: typing.List[AvailableMcpServer]
    pagination: TokenPagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
