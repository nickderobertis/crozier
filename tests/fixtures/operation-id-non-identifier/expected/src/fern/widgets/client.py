

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWidgetsClient, RawWidgetsClient
from .types.verify_code_response import VerifyCodeResponse


class WidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWidgetsClient
        """
        return self._raw_client

    def get_all_widgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.get_all_widgets()
        """
        _response = self._raw_client.get_all_widgets(request_options=request_options)
        return _response.data

    def verify_code(self, *, request_options: typing.Optional[RequestOptions] = None) -> VerifyCodeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyCodeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.widgets.verify_code()
        """
        _response = self._raw_client.verify_code(request_options=request_options)
        return _response.data


class AsyncWidgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWidgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWidgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWidgetsClient
        """
        return self._raw_client

    async def get_all_widgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.get_all_widgets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_widgets(request_options=request_options)
        return _response.data

    async def verify_code(self, *, request_options: typing.Optional[RequestOptions] = None) -> VerifyCodeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyCodeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.widgets.verify_code()


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_code(request_options=request_options)
        return _response.data
