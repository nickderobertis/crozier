

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.admin import Admin
from ..types.api_key import ApiKey
from ..types.api_response import ApiResponse
from ..types.base_virtual_folder import BaseVirtualFolder
from ..types.dump_data_scopes import DumpDataScopes
from ..types.event_action import EventAction
from ..types.event_rule import EventRule
from ..types.group import Group
from ..types.role import Role
from ..types.services_status import ServicesStatus
from ..types.share import Share
from ..types.user import User
from ..types.version_info import VersionInfo
from .types.dumpdata_response import DumpdataResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[VersionInfo]:
        """
        Returns version details such as the version number, build date, commit hash and enabled features

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VersionInfo]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionInfo,
                    parse_obj_as(
                        type_=VersionInfo,
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

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ServicesStatus]:
        """
        Retrieves the status of the active services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ServicesStatus]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicesStatus,
                    parse_obj_as(
                        type_=ServicesStatus,
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

    def dumpdata(
        self,
        *,
        output_file: typing.Optional[str] = None,
        output_data: typing.Optional[int] = None,
        indent: typing.Optional[int] = None,
        scopes: typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DumpdataResponse]:
        """
        Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata

        Parameters
        ----------
        output_file : typing.Optional[str]
            Path for the file to write the JSON serialized data to. This path is relative to the configured "backups_path". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead.

        output_data : typing.Optional[int]
            output data:
              * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required
              * `1` the backup will be returned as response body

        indent : typing.Optional[int]
            indent:
              * `0` no indentation. This is the default
              * `1` format the output JSON

        scopes : typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]]
            You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DumpdataResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "dumpdata",
            method="GET",
            params={
                "output-file": output_file,
                "output-data": output_data,
                "indent": indent,
                "scopes": ",".join(map(str, scopes)) if isinstance(scopes, (list, tuple, set)) else scopes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DumpdataResponse,
                    parse_obj_as(
                        type_=DumpdataResponse,
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

    def loaddata_from_file(
        self,
        *,
        input_file: str,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        input_file : str
            Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured "backups_path". The max allowed file size is 10MB

        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "loaddata",
            method="GET",
            params={
                "scan-quota": scan_quota,
                "mode": mode,
                "input-file": input_file,
            },
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

    def loaddata_from_request_body(
        self,
        *,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        users: typing.Optional[typing.Sequence[User]] = OMIT,
        folders: typing.Optional[typing.Sequence[BaseVirtualFolder]] = OMIT,
        groups: typing.Optional[typing.Sequence[Group]] = OMIT,
        admins: typing.Optional[typing.Sequence[Admin]] = OMIT,
        api_keys: typing.Optional[typing.Sequence[ApiKey]] = OMIT,
        shares: typing.Optional[typing.Sequence[Share]] = OMIT,
        event_actions: typing.Optional[typing.Sequence[EventAction]] = OMIT,
        event_rules: typing.Optional[typing.Sequence[EventRule]] = OMIT,
        roles: typing.Optional[typing.Sequence[Role]] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiResponse]:
        """
        Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        users : typing.Optional[typing.Sequence[User]]

        folders : typing.Optional[typing.Sequence[BaseVirtualFolder]]

        groups : typing.Optional[typing.Sequence[Group]]

        admins : typing.Optional[typing.Sequence[Admin]]

        api_keys : typing.Optional[typing.Sequence[ApiKey]]

        shares : typing.Optional[typing.Sequence[Share]]

        event_actions : typing.Optional[typing.Sequence[EventAction]]

        event_rules : typing.Optional[typing.Sequence[EventRule]]

        roles : typing.Optional[typing.Sequence[Role]]

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiResponse]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "loaddata",
            method="POST",
            params={
                "scan-quota": scan_quota,
                "mode": mode,
            },
            json={
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[User], direction="write"
                ),
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=typing.Sequence[BaseVirtualFolder], direction="write"
                ),
                "groups": convert_and_respect_annotation_metadata(
                    object_=groups, annotation=typing.Sequence[Group], direction="write"
                ),
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[Admin], direction="write"
                ),
                "api_keys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ApiKey], direction="write"
                ),
                "shares": convert_and_respect_annotation_metadata(
                    object_=shares, annotation=typing.Sequence[Share], direction="write"
                ),
                "event_actions": convert_and_respect_annotation_metadata(
                    object_=event_actions, annotation=typing.Sequence[EventAction], direction="write"
                ),
                "event_rules": convert_and_respect_annotation_metadata(
                    object_=event_rules, annotation=typing.Sequence[EventRule], direction="write"
                ),
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles, annotation=typing.Sequence[Role], direction="write"
                ),
                "version": version,
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


class AsyncRawMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_version(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VersionInfo]:
        """
        Returns version details such as the version number, build date, commit hash and enabled features

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VersionInfo]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "version",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VersionInfo,
                    parse_obj_as(
                        type_=VersionInfo,
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

    async def get_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ServicesStatus]:
        """
        Retrieves the status of the active services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ServicesStatus]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicesStatus,
                    parse_obj_as(
                        type_=ServicesStatus,
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

    async def dumpdata(
        self,
        *,
        output_file: typing.Optional[str] = None,
        output_data: typing.Optional[int] = None,
        indent: typing.Optional[int] = None,
        scopes: typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DumpdataResponse]:
        """
        Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata

        Parameters
        ----------
        output_file : typing.Optional[str]
            Path for the file to write the JSON serialized data to. This path is relative to the configured "backups_path". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead.

        output_data : typing.Optional[int]
            output data:
              * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required
              * `1` the backup will be returned as response body

        indent : typing.Optional[int]
            indent:
              * `0` no indentation. This is the default
              * `1` format the output JSON

        scopes : typing.Optional[typing.Union[DumpDataScopes, typing.Sequence[DumpDataScopes]]]
            You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DumpdataResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dumpdata",
            method="GET",
            params={
                "output-file": output_file,
                "output-data": output_data,
                "indent": indent,
                "scopes": ",".join(map(str, scopes)) if isinstance(scopes, (list, tuple, set)) else scopes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DumpdataResponse,
                    parse_obj_as(
                        type_=DumpdataResponse,
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

    async def loaddata_from_file(
        self,
        *,
        input_file: str,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        input_file : str
            Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured "backups_path". The max allowed file size is 10MB

        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "loaddata",
            method="GET",
            params={
                "scan-quota": scan_quota,
                "mode": mode,
                "input-file": input_file,
            },
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

    async def loaddata_from_request_body(
        self,
        *,
        scan_quota: typing.Optional[int] = None,
        mode: typing.Optional[int] = None,
        users: typing.Optional[typing.Sequence[User]] = OMIT,
        folders: typing.Optional[typing.Sequence[BaseVirtualFolder]] = OMIT,
        groups: typing.Optional[typing.Sequence[Group]] = OMIT,
        admins: typing.Optional[typing.Sequence[Admin]] = OMIT,
        api_keys: typing.Optional[typing.Sequence[ApiKey]] = OMIT,
        shares: typing.Optional[typing.Sequence[Share]] = OMIT,
        event_actions: typing.Optional[typing.Sequence[EventAction]] = OMIT,
        event_rules: typing.Optional[typing.Sequence[EventRule]] = OMIT,
        roles: typing.Optional[typing.Sequence[Role]] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiResponse]:
        """
        Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

        Parameters
        ----------
        scan_quota : typing.Optional[int]
            Quota scan:
              * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default
              * `1` scan quota
              * `2` scan quota if the user has quota restrictions
            required: false

        mode : typing.Optional[int]
            Mode:
              * `0` New objects are added, existing ones are updated. This is the default
              * `1` New objects are added, existing ones are not modified
              * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration

        users : typing.Optional[typing.Sequence[User]]

        folders : typing.Optional[typing.Sequence[BaseVirtualFolder]]

        groups : typing.Optional[typing.Sequence[Group]]

        admins : typing.Optional[typing.Sequence[Admin]]

        api_keys : typing.Optional[typing.Sequence[ApiKey]]

        shares : typing.Optional[typing.Sequence[Share]]

        event_actions : typing.Optional[typing.Sequence[EventAction]]

        event_rules : typing.Optional[typing.Sequence[EventRule]]

        roles : typing.Optional[typing.Sequence[Role]]

        version : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiResponse]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "loaddata",
            method="POST",
            params={
                "scan-quota": scan_quota,
                "mode": mode,
            },
            json={
                "users": convert_and_respect_annotation_metadata(
                    object_=users, annotation=typing.Sequence[User], direction="write"
                ),
                "folders": convert_and_respect_annotation_metadata(
                    object_=folders, annotation=typing.Sequence[BaseVirtualFolder], direction="write"
                ),
                "groups": convert_and_respect_annotation_metadata(
                    object_=groups, annotation=typing.Sequence[Group], direction="write"
                ),
                "admins": convert_and_respect_annotation_metadata(
                    object_=admins, annotation=typing.Sequence[Admin], direction="write"
                ),
                "api_keys": convert_and_respect_annotation_metadata(
                    object_=api_keys, annotation=typing.Sequence[ApiKey], direction="write"
                ),
                "shares": convert_and_respect_annotation_metadata(
                    object_=shares, annotation=typing.Sequence[Share], direction="write"
                ),
                "event_actions": convert_and_respect_annotation_metadata(
                    object_=event_actions, annotation=typing.Sequence[EventAction], direction="write"
                ),
                "event_rules": convert_and_respect_annotation_metadata(
                    object_=event_rules, annotation=typing.Sequence[EventRule], direction="write"
                ),
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles, annotation=typing.Sequence[Role], direction="write"
                ),
                "version": version,
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
