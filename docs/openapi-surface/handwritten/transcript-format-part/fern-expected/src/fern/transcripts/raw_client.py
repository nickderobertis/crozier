

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..types.caption_format import CaptionFormat
from ..types.margins import Margins
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTranscriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_transcript(
        self,
        *,
        audio: typing.Optional[core.File] = OMIT,
        format: typing.Optional[CaptionFormat] = OMIT,
        margins: typing.Optional[Margins] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        audio : typing.Optional[core.File]
            See core.File for more documentation

        format : typing.Optional[CaptionFormat]

        margins : typing.Optional[Margins]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "transcripts",
            method="POST",
            data={
                "format": format,
                "margins": json.dumps(jsonable_encoder(margins)) if margins is not OMIT else OMIT,
            },
            files={
                **({"audio": audio} if audio is not None else {}),
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


class AsyncRawTranscriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_transcript(
        self,
        *,
        audio: typing.Optional[core.File] = OMIT,
        format: typing.Optional[CaptionFormat] = OMIT,
        margins: typing.Optional[Margins] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        audio : typing.Optional[core.File]
            See core.File for more documentation

        format : typing.Optional[CaptionFormat]

        margins : typing.Optional[Margins]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transcripts",
            method="POST",
            data={
                "format": format,
                "margins": json.dumps(jsonable_encoder(margins)) if margins is not OMIT else OMIT,
            },
            files={
                **({"audio": audio} if audio is not None else {}),
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
