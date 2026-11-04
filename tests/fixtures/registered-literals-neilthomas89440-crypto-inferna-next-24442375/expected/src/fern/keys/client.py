

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key_out import ApiKeyOut
from ..types.api_key_secret_out import ApiKeySecretOut
from .raw_client import AsyncRawKeysClient, RawKeysClient


OMIT = typing.cast(typing.Any, ...)


class KeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeysClient
        """
        return self._raw_client

    def list_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ApiKeyOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyOut]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.keys.list_keys()
        """
        _response = self._raw_client.list_keys(request_options=request_options)
        return _response.data

    def create_key(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> ApiKeySecretOut:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeySecretOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.keys.create_key(
            name="name",
        )
        """
        _response = self._raw_client.create_key(name=name, request_options=request_options)
        return _response.data

    def revoke_key(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyOut:
        """
        Revoke an API key (idempotent).

        POST-with-explicit-verb (not DELETE) is deliberate: revoke is a state
        transition on a still-existing resource, not deletion; repeat calls are
        no-ops.

        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.keys.revoke_key(
            key_id="key_id",
        )
        """
        _response = self._raw_client.revoke_key(key_id, request_options=request_options)
        return _response.data


class AsyncKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeysClient
        """
        return self._raw_client

    async def list_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ApiKeyOut]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKeyOut]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keys.list_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_keys(request_options=request_options)
        return _response.data

    async def create_key(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiKeySecretOut:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeySecretOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keys.create_key(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_key(name=name, request_options=request_options)
        return _response.data

    async def revoke_key(self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiKeyOut:
        """
        Revoke an API key (idempotent).

        POST-with-explicit-verb (not DELETE) is deliberate: revoke is a state
        transition on a still-existing resource, not deletion; repeat calls are
        no-ops.

        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiKeyOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.keys.revoke_key(
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_key(key_id, request_options=request_options)
        return _response.data
