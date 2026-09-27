

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityResourceClient, RawIdentityResourceClient


class IdentityResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityResourceClient
        """
        return self._raw_client

    def get_continue_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )
        client.identity_resource.get_continue_login()
        """
        _response = self._raw_client.get_continue_login(request_options=request_options)
        return _response.data

    def get_error(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_resource.get_error()
        """
        _response = self._raw_client.get_error(request_options=request_options)
        return _response.data

    def get_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_resource.get_login()
        """
        _response = self._raw_client.get_login(request_options=request_options)
        return _response.data

    def delete_session_nonce(self, nonce: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        nonce : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_resource.delete_session_nonce(
            nonce="nonce",
        )
        """
        _response = self._raw_client.delete_session_nonce(nonce, request_options=request_options)
        return _response.data

    def get_start_login_nonce(self, nonce: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        nonce : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_resource.get_start_login_nonce(
            nonce="nonce",
        )
        """
        _response = self._raw_client.get_start_login_nonce(nonce, request_options=request_options)
        return _response.data


class AsyncIdentityResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityResourceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityResourceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityResourceClient
        """
        return self._raw_client

    async def get_continue_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_resource.get_continue_login()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_continue_login(request_options=request_options)
        return _response.data

    async def get_error(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_resource.get_error()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_error(request_options=request_options)
        return _response.data

    async def get_login(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_resource.get_login()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_login(request_options=request_options)
        return _response.data

    async def delete_session_nonce(
        self, nonce: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        nonce : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_resource.delete_session_nonce(
                nonce="nonce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_session_nonce(nonce, request_options=request_options)
        return _response.data

    async def get_start_login_nonce(
        self, nonce: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        nonce : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_resource.get_start_login_nonce(
                nonce="nonce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_start_login_nonce(nonce, request_options=request_options)
        return _response.data
