

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSettingsClient, RawSettingsClient
from .types.get_settings_response import GetSettingsResponse
from .types.replace_settings_request_services import ReplaceSettingsRequestServices
from .types.replace_settings_request_system import ReplaceSettingsRequestSystem
from .types.replace_settings_response import ReplaceSettingsResponse
from .types.update_settings_request_services import UpdateSettingsRequestServices
from .types.update_settings_request_system import UpdateSettingsRequestSystem
from .types.update_settings_response import UpdateSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class SettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSettingsClient
        """
        return self._raw_client

    def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSettingsResponse:
        """
        Reads the current configuration. Most settings apply dynamically without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSettingsResponse
            Current settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.settings.get_settings()
        """
        _response = self._raw_client.get_settings(request_options=request_options)
        return _response.data

    def replace_settings(
        self,
        *,
        system: typing.Optional[ReplaceSettingsRequestSystem] = OMIT,
        services: typing.Optional[ReplaceSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceSettingsResponse:
        """
        Replaces the entire configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[ReplaceSettingsRequestSystem]

        services : typing.Optional[ReplaceSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceSettingsResponse
            Replaced settings

        Examples
        --------
        from fern.settings import (
            ReplaceSettingsRequestServices,
            ReplaceSettingsRequestSystem,
        )

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.settings.replace_settings(
            system=ReplaceSettingsRequestSystem(
                name="Plant A",
                host_name="whatwatt_9F8124",
                protection=False,
            ),
            services=ReplaceSettingsRequestServices(
                report_interval=30,
                log=True,
            ),
        )
        """
        _response = self._raw_client.replace_settings(system=system, services=services, request_options=request_options)
        return _response.data

    def update_settings(
        self,
        *,
        system: typing.Optional[UpdateSettingsRequestSystem] = OMIT,
        services: typing.Optional[UpdateSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSettingsResponse:
        """
        Partially updates the configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[UpdateSettingsRequestSystem]

        services : typing.Optional[UpdateSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSettingsResponse
            Updated settings

        Examples
        --------
        from fern.settings import (
            UpdateSettingsRequestServices,
            UpdateSettingsRequestSystem,
        )

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.settings.update_settings(
            system=UpdateSettingsRequestSystem(
                host_name="whatwatt_9F8124",
                protection=True,
            ),
            services=UpdateSettingsRequestServices(
                report_interval=15,
            ),
        )
        """
        _response = self._raw_client.update_settings(system=system, services=services, request_options=request_options)
        return _response.data


class AsyncSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSettingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSettingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSettingsClient
        """
        return self._raw_client

    async def get_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetSettingsResponse:
        """
        Reads the current configuration. Most settings apply dynamically without reboot.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSettingsResponse
            Current settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.settings.get_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_settings(request_options=request_options)
        return _response.data

    async def replace_settings(
        self,
        *,
        system: typing.Optional[ReplaceSettingsRequestSystem] = OMIT,
        services: typing.Optional[ReplaceSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceSettingsResponse:
        """
        Replaces the entire configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[ReplaceSettingsRequestSystem]

        services : typing.Optional[ReplaceSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceSettingsResponse
            Replaced settings

        Examples
        --------
        import asyncio

        from fern.settings import (
            ReplaceSettingsRequestServices,
            ReplaceSettingsRequestSystem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.settings.replace_settings(
                system=ReplaceSettingsRequestSystem(
                    name="Plant A",
                    host_name="whatwatt_9F8124",
                    protection=False,
                ),
                services=ReplaceSettingsRequestServices(
                    report_interval=30,
                    log=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_settings(
            system=system, services=services, request_options=request_options
        )
        return _response.data

    async def update_settings(
        self,
        *,
        system: typing.Optional[UpdateSettingsRequestSystem] = OMIT,
        services: typing.Optional[UpdateSettingsRequestServices] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSettingsResponse:
        """
        Partially updates the configuration object. Values apply dynamically.

        Parameters
        ----------
        system : typing.Optional[UpdateSettingsRequestSystem]

        services : typing.Optional[UpdateSettingsRequestServices]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSettingsResponse
            Updated settings

        Examples
        --------
        import asyncio

        from fern.settings import (
            UpdateSettingsRequestServices,
            UpdateSettingsRequestSystem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.settings.update_settings(
                system=UpdateSettingsRequestSystem(
                    host_name="whatwatt_9F8124",
                    protection=True,
                ),
                services=UpdateSettingsRequestServices(
                    report_interval=15,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_settings(
            system=system, services=services, request_options=request_options
        )
        return _response.data
