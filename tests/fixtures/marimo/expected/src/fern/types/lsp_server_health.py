

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lsp_server_health_status import LspServerHealthStatus


class LspServerHealth(UniversalBaseModel):
    """
    Health status for a single LSP server.

        Status meanings:
        - starting: process launched, initializing
        - running: healthy and responsive to pings
        - stopped: not running (never started or cleanly stopped)
        - crashed: exited with non-zero code
        - unresponsive: process alive but not responding to pings
    """

    error: typing.Optional[str] = None
    last_ping_ms: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastPingMs"), pydantic.Field(alias="lastPingMs")
    ] = None
    port: int
    server_id: typing_extensions.Annotated[str, FieldMetadata(alias="serverId"), pydantic.Field(alias="serverId")]
    started_at: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    status: LspServerHealthStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
