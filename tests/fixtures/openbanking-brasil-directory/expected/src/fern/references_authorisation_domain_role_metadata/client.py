

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authorisation_domain_role_name import AuthorisationDomainRoleName
from ..types.metadata_id import MetadataId
from ..types.metadata_response import MetadataResponse
from .raw_client import (
    AsyncRawReferencesAuthorisationDomainRoleMetadataClient,
    RawReferencesAuthorisationDomainRoleMetadataClient,
)


class ReferencesAuthorisationDomainRoleMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferencesAuthorisationDomainRoleMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferencesAuthorisationDomainRoleMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferencesAuthorisationDomainRoleMetadataClient
        """
        return self._raw_client

    def get_metadata_associated_with_an_authorisation_domain_role(
        self,
        authorisation_domain_role_name: AuthorisationDomainRoleName,
        metadata_id: MetadataId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataResponse:
        """
        Parameters
        ----------
        authorisation_domain_role_name : AuthorisationDomainRoleName
            Authorisation Domain Role Name. Eg:TPP

        metadata_id : MetadataId
            The metadata id object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataResponse
            Single metadata object

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
        client.references_authorisation_domain_role_metadata.get_metadata_associated_with_an_authorisation_domain_role(
            authorisation_domain_role_name="PAGTO",
            metadata_id="MetadataId",
        )
        """
        _response = self._raw_client.get_metadata_associated_with_an_authorisation_domain_role(
            authorisation_domain_role_name, metadata_id, request_options=request_options
        )
        return _response.data


class AsyncReferencesAuthorisationDomainRoleMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferencesAuthorisationDomainRoleMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferencesAuthorisationDomainRoleMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferencesAuthorisationDomainRoleMetadataClient
        """
        return self._raw_client

    async def get_metadata_associated_with_an_authorisation_domain_role(
        self,
        authorisation_domain_role_name: AuthorisationDomainRoleName,
        metadata_id: MetadataId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataResponse:
        """
        Parameters
        ----------
        authorisation_domain_role_name : AuthorisationDomainRoleName
            Authorisation Domain Role Name. Eg:TPP

        metadata_id : MetadataId
            The metadata id object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataResponse
            Single metadata object

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
            await client.references_authorisation_domain_role_metadata.get_metadata_associated_with_an_authorisation_domain_role(
                authorisation_domain_role_name="PAGTO",
                metadata_id="MetadataId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_metadata_associated_with_an_authorisation_domain_role(
            authorisation_domain_role_name, metadata_id, request_options=request_options
        )
        return _response.data
