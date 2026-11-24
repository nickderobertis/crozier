

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.profile import Profile
from .raw_client import AsyncRawAgentRuntimeClient, RawAgentRuntimeClient
from .types.create_runtime_profile_request_mode import CreateRuntimeProfileRequestMode


OMIT = typing.cast(typing.Any, ...)


class AgentRuntimeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentRuntimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentRuntimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentRuntimeClient
        """
        return self._raw_client

    def create_runtime_profile(
        self, *, mode: CreateRuntimeProfileRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> Profile:
        """
        Parameters
        ----------
        mode : CreateRuntimeProfileRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Profile
            The profile.

        Examples
        --------
        from fern.agent_runtime import CreateRuntimeProfileRequestMode

        from fern import FernApi

        client = FernApi()
        client.agent_runtime.create_runtime_profile(
            mode=CreateRuntimeProfileRequestMode.WARM,
        )
        """
        _response = self._raw_client.create_runtime_profile(mode=mode, request_options=request_options)
        return _response.data


class AsyncAgentRuntimeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentRuntimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentRuntimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentRuntimeClient
        """
        return self._raw_client

    async def create_runtime_profile(
        self, *, mode: CreateRuntimeProfileRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> Profile:
        """
        Parameters
        ----------
        mode : CreateRuntimeProfileRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Profile
            The profile.

        Examples
        --------
        import asyncio

        from fern.agent_runtime import CreateRuntimeProfileRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agent_runtime.create_runtime_profile(
                mode=CreateRuntimeProfileRequestMode.WARM,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_runtime_profile(mode=mode, request_options=request_options)
        return _response.data
