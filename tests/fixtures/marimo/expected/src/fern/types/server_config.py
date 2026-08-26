

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .server_config_browser import ServerConfigBrowser
from .server_config_transport import ServerConfigTransport


class ServerConfig(UniversalBaseModel):
    """
    Configuration for the server.

        **Keys.**

        - `browser`: the web browser to use. `"default"` or a browser registered
            with Python's webbrowser module (eg, `"firefox"` or `"chrome"`)
        - `follow_symlink`: if true, the server will follow symlinks it finds
            inside its static assets directory.
        - `disable_file_downloads`: if true, the file download button will be
            hidden in the file explorer.
        - `transport`: experimental. The transport used to stream kernel
            messages to the frontend, typically set with the
            `MARIMO_SERVER_TRANSPORT` environment variable. `"websocket"`
            (default) uses the `/ws` WebSocket endpoint; `"sse"` uses
            server-sent events over HTTP, for deployments behind proxies or
            services that do not support WebSockets. Terminal, LSP, and
            real-time collaboration still require WebSockets; RTC is disabled
            when using `"sse"`.
    """

    browser: ServerConfigBrowser
    disable_file_downloads: typing.Optional[bool] = None
    follow_symlink: bool
    transport: typing.Optional[ServerConfigTransport] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
