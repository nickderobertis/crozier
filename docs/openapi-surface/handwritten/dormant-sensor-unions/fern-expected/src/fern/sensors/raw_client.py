

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.channels import Channels
from ..types.gap import Gap
from ..types.lull import Lull
from ..types.pitch import Pitch
from ..types.reading import Reading
from ..types.reading_alarm import ReadingAlarm
from ..types.reading_mode import ReadingMode
from ..types.silence import Silence
from ..types.stillness import Stillness
from ..types.tone import Tone
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSensorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_silence(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Silence]]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[Silence]]
            The sensor's silence marker.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/silence",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Silence],
                    parse_obj_as(
                        type_=typing.Optional[Silence],
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

    def get_gap(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Gap]]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[Gap]]
            The sensor's gap marker.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/gap",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Gap],
                    parse_obj_as(
                        type_=typing.Optional[Gap],
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

    def put_reading(
        self,
        sensor_id: str,
        *,
        label: str,
        silence: typing.Optional[Silence] = OMIT,
        lull: typing.Optional[Lull] = OMIT,
        hush: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        stillness: typing.Optional[Stillness] = OMIT,
        void: typing.Optional[typing.Any] = OMIT,
        pitch: typing.Optional[Pitch] = OMIT,
        tone: typing.Optional[Tone] = OMIT,
        mode: typing.Optional[ReadingMode] = OMIT,
        alarm: typing.Optional[ReadingAlarm] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reading]:
        """
        Parameters
        ----------
        sensor_id : str

        label : str

        silence : typing.Optional[Silence]

        lull : typing.Optional[Lull]

        hush : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        stillness : typing.Optional[Stillness]

        void : typing.Optional[typing.Any]

        pitch : typing.Optional[Pitch]

        tone : typing.Optional[Tone]

        mode : typing.Optional[ReadingMode]
            Whether the sensor is sampling.

        alarm : typing.Optional[ReadingAlarm]
            How the sensor alerts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reading]
            The stored reading.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/reading",
            method="PUT",
            json={
                "label": label,
                "silence": silence,
                "lull": lull,
                "hush": hush,
                "stillness": stillness,
                "void": void,
                "pitch": pitch,
                "tone": tone,
                "mode": mode,
                "alarm": alarm,
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
                    Reading,
                    parse_obj_as(
                        type_=Reading,
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

    def put_channel(
        self, sensor_id: str, *, request: Channels, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Channels]:
        """
        Parameters
        ----------
        sensor_id : str

        request : Channels

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Channels]
            The channel the sensor now listens on.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/channel",
            method="PUT",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Channels, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Channels,
                    parse_obj_as(
                        type_=Channels,
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


class AsyncRawSensorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_silence(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Silence]]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[Silence]]
            The sensor's silence marker.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/silence",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Silence],
                    parse_obj_as(
                        type_=typing.Optional[Silence],
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

    async def get_gap(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Gap]]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[Gap]]
            The sensor's gap marker.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/gap",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Gap],
                    parse_obj_as(
                        type_=typing.Optional[Gap],
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

    async def put_reading(
        self,
        sensor_id: str,
        *,
        label: str,
        silence: typing.Optional[Silence] = OMIT,
        lull: typing.Optional[Lull] = OMIT,
        hush: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        stillness: typing.Optional[Stillness] = OMIT,
        void: typing.Optional[typing.Any] = OMIT,
        pitch: typing.Optional[Pitch] = OMIT,
        tone: typing.Optional[Tone] = OMIT,
        mode: typing.Optional[ReadingMode] = OMIT,
        alarm: typing.Optional[ReadingAlarm] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reading]:
        """
        Parameters
        ----------
        sensor_id : str

        label : str

        silence : typing.Optional[Silence]

        lull : typing.Optional[Lull]

        hush : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        stillness : typing.Optional[Stillness]

        void : typing.Optional[typing.Any]

        pitch : typing.Optional[Pitch]

        tone : typing.Optional[Tone]

        mode : typing.Optional[ReadingMode]
            Whether the sensor is sampling.

        alarm : typing.Optional[ReadingAlarm]
            How the sensor alerts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reading]
            The stored reading.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/reading",
            method="PUT",
            json={
                "label": label,
                "silence": silence,
                "lull": lull,
                "hush": hush,
                "stillness": stillness,
                "void": void,
                "pitch": pitch,
                "tone": tone,
                "mode": mode,
                "alarm": alarm,
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
                    Reading,
                    parse_obj_as(
                        type_=Reading,
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

    async def put_channel(
        self, sensor_id: str, *, request: Channels, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Channels]:
        """
        Parameters
        ----------
        sensor_id : str

        request : Channels

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Channels]
            The channel the sensor now listens on.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sensors/{encode_path_param(sensor_id)}/channel",
            method="PUT",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Channels, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Channels,
                    parse_obj_as(
                        type_=Channels,
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
