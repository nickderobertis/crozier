

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawPlansClient, RawPlansClient
from .types.get_site_plan_plans_response import GetSitePlanPlansResponse


class PlansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlansClient
        """
        return self._raw_client

    def get_site_plan(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSitePlanPlansResponse:
        """
        Get site plan details for the specified Site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSitePlanPlansResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.sites.plans.get_site_plan(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.get_site_plan(site_id, request_options=request_options)
        return _response.data


class AsyncPlansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlansClient
        """
        return self._raw_client

    async def get_site_plan(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSitePlanPlansResponse:
        """
        Get site plan details for the specified Site.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSitePlanPlansResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sites.plans.get_site_plan(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_site_plan(site_id, request_options=request_options)
        return _response.data
