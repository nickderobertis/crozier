

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.under_investigation_response_body import UnderInvestigationResponseBody
from .raw_client import AsyncRawResourcesClient, RawResourcesClient


class ResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResourcesClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_resources_resource_id_under_investigation(
        self, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnderInvestigationResponseBody:
        """
        Parameters
        ----------
        resource_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnderInvestigationResponseBody
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.resources.post_api_v1geneva_actions_resources_resource_id_under_investigation(
            resource_id="resourceId",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_resources_resource_id_under_investigation(
            resource_id, request_options=request_options
        )
        return _response.data


class AsyncResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResourcesClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_resources_resource_id_under_investigation(
        self, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnderInvestigationResponseBody:
        """
        Parameters
        ----------
        resource_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnderInvestigationResponseBody
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.resources.post_api_v1geneva_actions_resources_resource_id_under_investigation(
                resource_id="resourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_resources_resource_id_under_investigation(
            resource_id, request_options=request_options
        )
        return _response.data
