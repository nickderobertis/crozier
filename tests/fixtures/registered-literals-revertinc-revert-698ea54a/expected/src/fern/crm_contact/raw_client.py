

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
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.common_base_error import CommonBaseError
from ..types.common_contact_association import CommonContactAssociation
from ..types.crm_create_or_update_contact_response import CrmCreateOrUpdateContactResponse
from ..types.crm_get_contact_response import CrmGetContactResponse
from ..types.crm_get_contacts_response import CrmGetContactsResponse
from ..types.crm_search_contacts_response import CrmSearchContactsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrmContactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crm_contact_get_contact(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetContactResponse]:
        """
        Get details of a contact

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetContactResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetContactResponse,
                    parse_obj_as(
                        type_=CrmGetContactResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_contact_update_contact(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateContactResponse]:
        """
        Update a contact

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateContactResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonContactAssociation, direction="write"
                ),
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
                "email": email,
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
                    CrmCreateOrUpdateContactResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateContactResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_contact_get_contacts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmGetContactsResponse]:
        """
        Get all the contacts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmGetContactsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetContactsResponse,
                    parse_obj_as(
                        type_=CrmGetContactsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_contact_create_contact(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmCreateOrUpdateContactResponse]:
        """
        Create a new contact

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmCreateOrUpdateContactResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonContactAssociation, direction="write"
                ),
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
                "email": email,
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
                    CrmCreateOrUpdateContactResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateContactResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crm_contact_search_contacts(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrmSearchContactsResponse]:
        """
        Search for contacts

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrmSearchContactsResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/contacts/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
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
                    CrmSearchContactsResponse,
                    parse_obj_as(
                        type_=CrmSearchContactsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCrmContactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crm_contact_get_contact(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetContactResponse]:
        """
        Get details of a contact

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetContactResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="GET",
            params={
                "fields": fields,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetContactResponse,
                    parse_obj_as(
                        type_=CrmGetContactResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_contact_update_contact(
        self,
        id: str,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateContactResponse]:
        """
        Update a contact

        Parameters
        ----------
        id : str

        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateContactResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/contacts/{encode_path_param(id)}",
            method="PATCH",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonContactAssociation, direction="write"
                ),
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
                "email": email,
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
                    CrmCreateOrUpdateContactResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateContactResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_contact_get_contacts(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmGetContactsResponse]:
        """
        Get all the contacts

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmGetContactsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="GET",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
                "associations": associations,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CrmGetContactsResponse,
                    parse_obj_as(
                        type_=CrmGetContactsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_contact_create_contact(
        self,
        *,
        additional: typing.Any,
        first_name: str,
        last_name: str,
        phone: str,
        email: str,
        associations: typing.Optional[CommonContactAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmCreateOrUpdateContactResponse]:
        """
        Create a new contact

        Parameters
        ----------
        additional : typing.Any

        first_name : str
            The first name of the contact in a CRM.

        last_name : str
            The last name of the contact in a CRM.

        phone : str
            The phone number of the contact in a CRM.

        email : str
            The email of the contact in a CRM.

        associations : typing.Optional[CommonContactAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmCreateOrUpdateContactResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/contacts",
            method="POST",
            json={
                "additional": additional,
                "associations": convert_and_respect_annotation_metadata(
                    object_=associations, annotation=CommonContactAssociation, direction="write"
                ),
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
                "email": email,
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
                    CrmCreateOrUpdateContactResponse,
                    parse_obj_as(
                        type_=CrmCreateOrUpdateContactResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crm_contact_search_contacts(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrmSearchContactsResponse]:
        """
        Search for contacts

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrmSearchContactsResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/contacts/search",
            method="POST",
            params={
                "fields": fields,
                "pageSize": page_size,
                "cursor": cursor,
            },
            json={
                "searchCriteria": search_criteria,
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
                    CrmSearchContactsResponse,
                    parse_obj_as(
                        type_=CrmSearchContactsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        CommonBaseError,
                        parse_obj_as(
                            type_=CommonBaseError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
