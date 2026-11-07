

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.backup_file import BackupFile
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMigrationV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_backup_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[BackupFile]]:
        """
        Get backup files from backup root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BackupFile]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/console.api.migration.halo.run/v1alpha1/backup-files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BackupFile],
                    parse_obj_as(
                        type_=typing.List[BackupFile],
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

    def download_backups(
        self, name: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Download a file from the specified backup as an octet-stream attachment.

        Parameters
        ----------
        name : str
            Backup metadata.name.

        filename : str
            Backup filename.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/console.api.migration.halo.run/v1alpha1/backups/{encode_path_param(name)}/files/{encode_path_param(filename)}",
            method="GET",
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

    def restore_backup(
        self,
        *,
        backup_name: typing.Optional[str] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Restore backup by uploading file or providing download link or backup name.

        Parameters
        ----------
        backup_name : typing.Optional[str]
            Backup <code>metadata.name</code>.

        download_url : typing.Optional[str]
            Remote backup HTTP URL.

        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            Filename of backup file in backups root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Backup restored successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/console.api.migration.halo.run/v1alpha1/restorations",
            method="POST",
            data={
                "backupName": backup_name,
                "downloadUrl": download_url,
                "filename": filename,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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


class AsyncRawMigrationV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_backup_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[BackupFile]]:
        """
        Get backup files from backup root.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BackupFile]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/console.api.migration.halo.run/v1alpha1/backup-files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BackupFile],
                    parse_obj_as(
                        type_=typing.List[BackupFile],
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

    async def download_backups(
        self, name: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Download a file from the specified backup as an octet-stream attachment.

        Parameters
        ----------
        name : str
            Backup metadata.name.

        filename : str
            Backup filename.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/console.api.migration.halo.run/v1alpha1/backups/{encode_path_param(name)}/files/{encode_path_param(filename)}",
            method="GET",
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

    async def restore_backup(
        self,
        *,
        backup_name: typing.Optional[str] = OMIT,
        download_url: typing.Optional[str] = OMIT,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Restore backup by uploading file or providing download link or backup name.

        Parameters
        ----------
        backup_name : typing.Optional[str]
            Backup <code>metadata.name</code>.

        download_url : typing.Optional[str]
            Remote backup HTTP URL.

        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            Filename of backup file in backups root.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Backup restored successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/console.api.migration.halo.run/v1alpha1/restorations",
            method="POST",
            data={
                "backupName": backup_name,
                "downloadUrl": download_url,
                "filename": filename,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
