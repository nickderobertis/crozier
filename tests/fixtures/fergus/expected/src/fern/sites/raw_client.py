

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
from ..types.person_payload import PersonPayload
from ..types.site_by_id_response import SiteByIdResponse
from ..types.sites_response import SitesResponse
from .types.get_sites_request_sort_field import GetSitesRequestSortField
from .types.get_sites_request_sort_order import GetSitesRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_sites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetSitesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_site_name: typing.Optional[str] = None,
        filter_address_city: typing.Optional[str] = None,
        filter_address_postal_code: typing.Optional[str] = None,
        sort_field: typing.Optional[GetSitesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SitesResponse]:
        """
        Returns a list of sites. The list can be filtered by site name, address city, and address postal code.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetSitesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_site_name : typing.Optional[str]

        filter_address_city : typing.Optional[str]

        filter_address_postal_code : typing.Optional[str]

        sort_field : typing.Optional[GetSitesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `defaultContact.firstName`
            - `defaultContact.lastName`
            - `customer.customerFullName`
            - `billingContact.firstName`
            - `billingContact.lastName`
            - `physicalAddress.address1`
            - `physicalAddress.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SitesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "sites",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterSiteName": filter_site_name,
                "filterAddressCity": filter_address_city,
                "filterAddressPostalCode": filter_address_postal_code,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SitesResponse,
                    parse_obj_as(
                        type_=SitesResponse,
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

    def post_sites(
        self,
        *,
        default_contact: PersonPayload,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        billing_contact: typing.Optional[PersonPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SiteByIdResponse]:
        """
        Create a new site

        Parameters
        ----------
        default_contact : PersonPayload

        site_address : AddressPayload

        name : typing.Optional[str]

        billing_contact : typing.Optional[PersonPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiteByIdResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "sites",
            method="POST",
            json={
                "name": name,
                "defaultContact": convert_and_respect_annotation_metadata(
                    object_=default_contact, annotation=PersonPayload, direction="write"
                ),
                "billingContact": convert_and_respect_annotation_metadata(
                    object_=billing_contact, annotation=PersonPayload, direction="write"
                ),
                "siteAddress": convert_and_respect_annotation_metadata(
                    object_=site_address, annotation=AddressPayload, direction="write"
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
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    def get_sites_site_id(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SiteByIdResponse]:
        """
        Returns a site by ID.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    def patch_sites_site_id(
        self,
        site_id: str,
        *,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SiteByIdResponse]:
        """
        Update site

        Parameters
        ----------
        site_id : str

        site_address : AddressPayload

        name : typing.Optional[str]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}",
            method="PATCH",
            json={
                "name": name,
                "siteAddress": convert_and_respect_annotation_metadata(
                    object_=site_address, annotation=AddressPayload, direction="write"
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
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    def post_sites_site_id_archive(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Archive Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/archive",
            method="POST",
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

    def post_sites_site_id_restore(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SiteByIdResponse]:
        """
        Restore Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/restore",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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


class AsyncRawSitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_sites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetSitesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_site_name: typing.Optional[str] = None,
        filter_address_city: typing.Optional[str] = None,
        filter_address_postal_code: typing.Optional[str] = None,
        sort_field: typing.Optional[GetSitesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SitesResponse]:
        """
        Returns a list of sites. The list can be filtered by site name, address city, and address postal code.

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetSitesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_site_name : typing.Optional[str]

        filter_address_city : typing.Optional[str]

        filter_address_postal_code : typing.Optional[str]

        sort_field : typing.Optional[GetSitesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `name`
            - `defaultContact.firstName`
            - `defaultContact.lastName`
            - `customer.customerFullName`
            - `billingContact.firstName`
            - `billingContact.lastName`
            - `physicalAddress.address1`
            - `physicalAddress.address2`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SitesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sites",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterSiteName": filter_site_name,
                "filterAddressCity": filter_address_city,
                "filterAddressPostalCode": filter_address_postal_code,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SitesResponse,
                    parse_obj_as(
                        type_=SitesResponse,
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

    async def post_sites(
        self,
        *,
        default_contact: PersonPayload,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        billing_contact: typing.Optional[PersonPayload] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SiteByIdResponse]:
        """
        Create a new site

        Parameters
        ----------
        default_contact : PersonPayload

        site_address : AddressPayload

        name : typing.Optional[str]

        billing_contact : typing.Optional[PersonPayload]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiteByIdResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sites",
            method="POST",
            json={
                "name": name,
                "defaultContact": convert_and_respect_annotation_metadata(
                    object_=default_contact, annotation=PersonPayload, direction="write"
                ),
                "billingContact": convert_and_respect_annotation_metadata(
                    object_=billing_contact, annotation=PersonPayload, direction="write"
                ),
                "siteAddress": convert_and_respect_annotation_metadata(
                    object_=site_address, annotation=AddressPayload, direction="write"
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
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    async def get_sites_site_id(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SiteByIdResponse]:
        """
        Returns a site by ID.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    async def patch_sites_site_id(
        self,
        site_id: str,
        *,
        site_address: AddressPayload,
        name: typing.Optional[str] = OMIT,
        postal_address: typing.Optional[AddressPayload] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SiteByIdResponse]:
        """
        Update site

        Parameters
        ----------
        site_id : str

        site_address : AddressPayload

        name : typing.Optional[str]

        postal_address : typing.Optional[AddressPayload]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}",
            method="PATCH",
            json={
                "name": name,
                "siteAddress": convert_and_respect_annotation_metadata(
                    object_=site_address, annotation=AddressPayload, direction="write"
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
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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

    async def post_sites_site_id_archive(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Archive Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/archive",
            method="POST",
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

    async def post_sites_site_id_restore(
        self, site_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SiteByIdResponse]:
        """
        Restore Site.

        Parameters
        ----------
        site_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SiteByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/restore",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SiteByIdResponse,
                    parse_obj_as(
                        type_=SiteByIdResponse,
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
