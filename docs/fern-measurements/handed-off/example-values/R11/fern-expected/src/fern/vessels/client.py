

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.hull import Hull
from .raw_client import AsyncRawVesselsClient, RawVesselsClient


class VesselsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVesselsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVesselsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVesselsClient
        """
        return self._raw_client

    def list_vessels(
        self,
        *,
        owners: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hulls: typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]] = None,
        flags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        port: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        owners : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        hulls : typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]]

        flags : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        port : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Vessels

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.vessels.list_vessels(
            port="falmouth",
        )
        """
        _response = self._raw_client.list_vessels(
            owners=owners, hulls=hulls, flags=flags, port=port, request_options=request_options
        )
        return _response.data


class AsyncVesselsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVesselsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVesselsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVesselsClient
        """
        return self._raw_client

    async def list_vessels(
        self,
        *,
        owners: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        hulls: typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]] = None,
        flags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        port: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        owners : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        hulls : typing.Optional[typing.Union[Hull, typing.Sequence[Hull]]]

        flags : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        port : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Vessels

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vessels.list_vessels(
                port="falmouth",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_vessels(
            owners=owners, hulls=hulls, flags=flags, port=port, request_options=request_options
        )
        return _response.data
