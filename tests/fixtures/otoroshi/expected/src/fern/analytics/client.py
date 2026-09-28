

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAnalyticsClient, RawAnalyticsClient


OMIT = typing.cast(typing.Any, ...)


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_analytics_controller_global_stats(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_analytics_controller_global_stats()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_global_stats(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_global_status(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_analytics_controller_global_status()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_global_status(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_filterable_stats(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_analytics_controller_filterable_stats()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_filterable_stats(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_filterable_events(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_analytics_controller_filterable_events()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_filterable_events(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_template_spec(
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
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_templates_controller_template_spec()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_template_spec(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_services_status(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.analytics.otoroshi_controllers_adminapi_analytics_controller_services_status(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_services_status(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_analytics_controller_global_stats(
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
            await client.analytics.otoroshi_controllers_adminapi_analytics_controller_global_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_global_stats(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_global_status(
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
            await client.analytics.otoroshi_controllers_adminapi_analytics_controller_global_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_global_status(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_filterable_stats(
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
            await client.analytics.otoroshi_controllers_adminapi_analytics_controller_filterable_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_filterable_stats(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_filterable_events(
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
            await client.analytics.otoroshi_controllers_adminapi_analytics_controller_filterable_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_filterable_events(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_template_spec(
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
            await client.analytics.otoroshi_controllers_adminapi_templates_controller_template_spec()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_template_spec(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_services_status(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.analytics.otoroshi_controllers_adminapi_analytics_controller_services_status(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_services_status(
            request=request, request_options=request_options
        )
        return _response.data
