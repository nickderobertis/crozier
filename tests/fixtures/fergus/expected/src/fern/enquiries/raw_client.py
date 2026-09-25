

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.enquiries_response import EnquiriesResponse
from ..types.enquiry_by_id_response import EnquiryByIdResponse
from ..types.enquiry_created_response import EnquiryCreatedResponse
from .types.get_enquiries_request_filter_status import GetEnquiriesRequestFilterStatus
from .types.get_enquiries_request_sort_field import GetEnquiriesRequestSortField
from .types.get_enquiries_request_sort_order import GetEnquiriesRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEnquiriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_enquiries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetEnquiriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetEnquiriesRequestSortField] = None,
        filter_status: typing.Optional[GetEnquiriesRequestFilterStatus] = None,
        filter_source: typing.Optional[str] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnquiriesResponse]:
        """
        Get all enquiries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetEnquiriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetEnquiriesRequestSortField]

        filter_status : typing.Optional[GetEnquiriesRequestFilterStatus]

        filter_source : typing.Optional[str]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `description`
            - `phone`
            - `email`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnquiriesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "enquiries",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterStatus": filter_status,
                "filterSource": filter_source,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnquiriesResponse,
                    parse_obj_as(
                        type_=EnquiriesResponse,
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

    def post_enquiries(
        self,
        *,
        name: str,
        email: str,
        phone_number: str,
        description: str,
        source: str,
        address1: str,
        post_enquiries_request_address_city: str,
        address2: typing.Optional[str] = OMIT,
        address_suburb: typing.Optional[str] = OMIT,
        address_region: typing.Optional[str] = OMIT,
        address_postcode: typing.Optional[str] = OMIT,
        address_country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnquiryCreatedResponse]:
        """
        Create Enquiry

        Parameters
        ----------
        name : str

        email : str

        phone_number : str

        description : str

        source : str

        address1 : str

        post_enquiries_request_address_city : str

        address2 : typing.Optional[str]

        address_suburb : typing.Optional[str]

        address_region : typing.Optional[str]

        address_postcode : typing.Optional[str]

        address_country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnquiryCreatedResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "enquiries",
            method="POST",
            json={
                "name": name,
                "email": email,
                "phoneNumber": phone_number,
                "description": description,
                "source": source,
                "address1": address1,
                "address2": address2,
                "addressSuburb": address_suburb,
                "addressCity": post_enquiries_request_address_city,
                "addressRegion": address_region,
                "addressPostcode": address_postcode,
                "addressCountry": address_country,
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
                    EnquiryCreatedResponse,
                    parse_obj_as(
                        type_=EnquiryCreatedResponse,
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

    def get_enquiries_enquiry_id(
        self, enquiry_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnquiryByIdResponse]:
        """
        Returns enquiry by ID.

        Parameters
        ----------
        enquiry_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnquiryByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"enquiries/{encode_path_param(enquiry_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnquiryByIdResponse,
                    parse_obj_as(
                        type_=EnquiryByIdResponse,
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


class AsyncRawEnquiriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_enquiries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetEnquiriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetEnquiriesRequestSortField] = None,
        filter_status: typing.Optional[GetEnquiriesRequestFilterStatus] = None,
        filter_source: typing.Optional[str] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnquiriesResponse]:
        """
        Get all enquiries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetEnquiriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetEnquiriesRequestSortField]

        filter_status : typing.Optional[GetEnquiriesRequestFilterStatus]

        filter_source : typing.Optional[str]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `description`
            - `phone`
            - `email`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnquiriesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "enquiries",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterStatus": filter_status,
                "filterSource": filter_source,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnquiriesResponse,
                    parse_obj_as(
                        type_=EnquiriesResponse,
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

    async def post_enquiries(
        self,
        *,
        name: str,
        email: str,
        phone_number: str,
        description: str,
        source: str,
        address1: str,
        post_enquiries_request_address_city: str,
        address2: typing.Optional[str] = OMIT,
        address_suburb: typing.Optional[str] = OMIT,
        address_region: typing.Optional[str] = OMIT,
        address_postcode: typing.Optional[str] = OMIT,
        address_country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnquiryCreatedResponse]:
        """
        Create Enquiry

        Parameters
        ----------
        name : str

        email : str

        phone_number : str

        description : str

        source : str

        address1 : str

        post_enquiries_request_address_city : str

        address2 : typing.Optional[str]

        address_suburb : typing.Optional[str]

        address_region : typing.Optional[str]

        address_postcode : typing.Optional[str]

        address_country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnquiryCreatedResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "enquiries",
            method="POST",
            json={
                "name": name,
                "email": email,
                "phoneNumber": phone_number,
                "description": description,
                "source": source,
                "address1": address1,
                "address2": address2,
                "addressSuburb": address_suburb,
                "addressCity": post_enquiries_request_address_city,
                "addressRegion": address_region,
                "addressPostcode": address_postcode,
                "addressCountry": address_country,
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
                    EnquiryCreatedResponse,
                    parse_obj_as(
                        type_=EnquiryCreatedResponse,
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

    async def get_enquiries_enquiry_id(
        self, enquiry_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnquiryByIdResponse]:
        """
        Returns enquiry by ID.

        Parameters
        ----------
        enquiry_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnquiryByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"enquiries/{encode_path_param(enquiry_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnquiryByIdResponse,
                    parse_obj_as(
                        type_=EnquiryByIdResponse,
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
