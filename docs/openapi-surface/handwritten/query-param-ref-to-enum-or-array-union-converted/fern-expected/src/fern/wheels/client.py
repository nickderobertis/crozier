

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.rind_filter import RindFilter
from .raw_client import AsyncRawWheelsClient, RawWheelsClient


class WheelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWheelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWheelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWheelsClient
        """
        return self._raw_client

    def list_wheels(
        self, *, rind: typing.Optional[RindFilter] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        rind : typing.Optional[RindFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The matching wheels.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.wheels.list_wheels()
        """
        _response = self._raw_client.list_wheels(rind=rind, request_options=request_options)
        return _response.data


class AsyncWheelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWheelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWheelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWheelsClient
        """
        return self._raw_client

    async def list_wheels(
        self, *, rind: typing.Optional[RindFilter] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        rind : typing.Optional[RindFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The matching wheels.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.wheels.list_wheels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_wheels(rind=rind, request_options=request_options)
        return _response.data
