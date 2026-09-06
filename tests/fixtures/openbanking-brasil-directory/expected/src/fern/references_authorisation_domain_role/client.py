

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_domain_role import AuthorisationDomainRole
from ..types.authorisation_domain_role_name import AuthorisationDomainRoleName
from ..types.authorisation_domain_roles_page import AuthorisationDomainRolesPage
from .raw_client import AsyncRawReferencesAuthorisationDomainRoleClient, RawReferencesAuthorisationDomainRoleClient


class ReferencesAuthorisationDomainRoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesAuthorisationDomainRoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesAuthorisationDomainRoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesAuthorisationDomainRoleClient
        """
        return self._raw_client

    def reference_data_of_all_authorisation_domain_roles(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainRolesPage:
        """
        Parameters
        ----------
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
        AuthorisationDomainRolesPage
            All data of authorisation domains mapped to an authority

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
        client.references_authorisation_domain_role.reference_data_of_all_authorisation_domain_roles()
        """
        _response = self._raw_client.reference_data_of_all_authorisation_domain_roles(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authorisation_domain_role_by_name(
        self,
        authorisation_domain_role_name: AuthorisationDomainRoleName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainRole:
        """
        Parameters
        ----------
        authorisation_domain_role_name : AuthorisationDomainRoleName
            Authorisation Domain Role Name. Eg:TPP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationDomainRole
            Role data

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
        client.references_authorisation_domain_role.get_an_authorisation_domain_role_by_name(
            authorisation_domain_role_name="PAGTO",
        )
        """
        _response = self._raw_client.get_an_authorisation_domain_role_by_name(
            authorisation_domain_role_name, request_options=request_options
        )
        return _response.data


class AsyncReferencesAuthorisationDomainRoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesAuthorisationDomainRoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesAuthorisationDomainRoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesAuthorisationDomainRoleClient
        """
        return self._raw_client

    async def reference_data_of_all_authorisation_domain_roles(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainRolesPage:
        """
        Parameters
        ----------
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
        AuthorisationDomainRolesPage
            All data of authorisation domains mapped to an authority

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
            await client.references_authorisation_domain_role.reference_data_of_all_authorisation_domain_roles()


        asyncio.run(main())
        """
        _response = await self._raw_client.reference_data_of_all_authorisation_domain_roles(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authorisation_domain_role_by_name(
        self,
        authorisation_domain_role_name: AuthorisationDomainRoleName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainRole:
        """
        Parameters
        ----------
        authorisation_domain_role_name : AuthorisationDomainRoleName
            Authorisation Domain Role Name. Eg:TPP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationDomainRole
            Role data

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
            await client.references_authorisation_domain_role.get_an_authorisation_domain_role_by_name(
                authorisation_domain_role_name="PAGTO",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authorisation_domain_role_by_name(
            authorisation_domain_role_name, request_options=request_options
        )
        return _response.data
