

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_bridge_token_endpoint_output import CreateBridgeTokenEndpointOutput
from ..types.google_one_tap_login_endpoint_output import GoogleOneTapLoginEndpointOutput
from ..types.read_bridge_token_endpoint_keys_output import ReadBridgeTokenEndpointKeysOutput
from .raw_client import AsyncRawIdentityClient, RawIdentityClient


OMIT = typing.cast(typing.Any, ...)


class IdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityClient
        """
        return self._raw_client

    def reads_the_bridge_token_keys_for_a_given_read_key(
        self, *, read_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadBridgeTokenEndpointKeysOutput:
        """
        Returns 200 with the keys when available, 202 when they are not yet available, or 404 when not found.

        Parameters
        ----------
        read_key : str
            The read key to read the bridge token keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadBridgeTokenEndpointKeysOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.reads_the_bridge_token_keys_for_a_given_read_key(
            read_key="readKey",
        )
        """
        _response = self._raw_client.reads_the_bridge_token_keys_for_a_given_read_key(
            read_key=read_key, request_options=request_options
        )
        return _response.data

    def creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBridgeTokenEndpointOutput:
        """
        The write key stores the authentication result and the read key retrieves it.

        Parameters
        ----------
        client_id : str
            The client ID to create the keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBridgeTokenEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
            client_id="clientId",
        )
        """
        _response = self._raw_client.creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
            client_id=client_id, request_options=request_options
        )
        return _response.data

    def signs_in_a_user_using_a_token_received_from_google_one_tap(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GoogleOneTapLoginEndpointOutput:
        """
        Redirects to the register confirmation page when the account requires email confirmation.

        Parameters
        ----------
        id_token : str
            The id token received from the Google One Tap login.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleOneTapLoginEndpointOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.signs_in_a_user_using_a_token_received_from_google_one_tap(
            id_token="idToken",
        )
        """
        _response = self._raw_client.signs_in_a_user_using_a_token_received_from_google_one_tap(
            id_token=id_token, request_options=request_options
        )
        return _response.data

    def stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
        self, *, referrer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        referrer : str
            The referrer value to store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
            referrer="referrer",
        )
        """
        _response = self._raw_client.stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
            referrer=referrer, request_options=request_options
        )
        return _response.data


class AsyncIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityClient
        """
        return self._raw_client

    async def reads_the_bridge_token_keys_for_a_given_read_key(
        self, *, read_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadBridgeTokenEndpointKeysOutput:
        """
        Returns 200 with the keys when available, 202 when they are not yet available, or 404 when not found.

        Parameters
        ----------
        read_key : str
            The read key to read the bridge token keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadBridgeTokenEndpointKeysOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.reads_the_bridge_token_keys_for_a_given_read_key(
                read_key="readKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reads_the_bridge_token_keys_for_a_given_read_key(
            read_key=read_key, request_options=request_options
        )
        return _response.data

    async def creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateBridgeTokenEndpointOutput:
        """
        The write key stores the authentication result and the read key retrieves it.

        Parameters
        ----------
        client_id : str
            The client ID to create the keys for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateBridgeTokenEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
                client_id="clientId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_pair_of_read_and_write_bridge_token_keys_for_a_client(
            client_id=client_id, request_options=request_options
        )
        return _response.data

    async def signs_in_a_user_using_a_token_received_from_google_one_tap(
        self, *, id_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GoogleOneTapLoginEndpointOutput:
        """
        Redirects to the register confirmation page when the account requires email confirmation.

        Parameters
        ----------
        id_token : str
            The id token received from the Google One Tap login.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GoogleOneTapLoginEndpointOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.signs_in_a_user_using_a_token_received_from_google_one_tap(
                id_token="idToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.signs_in_a_user_using_a_token_received_from_google_one_tap(
            id_token=id_token, request_options=request_options
        )
        return _response.data

    async def stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
        self, *, referrer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        referrer : str
            The referrer value to store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
                referrer="referrer",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stores_the_referrer_in_a_cookie_for_later_use_during_sign_up(
            referrer=referrer, request_options=request_options
        )
        return _response.data
