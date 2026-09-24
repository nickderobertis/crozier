

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
from ..types.get_customer_by_id_response import GetCustomerByIdResponse
from ..types.get_customers_response import GetCustomersResponse
from ..types.person_payload import PersonPayload
from .types.get_customers_request_sort_field import GetCustomersRequestSortField
from .types.get_customers_request_sort_order import GetCustomersRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCustomersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_customers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomersRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCustomersResponse]:
        """
        Returns a list of customers. The list can be filtered by customer name.<br/><br/>
            A note about contact items on each person:<br>
            <ul>
              <li>The contact items are an array of objects. Each object has a `contactType` and a `contactValue`.
              <li>The `contactType` can be one of the following: email, phone, mobile, or fax.
              <li>The `contactValue` can be an email address or phone number.
            </ul>


        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomersRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `customerFullName`
            - `mainContact.firstName`
            - `mainContact.lastName`
            - `mainContact.contactItems[].contactValue`
            - `billingContact.firstName`
            - `billingContact.lastName`,
            - `billingContact.contactItems[].contactValue`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "customers",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomersResponse,
                    parse_obj_as(
                        type_=GetCustomersResponse,
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

    def post_customers(
        self,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCustomerByIdResponse]:
        """
        Creates a new customer.

        Parameters
        ----------
        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomerByIdResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "customers",
            method="POST",
            json={
                "customerFullName": customer_full_name,
                "mainContact": convert_and_respect_annotation_metadata(
                    object_=main_contact, annotation=PersonPayload, direction="write"
                ),
                "physicalAddress": convert_and_respect_annotation_metadata(
                    object_=physical_address, annotation=AddressPayload, direction="write"
                ),
                "postalAddress": convert_and_respect_annotation_metadata(
                    object_=postal_address, annotation=AddressPayload, direction="write"
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
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    def get_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCustomerByIdResponse]:
        """
        Returns a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomerByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    def put_customers_customer_id(
        self,
        customer_id: float,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCustomerByIdResponse]:
        """
        Update a customer.

        Parameters
        ----------
        customer_id : float

        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCustomerByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="PUT",
            json={
                "customerFullName": customer_full_name,
                "mainContact": convert_and_respect_annotation_metadata(
                    object_=main_contact, annotation=PersonPayload, direction="write"
                ),
                "physicalAddress": convert_and_respect_annotation_metadata(
                    object_=physical_address, annotation=AddressPayload, direction="write"
                ),
                "postalAddress": convert_and_respect_annotation_metadata(
                    object_=postal_address, annotation=AddressPayload, direction="write"
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
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    def delete_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCustomersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_customers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetCustomersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCustomersRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCustomersResponse]:
        """
        Returns a list of customers. The list can be filtered by customer name.<br/><br/>
            A note about contact items on each person:<br>
            <ul>
              <li>The contact items are an array of objects. Each object has a `contactType` and a `contactValue`.
              <li>The `contactType` can be one of the following: email, phone, mobile, or fax.
              <li>The `contactValue` can be an email address or phone number.
            </ul>


        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetCustomersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetCustomersRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `customerFullName`
            - `mainContact.firstName`
            - `mainContact.lastName`
            - `mainContact.contactItems[].contactValue`
            - `billingContact.firstName`
            - `billingContact.lastName`,
            - `billingContact.contactItems[].contactValue`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customers",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomersResponse,
                    parse_obj_as(
                        type_=GetCustomersResponse,
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

    async def post_customers(
        self,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCustomerByIdResponse]:
        """
        Creates a new customer.

        Parameters
        ----------
        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomerByIdResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "customers",
            method="POST",
            json={
                "customerFullName": customer_full_name,
                "mainContact": convert_and_respect_annotation_metadata(
                    object_=main_contact, annotation=PersonPayload, direction="write"
                ),
                "physicalAddress": convert_and_respect_annotation_metadata(
                    object_=physical_address, annotation=AddressPayload, direction="write"
                ),
                "postalAddress": convert_and_respect_annotation_metadata(
                    object_=postal_address, annotation=AddressPayload, direction="write"
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
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    async def get_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCustomerByIdResponse]:
        """
        Returns a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomerByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    async def put_customers_customer_id(
        self,
        customer_id: float,
        *,
        customer_full_name: str,
        main_contact: PersonPayload,
        physical_address: typing.Optional[AddressPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCustomerByIdResponse]:
        """
        Update a customer.

        Parameters
        ----------
        customer_id : float

        customer_full_name : str

        main_contact : PersonPayload

        physical_address : typing.Optional[AddressPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCustomerByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="PUT",
            json={
                "customerFullName": customer_full_name,
                "mainContact": convert_and_respect_annotation_metadata(
                    object_=main_contact, annotation=PersonPayload, direction="write"
                ),
                "physicalAddress": convert_and_respect_annotation_metadata(
                    object_=physical_address, annotation=AddressPayload, direction="write"
                ),
                "postalAddress": convert_and_respect_annotation_metadata(
                    object_=postal_address, annotation=AddressPayload, direction="write"
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
                    GetCustomerByIdResponse,
                    parse_obj_as(
                        type_=GetCustomerByIdResponse,
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

    async def delete_customers_customer_id(
        self, customer_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a customer by ID.

        Parameters
        ----------
        customer_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"customers/{encode_path_param(customer_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
