

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_web_key_set import JsonWebKeySet
from .raw_client import AsyncRawOpenIdConnectClient, RawOpenIdConnectClient


class OpenIdConnectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenIdConnectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenIdConnectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenIdConnectClient
        """
        return self._raw_client

    def get_claims_for_the_authenticated_subject(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Claims for the authenticated subject

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_connect.get_claims_for_the_authenticated_subject()
        """
        _response = self._raw_client.get_claims_for_the_authenticated_subject(request_options=request_options)
        return _response.data

    def list_json_web_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonWebKeySet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonWebKeySet
            JSON Web Key Set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_connect.list_json_web_keys()
        """
        _response = self._raw_client.list_json_web_keys(request_options=request_options)
        return _response.data

    def get_json_web_keys_for_a_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonWebKeySet:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonWebKeySet
            JSON Web Key Set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.open_id_connect.get_json_web_keys_for_a_client(
            client_id="client_id",
        )
        """
        _response = self._raw_client.get_json_web_keys_for_a_client(client_id, request_options=request_options)
        return _response.data


class AsyncOpenIdConnectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenIdConnectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenIdConnectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenIdConnectClient
        """
        return self._raw_client

    async def get_claims_for_the_authenticated_subject(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Claims for the authenticated subject

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_connect.get_claims_for_the_authenticated_subject()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_claims_for_the_authenticated_subject(request_options=request_options)
        return _response.data

    async def list_json_web_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonWebKeySet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonWebKeySet
            JSON Web Key Set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_connect.list_json_web_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_json_web_keys(request_options=request_options)
        return _response.data

    async def get_json_web_keys_for_a_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JsonWebKeySet:
        """
        Parameters
        ----------
        client_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonWebKeySet
            JSON Web Key Set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_connect.get_json_web_keys_for_a_client(
                client_id="client_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_json_web_keys_for_a_client(client_id, request_options=request_options)
        return _response.data
