

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.create_session_agent import CreateSessionAgent
from ...types.get_session_response import GetSessionResponse
from .raw_client import AsyncRawSessionsClient, RawSessionsClient


OMIT = typing.cast(typing.Any, ...)


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionsClient
        """
        return self._raw_client

    def get_or_create_by_external_id(
        self, *, agent: CreateSessionAgent, external_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSessionResponse:
        """
        Idempotent get-or-create: returns the existing session for this `external_id`, or creates one

        Parameters
        ----------
        agent : CreateSessionAgent

        external_id : str
            Caller-supplied id unique within the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionResponse
            Session already existed for this external id.

        Examples
        --------
        from fern import FernApi, SessionAgentNameRef

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.sessions.get_or_create_by_external_id(
            agent=SessionAgentNameRef(
                name="name",
            ),
            external_id="external_id",
        )
        """
        _response = self._raw_client.get_or_create_by_external_id(
            agent=agent, external_id=external_id, request_options=request_options
        )
        return _response.data


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionsClient
        """
        return self._raw_client

    async def get_or_create_by_external_id(
        self, *, agent: CreateSessionAgent, external_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSessionResponse:
        """
        Idempotent get-or-create: returns the existing session for this `external_id`, or creates one

        Parameters
        ----------
        agent : CreateSessionAgent

        external_id : str
            Caller-supplied id unique within the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionResponse
            Session already existed for this external id.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SessionAgentNameRef

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.sessions.get_or_create_by_external_id(
                agent=SessionAgentNameRef(
                    name="name",
                ),
                external_id="external_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_or_create_by_external_id(
            agent=agent, external_id=external_id, request_options=request_options
        )
        return _response.data
