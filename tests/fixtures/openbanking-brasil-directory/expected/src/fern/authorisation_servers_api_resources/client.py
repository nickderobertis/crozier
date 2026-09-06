

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_resource import ApiResource
from ..types.api_resource_id import ApiResourceId
from ..types.api_resources import ApiResources
from ..types.authorisation_server_id import AuthorisationServerId
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawAuthorisationServersApiResourcesClient, RawAuthorisationServersApiResourcesClient


class AuthorisationServersApiResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorisationServersApiResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorisationServersApiResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorisationServersApiResourcesClient
        """
        return self._raw_client

    def get_all_api_resources_for_the_given_authorisation_server(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResources:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResources
            Authorisation server Api Resources response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.authorisation_servers_api_resources.get_all_api_resources_for_the_given_authorisation_server(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
        )
        """
        _response = self._raw_client.get_all_api_resources_for_the_given_authorisation_server(
            organisation_id, authorisation_server_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authorisation_server_api_resource_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResource:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResource
            Authorisation server Api Resource response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
            api_resource_id="ApiResourceId",
        )
        """
        _response = self._raw_client.get_an_authorisation_server_api_resource_by_id(
            organisation_id, authorisation_server_id, api_resource_id, request_options=request_options
        )
        return _response.data

    def get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResources:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResources
            Authorisation server Api Resources response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
        )
        """
        _response = (
            self._raw_client.get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
                organisation_id, authorisation_server_id, request_options=request_options
            )
        )
        return _response.data


class AsyncAuthorisationServersApiResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorisationServersApiResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorisationServersApiResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorisationServersApiResourcesClient
        """
        return self._raw_client

    async def get_all_api_resources_for_the_given_authorisation_server(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResources:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResources
            Authorisation server Api Resources response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.authorisation_servers_api_resources.get_all_api_resources_for_the_given_authorisation_server(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_api_resources_for_the_given_authorisation_server(
            organisation_id, authorisation_server_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authorisation_server_api_resource_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResource:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResource
            Authorisation server Api Resource response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
                api_resource_id="ApiResourceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authorisation_server_api_resource_by_id(
            organisation_id, authorisation_server_id, api_resource_id, request_options=request_options
        )
        return _response.data

    async def get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResources:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResources
            Authorisation server Api Resources response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            fapi_auth_date="YOUR_FAPI_AUTH_DATE",
            fapi_customer_ip_address="YOUR_FAPI_CUSTOMER_IP_ADDRESS",
            fapi_interaction_id="YOUR_FAPI_INTERACTION_ID",
            customer_user_agent="YOUR_CUSTOMER_USER_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.authorisation_servers_api_resources.get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.get_an_authorisation_server_api_resource_by_id_and_returns_the_latest_family_status(
                organisation_id, authorisation_server_id, request_options=request_options
            )
        )
        return _response.data
