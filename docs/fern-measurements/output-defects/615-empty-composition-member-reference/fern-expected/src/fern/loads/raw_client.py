

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
from ..types.kiln import Kiln
from ..types.load import Load
from ..types.load_noted_kiln import LoadNotedKiln
from ..types.load_reserved_kiln import LoadReservedKiln
from .types.transfer_load_request_fallback import TransferLoadRequestFallback
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLoadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def schedule_load(
        self,
        *,
        label: str,
        kiln: Kiln,
        overflow_kiln: typing.Optional[Kiln] = OMIT,
        usual_kiln: typing.Optional[Kiln] = OMIT,
        solo_kiln: typing.Optional[Kiln] = OMIT,
        noted_kiln: typing.Optional[LoadNotedKiln] = OMIT,
        reserved_kiln: typing.Optional[LoadReservedKiln] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Load]:
        """
        Parameters
        ----------
        label : str

        kiln : Kiln

        overflow_kiln : typing.Optional[Kiln]

        usual_kiln : typing.Optional[Kiln]

        solo_kiln : typing.Optional[Kiln]

        noted_kiln : typing.Optional[LoadNotedKiln]
            Kiln named in the firing log.

        reserved_kiln : typing.Optional[LoadReservedKiln]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Load]
            The scheduled load.
        """
        _response = self._client_wrapper.httpx_client.request(
            "loads",
            method="POST",
            json={
                "label": label,
                "kiln": convert_and_respect_annotation_metadata(object_=kiln, annotation=Kiln, direction="write"),
                "overflowKiln": convert_and_respect_annotation_metadata(
                    object_=overflow_kiln, annotation=Kiln, direction="write"
                ),
                "usualKiln": convert_and_respect_annotation_metadata(
                    object_=usual_kiln, annotation=Kiln, direction="write"
                ),
                "soloKiln": convert_and_respect_annotation_metadata(
                    object_=solo_kiln, annotation=Kiln, direction="write"
                ),
                "notedKiln": convert_and_respect_annotation_metadata(
                    object_=noted_kiln, annotation=LoadNotedKiln, direction="write"
                ),
                "reservedKiln": convert_and_respect_annotation_metadata(
                    object_=reserved_kiln, annotation=LoadReservedKiln, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Load,
                    parse_obj_as(
                        type_=Load,
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

    def transfer_load(
        self,
        load_id: str,
        *,
        destination: Kiln,
        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Load]:
        """
        Parameters
        ----------
        load_id : str

        destination : Kiln

        fallback : typing.Optional[TransferLoadRequestFallback]
            Kiln to use when the destination is full.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Load]
            The moved load.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"loads/{encode_path_param(load_id)}/transfer",
            method="POST",
            json={
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=Kiln, direction="write"
                ),
                "fallback": convert_and_respect_annotation_metadata(
                    object_=fallback, annotation=TransferLoadRequestFallback, direction="write"
                ),
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
                    Load,
                    parse_obj_as(
                        type_=Load,
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


class AsyncRawLoadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def schedule_load(
        self,
        *,
        label: str,
        kiln: Kiln,
        overflow_kiln: typing.Optional[Kiln] = OMIT,
        usual_kiln: typing.Optional[Kiln] = OMIT,
        solo_kiln: typing.Optional[Kiln] = OMIT,
        noted_kiln: typing.Optional[LoadNotedKiln] = OMIT,
        reserved_kiln: typing.Optional[LoadReservedKiln] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Load]:
        """
        Parameters
        ----------
        label : str

        kiln : Kiln

        overflow_kiln : typing.Optional[Kiln]

        usual_kiln : typing.Optional[Kiln]

        solo_kiln : typing.Optional[Kiln]

        noted_kiln : typing.Optional[LoadNotedKiln]
            Kiln named in the firing log.

        reserved_kiln : typing.Optional[LoadReservedKiln]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Load]
            The scheduled load.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "loads",
            method="POST",
            json={
                "label": label,
                "kiln": convert_and_respect_annotation_metadata(object_=kiln, annotation=Kiln, direction="write"),
                "overflowKiln": convert_and_respect_annotation_metadata(
                    object_=overflow_kiln, annotation=Kiln, direction="write"
                ),
                "usualKiln": convert_and_respect_annotation_metadata(
                    object_=usual_kiln, annotation=Kiln, direction="write"
                ),
                "soloKiln": convert_and_respect_annotation_metadata(
                    object_=solo_kiln, annotation=Kiln, direction="write"
                ),
                "notedKiln": convert_and_respect_annotation_metadata(
                    object_=noted_kiln, annotation=LoadNotedKiln, direction="write"
                ),
                "reservedKiln": convert_and_respect_annotation_metadata(
                    object_=reserved_kiln, annotation=LoadReservedKiln, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Load,
                    parse_obj_as(
                        type_=Load,
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

    async def transfer_load(
        self,
        load_id: str,
        *,
        destination: Kiln,
        fallback: typing.Optional[TransferLoadRequestFallback] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Load]:
        """
        Parameters
        ----------
        load_id : str

        destination : Kiln

        fallback : typing.Optional[TransferLoadRequestFallback]
            Kiln to use when the destination is full.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Load]
            The moved load.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"loads/{encode_path_param(load_id)}/transfer",
            method="POST",
            json={
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=Kiln, direction="write"
                ),
                "fallback": convert_and_respect_annotation_metadata(
                    object_=fallback, annotation=TransferLoadRequestFallback, direction="write"
                ),
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
                    Load,
                    parse_obj_as(
                        type_=Load,
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
