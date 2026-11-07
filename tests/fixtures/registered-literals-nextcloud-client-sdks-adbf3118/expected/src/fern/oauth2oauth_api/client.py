

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.oauth2oauth_api_get_token200response import Oauth2OauthApiGetToken200Response
from .raw_client import AsyncRawOauth2OauthApiClient, RawOauth2OauthApiClient


class Oauth2OauthApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOauth2OauthApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOauth2OauthApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOauth2OauthApiClient
        """
        return self._raw_client

    def get_token(
        self,
        *,
        grant_type: str,
        code: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Oauth2OauthApiGetToken200Response:
        """
        Parameters
        ----------
        grant_type : str
            Token type that should be granted

        code : str
            Code of the flow

        refresh_token : str
            Refresh token

        client_id : str
            Client ID

        client_secret : str
            Client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Oauth2OauthApiGetToken200Response
            Token returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.oauth2oauth_api.get_token(
            grant_type="grant_type",
            code="code",
            refresh_token="refresh_token",
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._raw_client.get_token(
            grant_type=grant_type,
            code=code,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data


class AsyncOauth2OauthApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOauth2OauthApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOauth2OauthApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOauth2OauthApiClient
        """
        return self._raw_client

    async def get_token(
        self,
        *,
        grant_type: str,
        code: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Oauth2OauthApiGetToken200Response:
        """
        Parameters
        ----------
        grant_type : str
            Token type that should be granted

        code : str
            Code of the flow

        refresh_token : str
            Refresh token

        client_id : str
            Client ID

        client_secret : str
            Client secret

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Oauth2OauthApiGetToken200Response
            Token returned

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
            await client.oauth2oauth_api.get_token(
                grant_type="grant_type",
                code="code",
                refresh_token="refresh_token",
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token(
            grant_type=grant_type,
            code=code,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data
