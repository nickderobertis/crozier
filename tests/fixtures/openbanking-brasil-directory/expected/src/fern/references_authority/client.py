

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorities import Authorities
from ..types.authority import Authority
from ..types.authority_id import AuthorityId
from .raw_client import AsyncRawReferencesAuthorityClient, RawReferencesAuthorityClient


class ReferencesAuthorityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesAuthorityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesAuthorityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesAuthorityClient
        """
        return self._raw_client

    def reference_data_of_all_authorities(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Authorities:
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
        Authorities
            Reference data table for all authorities with their countries

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
        client.references_authority.reference_data_of_all_authorities()
        """
        _response = self._raw_client.reference_data_of_all_authorities(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    def get_a_reference_authority_by_id(
        self, authority_id: AuthorityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Authority:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Authority
            Get a reference authority by Id

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
        client.references_authority.get_a_reference_authority_by_id(
            authority_id="AuthorityId",
        )
        """
        _response = self._raw_client.get_a_reference_authority_by_id(authority_id, request_options=request_options)
        return _response.data


class AsyncReferencesAuthorityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesAuthorityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesAuthorityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesAuthorityClient
        """
        return self._raw_client

    async def reference_data_of_all_authorities(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Authorities:
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
        Authorities
            Reference data table for all authorities with their countries

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
            await client.references_authority.reference_data_of_all_authorities()


        asyncio.run(main())
        """
        _response = await self._raw_client.reference_data_of_all_authorities(
            page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data

    async def get_a_reference_authority_by_id(
        self, authority_id: AuthorityId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Authority:
        """
        Parameters
        ----------
        authority_id : AuthorityId
            The reference authority Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Authority
            Get a reference authority by Id

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
            await client.references_authority.get_a_reference_authority_by_id(
                authority_id="AuthorityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_reference_authority_by_id(
            authority_id, request_options=request_options
        )
        return _response.data
