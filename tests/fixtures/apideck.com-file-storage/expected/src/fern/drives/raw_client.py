

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.create_drive_response import CreateDriveResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_drive_response import DeleteDriveResponse
from ..types.description import Description
from ..types.drives_filter import DrivesFilter
from ..types.get_drive_response import GetDriveResponse
from ..types.get_drives_response import GetDrivesResponse
from ..types.id import Id
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_drive_response import UpdateDriveResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy


OMIT = typing.cast(typing.Any, ...)


class RawDrivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[DrivesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDrivesResponse]:
        """
        List Drives

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[DrivesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDrivesResponse]
            Drives
        """
        _response = self._client_wrapper.httpx_client.request(
            "file-storage/drives",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=DrivesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDrivesResponse,
                    parse_obj_as(
                        type_=GetDrivesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[Description] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDriveResponse]:
        """
        Create Drive

        Parameters
        ----------
        name : str
            The name of the drive

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[Description]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDriveResponse]
            Drives
        """
        _response = self._client_wrapper.httpx_client.request(
            "file-storage/drives",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    CreateDriveResponse,
                    parse_obj_as(
                        type_=CreateDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDriveResponse]:
        """
        Get Drive

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDriveResponse]
            Drives
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDriveResponse,
                    parse_obj_as(
                        type_=GetDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteDriveResponse]:
        """
        Delete Drive

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDriveResponse]
            Drives
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDriveResponse,
                    parse_obj_as(
                        type_=DeleteDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[Description] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateDriveResponse]:
        """
        Update Drive

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str
            The name of the drive

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[Description]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateDriveResponse]
            Drives
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    UpdateDriveResponse,
                    parse_obj_as(
                        type_=UpdateDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDrivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[DrivesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDrivesResponse]:
        """
        List Drives

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[DrivesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDrivesResponse]
            Drives
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file-storage/drives",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=DrivesFilter, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDrivesResponse,
                    parse_obj_as(
                        type_=GetDrivesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add(
        self,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[Description] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDriveResponse]:
        """
        Create Drive

        Parameters
        ----------
        name : str
            The name of the drive

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[Description]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDriveResponse]
            Drives
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file-storage/drives",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    CreateDriveResponse,
                    parse_obj_as(
                        type_=CreateDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDriveResponse]:
        """
        Get Drive

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDriveResponse]
            Drives
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDriveResponse,
                    parse_obj_as(
                        type_=GetDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteDriveResponse]:
        """
        Delete Drive

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDriveResponse]
            Drives
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteDriveResponse,
                    parse_obj_as(
                        type_=DeleteDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id_: str,
        *,
        name: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[Description] = OMIT,
        id: typing.Optional[Id] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateDriveResponse]:
        """
        Update Drive

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        name : str
            The name of the drive

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[Description]

        id : typing.Optional[Id]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateDriveResponse]
            Drives
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/drives/{jsonable_encoder(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "id": id,
                "name": name,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    UpdateDriveResponse,
                    parse_obj_as(
                        type_=UpdateDriveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
