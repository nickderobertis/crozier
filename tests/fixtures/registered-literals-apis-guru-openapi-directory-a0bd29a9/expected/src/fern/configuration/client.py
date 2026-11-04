

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.system_configuration_response import SystemConfigurationResponse
from .raw_client import AsyncRawConfigurationClient, RawConfigurationClient


OMIT = typing.cast(typing.Any, ...)


class ConfigurationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigurationClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_configuration_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        key : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.configuration.post_api_v1geneva_actions_configuration_target(
            target="target",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_configuration_target(
            target, comment=comment, key=key, value=value, request_options=request_options
        )
        return _response.data

    def get_api_v1geneva_actions_configuration_target_key(
        self, target: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.configuration.get_api_v1geneva_actions_configuration_target_key(
            target="target",
            key="key",
        )
        """
        _response = self._raw_client.get_api_v1geneva_actions_configuration_target_key(
            target, key, request_options=request_options
        )
        return _response.data

    def delete_api_v1geneva_actions_configuration_target_key(
        self, target: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        target : str

        key : str

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
        client.configuration.delete_api_v1geneva_actions_configuration_target_key(
            target="target",
            key="key",
        )
        """
        _response = self._raw_client.delete_api_v1geneva_actions_configuration_target_key(
            target, key, request_options=request_options
        )
        return _response.data


class AsyncConfigurationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigurationClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_configuration_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        key : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.configuration.post_api_v1geneva_actions_configuration_target(
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_configuration_target(
            target, comment=comment, key=key, value=value, request_options=request_options
        )
        return _response.data

    async def get_api_v1geneva_actions_configuration_target_key(
        self, target: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.configuration.get_api_v1geneva_actions_configuration_target_key(
                target="target",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1geneva_actions_configuration_target_key(
            target, key, request_options=request_options
        )
        return _response.data

    async def delete_api_v1geneva_actions_configuration_target_key(
        self, target: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        target : str

        key : str

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
            await client.configuration.delete_api_v1geneva_actions_configuration_target_key(
                target="target",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1geneva_actions_configuration_target_key(
            target, key, request_options=request_options
        )
        return _response.data
