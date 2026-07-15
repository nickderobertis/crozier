

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_api_resource_coverage_response import GetApiResourceCoverageResponse
from ..types.get_api_resource_response import GetApiResourceResponse
from .raw_client import AsyncRawApiResourcesClient, RawApiResourcesClient


class ApiResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiResourcesClient
        """
        return self._raw_client

    def one(
        self, id: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiResourceResponse:
        """
        Get API Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResourceResponse
            ApiResources

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.api_resources.one(
            id="id",
            resource_id="resource_id",
        )
        """
        _response = self._raw_client.one(id, resource_id, request_options=request_options)
        return _response.data

    def api_resource_coverage_one(
        self, id: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiResourceCoverageResponse:
        """
        Get API Resource Coverage

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResourceCoverageResponse
            ApiResources

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.api_resources.api_resource_coverage_one(
            id="id",
            resource_id="resource_id",
        )
        """
        _response = self._raw_client.api_resource_coverage_one(id, resource_id, request_options=request_options)
        return _response.data


class AsyncApiResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiResourcesClient
        """
        return self._raw_client

    async def one(
        self, id: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiResourceResponse:
        """
        Get API Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResourceResponse
            ApiResources

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_resources.one(
                id="id",
                resource_id="resource_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, resource_id, request_options=request_options)
        return _response.data

    async def api_resource_coverage_one(
        self, id: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiResourceCoverageResponse:
        """
        Get API Resource Coverage

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiResourceCoverageResponse
            ApiResources

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.api_resources.api_resource_coverage_one(
                id="id",
                resource_id="resource_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.api_resource_coverage_one(id, resource_id, request_options=request_options)
        return _response.data
