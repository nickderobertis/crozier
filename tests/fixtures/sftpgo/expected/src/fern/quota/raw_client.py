

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_response import ApiResponse
from ..types.folder_quota_scan import FolderQuotaScan
from ..types.quota_scan import QuotaScan
from .types.folder_quota_update_usage_request_mode import FolderQuotaUpdateUsageRequestMode
from .types.user_quota_update_usage_request_mode import UserQuotaUpdateUsageRequestMode
from .types.user_transfer_quota_update_usage_request_mode import UserTransferQuotaUpdateUsageRequestMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawQuotaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_users_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[QuotaScan]]:
        """
        Returns the active user quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[QuotaScan]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "quotas/users/scans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[QuotaScan],
                    parse_obj_as(
                        type_=typing.List[QuotaScan],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def start_user_quota_scan(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiResponse]:
        """
        Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/scan",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def user_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Sets the current used quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_quota_size": used_quota_size,
                "used_quota_files": used_quota_files,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def user_transfer_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserTransferQuotaUpdateUsageRequestMode] = None,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Sets the current used transfer quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserTransferQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_upload_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        used_download_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/transfer-usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_upload_data_transfer": used_upload_data_transfer,
                "used_download_data_transfer": used_download_data_transfer,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def get_folders_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FolderQuotaScan]]:
        """
        Returns the active folder quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FolderQuotaScan]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "quotas/folders/scans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FolderQuotaScan],
                    parse_obj_as(
                        type_=typing.List[FolderQuotaScan],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def start_folder_quota_scan(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiResponse]:
        """
        Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder

        Parameters
        ----------
        name : str
            folder name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"quotas/folders/{encode_path_param(name)}/scan",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def folder_quota_update_usage(
        self,
        name: str,
        *,
        mode: typing.Optional[FolderQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Sets the current used quota limits for the given folder

        Parameters
        ----------
        name : str
            folder name

        mode : typing.Optional[FolderQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"quotas/folders/{encode_path_param(name)}/usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_quota_size": used_quota_size,
                "used_quota_files": used_quota_files,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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


class AsyncRawQuotaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_users_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[QuotaScan]]:
        """
        Returns the active user quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[QuotaScan]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "quotas/users/scans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[QuotaScan],
                    parse_obj_as(
                        type_=typing.List[QuotaScan],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def start_user_quota_scan(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota

        Parameters
        ----------
        username : str
            the username

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/scan",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def user_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Sets the current used quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_quota_size": used_quota_size,
                "used_quota_files": used_quota_files,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def user_transfer_quota_update_usage(
        self,
        username: str,
        *,
        mode: typing.Optional[UserTransferQuotaUpdateUsageRequestMode] = None,
        used_upload_data_transfer: typing.Optional[int] = OMIT,
        used_download_data_transfer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Sets the current used transfer quota limits for the given user

        Parameters
        ----------
        username : str
            the username

        mode : typing.Optional[UserTransferQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_upload_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        used_download_data_transfer : typing.Optional[int]
            The value must be specified as bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"quotas/users/{encode_path_param(username)}/transfer-usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_upload_data_transfer": used_upload_data_transfer,
                "used_download_data_transfer": used_download_data_transfer,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def get_folders_quota_scans(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FolderQuotaScan]]:
        """
        Returns the active folder quota scans

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FolderQuotaScan]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "quotas/folders/scans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FolderQuotaScan],
                    parse_obj_as(
                        type_=typing.List[FolderQuotaScan],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def start_folder_quota_scan(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder

        Parameters
        ----------
        name : str
            folder name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"quotas/folders/{encode_path_param(name)}/scan",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def folder_quota_update_usage(
        self,
        name: str,
        *,
        mode: typing.Optional[FolderQuotaUpdateUsageRequestMode] = None,
        used_quota_size: typing.Optional[int] = OMIT,
        used_quota_files: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Sets the current used quota limits for the given folder

        Parameters
        ----------
        name : str
            folder name

        mode : typing.Optional[FolderQuotaUpdateUsageRequestMode]
            the update mode specifies if the given quota usage values should be added or replace the current ones

        used_quota_size : typing.Optional[int]

        used_quota_files : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"quotas/folders/{encode_path_param(name)}/usage",
            method="PUT",
            params={
                "mode": mode,
            },
            json={
                "used_quota_size": used_quota_size,
                "used_quota_files": used_quota_files,
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
                    ApiResponse,
                    parse_obj_as(
                        type_=ApiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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
