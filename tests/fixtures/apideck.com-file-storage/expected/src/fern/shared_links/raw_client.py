

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
from ..types.create_shared_link_response import CreateSharedLinkResponse
from ..types.created_at import CreatedAt
from ..types.delete_shared_link_response import DeleteSharedLinkResponse
from ..types.expires_at import ExpiresAt
from ..types.get_shared_link_response import GetSharedLinkResponse
from ..types.get_shared_links_response import GetSharedLinksResponse
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.shared_link_scope import SharedLinkScope
from ..types.shared_link_target import SharedLinkTarget
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_shared_link_response import UpdateSharedLinkResponse
from ..types.updated_at import UpdatedAt


OMIT = typing.cast(typing.Any, ...)


class RawSharedLinksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSharedLinksResponse]:
        """
        List SharedLinks

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSharedLinksResponse]
            Shared Links
        """
        _response = self._client_wrapper.httpx_client.request(
            "file-storage/shared-links",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSharedLinksResponse,
                    parse_obj_as(
                        type_=GetSharedLinksResponse,
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
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSharedLinkResponse]:
        """
        Create Shared Link

        Parameters
        ----------
        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSharedLinkResponse]
            Shared Links
        """
        _response = self._client_wrapper.httpx_client.request(
            "file-storage/shared-links",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "download_url": download_url,
                "expires_at": expires_at,
                "password": password,
                "password_protected": password_protected,
                "scope": scope,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=SharedLinkTarget, direction="write"
                ),
                "target_id": target_id,
                "updated_at": updated_at,
                "url": url,
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
                    CreateSharedLinkResponse,
                    parse_obj_as(
                        type_=CreateSharedLinkResponse,
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
    ) -> HttpResponse[GetSharedLinkResponse]:
        """
        Get Shared Link

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
        HttpResponse[GetSharedLinkResponse]
            Shared Link
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
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
                    GetSharedLinkResponse,
                    parse_obj_as(
                        type_=GetSharedLinkResponse,
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
    ) -> HttpResponse[DeleteSharedLinkResponse]:
        """
        Delete Shared Link

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
        HttpResponse[DeleteSharedLinkResponse]
            Shared Links
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSharedLinkResponse,
                    parse_obj_as(
                        type_=DeleteSharedLinkResponse,
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
        id: str,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSharedLinkResponse]:
        """
        Update Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSharedLinkResponse]
            Shared Links
        """
        _response = self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "download_url": download_url,
                "expires_at": expires_at,
                "password": password,
                "password_protected": password_protected,
                "scope": scope,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=SharedLinkTarget, direction="write"
                ),
                "target_id": target_id,
                "updated_at": updated_at,
                "url": url,
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
                    UpdateSharedLinkResponse,
                    parse_obj_as(
                        type_=UpdateSharedLinkResponse,
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


class AsyncRawSharedLinksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSharedLinksResponse]:
        """
        List SharedLinks

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSharedLinksResponse]
            Shared Links
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file-storage/shared-links",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSharedLinksResponse,
                    parse_obj_as(
                        type_=GetSharedLinksResponse,
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
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSharedLinkResponse]:
        """
        Create Shared Link

        Parameters
        ----------
        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSharedLinkResponse]
            Shared Links
        """
        _response = await self._client_wrapper.httpx_client.request(
            "file-storage/shared-links",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "download_url": download_url,
                "expires_at": expires_at,
                "password": password,
                "password_protected": password_protected,
                "scope": scope,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=SharedLinkTarget, direction="write"
                ),
                "target_id": target_id,
                "updated_at": updated_at,
                "url": url,
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
                    CreateSharedLinkResponse,
                    parse_obj_as(
                        type_=CreateSharedLinkResponse,
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
    ) -> AsyncHttpResponse[GetSharedLinkResponse]:
        """
        Get Shared Link

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
        AsyncHttpResponse[GetSharedLinkResponse]
            Shared Link
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
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
                    GetSharedLinkResponse,
                    parse_obj_as(
                        type_=GetSharedLinkResponse,
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
    ) -> AsyncHttpResponse[DeleteSharedLinkResponse]:
        """
        Delete Shared Link

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
        AsyncHttpResponse[DeleteSharedLinkResponse]
            Shared Links
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSharedLinkResponse,
                    parse_obj_as(
                        type_=DeleteSharedLinkResponse,
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
        id: str,
        *,
        target_id: str,
        raw: typing.Optional[bool] = None,
        created_at: typing.Optional[CreatedAt] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        expires_at: typing.Optional[ExpiresAt] = OMIT,
        password: typing.Optional[str] = OMIT,
        password_protected: typing.Optional[bool] = OMIT,
        scope: typing.Optional[SharedLinkScope] = OMIT,
        target: typing.Optional[SharedLinkTarget] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSharedLinkResponse]:
        """
        Update Shared Link

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        target_id : str
            The ID of the file or folder to link.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        created_at : typing.Optional[CreatedAt]

        download_url : typing.Optional[str]
            The URL that can be used to download the file.

        expires_at : typing.Optional[ExpiresAt]

        password : typing.Optional[str]
            Optional password for the shared link.

        password_protected : typing.Optional[bool]
            Indicated if the shared link is password protected.

        scope : typing.Optional[SharedLinkScope]
            The scope of the shared link.

        target : typing.Optional[SharedLinkTarget]

        updated_at : typing.Optional[UpdatedAt]

        url : typing.Optional[str]
            The URL that can be used to view the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSharedLinkResponse]
            Shared Links
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"file-storage/shared-links/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "created_at": created_at,
                "download_url": download_url,
                "expires_at": expires_at,
                "password": password,
                "password_protected": password_protected,
                "scope": scope,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=SharedLinkTarget, direction="write"
                ),
                "target_id": target_id,
                "updated_at": updated_at,
                "url": url,
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
                    UpdateSharedLinkResponse,
                    parse_obj_as(
                        type_=UpdateSharedLinkResponse,
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
