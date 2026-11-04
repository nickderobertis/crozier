

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_hover_card_get_user200response import CoreHoverCardGetUser200Response
from .raw_client import AsyncRawCoreHoverCardClient, RawCoreHoverCardClient


class CoreHoverCardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreHoverCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreHoverCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreHoverCardClient
        """
        return self._raw_client

    def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreHoverCardGetUser200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreHoverCardGetUser200Response
            User details returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_hover_card.get_user(
            user_id="userId",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data


class AsyncCoreHoverCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreHoverCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreHoverCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreHoverCardClient
        """
        return self._raw_client

    async def get_user(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreHoverCardGetUser200Response:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreHoverCardGetUser200Response
            User details returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_hover_card.get_user(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data
