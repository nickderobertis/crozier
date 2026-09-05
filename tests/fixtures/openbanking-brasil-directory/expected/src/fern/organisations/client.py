

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.org_terms_and_conditions_page import OrgTermsAndConditionsPage
from ..types.organisation_id import OrganisationId
from ..types.organisation_with_tnc import OrganisationWithTnc
from ..types.organisations_page import OrganisationsPage
from .raw_client import AsyncRawOrganisationsClient, RawOrganisationsClient


class OrganisationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganisationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganisationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganisationsClient
        """
        return self._raw_client

    def get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        display_mine: typing.Optional[str] = None,
        filter_by: typing.Optional[str] = None,
        hide_inactive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationsPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        display_mine : typing.Optional[str]
            Set to an email value to instruct the backend to only return organisations related to the user

        filter_by : typing.Optional[str]
            Will return organisations with data like the provided value

        hide_inactive : typing.Optional[bool]
            Will return only active organisations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationsPage
            All organisations

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
        client.organisations.get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services()
        """
        _response = self._raw_client.get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services(
            page=page,
            size=size,
            sort=sort,
            display_mine=display_mine,
            filter_by=filter_by,
            hide_inactive=hide_inactive,
            request_options=request_options,
        )
        return _response.data

    def get_the_given_organisations_details(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganisationWithTnc:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationWithTnc
            Full details of the organisation including TnC information

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
        client.organisations.get_the_given_organisations_details(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_the_given_organisations_details(
            organisation_id, request_options=request_options
        )
        return _response.data

    def get_all_tn_c_data_of_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrgTermsAndConditionsPage:
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
        OrgTermsAndConditionsPage
            Org TnCs history

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
        client.organisations.get_all_tn_c_data_of_the_given_organisation(
            organisation_id="OrganisationId",
        )
        """
        _response = self._raw_client.get_all_tn_c_data_of_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data


class AsyncOrganisationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganisationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganisationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganisationsClient
        """
        return self._raw_client

    async def get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        display_mine: typing.Optional[str] = None,
        filter_by: typing.Optional[str] = None,
        hide_inactive: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganisationsPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            The page number to return of the result set

        size : typing.Optional[int]
            The size of the pages to return

        sort : typing.Optional[str]
            The field name to sort

        display_mine : typing.Optional[str]
            Set to an email value to instruct the backend to only return organisations related to the user

        filter_by : typing.Optional[str]
            Will return organisations with data like the provided value

        hide_inactive : typing.Optional[bool]
            Will return only active organisations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationsPage
            All organisations

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
            await client.organisations.get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_organisations_that_the_logged_in_user_is_authorised_to_retrieve_from_trusted_services(
            page=page,
            size=size,
            sort=sort,
            display_mine=display_mine,
            filter_by=filter_by,
            hide_inactive=hide_inactive,
            request_options=request_options,
        )
        return _response.data

    async def get_the_given_organisations_details(
        self, organisation_id: OrganisationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganisationWithTnc:
        """
        Parameters
        ----------
        organisation_id : OrganisationId
            The organisation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganisationWithTnc
            Full details of the organisation including TnC information

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
            await client.organisations.get_the_given_organisations_details(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_given_organisations_details(
            organisation_id, request_options=request_options
        )
        return _response.data

    async def get_all_tn_c_data_of_the_given_organisation(
        self,
        organisation_id: OrganisationId,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrgTermsAndConditionsPage:
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
        OrgTermsAndConditionsPage
            Org TnCs history

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
            await client.organisations.get_all_tn_c_data_of_the_given_organisation(
                organisation_id="OrganisationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_tn_c_data_of_the_given_organisation(
            organisation_id, page=page, size=size, sort=sort, request_options=request_options
        )
        return _response.data
