

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
from ..types.create_customer_group_response import CreateCustomerGroupResponse
from ..types.customer_group import CustomerGroup
from ..types.delete_customer_group_response import DeleteCustomerGroupResponse
from ..types.list_customer_groups_response import ListCustomerGroupsResponse
from ..types.retrieve_customer_group_response import RetrieveCustomerGroupResponse
from ..types.update_customer_group_response import UpdateCustomerGroupResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCustomerGroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_customer_groups(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCustomerGroupsResponse]:
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
        HttpResponse[ListCustomerGroupsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/customers/groups",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerGroupsResponse,
                    parse_obj_as(
                        type_=ListCustomerGroupsResponse,
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

    def create_customer_group(
        self,
        *,
        group: CustomerGroup,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCustomerGroupResponse]:
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
        HttpResponse[CreateCustomerGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/customers/groups",
            method="POST",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CustomerGroup, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateCustomerGroupResponse,
                    parse_obj_as(
                        type_=CreateCustomerGroupResponse,
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

    def retrieve_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveCustomerGroupResponse]:
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
        HttpResponse[RetrieveCustomerGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCustomerGroupResponse,
                    parse_obj_as(
                        type_=RetrieveCustomerGroupResponse,
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

    def update_customer_group(
        self, group_id: str, *, group: CustomerGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateCustomerGroupResponse]:
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
        HttpResponse[UpdateCustomerGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CustomerGroup, direction="write"
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
                    UpdateCustomerGroupResponse,
                    parse_obj_as(
                        type_=UpdateCustomerGroupResponse,
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

    def delete_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteCustomerGroupResponse]:
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
        HttpResponse[DeleteCustomerGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCustomerGroupResponse,
                    parse_obj_as(
                        type_=DeleteCustomerGroupResponse,
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


class AsyncRawCustomerGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_customer_groups(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCustomerGroupsResponse]:
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
        AsyncHttpResponse[ListCustomerGroupsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/customers/groups",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerGroupsResponse,
                    parse_obj_as(
                        type_=ListCustomerGroupsResponse,
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

    async def create_customer_group(
        self,
        *,
        group: CustomerGroup,
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCustomerGroupResponse]:
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
        AsyncHttpResponse[CreateCustomerGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/customers/groups",
            method="POST",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CustomerGroup, direction="write"
                ),
                "idempotency_key": idempotency_key,
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
                    CreateCustomerGroupResponse,
                    parse_obj_as(
                        type_=CreateCustomerGroupResponse,
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

    async def retrieve_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveCustomerGroupResponse]:
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
        AsyncHttpResponse[RetrieveCustomerGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCustomerGroupResponse,
                    parse_obj_as(
                        type_=RetrieveCustomerGroupResponse,
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

    async def update_customer_group(
        self, group_id: str, *, group: CustomerGroup, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateCustomerGroupResponse]:
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
        AsyncHttpResponse[UpdateCustomerGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "group": convert_and_respect_annotation_metadata(
                    object_=group, annotation=CustomerGroup, direction="write"
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
                    UpdateCustomerGroupResponse,
                    parse_obj_as(
                        type_=UpdateCustomerGroupResponse,
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

    async def delete_customer_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteCustomerGroupResponse]:
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
        AsyncHttpResponse[DeleteCustomerGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/customers/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteCustomerGroupResponse,
                    parse_obj_as(
                        type_=DeleteCustomerGroupResponse,
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
