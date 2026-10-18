

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.realtime_config_response_output import RealtimeConfigResponseOutput
from .raw_client import AsyncRawRealtimeClient, RawRealtimeClient


OMIT = typing.cast(typing.Any, ...)


class RealtimeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRealtimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRealtimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRealtimeClient
        """
        return self._raw_client

    def v1get_realtime_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RealtimeConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RealtimeConfigResponseOutput
            Gets project's realtime configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.realtime.v1get_realtime_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_realtime_config(ref, request_options=request_options)
        return _response.data

    def v1update_realtime_config(
        self,
        ref: str,
        *,
        private_only: typing.Optional[bool] = OMIT,
        connection_pool: typing.Optional[int] = OMIT,
        postgres_changes_pool: typing.Optional[int] = OMIT,
        max_concurrent_users: typing.Optional[int] = OMIT,
        max_events_per_second: typing.Optional[int] = OMIT,
        max_bytes_per_second: typing.Optional[int] = OMIT,
        max_channels_per_client: typing.Optional[int] = OMIT,
        max_joins_per_second: typing.Optional[int] = OMIT,
        max_presence_events_per_second: typing.Optional[int] = OMIT,
        max_payload_size_in_kb: typing.Optional[int] = OMIT,
        suspend: typing.Optional[bool] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        private_only : typing.Optional[bool]
            Whether to only allow private channels

        connection_pool : typing.Optional[int]
            Sets connection pool size for Realtime Authorization

        postgres_changes_pool : typing.Optional[int]
            Sets connection pool size used to create Postgres Changes subscriptions

        max_concurrent_users : typing.Optional[int]
            Sets maximum number of concurrent users rate limit

        max_events_per_second : typing.Optional[int]
            Sets maximum number of events per second rate per channel limit

        max_bytes_per_second : typing.Optional[int]
            Sets maximum number of bytes per second rate per channel limit

        max_channels_per_client : typing.Optional[int]
            Sets maximum number of channels per client rate limit

        max_joins_per_second : typing.Optional[int]
            Sets maximum number of joins per second rate limit

        max_presence_events_per_second : typing.Optional[int]
            Sets maximum number of presence events per second rate limit

        max_payload_size_in_kb : typing.Optional[int]
            Sets maximum number of payload size in KB rate limit

        suspend : typing.Optional[bool]
            Disables the Realtime service for this project when true. Set to false to re-enable it.

        presence_enabled : typing.Optional[bool]
            Whether to enable presence

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
        client.realtime.v1update_realtime_config(
            ref="abcdefghijklmnopqrst",
            private_only=False,
            max_concurrent_users=1000,
            max_channels_per_client=100,
        )
        """
        _response = self._raw_client.v1update_realtime_config(
            ref,
            private_only=private_only,
            connection_pool=connection_pool,
            postgres_changes_pool=postgres_changes_pool,
            max_concurrent_users=max_concurrent_users,
            max_events_per_second=max_events_per_second,
            max_bytes_per_second=max_bytes_per_second,
            max_channels_per_client=max_channels_per_client,
            max_joins_per_second=max_joins_per_second,
            max_presence_events_per_second=max_presence_events_per_second,
            max_payload_size_in_kb=max_payload_size_in_kb,
            suspend=suspend,
            presence_enabled=presence_enabled,
            request_options=request_options,
        )
        return _response.data

    def v1shutdown_realtime(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.realtime.v1shutdown_realtime(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1shutdown_realtime(ref, request_options=request_options)
        return _response.data


class AsyncRealtimeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRealtimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRealtimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRealtimeClient
        """
        return self._raw_client

    async def v1get_realtime_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RealtimeConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RealtimeConfigResponseOutput
            Gets project's realtime configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.realtime.v1get_realtime_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_realtime_config(ref, request_options=request_options)
        return _response.data

    async def v1update_realtime_config(
        self,
        ref: str,
        *,
        private_only: typing.Optional[bool] = OMIT,
        connection_pool: typing.Optional[int] = OMIT,
        postgres_changes_pool: typing.Optional[int] = OMIT,
        max_concurrent_users: typing.Optional[int] = OMIT,
        max_events_per_second: typing.Optional[int] = OMIT,
        max_bytes_per_second: typing.Optional[int] = OMIT,
        max_channels_per_client: typing.Optional[int] = OMIT,
        max_joins_per_second: typing.Optional[int] = OMIT,
        max_presence_events_per_second: typing.Optional[int] = OMIT,
        max_payload_size_in_kb: typing.Optional[int] = OMIT,
        suspend: typing.Optional[bool] = OMIT,
        presence_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        private_only : typing.Optional[bool]
            Whether to only allow private channels

        connection_pool : typing.Optional[int]
            Sets connection pool size for Realtime Authorization

        postgres_changes_pool : typing.Optional[int]
            Sets connection pool size used to create Postgres Changes subscriptions

        max_concurrent_users : typing.Optional[int]
            Sets maximum number of concurrent users rate limit

        max_events_per_second : typing.Optional[int]
            Sets maximum number of events per second rate per channel limit

        max_bytes_per_second : typing.Optional[int]
            Sets maximum number of bytes per second rate per channel limit

        max_channels_per_client : typing.Optional[int]
            Sets maximum number of channels per client rate limit

        max_joins_per_second : typing.Optional[int]
            Sets maximum number of joins per second rate limit

        max_presence_events_per_second : typing.Optional[int]
            Sets maximum number of presence events per second rate limit

        max_payload_size_in_kb : typing.Optional[int]
            Sets maximum number of payload size in KB rate limit

        suspend : typing.Optional[bool]
            Disables the Realtime service for this project when true. Set to false to re-enable it.

        presence_enabled : typing.Optional[bool]
            Whether to enable presence

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
            await client.realtime.v1update_realtime_config(
                ref="abcdefghijklmnopqrst",
                private_only=False,
                max_concurrent_users=1000,
                max_channels_per_client=100,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_realtime_config(
            ref,
            private_only=private_only,
            connection_pool=connection_pool,
            postgres_changes_pool=postgres_changes_pool,
            max_concurrent_users=max_concurrent_users,
            max_events_per_second=max_events_per_second,
            max_bytes_per_second=max_bytes_per_second,
            max_channels_per_client=max_channels_per_client,
            max_joins_per_second=max_joins_per_second,
            max_presence_events_per_second=max_presence_events_per_second,
            max_payload_size_in_kb=max_payload_size_in_kb,
            suspend=suspend,
            presence_enabled=presence_enabled,
            request_options=request_options,
        )
        return _response.data

    async def v1shutdown_realtime(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.realtime.v1shutdown_realtime(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1shutdown_realtime(ref, request_options=request_options)
        return _response.data
