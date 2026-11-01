

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawTrackMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_meta_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        JSON Response
        {
         "metaData": {
          "album": "Country Heat",
          "title": "Old Dirt Roads",
          "subtitle": "",
          "artist": "Owen Riegling",
          "albumArtURI ": "https://m.media-amazon.com/images/I/51iU0odzJwL.jpg",
          "sampleRate ": "44100",
          "bitDepth": "16",
          "bitRate": "63",
          "trackId": "s6707",
         }
        }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "getMetaInfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTrackMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_meta_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        JSON Response
        {
         "metaData": {
          "album": "Country Heat",
          "title": "Old Dirt Roads",
          "subtitle": "",
          "artist": "Owen Riegling",
          "albumArtURI ": "https://m.media-amazon.com/images/I/51iU0odzJwL.jpg",
          "sampleRate ": "44100",
          "bitDepth": "16",
          "bitRate": "63",
          "trackId": "s6707",
         }
        }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getMetaInfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
