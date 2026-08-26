

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lsp_health_response_status import LspHealthResponseStatus
from .lsp_server_health import LspServerHealth


class LspHealthResponse(UniversalBaseModel):
    """
    Aggregated health response for all LSP servers.
    """

    servers: typing.List[LspServerHealth]
    status: LspHealthResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
