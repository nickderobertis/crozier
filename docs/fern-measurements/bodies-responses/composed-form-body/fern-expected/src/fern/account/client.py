

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAccountClient, RawAccountClient


OMIT = typing.cast(typing.Any, ...)


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def perform_external_login(
        self, *, provider: str, return_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        provider : str

        return_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.perform_external_login(
            provider="provider",
            return_url="returnUrl",
        )
        """
        _response = self._raw_client.perform_external_login(
            provider=provider, return_url=return_url, request_options=request_options
        )
        return _response.data

    def perform_logout(
        self,
        *,
        reason: str,
        everywhere: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        reason : str

        everywhere : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.account.perform_logout(
            reason="reason",
        )
        """
        _response = self._raw_client.perform_logout(
            reason=reason, everywhere=everywhere, request_options=request_options
        )
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def perform_external_login(
        self, *, provider: str, return_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        provider : str

        return_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.account.perform_external_login(
                provider="provider",
                return_url="returnUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_external_login(
            provider=provider, return_url=return_url, request_options=request_options
        )
        return _response.data

    async def perform_logout(
        self,
        *,
        reason: str,
        everywhere: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        reason : str

        everywhere : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.account.perform_logout(
                reason="reason",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_logout(
            reason=reason, everywhere=everywhere, request_options=request_options
        )
        return _response.data
