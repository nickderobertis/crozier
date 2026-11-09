

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.access_token_id_list_response import AccessTokenIdListResponse
from ..types.access_token_response import AccessTokenResponse
from ..types.success import Success
from .raw_client import AsyncRawAuthenticationApiClient, RawAuthenticationApiClient


OMIT = typing.cast(typing.Any, ...)


class AuthenticationApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthenticationApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthenticationApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthenticationApiClient
        """
        return self._raw_client

    def generate_new_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessTokenResponse:
        """
        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication_api.generate_new_token(
            client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
            client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
        )
        """
        _response = self._raw_client.generate_new_token(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def invalidate_all_tokens(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication_api.invalidate_all_tokens(
            client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
            client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
        )
        """
        _response = self._raw_client.invalidate_all_tokens(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    def invalidate_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        token_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        An endpoint which allows you to invalidate a given access token.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        token_id : str
            The Token ID of token being invalidated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication_api.invalidate_token(
            client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
            client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
            token_id="TKID384a057WFC3Dp3",
        )
        """
        _response = self._raw_client.invalidate_token(
            client_id=client_id, client_secret=client_secret, token_id=token_id, request_options=request_options
        )
        return _response.data

    def list_all_token_ids(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessTokenIdListResponse:
        """
        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenIdListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.authentication_api.list_all_token_ids(
            client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
            client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
        )
        """
        _response = self._raw_client.list_all_token_ids(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data


class AsyncAuthenticationApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthenticationApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthenticationApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthenticationApiClient
        """
        return self._raw_client

    async def generate_new_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessTokenResponse:
        """
        This endpoint allows you to generate a new access token, which is a required field for all UniCourt API endpoints except for the Authentication API. To generate a new token, you must provide your Client ID and Client Secret ID which you can find by logging into your UniCourt account. At any time, you can have a maximum of 10 active access tokens. The tokens never expire and, if you make a request which would otherwise lead to you having more than 10 active tokens, you will receive an error message.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication_api.generate_new_token(
                client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
                client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_new_token(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def invalidate_all_tokens(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        An endpoint which allows you to invalidate all existing access tokens associated with your UniCourt account.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication_api.invalidate_all_tokens(
                client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
                client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_all_tokens(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data

    async def invalidate_token(
        self,
        *,
        client_id: str,
        client_secret: str,
        token_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        An endpoint which allows you to invalidate a given access token.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        token_id : str
            The Token ID of token being invalidated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication_api.invalidate_token(
                client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
                client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
                token_id="TKID384a057WFC3Dp3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_token(
            client_id=client_id, client_secret=client_secret, token_id=token_id, request_options=request_options
        )
        return _response.data

    async def list_all_token_ids(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccessTokenIdListResponse:
        """
        An endpoint which allows you to view all active access tokens associated with your Client ID and Client Secret ID.

        Parameters
        ----------
        client_id : str
            Your Client ID obtainable by logging into your UniCourt account.

        client_secret : str
            Your Client Secret ID obtainable by logging into your UniCourt account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccessTokenIdListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.authentication_api.list_all_token_ids(
                client_id="G3cfixgetVzfaoszGOBp5LPGtih1nMJ9",
                client_secret="u6PTti57IjPlrwU5MzOwLBD2MCwx-IEbo8sTStTivh1I-EqQ8Jcm27Gfo2GhpHCw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_token_ids(
            client_id=client_id, client_secret=client_secret, request_options=request_options
        )
        return _response.data
