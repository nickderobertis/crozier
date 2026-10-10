

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawCatalogsClient, RawCatalogsClient

if typing.TYPE_CHECKING:
    from .mcp_servers.client import AsyncMcpServersClient, McpServersClient
    from .model_providers.client import AsyncModelProvidersClient, ModelProvidersClient
    from .sandbox_providers.client import AsyncSandboxProvidersClient, SandboxProvidersClient
    from .skills.client import AsyncSkillsClient, SkillsClient


class CatalogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._mcp_servers: typing.Optional[McpServersClient] = None
        self._model_providers: typing.Optional[ModelProvidersClient] = None
        self._sandbox_providers: typing.Optional[SandboxProvidersClient] = None
        self._skills: typing.Optional[SkillsClient] = None

    @property
    def with_raw_response(self) -> RawCatalogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogsClient
        """
        return self._raw_client

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import McpServersClient

            self._mcp_servers = McpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def model_providers(self):
        if self._model_providers is None:
            from .model_providers.client import ModelProvidersClient

            self._model_providers = ModelProvidersClient(client_wrapper=self._client_wrapper)
        return self._model_providers

    @property
    def sandbox_providers(self):
        if self._sandbox_providers is None:
            from .sandbox_providers.client import SandboxProvidersClient

            self._sandbox_providers = SandboxProvidersClient(client_wrapper=self._client_wrapper)
        return self._sandbox_providers

    @property
    def skills(self):
        if self._skills is None:
            from .skills.client import SkillsClient

            self._skills = SkillsClient(client_wrapper=self._client_wrapper)
        return self._skills


class AsyncCatalogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._mcp_servers: typing.Optional[AsyncMcpServersClient] = None
        self._model_providers: typing.Optional[AsyncModelProvidersClient] = None
        self._sandbox_providers: typing.Optional[AsyncSandboxProvidersClient] = None
        self._skills: typing.Optional[AsyncSkillsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawCatalogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogsClient
        """
        return self._raw_client

    @property
    def mcp_servers(self):
        if self._mcp_servers is None:
            from .mcp_servers.client import AsyncMcpServersClient

            self._mcp_servers = AsyncMcpServersClient(client_wrapper=self._client_wrapper)
        return self._mcp_servers

    @property
    def model_providers(self):
        if self._model_providers is None:
            from .model_providers.client import AsyncModelProvidersClient

            self._model_providers = AsyncModelProvidersClient(client_wrapper=self._client_wrapper)
        return self._model_providers

    @property
    def sandbox_providers(self):
        if self._sandbox_providers is None:
            from .sandbox_providers.client import AsyncSandboxProvidersClient

            self._sandbox_providers = AsyncSandboxProvidersClient(client_wrapper=self._client_wrapper)
        return self._sandbox_providers

    @property
    def skills(self):
        if self._skills is None:
            from .skills.client import AsyncSkillsClient

            self._skills = AsyncSkillsClient(client_wrapper=self._client_wrapper)
        return self._skills
