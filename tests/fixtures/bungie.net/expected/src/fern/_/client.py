

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClient, RawClient
from .types.get_available_locales_response import GetAvailableLocalesResponse
from .types.get_common_settings_response import GetCommonSettingsResponse
from .types.get_global_alerts_response import GetGlobalAlertsResponse
from .types.get_user_system_overrides_response import GetUserSystemOverridesResponse


class Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClient
        """
        return self._raw_client

    def getavailablelocales(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAvailableLocalesResponse:
        """
        List of available localization cultures

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAvailableLocalesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client._.getavailablelocales()
        """
        _response = self._raw_client.getavailablelocales(request_options=request_options)
        return _response.data

    def getglobalalerts(
        self, *, includestreaming: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGlobalAlertsResponse:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Parameters
        ----------
        includestreaming : typing.Optional[bool]
            Determines whether Streaming Alerts are included in results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGlobalAlertsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client._.getglobalalerts()
        """
        _response = self._raw_client.getglobalalerts(includestreaming=includestreaming, request_options=request_options)
        return _response.data

    def getcommonsettings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCommonSettingsResponse:
        """
        Get the common settings used by the Bungie.Net environment.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCommonSettingsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client._.getcommonsettings()
        """
        _response = self._raw_client.getcommonsettings(request_options=request_options)
        return _response.data

    def getusersystemoverrides(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSystemOverridesResponse:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSystemOverridesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client._.getusersystemoverrides()
        """
        _response = self._raw_client.getusersystemoverrides(request_options=request_options)
        return _response.data


class AsyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClient
        """
        return self._raw_client

    async def getavailablelocales(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAvailableLocalesResponse:
        """
        List of available localization cultures

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAvailableLocalesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client._.getavailablelocales()


        asyncio.run(main())
        """
        _response = await self._raw_client.getavailablelocales(request_options=request_options)
        return _response.data

    async def getglobalalerts(
        self, *, includestreaming: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGlobalAlertsResponse:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Parameters
        ----------
        includestreaming : typing.Optional[bool]
            Determines whether Streaming Alerts are included in results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGlobalAlertsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client._.getglobalalerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.getglobalalerts(
            includestreaming=includestreaming, request_options=request_options
        )
        return _response.data

    async def getcommonsettings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCommonSettingsResponse:
        """
        Get the common settings used by the Bungie.Net environment.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCommonSettingsResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client._.getcommonsettings()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcommonsettings(request_options=request_options)
        return _response.data

    async def getusersystemoverrides(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserSystemOverridesResponse:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUserSystemOverridesResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client._.getusersystemoverrides()


        asyncio.run(main())
        """
        _response = await self._raw_client.getusersystemoverrides(request_options=request_options)
        return _response.data
