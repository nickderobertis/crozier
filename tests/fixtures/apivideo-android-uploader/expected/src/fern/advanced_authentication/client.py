

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_token import AccessToken
from .raw_client import AsyncRawAdvancedAuthenticationClient, RawAdvancedAuthenticationClient


OMIT = typing.cast(typing.Any, ...)


class AdvancedAuthenticationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdvancedAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdvancedAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdvancedAuthenticationClient
        """
        return self._raw_client

    def post_auth_api_key(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessToken:
        """
        Returns a bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        api_key : str
            Your account API key. You can use your sandbox API key, or you can use your production API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.advanced_authentication.post_auth_api_key(
            api_key="9VxMaPgsaFg7EBqmuspSzF7",
        )
        """
        _response = self._raw_client.post_auth_api_key(api_key=api_key, request_options=request_options)
        return _response.data

    def post_auth_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessToken:
        """
        Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        refresh_token : str
            The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.advanced_authentication.post_auth_refresh(
            refresh_token="def502005346d9cc2bd79a7793ab5bdabfefcaabfbb8c253f14733f1262077e1a3f38c4751d6d20f590c3784e531a82adc11f05fc1949aa46d5575aaa99cb84b9334ba66ac773576b5d7a418937ae337de62811d086dd42ad1164b12f87d67be6ffea18f2d50be9b95697b21c4d3c4372849bdb2287259cb80541570e913691a08b2fa33c85885930de15cebea627fc09f0255562ab3d39d87d4ff8fc02b00e252afcd480421dec7de9d1411176bcf669c527762e22294b453bc9ea06e9fa8ba5b873feb2ee14ce0a6a6ddd4b78c580631e210e9b9387265dc2bec9478a66a09dcdce1c40d2f856689e9d81742c9628a0b87b359e0b218ea1f07427eef89f999e47af89792f598e05847bd008fddc32ee63f4a601ffb4cd2ad08977f1c854ec358238322c918f05aa5a41f8a171dee497218408abc8283473f6112aeed7310815416a0fa36c63667e0ed014fa40b8992891bf58bae400d901c01450101c88f4978938ad138adc19cfe5698d60fd82cb27c586f6a8f70f4393c7c9e579df8739d46d249fb76d7",
        )
        """
        _response = self._raw_client.post_auth_refresh(refresh_token=refresh_token, request_options=request_options)
        return _response.data


class AsyncAdvancedAuthenticationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdvancedAuthenticationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdvancedAuthenticationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdvancedAuthenticationClient
        """
        return self._raw_client

    async def post_auth_api_key(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessToken:
        """
        Returns a bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        api_key : str
            Your account API key. You can use your sandbox API key, or you can use your production API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advanced_authentication.post_auth_api_key(
                api_key="9VxMaPgsaFg7EBqmuspSzF7",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_auth_api_key(api_key=api_key, request_options=request_options)
        return _response.data

    async def post_auth_refresh(
        self, *, refresh_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessToken:
        """
        Accepts the old bearer token and returns a new bearer token that can be used to authenticate other endpoint.

        You can find the tutorial on using the disposable bearer token [here](https://docs.api.video/reference/disposable-bearer-token-authentication).

        Parameters
        ----------
        refresh_token : str
            The refresh token is either the first refresh token you received when you authenticated with the auth/api-key endpoint, or it's the refresh token from the last time you used the auth/refresh endpoint. Place this in the body of your request to obtain a new access token (which is valid for an hour) and a new refresh token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessToken
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advanced_authentication.post_auth_refresh(
                refresh_token="def502005346d9cc2bd79a7793ab5bdabfefcaabfbb8c253f14733f1262077e1a3f38c4751d6d20f590c3784e531a82adc11f05fc1949aa46d5575aaa99cb84b9334ba66ac773576b5d7a418937ae337de62811d086dd42ad1164b12f87d67be6ffea18f2d50be9b95697b21c4d3c4372849bdb2287259cb80541570e913691a08b2fa33c85885930de15cebea627fc09f0255562ab3d39d87d4ff8fc02b00e252afcd480421dec7de9d1411176bcf669c527762e22294b453bc9ea06e9fa8ba5b873feb2ee14ce0a6a6ddd4b78c580631e210e9b9387265dc2bec9478a66a09dcdce1c40d2f856689e9d81742c9628a0b87b359e0b218ea1f07427eef89f999e47af89792f598e05847bd008fddc32ee63f4a601ffb4cd2ad08977f1c854ec358238322c918f05aa5a41f8a171dee497218408abc8283473f6112aeed7310815416a0fa36c63667e0ed014fa40b8992891bf58bae400d901c01450101c88f4978938ad138adc19cfe5698d60fd82cb27c586f6a8f70f4393c7c9e579df8739d46d249fb76d7",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_auth_refresh(
            refresh_token=refresh_token, request_options=request_options
        )
        return _response.data
