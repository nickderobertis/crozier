

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawPresetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_mcu_key_short_click(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d

        %d: Range is from 1 to 12

        Parameters
        ----------
        n : int
            Preset number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"MCUKeyShortClick:{encode_path_param(n)}",
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

    def get_mcu_key_short_click_track(
        self, n: int, t: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d:%t

        %d: Range is from 1 to 12
        %t: Track number, start from 1, default is 1

        Parameters
        ----------
        n : int
            Preset number

        t : int
            Track number, start from 1, default is 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"MCUKeyShortClick:{encode_path_param(n)}:{encode_path_param(t)}",
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

    def get_preset_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=getPresetInfo


        JSON Response

        {
          "preset_num": 3,
          "preset_list": [
          {
            "number": 1,
            "name": "BBC Radio Norfolk",
            "url": "http:\\/\\/as-hls-wwlive.akamaized.net\\/pool_904\\/live\\/ww\\/bbc_radio_norfolk\\/bbc_radio_norfolk.isml\\/bbc_radio_norfolk-audio%3d96000.norewind.m3u8",
            "source": "Linkplay Radio",
            "picurl": "http:\\/\\/cdnprofiles.tunein.com\\/s6852\\/images\\/logoq.jpg?t=638353933090000000"
          },
          {
            "number": 6,
            "name": "Radio Paradise",
            "url": "http:\\/\\/stream.radioparadise.com\\/flacm",
            "source": "RadioParadise",
            "picurl": "https:\\/\\/cdnprofiles.tunein.com\\/s13606\\/images\\/logod.png?t=637541039930000000"
          },
          {
            "number": 8,
            "name": "1. Country Heat",
            "url": "unknow",
            "source": "Prime",
            "picurl": "https:\\/\\/m.media-amazon.com\\/images\\/I\\/51uR6AJUAQL.jpg"
          }
          ]
        }


        Description

        Field type Description

        preset_num int Total number of presets

        preset_list json array Preset list information

        number int Preset index (Start from 1)

        name string Playlist name

        url string Play url

        source string Music source

        picurl string Cover picture url

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
            "getPresetInfo",
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


class AsyncRawPresetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_mcu_key_short_click(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d

        %d: Range is from 1 to 12

        Parameters
        ----------
        n : int
            Preset number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"MCUKeyShortClick:{encode_path_param(n)}",
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

    async def get_mcu_key_short_click_track(
        self, n: int, t: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=MCUKeyShortClick:%d:%t

        %d: Range is from 1 to 12
        %t: Track number, start from 1, default is 1

        Parameters
        ----------
        n : int
            Preset number

        t : int
            Track number, start from 1, default is 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"MCUKeyShortClick:{encode_path_param(n)}:{encode_path_param(t)}",
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

    async def get_preset_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        http://10.10.10.254/httpapi.asp?command=getPresetInfo


        JSON Response

        {
          "preset_num": 3,
          "preset_list": [
          {
            "number": 1,
            "name": "BBC Radio Norfolk",
            "url": "http:\\/\\/as-hls-wwlive.akamaized.net\\/pool_904\\/live\\/ww\\/bbc_radio_norfolk\\/bbc_radio_norfolk.isml\\/bbc_radio_norfolk-audio%3d96000.norewind.m3u8",
            "source": "Linkplay Radio",
            "picurl": "http:\\/\\/cdnprofiles.tunein.com\\/s6852\\/images\\/logoq.jpg?t=638353933090000000"
          },
          {
            "number": 6,
            "name": "Radio Paradise",
            "url": "http:\\/\\/stream.radioparadise.com\\/flacm",
            "source": "RadioParadise",
            "picurl": "https:\\/\\/cdnprofiles.tunein.com\\/s13606\\/images\\/logod.png?t=637541039930000000"
          },
          {
            "number": 8,
            "name": "1. Country Heat",
            "url": "unknow",
            "source": "Prime",
            "picurl": "https:\\/\\/m.media-amazon.com\\/images\\/I\\/51uR6AJUAQL.jpg"
          }
          ]
        }


        Description

        Field type Description

        preset_num int Total number of presets

        preset_list json array Preset list information

        number int Preset index (Start from 1)

        name string Playlist name

        url string Play url

        source string Music source

        picurl string Cover picture url

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
            "getPresetInfo",
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
