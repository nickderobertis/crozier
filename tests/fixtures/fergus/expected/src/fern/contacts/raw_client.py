

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
from ..types.contact_by_id_response import ContactByIdResponse
from ..types.contact_item_payload import ContactItemPayload
from ..types.contacts_response import ContactsResponse
from .types.create_contact_payload_contact_type import CreateContactPayloadContactType
from .types.get_contacts_request_filter_contact_type import GetContactsRequestFilterContactType
from .types.get_contacts_request_sort_field import GetContactsRequestSortField
from .types.get_contacts_request_sort_order import GetContactsRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_contacts(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetContactsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetContactsRequestSortField] = None,
        filter_contact_type: typing.Optional[GetContactsRequestFilterContactType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactsResponse]:
        """
        Returns a list of contacts. The list can be filtered by contact type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetContactsRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetContactsRequestSortField]

        filter_contact_type : typing.Optional[GetContactsRequestFilterContactType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `email`
            - `phoneNumber`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "contacts",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterContactType": filter_contact_type,
                "filterCustomerId": filter_customer_id,
                "filterSiteId": filter_site_id,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactsResponse,
                    parse_obj_as(
                        type_=ContactsResponse,
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

    def post_contacts(
        self,
        *,
        first_name: str,
        email: str,
        contact_type: CreateContactPayloadContactType,
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        contact_items: typing.Optional[typing.Sequence[ContactItemPayload]] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactByIdResponse]:
        """
        Creates a new contact for a customer or site.

          - **firstName** is required
          - **email** is required and must be a valid email address. This will be added as a contact item.
          - **contactType** is required and must be one of the following: `CUSTOMER`, `SITE`.
            - When **contactType** is `CUSTOMER`:
              - **customerId** is required
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
            - When **contactType** is `SITE`:
              - **siteId** is required
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.

        Parameters
        ----------
        first_name : str

        email : str

        contact_type : CreateContactPayloadContactType

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        contact_items : typing.Optional[typing.Sequence[ContactItemPayload]]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        site_id : typing.Optional[float]

        customer_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactByIdResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "contacts",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "position": position,
                "company": company,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items, annotation=typing.Sequence[ContactItemPayload], direction="write"
                ),
                "email": email,
                "isMain": is_main,
                "isBilling": is_billing,
                "siteId": site_id,
                "customerId": customer_id,
                "contactType": contact_type,
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
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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

    def get_contacts_contact_id(
        self, contact_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContactByIdResponse]:
        """
        Returns a contact by ID.

        Parameters
        ----------
        contact_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contacts/{encode_path_param(contact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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

    def put_contacts_contact_id(
        self,
        contact_id: float,
        *,
        first_name: str,
        contact_items: typing.Sequence[ContactItemPayload],
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContactByIdResponse]:
        """
        Updates a customer contact or site contact.

          - **firstName** is required
          - NOTE: To update the main contact of a `CUSTOMER`, please use the /customers endpoint.
            - When the contact to update is of type `CUSTOMER`:
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
          - NOTE: To unset the main contact of a `SITE` as non-main is not allowed, either use the create endpoint or update another contact of this site and set it as the main contact.
            - When the contact to update is of type `SITE`:
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.
              - If the contact to update is the main and billing contact of the `SITE`, the **isBilling** flag will have no impact and the contact details will be updated. If you want to change the contact that is assigned as the billing contact, please use the create method or update another contact of this site and set it as a billing contact.
          - **contactItems** at least one contact item of type email is required.
            - It will replace the existing contact items.
            - To update a specific contact item, you have to provide the id of the contact item to update. Otherwise, new contact items will be added.

        Parameters
        ----------
        contact_id : float

        first_name : str

        contact_items : typing.Sequence[ContactItemPayload]

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contacts/{encode_path_param(contact_id)}",
            method="PUT",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "position": position,
                "company": company,
                "isMain": is_main,
                "isBilling": is_billing,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items, annotation=typing.Sequence[ContactItemPayload], direction="write"
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
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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


class AsyncRawContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_contacts(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetContactsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetContactsRequestSortField] = None,
        filter_contact_type: typing.Optional[GetContactsRequestFilterContactType] = None,
        filter_customer_id: typing.Optional[float] = None,
        filter_site_id: typing.Optional[float] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactsResponse]:
        """
        Returns a list of contacts. The list can be filtered by contact type.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetContactsRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetContactsRequestSortField]

        filter_contact_type : typing.Optional[GetContactsRequestFilterContactType]

        filter_customer_id : typing.Optional[float]

        filter_site_id : typing.Optional[float]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `firstName`
            - `lastName`
            - `email`
            - `phoneNumber`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contacts",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterContactType": filter_contact_type,
                "filterCustomerId": filter_customer_id,
                "filterSiteId": filter_site_id,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactsResponse,
                    parse_obj_as(
                        type_=ContactsResponse,
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

    async def post_contacts(
        self,
        *,
        first_name: str,
        email: str,
        contact_type: CreateContactPayloadContactType,
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        contact_items: typing.Optional[typing.Sequence[ContactItemPayload]] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        site_id: typing.Optional[float] = OMIT,
        customer_id: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactByIdResponse]:
        """
        Creates a new contact for a customer or site.

          - **firstName** is required
          - **email** is required and must be a valid email address. This will be added as a contact item.
          - **contactType** is required and must be one of the following: `CUSTOMER`, `SITE`.
            - When **contactType** is `CUSTOMER`:
              - **customerId** is required
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
            - When **contactType** is `SITE`:
              - **siteId** is required
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.

        Parameters
        ----------
        first_name : str

        email : str

        contact_type : CreateContactPayloadContactType

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        contact_items : typing.Optional[typing.Sequence[ContactItemPayload]]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        site_id : typing.Optional[float]

        customer_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactByIdResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contacts",
            method="POST",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "position": position,
                "company": company,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items, annotation=typing.Sequence[ContactItemPayload], direction="write"
                ),
                "email": email,
                "isMain": is_main,
                "isBilling": is_billing,
                "siteId": site_id,
                "customerId": customer_id,
                "contactType": contact_type,
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
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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

    async def get_contacts_contact_id(
        self, contact_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContactByIdResponse]:
        """
        Returns a contact by ID.

        Parameters
        ----------
        contact_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contacts/{encode_path_param(contact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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

    async def put_contacts_contact_id(
        self,
        contact_id: float,
        *,
        first_name: str,
        contact_items: typing.Sequence[ContactItemPayload],
        last_name: typing.Optional[str] = OMIT,
        position: typing.Optional[str] = OMIT,
        company: typing.Optional[str] = OMIT,
        is_main: typing.Optional[bool] = OMIT,
        is_billing: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContactByIdResponse]:
        """
        Updates a customer contact or site contact.

          - **firstName** is required
          - NOTE: To update the main contact of a `CUSTOMER`, please use the /customers endpoint.
            - When the contact to update is of type `CUSTOMER`:
              - **isMain** cannot be set to true and is optional. To update the main contact, use the '/customers' endpoint.
              - **isBilling** is optional and defaults to false.
          - NOTE: To unset the main contact of a `SITE` as non-main is not allowed, either use the create endpoint or update another contact of this site and set it as the main contact.
            - When the contact to update is of type `SITE`:
              - **isMain** is optional and defaults to false.
              - **isBilling** is optional and defaults to false.
              - If the contact to update is the main and billing contact of the `SITE`, the **isBilling** flag will have no impact and the contact details will be updated. If you want to change the contact that is assigned as the billing contact, please use the create method or update another contact of this site and set it as a billing contact.
          - **contactItems** at least one contact item of type email is required.
            - It will replace the existing contact items.
            - To update a specific contact item, you have to provide the id of the contact item to update. Otherwise, new contact items will be added.

        Parameters
        ----------
        contact_id : float

        first_name : str

        contact_items : typing.Sequence[ContactItemPayload]

        last_name : typing.Optional[str]

        position : typing.Optional[str]

        company : typing.Optional[str]

        is_main : typing.Optional[bool]

        is_billing : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contacts/{encode_path_param(contact_id)}",
            method="PUT",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "position": position,
                "company": company,
                "isMain": is_main,
                "isBilling": is_billing,
                "contactItems": convert_and_respect_annotation_metadata(
                    object_=contact_items, annotation=typing.Sequence[ContactItemPayload], direction="write"
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
                    ContactByIdResponse,
                    parse_obj_as(
                        type_=ContactByIdResponse,
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
