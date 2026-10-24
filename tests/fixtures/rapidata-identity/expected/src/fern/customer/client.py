

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_customers_request_email import GetCustomersRequestEmail
from ..types.get_customers_request_id import GetCustomersRequestId
from ..types.get_customers_request_organization_id import GetCustomersRequestOrganizationId
from ..types.get_customers_request_organization_name import GetCustomersRequestOrganizationName
from ..types.query_customers_endpoint_paged_result_of_output import QueryCustomersEndpointPagedResultOfOutput
from .raw_client import AsyncRawCustomerClient, RawCustomerClient
from .types.get_customers_request_logic import GetCustomersRequestLogic
from .types.get_customers_request_sort_item import GetCustomersRequestSortItem


class CustomerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerClient
        """
        return self._raw_client

    def deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This cannot be undone. An organization the account is the only member of is deleted with it,
         along with everything it owns; invoices already raised are kept. Responds with 409 when the
         account is the last owner of an organization that has other members — transfer ownership
         first — or when such an organization still has an open invoice or a billing reconciliation in
         progress. Issuing it again for an account that is already deleted succeeds and changes
         nothing further. The same address and the same external login can be used to register a new
         account afterwards; none of the old account's data comes back with it.

        Parameters
        ----------
        customer_id : str
            The id of the customer to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer.deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
            customer_id="customerId",
        )
        """
        _response = self._raw_client.deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
            customer_id, request_options=request_options
        )
        return _response.data

    def queries_customers_with_filtering_and_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]
        ] = None,
        id: typing.Optional[GetCustomersRequestId] = None,
        email: typing.Optional[GetCustomersRequestEmail] = None,
        organization_name: typing.Optional[GetCustomersRequestOrganizationName] = None,
        organization_id: typing.Optional[GetCustomersRequestOrganizationId] = None,
        logic: typing.Optional[GetCustomersRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryCustomersEndpointPagedResultOfOutput:
        """
        Results are scoped to customers that belong to the caller's organization.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetCustomersRequestId]
            Filter by id.

        email : typing.Optional[GetCustomersRequestEmail]
            Filter by email.

        organization_name : typing.Optional[GetCustomersRequestOrganizationName]
            Filter by organization_name.

        organization_id : typing.Optional[GetCustomersRequestOrganizationId]
            Filter by organization_id.

        logic : typing.Optional[GetCustomersRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryCustomersEndpointPagedResultOfOutput
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.customer.queries_customers_with_filtering_and_pagination()
        """
        _response = self._raw_client.queries_customers_with_filtering_and_pagination(
            page=page,
            page_size=page_size,
            sort=sort,
            id=id,
            email=email,
            organization_name=organization_name,
            organization_id=organization_id,
            logic=logic,
            request_options=request_options,
        )
        return _response.data


class AsyncCustomerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerClient
        """
        return self._raw_client

    async def deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
        self, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        This cannot be undone. An organization the account is the only member of is deleted with it,
         along with everything it owns; invoices already raised are kept. Responds with 409 when the
         account is the last owner of an organization that has other members — transfer ownership
         first — or when such an organization still has an open invoice or a billing reconciliation in
         progress. Issuing it again for an account that is already deleted succeeds and changes
         nothing further. The same address and the same external login can be used to register a new
         account afterwards; none of the old account's data comes back with it.

        Parameters
        ----------
        customer_id : str
            The id of the customer to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer.deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
                customer_id="customerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_the_account_it_can_no_longer_sign_in_stops_receiving_email_and_leaves_every_organization_it_belongs_to(
            customer_id, request_options=request_options
        )
        return _response.data

    async def queries_customers_with_filtering_and_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort: typing.Optional[
            typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]
        ] = None,
        id: typing.Optional[GetCustomersRequestId] = None,
        email: typing.Optional[GetCustomersRequestEmail] = None,
        organization_name: typing.Optional[GetCustomersRequestOrganizationName] = None,
        organization_id: typing.Optional[GetCustomersRequestOrganizationId] = None,
        logic: typing.Optional[GetCustomersRequestLogic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryCustomersEndpointPagedResultOfOutput:
        """
        Results are scoped to customers that belong to the caller's organization.

        Parameters
        ----------
        page : typing.Optional[int]
            The 1-based page index.

        page_size : typing.Optional[int]
            The number of items per page.

        sort : typing.Optional[typing.Union[GetCustomersRequestSortItem, typing.Sequence[GetCustomersRequestSortItem]]]
            Sort fields. Prefix with - for descending order (e.g. -created_at).

        id : typing.Optional[GetCustomersRequestId]
            Filter by id.

        email : typing.Optional[GetCustomersRequestEmail]
            Filter by email.

        organization_name : typing.Optional[GetCustomersRequestOrganizationName]
            Filter by organization_name.

        organization_id : typing.Optional[GetCustomersRequestOrganizationId]
            Filter by organization_id.

        logic : typing.Optional[GetCustomersRequestLogic]
            How to combine the field filters: "and" (default) requires every filter to match, "or" requires any of them to match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryCustomersEndpointPagedResultOfOutput
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer.queries_customers_with_filtering_and_pagination()


        asyncio.run(main())
        """
        _response = await self._raw_client.queries_customers_with_filtering_and_pagination(
            page=page,
            page_size=page_size,
            sort=sort,
            id=id,
            email=email,
            organization_name=organization_name,
            organization_id=organization_id,
            logic=logic,
            request_options=request_options,
        )
        return _response.data
