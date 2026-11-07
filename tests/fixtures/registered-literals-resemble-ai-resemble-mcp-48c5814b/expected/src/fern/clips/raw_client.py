

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.delete_clip_response import DeleteClipResponse
from .types.get_clip_response import GetClipResponse
from .types.list_clips_response import ListClipsResponse
from .types.update_clip_response import UpdateClipResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_clips(
        self,
        project_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListClipsResponse]:
        """
        List clips in a project

        Parameters
        ----------
        project_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListClipsResponse]
            List of clips
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListClipsResponse,
                    parse_obj_as(
                        type_=ListClipsResponse,
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

    def get_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetClipResponse]:
        """
        Get clip details

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetClipResponse]
            Clip details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClipResponse,
                    parse_obj_as(
                        type_=GetClipResponse,
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

    def delete_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteClipResponse]:
        """
        Delete a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteClipResponse]
            Clip deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteClipResponse,
                    parse_obj_as(
                        type_=DeleteClipResponse,
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

    def update_clip(
        self,
        project_uuid: str,
        clip_uuid: str,
        *,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateClipResponse]:
        """
        Update a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        title : typing.Optional[str]

        body : typing.Optional[str]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateClipResponse]
            Clip updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "title": title,
                "body": body,
                "is_archived": is_archived,
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
                    UpdateClipResponse,
                    parse_obj_as(
                        type_=UpdateClipResponse,
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


class AsyncRawClipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_clips(
        self,
        project_uuid: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListClipsResponse]:
        """
        List clips in a project

        Parameters
        ----------
        project_uuid : str

        page : int

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListClipsResponse]
            List of clips
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListClipsResponse,
                    parse_obj_as(
                        type_=ListClipsResponse,
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

    async def get_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetClipResponse]:
        """
        Get clip details

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetClipResponse]
            Clip details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClipResponse,
                    parse_obj_as(
                        type_=GetClipResponse,
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

    async def delete_clip(
        self, project_uuid: str, clip_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteClipResponse]:
        """
        Delete a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteClipResponse]
            Clip deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteClipResponse,
                    parse_obj_as(
                        type_=DeleteClipResponse,
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

    async def update_clip(
        self,
        project_uuid: str,
        clip_uuid: str,
        *,
        title: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        is_archived: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateClipResponse]:
        """
        Update a clip

        Parameters
        ----------
        project_uuid : str

        clip_uuid : str

        title : typing.Optional[str]

        body : typing.Optional[str]

        is_archived : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateClipResponse]
            Clip updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"projects/{encode_path_param(project_uuid)}/clips/{encode_path_param(clip_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "title": title,
                "body": body,
                "is_archived": is_archived,
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
                    UpdateClipResponse,
                    parse_obj_as(
                        type_=UpdateClipResponse,
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
