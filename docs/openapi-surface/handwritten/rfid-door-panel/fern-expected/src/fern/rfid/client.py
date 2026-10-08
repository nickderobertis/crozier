

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.decision import Decision
from .raw_client import AsyncRawRfidClient, RawRfidClient


OMIT = typing.cast(typing.Any, ...)


class RfidClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRfidClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRfidClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRfidClient
        """
        return self._raw_client

    def r_f_i_d_scan(
        self, *, reader: str, badge: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Decision:
        """
        Parameters
        ----------
        reader : str

        badge : str
            The badge's serial, in hex.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Decision
            Whether the door opened.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.rfid.r_f_i_d_scan(
            reader="reader",
            badge="badge",
        )
        """
        _response = self._raw_client.r_f_i_d_scan(reader=reader, badge=badge, request_options=request_options)
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Reader ids.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.rfid.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncRfidClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRfidClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRfidClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRfidClient
        """
        return self._raw_client

    async def r_f_i_d_scan(
        self, *, reader: str, badge: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Decision:
        """
        Parameters
        ----------
        reader : str

        badge : str
            The badge's serial, in hex.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Decision
            Whether the door opened.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.rfid.r_f_i_d_scan(
                reader="reader",
                badge="badge",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.r_f_i_d_scan(reader=reader, badge=badge, request_options=request_options)
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Reader ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.rfid.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
