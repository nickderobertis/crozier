

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOauth2LoginRedirectorClient, RawOauth2LoginRedirectorClient


class Oauth2LoginRedirectorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOauth2LoginRedirectorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOauth2LoginRedirectorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOauth2LoginRedirectorClient
        """
        return self._raw_client

    def authorize(
        self, *, client_id: str, state: str, response_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        client_id : str
            Client ID

        state : str
            State of the flow

        response_type : str
            Response type for the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Client not found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.oauth2login_redirector.authorize(
            client_id="client_id",
            state="state",
            response_type="response_type",
        )
        """
        _response = self._raw_client.authorize(
            client_id=client_id, state=state, response_type=response_type, request_options=request_options
        )
        return _response.data


class AsyncOauth2LoginRedirectorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOauth2LoginRedirectorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOauth2LoginRedirectorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOauth2LoginRedirectorClient
        """
        return self._raw_client

    async def authorize(
        self, *, client_id: str, state: str, response_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        client_id : str
            Client ID

        state : str
            State of the flow

        response_type : str
            Response type for the flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Client not found

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
            await client.oauth2login_redirector.authorize(
                client_id="client_id",
                state="state",
                response_type="response_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize(
            client_id=client_id, state=state, response_type=response_type, request_options=request_options
        )
        return _response.data
