

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSystemConfigV1Alpha1ConsoleClient, RawSystemConfigV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class SystemConfigV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemConfigV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemConfigV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemConfigV1Alpha1ConsoleClient
        """
        return self._raw_client

    def get_system_config_by_group(
        self, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get system config by group

        Parameters
        ----------
        group : str
            Group of the system config

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.system_config_v1alpha1console.get_system_config_by_group(
            group="group",
        )
        """
        _response = self._raw_client.get_system_config_by_group(group, request_options=request_options)
        return _response.data

    def update_system_config_by_group(
        self,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update system config by group

        Parameters
        ----------
        group : str
            Group of the system config

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.system_config_v1alpha1console.update_system_config_by_group(
            group="group",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_system_config_by_group(
            group, request=request, request_options=request_options
        )
        return _response.data


class AsyncSystemConfigV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemConfigV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemConfigV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemConfigV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def get_system_config_by_group(
        self, group: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get system config by group

        Parameters
        ----------
        group : str
            Group of the system config

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.system_config_v1alpha1console.get_system_config_by_group(
                group="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_config_by_group(group, request_options=request_options)
        return _response.data

    async def update_system_config_by_group(
        self,
        group: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update system config by group

        Parameters
        ----------
        group : str
            Group of the system config

        request : typing.Dict[str, typing.Any]

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
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.system_config_v1alpha1console.update_system_config_by_group(
                group="group",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_system_config_by_group(
            group, request=request, request_options=request_options
        )
        return _response.data
