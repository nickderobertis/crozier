

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGadgetsClient, RawGadgetsClient
from .types.create_gadget_response import CreateGadgetResponse


class GadgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGadgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGadgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGadgetsClient
        """
        return self._raw_client

    def list_gadgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
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
        client.gadgets.list_gadgets()
        """
        _response = self._raw_client.list_gadgets(request_options=request_options)
        return _response.data

    def create_gadget(self, *, request_options: typing.Optional[RequestOptions] = None) -> CreateGadgetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGadgetResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.gadgets.create_gadget()
        """
        _response = self._raw_client.create_gadget(request_options=request_options)
        return _response.data


class AsyncGadgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGadgetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGadgetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGadgetsClient
        """
        return self._raw_client

    async def list_gadgets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
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
            await client.gadgets.list_gadgets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_gadgets(request_options=request_options)
        return _response.data

    async def create_gadget(self, *, request_options: typing.Optional[RequestOptions] = None) -> CreateGadgetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGadgetResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gadgets.create_gadget()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_gadget(request_options=request_options)
        return _response.data
