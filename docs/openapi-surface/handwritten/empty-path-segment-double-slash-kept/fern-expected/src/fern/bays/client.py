

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBaysClient, RawBaysClient


class BaysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBaysClient
        """
        return self._raw_client

    def clear_bay(
        self, hangar_id: str, bay_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        hangar_id : str

        bay_id : str

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
        client.bays.clear_bay(
            hangar_id="hangarId",
            bay_id="bayId",
        )
        """
        _response = self._raw_client.clear_bay(hangar_id, bay_id, request_options=request_options)
        return _response.data


class AsyncBaysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBaysClient
        """
        return self._raw_client

    async def clear_bay(
        self, hangar_id: str, bay_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        hangar_id : str

        bay_id : str

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
            await client.bays.clear_bay(
                hangar_id="hangarId",
                bay_id="bayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_bay(hangar_id, bay_id, request_options=request_options)
        return _response.data
