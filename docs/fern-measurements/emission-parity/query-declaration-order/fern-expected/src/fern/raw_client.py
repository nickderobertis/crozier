

import typing
from json.decoder import JSONDecodeError

from . import core
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.logbook_entry import LogbookEntry
from .types.reading import Reading
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_readings(
        self,
        lamp_id: str,
        *,
        unit: str,
        shift: str,
        since: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Reading]]:
        """
        Parameters
        ----------
        lamp_id : str

        unit : str
            Unit the readings are reported in.

        shift : str

        since : typing.Optional[str]
            Earliest reading to include.

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Reading]]
            The readings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/readings",
            method="GET",
            params={
                "since": since,
                "unit": unit,
                "page": page,
                "limit": limit,
                "shift": shift,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Reading],
                    parse_obj_as(
                        type_=typing.List[Reading],
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

    def write_logbook(
        self,
        lamp_id: str,
        *,
        tide: str,
        keeper_id: str,
        text: str,
        draft: typing.Optional[bool] = None,
        watch_note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LogbookEntry]:
        """
        Parameters
        ----------
        lamp_id : str

        tide : str

        keeper_id : str

        text : str

        draft : typing.Optional[bool]

        watch_note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogbookEntry]
            Written
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/logbook",
            method="POST",
            params={
                "draft": draft,
                "tide": tide,
            },
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
                "X-Watch-Note": str(watch_note) if watch_note is not None else None,
                "X-Keeper-Id": str(keeper_id) if keeper_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogbookEntry,
                    parse_obj_as(
                        type_=LogbookEntry,
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

    def upload_photo(
        self,
        lamp_id: str,
        *,
        album: str,
        photo: core.File,
        caption: typing.Optional[str] = None,
        camera: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        lamp_id : str

        album : str

        photo : core.File
            See core.File for more documentation

        caption : typing.Optional[str]

        camera : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/photos",
            method="POST",
            params={
                "caption": caption,
                "album": album,
            },
            data={},
            files={
                "photo": photo,
            },
            headers={
                "X-Camera": str(camera) if camera is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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

    def list_lamps(
        self, *, region: str, lit: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        region : str

        lit : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            The lamps
        """
        _response = self._client_wrapper.httpx_client.request(
            "lamps",
            method="GET",
            params={
                "region": region,
                "lit": lit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_readings(
        self,
        lamp_id: str,
        *,
        unit: str,
        shift: str,
        since: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Reading]]:
        """
        Parameters
        ----------
        lamp_id : str

        unit : str
            Unit the readings are reported in.

        shift : str

        since : typing.Optional[str]
            Earliest reading to include.

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Reading]]
            The readings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/readings",
            method="GET",
            params={
                "since": since,
                "unit": unit,
                "page": page,
                "limit": limit,
                "shift": shift,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Reading],
                    parse_obj_as(
                        type_=typing.List[Reading],
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

    async def write_logbook(
        self,
        lamp_id: str,
        *,
        tide: str,
        keeper_id: str,
        text: str,
        draft: typing.Optional[bool] = None,
        watch_note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LogbookEntry]:
        """
        Parameters
        ----------
        lamp_id : str

        tide : str

        keeper_id : str

        text : str

        draft : typing.Optional[bool]

        watch_note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogbookEntry]
            Written
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/logbook",
            method="POST",
            params={
                "draft": draft,
                "tide": tide,
            },
            json={
                "text": text,
            },
            headers={
                "content-type": "application/json",
                "X-Watch-Note": str(watch_note) if watch_note is not None else None,
                "X-Keeper-Id": str(keeper_id) if keeper_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogbookEntry,
                    parse_obj_as(
                        type_=LogbookEntry,
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

    async def upload_photo(
        self,
        lamp_id: str,
        *,
        album: str,
        photo: core.File,
        caption: typing.Optional[str] = None,
        camera: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        lamp_id : str

        album : str

        photo : core.File
            See core.File for more documentation

        caption : typing.Optional[str]

        camera : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lamps/{encode_path_param(lamp_id)}/photos",
            method="POST",
            params={
                "caption": caption,
                "album": album,
            },
            data={},
            files={
                "photo": photo,
            },
            headers={
                "X-Camera": str(camera) if camera is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
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

    async def list_lamps(
        self, *, region: str, lit: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        region : str

        lit : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            The lamps
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lamps",
            method="GET",
            params={
                "region": region,
                "lit": lit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
