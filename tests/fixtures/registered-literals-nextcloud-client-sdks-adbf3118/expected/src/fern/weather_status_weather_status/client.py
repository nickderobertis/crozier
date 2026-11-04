

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_reference_api_touch_provider200response import CoreReferenceApiTouchProvider200Response
from ..types.provisioning_api_groups_get_sub_admins_of_group200response import (
    ProvisioningApiGroupsGetSubAdminsOfGroup200Response,
)
from ..types.weather_status_weather_status_get_forecast200response import (
    WeatherStatusWeatherStatusGetForecast200Response,
)
from ..types.weather_status_weather_status_get_location200response import (
    WeatherStatusWeatherStatusGetLocation200Response,
)
from ..types.weather_status_weather_status_use_personal_address200response import (
    WeatherStatusWeatherStatusUsePersonalAddress200Response,
)
from .raw_client import AsyncRawWeatherStatusWeatherStatusClient, RawWeatherStatusWeatherStatusClient


class WeatherStatusWeatherStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWeatherStatusWeatherStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWeatherStatusWeatherStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWeatherStatusWeatherStatusClient
        """
        return self._raw_client

    def set_mode(
        self, *, mode: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        mode : int
            New mode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.set_mode(
            mode=1000000,
        )
        """
        _response = self._raw_client.set_mode(mode=mode, request_options=request_options)
        return _response.data

    def use_personal_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusUsePersonalAddress200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusUsePersonalAddress200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.use_personal_address()
        """
        _response = self._raw_client.use_personal_address(request_options=request_options)
        return _response.data

    def get_location(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusGetLocation200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusGetLocation200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.get_location()
        """
        _response = self._raw_client.get_location(request_options=request_options)
        return _response.data

    def set_location(
        self,
        *,
        address: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lon: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WeatherStatusWeatherStatusUsePersonalAddress200Response:
        """
        Parameters
        ----------
        address : typing.Optional[str]
            Any approximative or exact address

        lat : typing.Optional[float]
            Latitude in decimal degree format

        lon : typing.Optional[float]
            Longitude in decimal degree format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusUsePersonalAddress200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.set_location()
        """
        _response = self._raw_client.set_location(address=address, lat=lat, lon=lon, request_options=request_options)
        return _response.data

    def get_forecast(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusGetForecast200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusGetForecast200Response
            Forecast returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.get_forecast()
        """
        _response = self._raw_client.get_forecast(request_options=request_options)
        return _response.data

    def get_favorites(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.get_favorites()
        """
        _response = self._raw_client.get_favorites(request_options=request_options)
        return _response.data

    def set_favorites(
        self, *, favorites: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        favorites : str
            Favorite addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.weather_status_weather_status.set_favorites(
            favorites="favorites",
        )
        """
        _response = self._raw_client.set_favorites(favorites=favorites, request_options=request_options)
        return _response.data


class AsyncWeatherStatusWeatherStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWeatherStatusWeatherStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWeatherStatusWeatherStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWeatherStatusWeatherStatusClient
        """
        return self._raw_client

    async def set_mode(
        self, *, mode: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        mode : int
            New mode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.set_mode(
                mode=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mode(mode=mode, request_options=request_options)
        return _response.data

    async def use_personal_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusUsePersonalAddress200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusUsePersonalAddress200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.use_personal_address()


        asyncio.run(main())
        """
        _response = await self._raw_client.use_personal_address(request_options=request_options)
        return _response.data

    async def get_location(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusGetLocation200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusGetLocation200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.get_location()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_location(request_options=request_options)
        return _response.data

    async def set_location(
        self,
        *,
        address: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        lon: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WeatherStatusWeatherStatusUsePersonalAddress200Response:
        """
        Parameters
        ----------
        address : typing.Optional[str]
            Any approximative or exact address

        lat : typing.Optional[float]
            Latitude in decimal degree format

        lon : typing.Optional[float]
            Longitude in decimal degree format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusUsePersonalAddress200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.set_location()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_location(
            address=address, lat=lat, lon=lon, request_options=request_options
        )
        return _response.data

    async def get_forecast(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WeatherStatusWeatherStatusGetForecast200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WeatherStatusWeatherStatusGetForecast200Response
            Forecast returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.get_forecast()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_forecast(request_options=request_options)
        return _response.data

    async def get_favorites(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvisioningApiGroupsGetSubAdminsOfGroup200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisioningApiGroupsGetSubAdminsOfGroup200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.get_favorites()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_favorites(request_options=request_options)
        return _response.data

    async def set_favorites(
        self, *, favorites: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreReferenceApiTouchProvider200Response:
        """
        Parameters
        ----------
        favorites : str
            Favorite addresses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreReferenceApiTouchProvider200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.weather_status_weather_status.set_favorites(
                favorites="favorites",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_favorites(favorites=favorites, request_options=request_options)
        return _response.data
