

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.address_payload import AddressPayload
from ..types.user_by_id_response import UserByIdResponse
from ..types.users_response import UsersResponse
from .types.get_users_request_filter_status import GetUsersRequestFilterStatus
from .types.get_users_request_filter_user_type import GetUsersRequestFilterUserType
from .types.get_users_request_sort_field import GetUsersRequestSortField
from .types.get_users_request_sort_order import GetUsersRequestSortOrder
from .types.patch_users_user_id_request_contact_items_item import PatchUsersUserIdRequestContactItemsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[UsersResponse]:
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
        HttpResponse[UsersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterUserType": filter_user_type,
                "filterStatus": filter_status,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersResponse,
                    parse_obj_as(
                        type_=UsersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_users_user_id(
        self, user_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserByIdResponse]:
        """
        Returns a user by ID.

        Parameters
        ----------
        user_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserByIdResponse,
                    parse_obj_as(
                        type_=UserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[UserByIdResponse]:
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
        HttpResponse[UserByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=AddressPayload, direction="write"
                ),
                "payRate": pay_rate,
                "chargeOutRate": charge_out_rate,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items,
                    annotation=typing.Sequence[PatchUsersUserIdRequestContactItemsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserByIdResponse,
                    parse_obj_as(
                        type_=UserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[UsersResponse]:
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
        AsyncHttpResponse[UsersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterUserType": filter_user_type,
                "filterStatus": filter_status,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UsersResponse,
                    parse_obj_as(
                        type_=UsersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_users_user_id(
        self, user_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserByIdResponse]:
        """
        Returns a user by ID.

        Parameters
        ----------
        user_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserByIdResponse,
                    parse_obj_as(
                        type_=UserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[UserByIdResponse]:
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
        AsyncHttpResponse[UserByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=AddressPayload, direction="write"
                ),
                "payRate": pay_rate,
                "chargeOutRate": charge_out_rate,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items,
                    annotation=typing.Sequence[PatchUsersUserIdRequestContactItemsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserByIdResponse,
                    parse_obj_as(
                        type_=UserByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
