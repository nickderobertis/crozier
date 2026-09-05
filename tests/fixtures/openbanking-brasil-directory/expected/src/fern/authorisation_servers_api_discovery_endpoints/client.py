

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_discovery_endpoint import ApiDiscoveryEndpoint
from ..types.api_discovery_endpoints import ApiDiscoveryEndpoints
from ..types.api_endpoint_id import ApiEndpointId
from ..types.api_resource_id import ApiResourceId
from ..types.authorisation_server_id import AuthorisationServerId
from ..types.organisation_id import OrganisationId
from .raw_client import (
    AsyncRawAuthorisationServersApiDiscoveryEndpointsClient,
    RawAuthorisationServersApiDiscoveryEndpointsClient,
)


class AuthorisationServersApiDiscoveryEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorisationServersApiDiscoveryEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorisationServersApiDiscoveryEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorisationServersApiDiscoveryEndpointsClient
        """
        return self._raw_client

    def get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiDiscoveryEndpoints:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

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
        ApiDiscoveryEndpoints
            Authorisation server response

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
        client.authorisation_servers_api_discovery_endpoints.get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
            api_resource_id="ApiResourceId",
        )
        """
        _response = self._raw_client.get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
            organisation_id,
            authorisation_server_id,
            api_resource_id,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def get_an_authorisation_server_api_discovery_endpoint_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        api_discovery_endpoint_id: ApiEndpointId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiDiscoveryEndpoint:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

        api_discovery_endpoint_id : ApiEndpointId
            The api discovery endpoint Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiDiscoveryEndpoint
            Authorisation server response

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
        client.authorisation_servers_api_discovery_endpoints.get_an_authorisation_server_api_discovery_endpoint_by_id(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
            api_resource_id="ApiResourceId",
            api_discovery_endpoint_id="ApiDiscoveryEndpointId",
        )
        """
        _response = self._raw_client.get_an_authorisation_server_api_discovery_endpoint_by_id(
            organisation_id,
            authorisation_server_id,
            api_resource_id,
            api_discovery_endpoint_id,
            request_options=request_options,
        )
        return _response.data


class AsyncAuthorisationServersApiDiscoveryEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorisationServersApiDiscoveryEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorisationServersApiDiscoveryEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorisationServersApiDiscoveryEndpointsClient
        """
        return self._raw_client

    async def get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiDiscoveryEndpoints:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

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
        ApiDiscoveryEndpoints
            Authorisation server response

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
            await client.authorisation_servers_api_discovery_endpoints.get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
                api_resource_id="ApiResourceId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.get_all_api_discovery_endpoints_for_the_given_authorisation_server_and_api_version(
                organisation_id,
                authorisation_server_id,
                api_resource_id,
                page=page,
                size=size,
                sort=sort,
                request_options=request_options,
            )
        )
        return _response.data

    async def get_an_authorisation_server_api_discovery_endpoint_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        api_resource_id: ApiResourceId,
        api_discovery_endpoint_id: ApiEndpointId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiDiscoveryEndpoint:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_server_id : AuthorisationServerId
            The authorisation server Id

        api_resource_id : ApiResourceId
            The api version Id

        api_discovery_endpoint_id : ApiEndpointId
            The api discovery endpoint Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiDiscoveryEndpoint
            Authorisation server response

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
            await client.authorisation_servers_api_discovery_endpoints.get_an_authorisation_server_api_discovery_endpoint_by_id(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
                api_resource_id="ApiResourceId",
                api_discovery_endpoint_id="ApiDiscoveryEndpointId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authorisation_server_api_discovery_endpoint_by_id(
            organisation_id,
            authorisation_server_id,
            api_resource_id,
            api_discovery_endpoint_id,
            request_options=request_options,
        )
        return _response.data
