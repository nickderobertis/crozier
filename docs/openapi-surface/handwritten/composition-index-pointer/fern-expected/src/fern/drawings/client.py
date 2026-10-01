

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.drawing import Drawing
from .raw_client import AsyncRawDrawingsClient, RawDrawingsClient


class DrawingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDrawingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDrawingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDrawingsClient
        """
        return self._raw_client

    def get_drawing(self, company_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Drawing:
        """
        Parameters
        ----------
        company_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Drawing
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.drawings.get_drawing(
            company_id="companyId",
        )
        """
        _response = self._raw_client.get_drawing(company_id, request_options=request_options)
        return _response.data


class AsyncDrawingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDrawingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDrawingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDrawingsClient
        """
        return self._raw_client

    async def get_drawing(self, company_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Drawing:
        """
        Parameters
        ----------
        company_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Drawing
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.drawings.get_drawing(
                company_id="companyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_drawing(company_id, request_options=request_options)
        return _response.data
