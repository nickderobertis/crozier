

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.session_delete import SessionDelete
from .raw_client import AsyncRawSessionClient, RawSessionClient


class SessionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionClient
        """
        return self._raw_client

    def delete_session(self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> SessionDelete:
        """
        Deletes the current session.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDelete
            Endpoint for operations over the current session.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.session.delete_session(
            item_id=1,
        )
        """
        _response = self._raw_client.delete_session(item_id, request_options=request_options)
        return _response.data


class AsyncSessionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionClient
        """
        return self._raw_client

    async def delete_session(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SessionDelete:
        """
        Deletes the current session.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionDelete
            Endpoint for operations over the current session.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.session.delete_session(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_session(item_id, request_options=request_options)
        return _response.data
