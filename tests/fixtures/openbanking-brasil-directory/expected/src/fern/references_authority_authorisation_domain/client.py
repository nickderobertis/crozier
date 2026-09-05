

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authority_authorisation_domain import AuthorityAuthorisationDomain
from ..types.authority_authorisation_domain_id import AuthorityAuthorisationDomainId
from ..types.authority_authorisation_domains_page import AuthorityAuthorisationDomainsPage
from ..types.authority_id import AuthorityId
from .raw_client import (
    AsyncRawReferencesAuthorityAuthorisationDomainClient,
    RawReferencesAuthorityAuthorisationDomainClient,
)


class ReferencesAuthorityAuthorisationDomainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesAuthorityAuthorisationDomainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesAuthorityAuthorisationDomainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesAuthorityAuthorisationDomainClient
        """
        return self._raw_client

    def reference_data_of_all_authorisation_domains_for_an_authority_id(
        self,
        authority_id: AuthorityId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomainsPage:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

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
        AuthorityAuthorisationDomainsPage
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
        client.references_authority_authorisation_domain.reference_data_of_all_authorisation_domains_for_an_authority_id(
            authority_id="AuthorityId",
        )
        """
        _response = self._raw_client.reference_data_of_all_authorisation_domains_for_an_authority_id(
            authority_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authority_authorisation_domain_by_id(
        self,
        authority_id: AuthorityId,
        authority_authorisation_domain_id: AuthorityAuthorisationDomainId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomain:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

        authority_authorisation_domain_id : AuthorityAuthorisationDomainId
            ID of the Authority mapped with Authorisation Domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorityAuthorisationDomain
            Authority to domain mapping data

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
        client.references_authority_authorisation_domain.get_an_authority_authorisation_domain_by_id(
            authority_id="AuthorityId",
            authority_authorisation_domain_id="AuthorityAuthorisationDomainId",
        )
        """
        _response = self._raw_client.get_an_authority_authorisation_domain_by_id(
            authority_id, authority_authorisation_domain_id, request_options=request_options
        )
        return _response.data

    def mappings_of_authorities_with_authorisation_domains(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomainsPage:
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
        AuthorityAuthorisationDomainsPage
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
        client.references_authority_authorisation_domain.mappings_of_authorities_with_authorisation_domains()
        """
        _response = self._raw_client.mappings_of_authorities_with_authorisation_domains(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncReferencesAuthorityAuthorisationDomainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesAuthorityAuthorisationDomainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesAuthorityAuthorisationDomainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesAuthorityAuthorisationDomainClient
        """
        return self._raw_client

    async def reference_data_of_all_authorisation_domains_for_an_authority_id(
        self,
        authority_id: AuthorityId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomainsPage:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

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
        AuthorityAuthorisationDomainsPage
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
            await client.references_authority_authorisation_domain.reference_data_of_all_authorisation_domains_for_an_authority_id(
                authority_id="AuthorityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reference_data_of_all_authorisation_domains_for_an_authority_id(
            authority_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authority_authorisation_domain_by_id(
        self,
        authority_id: AuthorityId,
        authority_authorisation_domain_id: AuthorityAuthorisationDomainId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomain:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

        authority_authorisation_domain_id : AuthorityAuthorisationDomainId
            ID of the Authority mapped with Authorisation Domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorityAuthorisationDomain
            Authority to domain mapping data

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
            await client.references_authority_authorisation_domain.get_an_authority_authorisation_domain_by_id(
                authority_id="AuthorityId",
                authority_authorisation_domain_id="AuthorityAuthorisationDomainId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authority_authorisation_domain_by_id(
            authority_id, authority_authorisation_domain_id, request_options=request_options
        )
        return _response.data

    async def mappings_of_authorities_with_authorisation_domains(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorityAuthorisationDomainsPage:
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
        AuthorityAuthorisationDomainsPage
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
            await client.references_authority_authorisation_domain.mappings_of_authorities_with_authorisation_domains()


        asyncio.run(main())
        """
        _response = await self._raw_client.mappings_of_authorities_with_authorisation_domains(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data
