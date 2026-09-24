

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_payload import AddressPayload
from ..types.user_by_id_response import UserByIdResponse
from ..types.users_response import UsersResponse
from .raw_client import AsyncRawUsersClient, RawUsersClient
from .types.get_users_request_filter_status import GetUsersRequestFilterStatus
from .types.get_users_request_filter_user_type import GetUsersRequestFilterUserType
from .types.get_users_request_sort_field import GetUsersRequestSortField
from .types.get_users_request_sort_order import GetUsersRequestSortOrder
from .types.patch_users_user_id_request_contact_items_item import PatchUsersUserIdRequestContactItemsItem


OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsersClient
        """
        return self._raw_client

    def get_users(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetUsersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetUsersRequestSortField] = None,
        filter_user_type: typing.Optional[GetUsersRequestFilterUserType] = None,
        filter_status: typing.Optional[GetUsersRequestFilterStatus] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersResponse:
        """
        Returns a list of users. The list can be filtered by first name, last name or email.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetUsersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetUsersRequestSortField]

        filter_user_type : typing.Optional[GetUsersRequestFilterUserType]

        filter_status : typing.Optional[GetUsersRequestFilterStatus]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `employee's username`
            - `email`
            - `address.address1`
            - `address.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users()
        """
        _response = self._raw_client.get_users(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_user_type=filter_user_type,
            filter_status=filter_status,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    def get_users_user_id(
        self, user_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserByIdResponse:
        """
        Returns a user by ID.

        Parameters
        ----------
        user_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.get_users_user_id(
            user_id=1.1,
        )
        """
        _response = self._raw_client.get_users_user_id(user_id, request_options=request_options)
        return _response.data

    def patch_users_user_id(
        self,
        user_id: float,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        address: typing.Optional[AddressPayload] = OMIT,
        pay_rate: typing.Optional[float] = OMIT,
        charge_out_rate: typing.Optional[float] = OMIT,
        contact_items: typing.Optional[typing.Sequence[PatchUsersUserIdRequestContactItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserByIdResponse:
        """
        Update user

        Parameters
        ----------
        user_id : float

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        address : typing.Optional[AddressPayload]

        pay_rate : typing.Optional[float]

        charge_out_rate : typing.Optional[float]

        contact_items : typing.Optional[typing.Sequence[PatchUsersUserIdRequestContactItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.users.patch_users_user_id(
            user_id=1.1,
        )
        """
        _response = self._raw_client.patch_users_user_id(
            user_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            pay_rate=pay_rate,
            charge_out_rate=charge_out_rate,
            contact_items=contact_items,
            request_options=request_options,
        )
        return _response.data


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsersClient
        """
        return self._raw_client

    async def get_users(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetUsersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetUsersRequestSortField] = None,
        filter_user_type: typing.Optional[GetUsersRequestFilterUserType] = None,
        filter_status: typing.Optional[GetUsersRequestFilterStatus] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsersResponse:
        """
        Returns a list of users. The list can be filtered by first name, last name or email.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetUsersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetUsersRequestSortField]

        filter_user_type : typing.Optional[GetUsersRequestFilterUserType]

        filter_status : typing.Optional[GetUsersRequestFilterStatus]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `employee's username`
            - `email`
            - `address.address1`
            - `address.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_user_type=filter_user_type,
            filter_status=filter_status,
            filter_search_text=filter_search_text,
            request_options=request_options,
        )
        return _response.data

    async def get_users_user_id(
        self, user_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserByIdResponse:
        """
        Returns a user by ID.

        Parameters
        ----------
        user_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.get_users_user_id(
                user_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_user_id(user_id, request_options=request_options)
        return _response.data

    async def patch_users_user_id(
        self,
        user_id: float,
        *,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        address: typing.Optional[AddressPayload] = OMIT,
        pay_rate: typing.Optional[float] = OMIT,
        charge_out_rate: typing.Optional[float] = OMIT,
        contact_items: typing.Optional[typing.Sequence[PatchUsersUserIdRequestContactItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserByIdResponse:
        """
        Update user

        Parameters
        ----------
        user_id : float

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        address : typing.Optional[AddressPayload]

        pay_rate : typing.Optional[float]

        charge_out_rate : typing.Optional[float]

        contact_items : typing.Optional[typing.Sequence[PatchUsersUserIdRequestContactItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.users.patch_users_user_id(
                user_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_users_user_id(
            user_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            pay_rate=pay_rate,
            charge_out_rate=charge_out_rate,
            contact_items=contact_items,
            request_options=request_options,
        )
        return _response.data
