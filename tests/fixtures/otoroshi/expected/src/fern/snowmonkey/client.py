

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.done import Done
from ..types.empty import Empty
from ..types.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from ..types.outages_list import OutagesList
from ..types.patch_body import PatchBody
from .raw_client import AsyncRawSnowmonkeyClient, RawSnowmonkeyClient


OMIT = typing.cast(typing.Any, ...)


class SnowmonkeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnowmonkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnowmonkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnowmonkeyClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OutagesList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OutagesList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
        self,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        outage_duration_to: typing.Optional[float] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        times_per_day: typing.Optional[int] = OMIT,
        outage_duration_from: typing.Optional[float] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        include_user_facing_descriptors: typing.Optional[bool] = OMIT,
        target_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stop_time: typing.Optional[str] = OMIT,
        outage_strategy: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        dry_run : typing.Optional[bool]
            Whether or not outages will actualy impact requests

        outage_duration_to : typing.Optional[float]
            End of outage duration range

        chaos_config : typing.Optional[typing.Any]

        times_per_day : typing.Optional[int]
            Number of time per day each service will be outage

        outage_duration_from : typing.Optional[float]
            Start of outage duration range

        start_time : typing.Optional[str]
            Start time of Snow Monkey each day

        include_user_facing_descriptors : typing.Optional[bool]
            Whether or not user facing apps. will be impacted by Snow Monkey

        target_groups : typing.Optional[typing.Sequence[str]]
            Groups impacted by Snow Monkey. If empty, all groups will be impacted

        enabled : typing.Optional[bool]
            Whether or not this config is enabled

        stop_time : typing.Optional[str]
            Stop time of Snow Monkey each day

        outage_strategy : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
            dry_run=dry_run,
            outage_duration_to=outage_duration_to,
            chaos_config=chaos_config,
            times_per_day=times_per_day,
            outage_duration_from=outage_duration_from,
            start_time=start_time,
            include_user_facing_descriptors=include_user_facing_descriptors,
            target_groups=target_groups,
            enabled=enabled,
            stop_time=stop_time,
            outage_strategy=outage_strategy,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchDocument, PatchDocumentOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
            request=[
                PatchDocument(
                    op=PatchDocumentOp.ADD,
                    path="path",
                )
            ],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncSnowmonkeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnowmonkeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnowmonkeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnowmonkeyClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_start_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_stop_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OutagesList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OutagesList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_outages(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_reset_snow_monkey(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_get_snow_monkey_config(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
        self,
        *,
        dry_run: typing.Optional[bool] = OMIT,
        outage_duration_to: typing.Optional[float] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        times_per_day: typing.Optional[int] = OMIT,
        outage_duration_from: typing.Optional[float] = OMIT,
        start_time: typing.Optional[str] = OMIT,
        include_user_facing_descriptors: typing.Optional[bool] = OMIT,
        target_groups: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        stop_time: typing.Optional[str] = OMIT,
        outage_strategy: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        dry_run : typing.Optional[bool]
            Whether or not outages will actualy impact requests

        outage_duration_to : typing.Optional[float]
            End of outage duration range

        chaos_config : typing.Optional[typing.Any]

        times_per_day : typing.Optional[int]
            Number of time per day each service will be outage

        outage_duration_from : typing.Optional[float]
            Start of outage duration range

        start_time : typing.Optional[str]
            Start time of Snow Monkey each day

        include_user_facing_descriptors : typing.Optional[bool]
            Whether or not user facing apps. will be impacted by Snow Monkey

        target_groups : typing.Optional[typing.Sequence[str]]
            Groups impacted by Snow Monkey. If empty, all groups will be impacted

        enabled : typing.Optional[bool]
            Whether or not this config is enabled

        stop_time : typing.Optional[str]
            Stop time of Snow Monkey each day

        outage_strategy : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_update_snow_monkey(
            dry_run=dry_run,
            outage_duration_to=outage_duration_to,
            chaos_config=chaos_config,
            times_per_day=times_per_day,
            outage_duration_from=outage_duration_from,
            start_time=start_time,
            include_user_facing_descriptors=include_user_facing_descriptors,
            target_groups=target_groups,
            enabled=enabled,
            stop_time=stop_time,
            outage_strategy=outage_strategy,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsSnowMonkeyConfig:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsSnowMonkeyConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchDocument, PatchDocumentOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snowmonkey.otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
                request=[
                    PatchDocument(
                        op=PatchDocumentOp.ADD,
                        path="path",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_snow_monkey_controller_patch_snow_monkey(
            request=request, request_options=request_options
        )
        return _response.data
