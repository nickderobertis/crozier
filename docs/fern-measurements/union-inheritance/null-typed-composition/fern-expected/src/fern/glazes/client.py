

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.glaze import Glaze
from .raw_client import AsyncRawGlazesClient, RawGlazesClient
from .types.list_glaze_firings_response import ListGlazeFiringsResponse


class GlazesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlazesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlazesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlazesClient
        """
        return self._raw_client

    def get_glaze(self, glaze_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Glaze:
        """
        Parameters
        ----------
        glaze_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Glaze
            The glaze.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glazes.get_glaze(
            glaze_id="glazeId",
        )
        """
        _response = self._raw_client.get_glaze(glaze_id, request_options=request_options)
        return _response.data

    def list_glaze_firings(
        self, glaze_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGlazeFiringsResponse:
        """
        Parameters
        ----------
        glaze_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGlazeFiringsResponse
            The firings of the glaze, by kiln.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.glazes.list_glaze_firings(
            glaze_id="glazeId",
        )
        """
        _response = self._raw_client.list_glaze_firings(glaze_id, request_options=request_options)
        return _response.data


class AsyncGlazesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlazesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlazesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlazesClient
        """
        return self._raw_client

    async def get_glaze(self, glaze_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Glaze:
        """
        Parameters
        ----------
        glaze_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Glaze
            The glaze.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glazes.get_glaze(
                glaze_id="glazeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_glaze(glaze_id, request_options=request_options)
        return _response.data

    async def list_glaze_firings(
        self, glaze_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGlazeFiringsResponse:
        """
        Parameters
        ----------
        glaze_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGlazeFiringsResponse
            The firings of the glaze, by kiln.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.glazes.list_glaze_firings(
                glaze_id="glazeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_glaze_firings(glaze_id, request_options=request_options)
        return _response.data
