

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user import User
from .raw_client import AsyncRawSessionClient, RawSessionClient


OMIT = typing.cast(typing.Any, ...)


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

    def fetch_session_information(
        self, *, token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.session.fetch_session_information()
        """
        _response = self._raw_client.fetch_session_information(token=token, request_options=request_options)
        return _response.data

    def create_a_new_session(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        email : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.session.create_a_new_session(
            email="email",
            password="password",
        )
        """
        _response = self._raw_client.create_a_new_session(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    def close_the_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.session.close_the_session()
        """
        _response = self._raw_client.close_the_session(request_options=request_options)
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

    async def fetch_session_information(
        self, *, token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.session.fetch_session_information()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_session_information(token=token, request_options=request_options)
        return _response.data

    async def create_a_new_session(
        self, *, email: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> User:
        """
        Parameters
        ----------
        email : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.session.create_a_new_session(
                email="email",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_session(
            email=email, password=password, request_options=request_options
        )
        return _response.data

    async def close_the_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.session.close_the_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.close_the_session(request_options=request_options)
        return _response.data
