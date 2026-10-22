

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.key_value import KeyValue
from ..types.write_result import WriteResult
from .raw_client import AsyncRawKeysClient, RawKeysClient
from .types.get_config_key_request_key import GetConfigKeyRequestKey
from .types.replace_config_key_request_key import ReplaceConfigKeyRequestKey


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

    def get_config_key(
        self, filename: str, key: GetConfigKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KeyValue:
        """
        Returns a single top-level key from the config.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        key : GetConfigKeyRequestKey
            A top-level config key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyValue
            Key value

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.keys.get_config_key(
            filename="conf.yml",
            key="pageInfo",
        )
        """
        _response = self._raw_client.get_config_key(filename, key, request_options=request_options)
        return _response.data

    def replace_config_key(
        self,
        filename: str,
        key: ReplaceConfigKeyRequestKey,
        *,
        request: KeyValue,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WriteResult:
        """
        Replaces a single top-level key, leaving the rest of the file untouched.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        key : ReplaceConfigKeyRequestKey
            A top-level config key.

        request : KeyValue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        from fern import AppConfig, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.keys.replace_config_key(
            filename="conf.yml",
            key="pageInfo",
            request=AppConfig(
                theme="nord-frost",
                layout="auto",
            ),
        )
        """
        _response = self._raw_client.replace_config_key(filename, key, request=request, request_options=request_options)
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

    async def get_config_key(
        self, filename: str, key: GetConfigKeyRequestKey, *, request_options: typing.Optional[RequestOptions] = None
    ) -> KeyValue:
        """
        Returns a single top-level key from the config.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        key : GetConfigKeyRequestKey
            A top-level config key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeyValue
            Key value

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.keys.get_config_key(
                filename="conf.yml",
                key="pageInfo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config_key(filename, key, request_options=request_options)
        return _response.data

    async def replace_config_key(
        self,
        filename: str,
        key: ReplaceConfigKeyRequestKey,
        *,
        request: KeyValue,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WriteResult:
        """
        Replaces a single top-level key, leaving the rest of the file untouched.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        key : ReplaceConfigKeyRequestKey
            A top-level config key.

        request : KeyValue

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WriteResult
            Saved

        Examples
        --------
        import asyncio

        from fern import AppConfig, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.keys.replace_config_key(
                filename="conf.yml",
                key="pageInfo",
                request=AppConfig(
                    theme="nord-frost",
                    layout="auto",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_config_key(
            filename, key, request=request, request_options=request_options
        )
        return _response.data
