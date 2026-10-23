

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_contact_response import CreateContactResponse
from .types.upload_bulk_contacts_request_contacts_item import UploadBulkContactsRequestContactsItem
from .types.upload_bulk_contacts_response import UploadBulkContactsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementApiContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_bulk_contacts(
        self,
        *,
        workspace_id: str,
        contacts: typing.Sequence[UploadBulkContactsRequestContactsItem],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadBulkContactsResponse]:
        """
        Uploads contacts in bulk. This endpoint expects the bulk request shape: `contacts` must be an array, and each contact item must contain an `attributes` array of `{ attributeKey, value }` objects. Unlike `POST /management/contacts`, this endpoint does not accept a top-level `attributes` object. Each contact must include an `email` attribute in its `attributes` array, and that email must be valid. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        contacts : typing.Sequence[UploadBulkContactsRequestContactsItem]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadBulkContactsResponse]
            Contacts uploaded successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/contacts/bulk",
            method="PUT",
            json={
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "contacts": convert_and_respect_annotation_metadata(
                    object_=contacts,
                    annotation=typing.Sequence[UploadBulkContactsRequestContactsItem],
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
                    UploadBulkContactsResponse,
                    parse_obj_as(
                        type_=UploadBulkContactsResponse,
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

    def create_contact(
        self,
        *,
        workspace_id: str,
        attributes: typing.Dict[str, str],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateContactResponse]:
        """
        Creates a single contact in the database. This endpoint expects a top-level `attributes` object. For bulk uploads, use `PUT /management/contacts/bulk`, which expects `contacts[].attributes[]` instead. Each contact must have a valid email address in the attributes. All attribute keys must already exist in the Workspace. The email is used as the unique identifier along with the Workspace. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        attributes : typing.Dict[str, str]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateContactResponse]
            Contact created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/contacts",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "attributes": attributes,
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
                    CreateContactResponse,
                    parse_obj_as(
                        type_=CreateContactResponse,
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


class AsyncRawManagementApiContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_bulk_contacts(
        self,
        *,
        workspace_id: str,
        contacts: typing.Sequence[UploadBulkContactsRequestContactsItem],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadBulkContactsResponse]:
        """
        Uploads contacts in bulk. This endpoint expects the bulk request shape: `contacts` must be an array, and each contact item must contain an `attributes` array of `{ attributeKey, value }` objects. Unlike `POST /management/contacts`, this endpoint does not accept a top-level `attributes` object. Each contact must include an `email` attribute in its `attributes` array, and that email must be valid. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        contacts : typing.Sequence[UploadBulkContactsRequestContactsItem]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadBulkContactsResponse]
            Contacts uploaded successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/contacts/bulk",
            method="PUT",
            json={
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "contacts": convert_and_respect_annotation_metadata(
                    object_=contacts,
                    annotation=typing.Sequence[UploadBulkContactsRequestContactsItem],
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
                    UploadBulkContactsResponse,
                    parse_obj_as(
                        type_=UploadBulkContactsResponse,
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

    async def create_contact(
        self,
        *,
        workspace_id: str,
        attributes: typing.Dict[str, str],
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateContactResponse]:
        """
        Creates a single contact in the database. This endpoint expects a top-level `attributes` object. For bulk uploads, use `PUT /management/contacts/bulk`, which expects `contacts[].attributes[]` instead. Each contact must have a valid email address in the attributes. All attribute keys must already exist in the Workspace. The email is used as the unique identifier along with the Workspace. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str

        attributes : typing.Dict[str, str]

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateContactResponse]
            Contact created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/contacts",
            method="POST",
            json={
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "attributes": attributes,
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
                    CreateContactResponse,
                    parse_obj_as(
                        type_=CreateContactResponse,
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
