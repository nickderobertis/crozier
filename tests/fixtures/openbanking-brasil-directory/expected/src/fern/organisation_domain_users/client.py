

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_domain_name import AuthorisationDomainName
from ..types.authorisation_domain_users_page import AuthorisationDomainUsersPage
from ..types.organisation_id import OrganisationId
from ..types.user_email_id import UserEmailId
from .raw_client import AsyncRawOrganisationDomainUsersClient, RawOrganisationDomainUsersClient


class OrganisationDomainUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationDomainUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationDomainUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationDomainUsersClient
        """
        return self._raw_client

    def all_users_for_the_given_authorisation_domain(
        self,
        organisation_id: OrganisationId,
        authorisation_domain_name: AuthorisationDomainName,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainUsersPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

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
        AuthorisationDomainUsersPage
            All users belonging to an authorisation domain

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
        client.organisation_domain_users.all_users_for_the_given_authorisation_domain(
            organisation_id="OrganisationId",
            authorisation_domain_name="AuthorisationDomainName",
        )
        """
        _response = self._raw_client.all_users_for_the_given_authorisation_domain(
            organisation_id, authorisation_domain_name, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def authorisation_domain_user_details(
        self,
        organisation_id: OrganisationId,
        authorisation_domain_name: AuthorisationDomainName,
        user_email_id: UserEmailId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainUsersPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

        user_email_id : UserEmailId
            Email address of the super user

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
        AuthorisationDomainUsersPage
            All users belonging to an authorisation domain

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
        client.organisation_domain_users.authorisation_domain_user_details(
            organisation_id="OrganisationId",
            authorisation_domain_name="AuthorisationDomainName",
            user_email_id="UserEmailId",
        )
        """
        _response = self._raw_client.authorisation_domain_user_details(
            organisation_id,
            authorisation_domain_name,
            user_email_id,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data


class AsyncOrganisationDomainUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationDomainUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationDomainUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationDomainUsersClient
        """
        return self._raw_client

    async def all_users_for_the_given_authorisation_domain(
        self,
        organisation_id: OrganisationId,
        authorisation_domain_name: AuthorisationDomainName,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainUsersPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

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
        AuthorisationDomainUsersPage
            All users belonging to an authorisation domain

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
            await client.organisation_domain_users.all_users_for_the_given_authorisation_domain(
                organisation_id="OrganisationId",
                authorisation_domain_name="AuthorisationDomainName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_users_for_the_given_authorisation_domain(
            organisation_id, authorisation_domain_name, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def authorisation_domain_user_details(
        self,
        organisation_id: OrganisationId,
        authorisation_domain_name: AuthorisationDomainName,
        user_email_id: UserEmailId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainUsersPage:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

        user_email_id : UserEmailId
            Email address of the super user

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
        AuthorisationDomainUsersPage
            All users belonging to an authorisation domain

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
            await client.organisation_domain_users.authorisation_domain_user_details(
                organisation_id="OrganisationId",
                authorisation_domain_name="AuthorisationDomainName",
                user_email_id="UserEmailId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorisation_domain_user_details(
            organisation_id,
            authorisation_domain_name,
            user_email_id,
            page=page,
            size=size,
            sort=sort,
            request_options=request_options,
        )
        return _response.data
