

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ap_is import ApIs
from ..types.api import Api
from ..types.metrics import Metrics
from .raw_client import AsyncRawApIsClient, RawApIsClient
from .types.get_providers_response import GetProvidersResponse
from .types.get_services_response import GetServicesResponse


class ApIsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApIsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApIsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApIsClient
        """
        return self._raw_client

    def list_ap_is(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApIs:
        """
        List all APIs in the directory.
        Returns links to the OpenAPI definitions for each API in the directory.
        If API exist in multiple versions `preferred` one is explicitly marked.
        Some basic info from the OpenAPI definition is cached inside each object.
        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIs
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.list_ap_is()
        """
        _response = self._raw_client.list_ap_is(request_options=request_options)
        return _response.data

    def get_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> Metrics:
        """
        Some basic metrics for the entire directory.
        Just stunning numbers to put on a front page and are intended purely for WoW effect :)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Metrics
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_metrics()
        """
        _response = self._raw_client.get_metrics(request_options=request_options)
        return _response.data

    def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProvidersResponse:
        """
        List all the providers in the directory

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProvidersResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_providers()
        """
        _response = self._raw_client.get_providers(request_options=request_options)
        return _response.data

    def get_api(self, provider: str, api: str, *, request_options: typing.Optional[RequestOptions] = None) -> Api:
        """
        Returns the API entry for one specific version of an API where there is no serviceName.

        Parameters
        ----------
        provider : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Api
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_api(
            provider="apis.guru",
            api="2.1.0",
        )
        """
        _response = self._raw_client.get_api(provider, api, request_options=request_options)
        return _response.data

    def get_service_api(
        self, provider: str, service: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Api:
        """
        Returns the API entry for one specific version of an API where there is a serviceName.

        Parameters
        ----------
        provider : str

        service : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Api
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_service_api(
            provider="apis.guru",
            service="graph",
            api="2.1.0",
        )
        """
        _response = self._raw_client.get_service_api(provider, service, api, request_options=request_options)
        return _response.data

    def get_provider(self, provider: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApIs:
        """
        List all APIs in the directory for a particular providerName
        Returns links to the individual API entry for each API.

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIs
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_provider(
            provider="apis.guru",
        )
        """
        _response = self._raw_client.get_provider(provider, request_options=request_options)
        return _response.data

    def get_services(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetServicesResponse:
        """
        List all serviceNames in the directory for a particular providerName

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServicesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ap_is.get_services(
            provider="apis.guru",
        )
        """
        _response = self._raw_client.get_services(provider, request_options=request_options)
        return _response.data


class AsyncApIsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApIsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApIsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApIsClient
        """
        return self._raw_client

    async def list_ap_is(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApIs:
        """
        List all APIs in the directory.
        Returns links to the OpenAPI definitions for each API in the directory.
        If API exist in multiple versions `preferred` one is explicitly marked.
        Some basic info from the OpenAPI definition is cached inside each object.
        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIs
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.list_ap_is()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ap_is(request_options=request_options)
        return _response.data

    async def get_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> Metrics:
        """
        Some basic metrics for the entire directory.
        Just stunning numbers to put on a front page and are intended purely for WoW effect :)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Metrics
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metrics(request_options=request_options)
        return _response.data

    async def get_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetProvidersResponse:
        """
        List all the providers in the directory

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProvidersResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_providers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_providers(request_options=request_options)
        return _response.data

    async def get_api(self, provider: str, api: str, *, request_options: typing.Optional[RequestOptions] = None) -> Api:
        """
        Returns the API entry for one specific version of an API where there is no serviceName.

        Parameters
        ----------
        provider : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Api
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_api(
                provider="apis.guru",
                api="2.1.0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api(provider, api, request_options=request_options)
        return _response.data

    async def get_service_api(
        self, provider: str, service: str, api: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Api:
        """
        Returns the API entry for one specific version of an API where there is a serviceName.

        Parameters
        ----------
        provider : str

        service : str

        api : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Api
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_service_api(
                provider="apis.guru",
                service="graph",
                api="2.1.0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_api(provider, service, api, request_options=request_options)
        return _response.data

    async def get_provider(self, provider: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApIs:
        """
        List all APIs in the directory for a particular providerName
        Returns links to the individual API entry for each API.

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIs
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_provider(
                provider="apis.guru",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider(provider, request_options=request_options)
        return _response.data

    async def get_services(
        self, provider: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetServicesResponse:
        """
        List all serviceNames in the directory for a particular providerName

        Parameters
        ----------
        provider : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetServicesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ap_is.get_services(
                provider="apis.guru",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_services(provider, request_options=request_options)
        return _response.data
