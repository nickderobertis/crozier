

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.token_response import TokenResponse
from .raw_client import AsyncRawAuthenticationClient, RawAuthenticationClient


OMIT = typing.cast(typing.Any, ...)


class AuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationClient
        """
        return self._raw_client

    def createauthtoken(
        self,
        *,
        grant_type: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication.createauthtoken(
            grant_type="grant_type",
            client_id="client_id",
            client_secret="client_secret",
        )
        """
        _response = self._raw_client.createauthtoken(
            grant_type=grant_type, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def request_authorization(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        scope: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Request OAuth2 authorization.

        Parameters
        ----------
        client_id : str
            OAuth2 client ID

        redirect_uri : str
            Redirect URI

        response_type : str
            Response type (code)

        scope : typing.Optional[str]
            Requested scopes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Request authorization successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication.request_authorization(
            client_id="client_id",
            redirect_uri="redirect_uri",
            response_type="response_type",
        )
        """
        _response = self._raw_client.request_authorization(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def request_access_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Exchange authorization code for access token.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Request access token successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication.request_access_token(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.request_access_token(request=request, request_options=request_options)
        return _response.data

    def refresh_access_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Refresh an expired access token using a refresh token.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Refresh access token successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication.refresh_access_token(
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.refresh_access_token(request=request, request_options=request_options)
        return _response.data


class AsyncAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationClient
        """
        return self._raw_client

    async def createauthtoken(
        self,
        *,
        grant_type: str,
        client_id: str,
        client_secret: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Parameters
        ----------
        grant_type : str

        client_id : str

        client_secret : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Token created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication.createauthtoken(
                grant_type="grant_type",
                client_id="client_id",
                client_secret="client_secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createauthtoken(
            grant_type=grant_type, client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def request_authorization(
        self,
        *,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        scope: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Request OAuth2 authorization.

        Parameters
        ----------
        client_id : str
            OAuth2 client ID

        redirect_uri : str
            Redirect URI

        response_type : str
            Response type (code)

        scope : typing.Optional[str]
            Requested scopes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Request authorization successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication.request_authorization(
                client_id="client_id",
                redirect_uri="redirect_uri",
                response_type="response_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_authorization(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type=response_type,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def request_access_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Exchange authorization code for access token.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Request access token successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication.request_access_token(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_access_token(request=request, request_options=request_options)
        return _response.data

    async def refresh_access_token(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Refresh an expired access token using a refresh token.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Refresh access token successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication.refresh_access_token(
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_access_token(request=request, request_options=request_options)
        return _response.data
