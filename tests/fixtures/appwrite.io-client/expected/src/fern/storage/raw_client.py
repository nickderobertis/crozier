

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.file import File
from ..types.file_list import FileList


OMIT = typing.cast(typing.Any, ...)


class RawStorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_files(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FileList]:
        """
        Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's files. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileList]
            Files List
        """
        _response = self._client_wrapper.httpx_client.request(
            "storage/files",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileList,
                    parse_obj_as(
                        type_=FileList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_file(
        self,
        *,
        file: str,
        read: typing.Optional[typing.List[str]] = OMIT,
        write: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[File]:
        """
        Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

        Parameters
        ----------
        file : str
            Binary file.

        read : typing.Optional[typing.List[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.List[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            File
        """
        _response = self._client_wrapper.httpx_client.request(
            "storage/files",
            method="POST",
            data={
                "file": file,
                "read": read,
                "write": write,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[File]:
        """
        Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            File
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_file(
        self,
        file_id: str,
        *,
        read: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[File]:
        """
        Update a file by its unique ID. Only users with write permissions have access to update this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            File
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
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
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_file_download(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_file_preview(
        self,
        file_id: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[float] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

        Parameters
        ----------
        file_id : str
            File unique ID

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 4000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 4000.

        gravity : typing.Optional[str]
            Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

        quality : typing.Optional[int]
            Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

        border_width : typing.Optional[int]
            Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

        border_color : typing.Optional[str]
            Preview image border color. Use a valid HEX color, no # is needed for prefix.

        border_radius : typing.Optional[int]
            Preview image border radius in pixels. Pass an integer between 0 to 4000.

        opacity : typing.Optional[float]
            Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

        rotation : typing.Optional[int]
            Preview image rotation in degrees. Pass an integer between 0 and 360.

        background : typing.Optional[str]
            Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

        output : typing.Optional[str]
            Output format type (jpeg, jpg, png, gif and webp).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/preview",
            method="GET",
            params={
                "width": width,
                "height": height,
                "gravity": gravity,
                "quality": quality,
                "borderWidth": border_width,
                "borderColor": border_color,
                "borderRadius": border_radius,
                "opacity": opacity,
                "rotation": rotation,
                "background": background,
                "output": output,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_file_view(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/view",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_files(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FileList]:
        """
        Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's files. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileList]
            Files List
        """
        _response = await self._client_wrapper.httpx_client.request(
            "storage/files",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileList,
                    parse_obj_as(
                        type_=FileList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_file(
        self,
        *,
        file: str,
        read: typing.Optional[typing.List[str]] = OMIT,
        write: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[File]:
        """
        Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

        Parameters
        ----------
        file : str
            Binary file.

        read : typing.Optional[typing.List[str]]
            An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Optional[typing.List[str]]
            An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            File
        """
        _response = await self._client_wrapper.httpx_client.request(
            "storage/files",
            method="POST",
            data={
                "file": file,
                "read": read,
                "write": write,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[File]:
        """
        Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            File
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_file(
        self,
        file_id: str,
        *,
        read: typing.Sequence[str],
        write: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[File]:
        """
        Update a file by its unique ID. Only users with write permissions have access to update this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        read : typing.Sequence[str]
            An array of strings with read permissions. By default no user is granted with any read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        write : typing.Sequence[str]
            An array of strings with write permissions. By default no user is granted with any write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            File
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
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
                    File,
                    parse_obj_as(
                        type_=File,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_file_download(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_file_preview(
        self,
        file_id: str,
        *,
        width: typing.Optional[int] = None,
        height: typing.Optional[int] = None,
        gravity: typing.Optional[str] = None,
        quality: typing.Optional[int] = None,
        border_width: typing.Optional[int] = None,
        border_color: typing.Optional[str] = None,
        border_radius: typing.Optional[int] = None,
        opacity: typing.Optional[float] = None,
        rotation: typing.Optional[int] = None,
        background: typing.Optional[str] = None,
        output: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

        Parameters
        ----------
        file_id : str
            File unique ID

        width : typing.Optional[int]
            Resize preview image width, Pass an integer between 0 to 4000.

        height : typing.Optional[int]
            Resize preview image height, Pass an integer between 0 to 4000.

        gravity : typing.Optional[str]
            Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right

        quality : typing.Optional[int]
            Preview image quality. Pass an integer between 0 to 100. Defaults to 100.

        border_width : typing.Optional[int]
            Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.

        border_color : typing.Optional[str]
            Preview image border color. Use a valid HEX color, no # is needed for prefix.

        border_radius : typing.Optional[int]
            Preview image border radius in pixels. Pass an integer between 0 to 4000.

        opacity : typing.Optional[float]
            Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.

        rotation : typing.Optional[int]
            Preview image rotation in degrees. Pass an integer between 0 and 360.

        background : typing.Optional[str]
            Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.

        output : typing.Optional[str]
            Output format type (jpeg, jpg, png, gif and webp).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/preview",
            method="GET",
            params={
                "width": width,
                "height": height,
                "gravity": gravity,
                "quality": quality,
                "borderWidth": border_width,
                "borderColor": border_color,
                "borderRadius": border_radius,
                "opacity": opacity,
                "rotation": rotation,
                "background": background,
                "output": output,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_file_view(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

        Parameters
        ----------
        file_id : str
            File unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"storage/files/{jsonable_encoder(file_id)}/view",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
