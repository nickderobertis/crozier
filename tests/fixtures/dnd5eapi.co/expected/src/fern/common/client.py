

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_reference_list import ApiReferenceList
from .raw_client import AsyncRawCommonClient, RawCommonClient
from .types.get_api_endpoint_request_endpoint import GetApiEndpointRequestEndpoint


class CommonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommonClient
        """
        return self._raw_client

    def get_all_resource_ur_ls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Making a request to the API's base URL returns an object containing available endpoints.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.common.get_all_resource_ur_ls()
        """
        _response = self._raw_client.get_all_resource_ur_ls(request_options=request_options)
        return _response.data

    def get_list_of_all_available_resources_for_an_endpoint(
        self, endpoint: GetApiEndpointRequestEndpoint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Currently only the [`/spells`](#get-/api/spells) and [`/monsters`](#get-/api/monsters) endpoints support filtering with query parameters. Use of these query parameters is documented under the respective [Spells](#tag--Spells) and [Monsters](#tag--Monsters) sections.

        Parameters
        ----------
        endpoint : GetApiEndpointRequestEndpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        from fern.common import GetApiEndpointRequestEndpoint

        from fern import FernApi

        client = FernApi()
        client.common.get_list_of_all_available_resources_for_an_endpoint(
            endpoint=GetApiEndpointRequestEndpoint.ABILITY_SCORES,
        )
        """
        _response = self._raw_client.get_list_of_all_available_resources_for_an_endpoint(
            endpoint, request_options=request_options
        )
        return _response.data


class AsyncCommonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommonClient
        """
        return self._raw_client

    async def get_all_resource_ur_ls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Making a request to the API's base URL returns an object containing available endpoints.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.common.get_all_resource_ur_ls()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_resource_ur_ls(request_options=request_options)
        return _response.data

    async def get_list_of_all_available_resources_for_an_endpoint(
        self, endpoint: GetApiEndpointRequestEndpoint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiReferenceList:
        """
        Currently only the [`/spells`](#get-/api/spells) and [`/monsters`](#get-/api/monsters) endpoints support filtering with query parameters. Use of these query parameters is documented under the respective [Spells](#tag--Spells) and [Monsters](#tag--Monsters) sections.

        Parameters
        ----------
        endpoint : GetApiEndpointRequestEndpoint

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiReferenceList
            OK

        Examples
        --------
        import asyncio

        from fern.common import GetApiEndpointRequestEndpoint

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.common.get_list_of_all_available_resources_for_an_endpoint(
                endpoint=GetApiEndpointRequestEndpoint.ABILITY_SCORES,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_list_of_all_available_resources_for_an_endpoint(
            endpoint, request_options=request_options
        )
        return _response.data
