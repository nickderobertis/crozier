

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_company_name_listing import UserCompanyNameListing
from .raw_client import AsyncRawNameClient, RawNameClient


class NameClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNameClient
        """
        return self._raw_client

    def list_all_name_for_user_company(
        self, user_company_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserCompanyNameListing]:
        """
        Return all the known (trade) names for a specific user company.

        Parameters
        ----------
        user_company_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserCompanyNameListing]
            Endpoint for getting all the known (trade) names for a user company. This is needed for updating the user name, as we only accept legal or trade names.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.name.list_all_name_for_user_company(
            user_company_id=1,
        )
        """
        _response = self._raw_client.list_all_name_for_user_company(user_company_id, request_options=request_options)
        return _response.data


class AsyncNameClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNameClient
        """
        return self._raw_client

    async def list_all_name_for_user_company(
        self, user_company_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[UserCompanyNameListing]:
        """
        Return all the known (trade) names for a specific user company.

        Parameters
        ----------
        user_company_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserCompanyNameListing]
            Endpoint for getting all the known (trade) names for a user company. This is needed for updating the user name, as we only accept legal or trade names.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.name.list_all_name_for_user_company(
                user_company_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_name_for_user_company(
            user_company_id, request_options=request_options
        )
        return _response.data
