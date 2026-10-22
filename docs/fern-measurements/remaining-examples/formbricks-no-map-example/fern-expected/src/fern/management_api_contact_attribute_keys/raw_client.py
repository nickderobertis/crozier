

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.contact_attribute_key_id import ContactAttributeKeyId
from .types.create_contact_attribute_key_response import CreateContactAttributeKeyResponse
from .types.delete_contact_attribute_key_response import DeleteContactAttributeKeyResponse
from .types.get_contact_attribute_key_response import GetContactAttributeKeyResponse
from .types.get_contact_attribute_keys_request_filter_date_field import GetContactAttributeKeysRequestFilterDateField
from .types.get_contact_attribute_keys_request_order import GetContactAttributeKeysRequestOrder
from .types.get_contact_attribute_keys_request_sort_by import GetContactAttributeKeysRequestSortBy
from .types.get_contact_attribute_keys_response import GetContactAttributeKeysResponse
from .types.update_contact_attribute_key_response import UpdateContactAttributeKeyResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementApiContactAttributeKeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_contact_attribute_keys(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetContactAttributeKeysRequestSortBy] = None,
        order: typing.Optional[GetContactAttributeKeysRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetContactAttributeKeysRequestFilterDateField] = None,
        workspace_id: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetContactAttributeKeysResponse]:
        """
        Gets contact attribute keys from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetContactAttributeKeysRequestSortBy]
            Sort by field

        order : typing.Optional[GetContactAttributeKeysRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetContactAttributeKeysRequestFilterDateField]
            Date field to filter by

        workspace_id : typing.Optional[str]
            The Workspace ID to filter by

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetContactAttributeKeysResponse]
            Contact attribute keys retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/contact-attribute-keys",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactAttributeKeysResponse,
                    parse_obj_as(
                        type_=GetContactAttributeKeysResponse,
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

    def create_contact_attribute_key(
        self,
        *,
        key: str,
        workspace_id: str,
        environment_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateContactAttributeKeyResponse]:
        """
        Creates a contact attribute key in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        key : str
            The attribute identifier used in the system

        workspace_id : str
            The ID of the Workspace this attribute belongs to

        environment_id : str
            Deprecated alias for workspaceId.

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateContactAttributeKeyResponse]
            Contact attribute key created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/contact-attribute-keys",
            method="POST",
            json={
                "key": key,
                "name": name,
                "description": description,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
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
                    CreateContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=CreateContactAttributeKeyResponse,
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

    def get_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetContactAttributeKeyResponse]:
        """
        Gets a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetContactAttributeKeyResponse]
            Contact attribute key retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=GetContactAttributeKeyResponse,
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

    def update_contact_attribute_key(
        self,
        id: ContactAttributeKeyId,
        *,
        key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateContactAttributeKeyResponse]:
        """
        Updates a contact attribute key in the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        key : str
            The attribute identifier used in the system

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateContactAttributeKeyResponse]
            Contact attribute key updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "key": key,
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
                    UpdateContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=UpdateContactAttributeKeyResponse,
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

    def delete_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteContactAttributeKeyResponse]:
        """
        Deletes a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteContactAttributeKeyResponse]
            Contact attribute key deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=DeleteContactAttributeKeyResponse,
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


class AsyncRawManagementApiContactAttributeKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_contact_attribute_keys(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetContactAttributeKeysRequestSortBy] = None,
        order: typing.Optional[GetContactAttributeKeysRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetContactAttributeKeysRequestFilterDateField] = None,
        workspace_id: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetContactAttributeKeysResponse]:
        """
        Gets contact attribute keys from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetContactAttributeKeysRequestSortBy]
            Sort by field

        order : typing.Optional[GetContactAttributeKeysRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetContactAttributeKeysRequestFilterDateField]
            Date field to filter by

        workspace_id : typing.Optional[str]
            The Workspace ID to filter by

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetContactAttributeKeysResponse]
            Contact attribute keys retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/contact-attribute-keys",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactAttributeKeysResponse,
                    parse_obj_as(
                        type_=GetContactAttributeKeysResponse,
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

    async def create_contact_attribute_key(
        self,
        *,
        key: str,
        workspace_id: str,
        environment_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateContactAttributeKeyResponse]:
        """
        Creates a contact attribute key in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        key : str
            The attribute identifier used in the system

        workspace_id : str
            The ID of the Workspace this attribute belongs to

        environment_id : str
            Deprecated alias for workspaceId.

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateContactAttributeKeyResponse]
            Contact attribute key created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/contact-attribute-keys",
            method="POST",
            json={
                "key": key,
                "name": name,
                "description": description,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
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
                    CreateContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=CreateContactAttributeKeyResponse,
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

    async def get_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetContactAttributeKeyResponse]:
        """
        Gets a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetContactAttributeKeyResponse]
            Contact attribute key retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=GetContactAttributeKeyResponse,
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

    async def update_contact_attribute_key(
        self,
        id: ContactAttributeKeyId,
        *,
        key: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateContactAttributeKeyResponse]:
        """
        Updates a contact attribute key in the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        key : str
            The attribute identifier used in the system

        name : typing.Optional[str]
            Display name for the attribute

        description : typing.Optional[str]
            Description of the attribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateContactAttributeKeyResponse]
            Contact attribute key updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "key": key,
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
                    UpdateContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=UpdateContactAttributeKeyResponse,
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

    async def delete_contact_attribute_key(
        self, id: ContactAttributeKeyId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteContactAttributeKeyResponse]:
        """
        Deletes a contact attribute key from the database.

        Parameters
        ----------
        id : ContactAttributeKeyId
            The ID of the contact attribute key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteContactAttributeKeyResponse]
            Contact attribute key deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/contact-attribute-keys/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteContactAttributeKeyResponse,
                    parse_obj_as(
                        type_=DeleteContactAttributeKeyResponse,
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
