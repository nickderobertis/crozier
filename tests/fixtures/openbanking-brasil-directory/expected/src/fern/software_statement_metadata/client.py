

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.metadata_list_response import MetadataListResponse
from ..types.organisation_id import OrganisationId
from ..types.software_statement_id import SoftwareStatementId
from .raw_client import AsyncRawSoftwareStatementMetadataClient, RawSoftwareStatementMetadataClient


class SoftwareStatementMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoftwareStatementMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoftwareStatementMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoftwareStatementMetadataClient
        """
        return self._raw_client

    def get_all_metadata_associated_with_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataListResponse:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        type : typing.Optional[str]
            Get all metadata of a specific type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataListResponse
            List of all metadata associated with an object

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
        client.software_statement_metadata.get_all_metadata_associated_with_a_software_statement(
            organisation_id="OrganisationId",
            software_statement_id="SoftwareStatementId",
        )
        """
        _response = self._raw_client.get_all_metadata_associated_with_a_software_statement(
            organisation_id, software_statement_id, type=type, request_options=request_options
        )
        return _response.data


class AsyncSoftwareStatementMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoftwareStatementMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoftwareStatementMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoftwareStatementMetadataClient
        """
        return self._raw_client

    async def get_all_metadata_associated_with_a_software_statement(
        self,
        organisation_id: OrganisationId,
        software_statement_id: SoftwareStatementId,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MetadataListResponse:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        software_statement_id : SoftwareStatementId
            The software statement ID

        type : typing.Optional[str]
            Get all metadata of a specific type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetadataListResponse
            List of all metadata associated with an object

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
            await client.software_statement_metadata.get_all_metadata_associated_with_a_software_statement(
                organisation_id="OrganisationId",
                software_statement_id="SoftwareStatementId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_metadata_associated_with_a_software_statement(
            organisation_id, software_statement_id, type=type, request_options=request_options
        )
        return _response.data
