

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawAudioOutputControlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_new_audio_output_hardware_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        JSON Response:
        {"hardware":"2","source":"0","audiocast":"0"}

        Description:
        Field Description
        hardware Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        source BT source output mode:
        0: disable
        1: active
        audiocast Audio cast output mode:
        0: disable
        1: active

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
            "getNewAudioOutputHardwareMode",
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

    def set_audio_output_hardware_mode(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Field Description
        Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        Response is 'OK'

        Parameters
        ----------
        n : int
            Hardware Interface output mode:
            1: AUDIO_OUTPUT_SPDIF_MODE
            2: AUDIO_OUTPUT_AUX_MODE
            3: AUDIO_OUTPUT_COAX_MODE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"setAudioOutputHardwareMode:{encode_path_param(n)}",
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

    def get_spdif_out_switch_delay_ms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getSpdifOutSwitchDelayMs

        Observations:
        - This value only makes sense if the output interface is SPDIF (optical out).
        - Value can be retrieved even if output is not SPDIF

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
            "getSpdifOutSwitchDelayMs",
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

    def set_spdif_out_switch_delay_ms(
        self, delay: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setSpdifOutSwitchDelayMs:800

        Observations:
        - Delay is in milliseconds
        - Value can be set even if output is not SPDIF
        - Delay is upper bound to 3000 milliseconds

        Parameters
        ----------
        delay : int
            The delay in milliseconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"setSpdifOutSwitchDelayMs:{encode_path_param(delay)}",
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

    def get_channel_balance(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getChannelBalance

        Observations:
        - The value will be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

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
            "getChannelBalance",
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

    def set_channel_balance(
        self, n: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setChannelBalance:0

        Observations:
        - The value must be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

        Parameters
        ----------
        n : float
            Balance from -1.0 (left) to 1.0 (right)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"setChannelBalance:{encode_path_param(n)}",
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

    def get_fade_feature(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetFadeFeature

        Returns {"FadeFeature": 1}

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
            "GetFadeFeature",
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

    def set_fade_feature(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=SetFadeFeature:0

        Parameters
        ----------
        n : int
            Fade feature value (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"SetFadeFeature:{encode_path_param(n)}",
            method="GET",
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


class AsyncRawAudioOutputControlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_new_audio_output_hardware_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        JSON Response:
        {"hardware":"2","source":"0","audiocast":"0"}

        Description:
        Field Description
        hardware Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        source BT source output mode:
        0: disable
        1: active
        audiocast Audio cast output mode:
        0: disable
        1: active

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
            "getNewAudioOutputHardwareMode",
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

    async def set_audio_output_hardware_mode(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Field Description
        Hardware Interface output mode:
        1: AUDIO_OUTPUT_SPDIF_MODE
        2: AUDIO_OUTPUT_AUX_MODE
        3: AUDIO_OUTPUT_COAX_MODE
        Response is 'OK'

        Parameters
        ----------
        n : int
            Hardware Interface output mode:
            1: AUDIO_OUTPUT_SPDIF_MODE
            2: AUDIO_OUTPUT_AUX_MODE
            3: AUDIO_OUTPUT_COAX_MODE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"setAudioOutputHardwareMode:{encode_path_param(n)}",
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

    async def get_spdif_out_switch_delay_ms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getSpdifOutSwitchDelayMs

        Observations:
        - This value only makes sense if the output interface is SPDIF (optical out).
        - Value can be retrieved even if output is not SPDIF

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
            "getSpdifOutSwitchDelayMs",
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

    async def set_spdif_out_switch_delay_ms(
        self, delay: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setSpdifOutSwitchDelayMs:800

        Observations:
        - Delay is in milliseconds
        - Value can be set even if output is not SPDIF
        - Delay is upper bound to 3000 milliseconds

        Parameters
        ----------
        delay : int
            The delay in milliseconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"setSpdifOutSwitchDelayMs:{encode_path_param(delay)}",
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

    async def get_channel_balance(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=getChannelBalance

        Observations:
        - The value will be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

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
            "getChannelBalance",
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

    async def set_channel_balance(
        self, n: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setChannelBalance:0

        Observations:
        - The value must be a number ranging from -1.0 (fully panned left) to 1.0 (fully panned right).

        Parameters
        ----------
        n : float
            Balance from -1.0 (left) to 1.0 (right)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"setChannelBalance:{encode_path_param(n)}",
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

    async def get_fade_feature(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=GetFadeFeature

        Returns {"FadeFeature": 1}

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
            "GetFadeFeature",
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

    async def set_fade_feature(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=SetFadeFeature:0

        Parameters
        ----------
        n : int
            Fade feature value (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"SetFadeFeature:{encode_path_param(n)}",
            method="GET",
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
