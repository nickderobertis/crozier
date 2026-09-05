

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_domain import AuthorisationDomain
from ..types.authorisation_domain_name import AuthorisationDomainName
from ..types.authorisation_domains_page import AuthorisationDomainsPage
from .raw_client import AsyncRawReferencesAuthorisationDomainClient, RawReferencesAuthorisationDomainClient


class ReferencesAuthorisationDomainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesAuthorisationDomainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesAuthorisationDomainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesAuthorisationDomainClient
        """
        return self._raw_client

    def reference_data_of_all_authorisation_domains(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainsPage:
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
        AuthorisationDomainsPage
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
        client.references_authorisation_domain.reference_data_of_all_authorisation_domains()
        """
        _response = self._raw_client.reference_data_of_all_authorisation_domains(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_an_authorisation_domain_by_name(
        self,
        authorisation_domain_name: AuthorisationDomainName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomain:
        """
        Parameters
        ----------
        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationDomain
            Data of an authorisation domain mapped to an authority

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
        client.references_authorisation_domain.get_an_authorisation_domain_by_name(
            authorisation_domain_name="AuthorisationDomainName",
        )
        """
        _response = self._raw_client.get_an_authorisation_domain_by_name(
            authorisation_domain_name, request_options=request_options
        )
        return _response.data


class AsyncReferencesAuthorisationDomainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesAuthorisationDomainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesAuthorisationDomainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesAuthorisationDomainClient
        """
        return self._raw_client

    async def reference_data_of_all_authorisation_domains(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomainsPage:
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
        AuthorisationDomainsPage
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
            await client.references_authorisation_domain.reference_data_of_all_authorisation_domains()


        asyncio.run(main())
        """
        _response = await self._raw_client.reference_data_of_all_authorisation_domains(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_an_authorisation_domain_by_name(
        self,
        authorisation_domain_name: AuthorisationDomainName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorisationDomain:
        """
        Parameters
        ----------
        authorisation_domain_name : AuthorisationDomainName
            Authorisation Domain Name. Eg:PSD2

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorisationDomain
            Data of an authorisation domain mapped to an authority

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
            await client.references_authorisation_domain.get_an_authorisation_domain_by_name(
                authorisation_domain_name="AuthorisationDomainName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_authorisation_domain_by_name(
            authorisation_domain_name, request_options=request_options
        )
        return _response.data
