

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.get_access_token_request_grant_type import GetAccessTokenRequestGrantType
from .types.get_access_token_response import GetAccessTokenResponse
from .types.get_rate_limit_response import GetRateLimitResponse
from .types.register_application_response import RegisterApplicationResponse


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def register_application(
        self, *, name: str, description: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterApplicationResponse:
        """
        Register a new application to obtain client credentials for API access.

        Parameters
        ----------
        name : str
            Application name

        description : str
            Application description

        email : str
            Contact email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterApplicationResponse
            Application registered successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.register_application(
            name="name",
            description="description",
            email="email",
        )
        """
        _response = self._raw_client.register_application(
            name=name, description=description, email=email, request_options=request_options
        )
        return _response.data

    def get_access_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GetAccessTokenRequestGrantType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAccessTokenResponse:
        """
        Exchange client credentials for an API access token.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GetAccessTokenRequestGrantType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccessTokenResponse
            Access token

        Examples
        --------
        from fern.auth import GetAccessTokenRequestGrantType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.get_access_token(
            client_id="client_id",
            client_secret="client_secret",
            grant_type=GetAccessTokenRequestGrantType.CLIENT_CREDENTIALS,
        )
        """
        _response = self._raw_client.get_access_token(
            client_id=client_id, client_secret=client_secret, grant_type=grant_type, request_options=request_options
        )
        return _response.data

    def get_rate_limit(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRateLimitResponse:
        """
        Check the current rate limit status for your API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRateLimitResponse
            Rate limit status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.get_rate_limit()
        """
        _response = self._raw_client.get_rate_limit(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def register_application(
        self, *, name: str, description: str, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterApplicationResponse:
        """
        Register a new application to obtain client credentials for API access.

        Parameters
        ----------
        name : str
            Application name

        description : str
            Application description

        email : str
            Contact email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterApplicationResponse
            Application registered successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.register_application(
                name="name",
                description="description",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_application(
            name=name, description=description, email=email, request_options=request_options
        )
        return _response.data

    async def get_access_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        grant_type: GetAccessTokenRequestGrantType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAccessTokenResponse:
        """
        Exchange client credentials for an API access token.

        Parameters
        ----------
        client_id : str

        client_secret : str

        grant_type : GetAccessTokenRequestGrantType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAccessTokenResponse
            Access token

        Examples
        --------
        import asyncio

        from fern.auth import GetAccessTokenRequestGrantType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.get_access_token(
                client_id="client_id",
                client_secret="client_secret",
                grant_type=GetAccessTokenRequestGrantType.CLIENT_CREDENTIALS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_access_token(
            client_id=client_id, client_secret=client_secret, grant_type=grant_type, request_options=request_options
        )
        return _response.data

    async def get_rate_limit(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetRateLimitResponse:
        """
        Check the current rate limit status for your API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRateLimitResponse
            Rate limit status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.get_rate_limit()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rate_limit(request_options=request_options)
        return _response.data
