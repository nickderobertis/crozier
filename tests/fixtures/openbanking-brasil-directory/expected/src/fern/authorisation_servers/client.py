

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_server import AuthorisationServer
from ..types.authorisation_server_id import AuthorisationServerId
from ..types.authorisation_servers import AuthorisationServers
from ..types.organisation_id import OrganisationId
from .raw_client import AsyncRawAuthorisationServersClient, RawAuthorisationServersClient


class AuthorisationServersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthorisationServersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthorisationServersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthorisationServersClient
        """
        return self._raw_client

    def get_all_authorisation_servers_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServers:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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
        AuthorisationServers
            All authorisation servers for the org

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
        client.authorisation_servers.get_all_authorisation_servers_for_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_all_authorisation_servers_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authorisation_server_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServer:
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
        AuthorisationServer
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
        client.authorisation_servers.get_an_authorisation_server_by_id(
            organisation_id="OrganisationId",
            authorisation_server_id="AuthorisationServerId",
        )
        """
        _response = self._raw_client.get_an_authorisation_server_by_id(
            organisation_id, authorisation_server_id, request_options=request_options
        )
        return _response.data


class AsyncAuthorisationServersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthorisationServersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthorisationServersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthorisationServersClient
        """
        return self._raw_client

    async def get_all_authorisation_servers_for_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServers:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

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
        AuthorisationServers
            All authorisation servers for the org

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
            await client.authorisation_servers.get_all_authorisation_servers_for_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_authorisation_servers_for_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authorisation_server_by_id(
        self,
        organisation_id: OrganisationId,
        authorisation_server_id: AuthorisationServerId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationServer:
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
        AuthorisationServer
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
            await client.authorisation_servers.get_an_authorisation_server_by_id(
                organisation_id="OrganisationId",
                authorisation_server_id="AuthorisationServerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authorisation_server_by_id(
            organisation_id, authorisation_server_id, request_options=request_options
        )
        return _response.data
