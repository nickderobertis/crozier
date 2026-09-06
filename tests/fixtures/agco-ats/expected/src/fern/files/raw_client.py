

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_global_resources_shared_models_file_download import (
    ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
)
from ..types.global_resources_shared_models_file_download import GlobalResourcesSharedModelsFileDownload
from ..types.global_resources_shared_models_file_download_state import GlobalResourcesSharedModelsFileDownloadState
from ..types.system_object import SystemObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getfiles(
        self,
        *,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsFileDownload]:
        """
        No Documentation Found.

        Parameters
        ----------
        include_deleted : typing.Optional[bool]
            Indicates whether to include files marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsFileDownload]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Files",
            method="GET",
            params={
                "includeDeleted": include_deleted,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
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

    def postfile(
        self,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Files",
            method="POST",
            json={
                "CRC": crc,
                "ContentType": content_type,
                "Description": description,
                "Id": id,
                "IsPublic": is_public,
                "Name": name,
                "Path": path,
                "Size": size,
                "State": state,
            },
            request_options=request_options,
            omit=OMIT,
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

    def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalResourcesSharedModelsFileDownload]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalResourcesSharedModelsFileDownload]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsFileDownload,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsFileDownload,
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

    def putfile(
        self,
        id_: str,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update the metadata for a file. Size may not be modified by the client.
                        Set status to 'Available' to publish a file. The file must be uploaded.
                        Set status to 'Created' to reset a file's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The file's id

        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id_)}",
            method="PUT",
            json={
                "CRC": crc,
                "ContentType": content_type,
                "Description": description,
                "Id": id,
                "IsPublic": is_public,
                "Name": name,
                "Path": path,
                "Size": size,
                "State": state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def deletefile(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}",
            method="DELETE",
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

    def getfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}/FileContents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    def putfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}/FileContents",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getfiles(
        self,
        *,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsFileDownload]:
        """
        No Documentation Found.

        Parameters
        ----------
        include_deleted : typing.Optional[bool]
            Indicates whether to include files marked as removed.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseGlobalResourcesSharedModelsFileDownload]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Files",
            method="GET",
            params={
                "includeDeleted": include_deleted,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
                    parse_obj_as(
                        type_=ApiIPagedResponseGlobalResourcesSharedModelsFileDownload,
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

    async def postfile(
        self,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Files",
            method="POST",
            json={
                "CRC": crc,
                "ContentType": content_type,
                "Description": description,
                "Id": id,
                "IsPublic": is_public,
                "Name": name,
                "Path": path,
                "Size": size,
                "State": state,
            },
            request_options=request_options,
            omit=OMIT,
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

    async def getfile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalResourcesSharedModelsFileDownload]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalResourcesSharedModelsFileDownload]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalResourcesSharedModelsFileDownload,
                    parse_obj_as(
                        type_=GlobalResourcesSharedModelsFileDownload,
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

    async def putfile(
        self,
        id_: str,
        *,
        crc: str,
        content_type: str,
        description: str,
        is_public: bool,
        name: str,
        path: str,
        state: GlobalResourcesSharedModelsFileDownloadState,
        id: typing.Optional[str] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update the metadata for a file. Size may not be modified by the client.
                        Set status to 'Available' to publish a file. The file must be uploaded.
                        Set status to 'Created' to reset a file's contents and re-upload.
                        A file may only be 'Removed' by the DELETE method.

        Parameters
        ----------
        id_ : str
            The file's id

        crc : str
            The crc of the file (SHA256, HEX-encoded). Must be provided when creating a file.

        content_type : str
            The type of file; sent as the content-type header.

        description : str
            The description of the file.

        is_public : bool
            Indicates whether this file is available to the public for download.

        name : str
            The name of the file when downloaded.

        path : str
            The Path of the file.

        state : GlobalResourcesSharedModelsFileDownloadState
            Indicates the state of this file. Must be 'Created' when created.

        id : typing.Optional[str]
            The Id of the file.

        size : typing.Optional[int]
            The size of the file in bytes. Null until assigned by server when marked as 'Available'. Read Only

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id_)}",
            method="PUT",
            json={
                "CRC": crc,
                "ContentType": content_type,
                "Description": description,
                "Id": id,
                "IsPublic": is_public,
                "Name": name,
                "Path": path,
                "Size": size,
                "State": state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def deletefile(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}",
            method="DELETE",
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

    async def getfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}/FileContents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    async def putfilecontents(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The file's metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Files/{encode_path_param(id)}/FileContents",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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
