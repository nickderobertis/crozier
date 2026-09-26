

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session import Session
from .raw_client import AsyncRawSessionClient, RawSessionClient


class SessionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionClient
        """
        return self._raw_client

    def get(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Retrieve detailed information about a specific OpenCode session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Get session

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session.get(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.get(session_id, directory=directory, request_options=request_options)
        return _response.data

    def children(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Session]:
        """
        Retrieve all child sessions that were forked from the specified parent session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            List of children

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.session.children(
            session_id="sessionID",
        )
        """
        _response = self._raw_client.children(session_id, directory=directory, request_options=request_options)
        return _response.data


class AsyncSessionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionClient
        """
        return self._raw_client

    async def get(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Session:
        """
        Retrieve detailed information about a specific OpenCode session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Session
            Get session

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session.get(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(session_id, directory=directory, request_options=request_options)
        return _response.data

    async def children(
        self,
        session_id: str,
        *,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Session]:
        """
        Retrieve all child sessions that were forked from the specified parent session.

        Parameters
        ----------
        session_id : str

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Session]
            List of children

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.session.children(
                session_id="sessionID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.children(session_id, directory=directory, request_options=request_options)
        return _response.data
