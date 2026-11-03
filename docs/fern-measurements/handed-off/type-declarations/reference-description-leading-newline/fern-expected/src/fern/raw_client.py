

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.packet import Packet
from .types.packet_note_create_request import PacketNoteCreateRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def deposit_packet(
        self,
        *,
        variety: str,
        labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Packet]:
        """
        Parameters
        ----------
        variety : str

            The variety's common name.

        labels : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Key-value labels kept with the packet. Keys are short words.

            Values are free text of at most 64 characters.

        origin : typing.Optional[str]

                    Where the seed was saved.
                    (ex. a garden name)


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Packet]
            The packet
        """
        _response = self._client_wrapper.httpx_client.request(
            "packets",
            method="POST",
            json={
                "variety": variety,
                "labels": labels,
                "origin": origin,
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
                    Packet,
                    parse_obj_as(
                        type_=Packet,
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

    def add_packet_note(
        self,
        packet_id: str,
        *,
        request: PacketNoteCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        packet_id : str

        request : PacketNoteCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Added
        """
        _response = self._client_wrapper.httpx_client.request(
            f"packets/{encode_path_param(packet_id)}/notes",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PacketNoteCreateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def deposit_packet(
        self,
        *,
        variety: str,
        labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        origin: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Packet]:
        """
        Parameters
        ----------
        variety : str

            The variety's common name.

        labels : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Key-value labels kept with the packet. Keys are short words.

            Values are free text of at most 64 characters.

        origin : typing.Optional[str]

                    Where the seed was saved.
                    (ex. a garden name)


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Packet]
            The packet
        """
        _response = await self._client_wrapper.httpx_client.request(
            "packets",
            method="POST",
            json={
                "variety": variety,
                "labels": labels,
                "origin": origin,
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
                    Packet,
                    parse_obj_as(
                        type_=Packet,
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

    async def add_packet_note(
        self,
        packet_id: str,
        *,
        request: PacketNoteCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        packet_id : str

        request : PacketNoteCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Added
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"packets/{encode_path_param(packet_id)}/notes",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PacketNoteCreateRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
