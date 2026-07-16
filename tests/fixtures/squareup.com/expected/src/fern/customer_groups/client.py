

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_customer_group_response import CreateCustomerGroupResponse
from ..types.customer_group import CustomerGroup
from ..types.delete_customer_group_response import DeleteCustomerGroupResponse
from ..types.list_customer_groups_response import ListCustomerGroupsResponse
from ..types.retrieve_customer_group_response import RetrieveCustomerGroupResponse
from ..types.update_customer_group_response import UpdateCustomerGroupResponse
from .raw_client import AsyncRawCustomerGroupsClient, RawCustomerGroupsClient


OMIT = typing.cast(typing.Any, ...)


class CustomerGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomerGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomerGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomerGroupsClient
        """
        return self._raw_client

    def list_customer_groups(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerGroupsResponse:
        """
        Retrieves the list of customer groups of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerGroupsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_groups.list_customer_groups()
        """
        _response = self._raw_client.list_customer_groups(cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def create_customer_group(
        self,
        *,
        group: CustomerGroup,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerGroupResponse:
        """
        Creates a new customer group for a business.

        The request must include the `name` value of the group.

        Parameters
        ----------
        group : CustomerGroup

        idempotency_key : typing.Optional[str]
            The idempotency key for the request. For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerGroupResponse
            Success

        Examples
        --------
        from fern import CustomerGroup, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_groups.create_customer_group(
            group=CustomerGroup(
                name="name",
            ),
        )
        """
        _response = self._raw_client.create_customer_group(
            group=group, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def retrieve_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerGroupResponse:
        """
        Retrieves a specific customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_groups.retrieve_customer_group(
            group_id="group_id",
        )
        """
        _response = self._raw_client.retrieve_customer_group(group_id, request_options=request_options)
        return _response.data

    def update_customer_group(
        self, group_id: str, *, group: CustomerGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomerGroupResponse:
        """
        Updates a customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to update.

        group : CustomerGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerGroupResponse
            Success

        Examples
        --------
        from fern import CustomerGroup, FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_groups.update_customer_group(
            group_id="group_id",
            group=CustomerGroup(
                name="name",
            ),
        )
        """
        _response = self._raw_client.update_customer_group(group_id, group=group, request_options=request_options)
        return _response.data

    def delete_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerGroupResponse:
        """
        Deletes a customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.customer_groups.delete_customer_group(
            group_id="group_id",
        )
        """
        _response = self._raw_client.delete_customer_group(group_id, request_options=request_options)
        return _response.data


class AsyncCustomerGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomerGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomerGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomerGroupsClient
        """
        return self._raw_client

    async def list_customer_groups(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomerGroupsResponse:
        """
        Retrieves the list of customer groups of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for your original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomerGroupsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_groups.list_customer_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_customer_groups(
            cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_customer_group(
        self,
        *,
        group: CustomerGroup,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomerGroupResponse:
        """
        Creates a new customer group for a business.

        The request must include the `name` value of the group.

        Parameters
        ----------
        group : CustomerGroup

        idempotency_key : typing.Optional[str]
            The idempotency key for the request. For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomerGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CustomerGroup

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_groups.create_customer_group(
                group=CustomerGroup(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_customer_group(
            group=group, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def retrieve_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveCustomerGroupResponse:
        """
        Retrieves a specific customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveCustomerGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_groups.retrieve_customer_group(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_customer_group(group_id, request_options=request_options)
        return _response.data

    async def update_customer_group(
        self, group_id: str, *, group: CustomerGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateCustomerGroupResponse:
        """
        Updates a customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to update.

        group : CustomerGroup

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomerGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CustomerGroup

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_groups.update_customer_group(
                group_id="group_id",
                group=CustomerGroup(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_customer_group(group_id, group=group, request_options=request_options)
        return _response.data

    async def delete_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteCustomerGroupResponse:
        """
        Deletes a customer group as identified by the `group_id` value.

        Parameters
        ----------
        group_id : str
            The ID of the customer group to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteCustomerGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.customer_groups.delete_customer_group(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_customer_group(group_id, request_options=request_options)
        return _response.data
