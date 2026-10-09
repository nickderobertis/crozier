

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.shift import Shift
from ..types.traction import Traction
from .raw_client import AsyncRawTramsClient, RawTramsClient


class TramsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTramsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTramsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTramsClient
        """
        return self._raw_client

    def list_trams(
        self,
        *,
        line: str,
        shift: Shift,
        traction: typing.Optional[Traction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        line : str

        shift : Shift

        traction : typing.Optional[Traction]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.trams.list_trams(
            shift="early",
            line="line",
        )
        """
        _response = self._raw_client.list_trams(
            line=line, shift=shift, traction=traction, request_options=request_options
        )
        return _response.data

    def count_idle(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )
        client.trams.count_idle()
        """
        _response = self._raw_client.count_idle(request_options=request_options)
        return _response.data


class AsyncTramsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTramsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTramsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTramsClient
        """
        return self._raw_client

    async def list_trams(
        self,
        *,
        line: str,
        shift: Shift,
        traction: typing.Optional[Traction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        line : str

        shift : Shift

        traction : typing.Optional[Traction]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.trams.list_trams(
                shift="early",
                line="line",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_trams(
            line=line, shift=shift, traction=traction, request_options=request_options
        )
        return _response.data

    async def count_idle(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.trams.count_idle()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_idle(request_options=request_options)
        return _response.data
