

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.complex_ import Complex
from ..types.range import Range
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSweepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def complex_(
        self,
        sweep_id: str,
        *,
        frequency: float,
        complex_: typing.Optional[bool] = None,
        complex_request_complex: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Complex]:
        """
        Parameters
        ----------
        sweep_id : str

        frequency : float
            Sweep frequency in hertz.

        complex_ : typing.Optional[bool]
            Report the point in rectangular rather than polar form.

        complex_request_complex : typing.Optional[bool]
            Return the conjugate as well.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Complex]
            The resolved point.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sweeps/{encode_path_param(sweep_id)}/impedance",
            method="POST",
            params={
                "complex": complex_,
            },
            json={
                "frequency": frequency,
                "complex": complex_request_complex,
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
                    Complex,
                    parse_obj_as(
                        type_=Complex,
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

    def calibrate(
        self,
        *,
        complex_: typing.Optional[bool] = None,
        calibration_complex: typing.Optional[float] = OMIT,
        gain: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        complex_ : typing.Optional[bool]
            Apply the correction to the complex plane only.

        calibration_complex : typing.Optional[float]
            Phase correction, in degrees.

        gain : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "calibrations",
            method="PUT",
            params={
                "complex": complex_,
            },
            json={
                "complex": calibration_complex,
                "gain": gain,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def get_range(
        self, sweep_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Range]:
        """
        Parameters
        ----------
        sweep_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Range]
            The frequency span the sweep covered.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sweeps/{encode_path_param(sweep_id)}/range",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Range,
                    parse_obj_as(
                        type_=Range,
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


class AsyncRawSweepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def complex_(
        self,
        sweep_id: str,
        *,
        frequency: float,
        complex_: typing.Optional[bool] = None,
        complex_request_complex: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Complex]:
        """
        Parameters
        ----------
        sweep_id : str

        frequency : float
            Sweep frequency in hertz.

        complex_ : typing.Optional[bool]
            Report the point in rectangular rather than polar form.

        complex_request_complex : typing.Optional[bool]
            Return the conjugate as well.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Complex]
            The resolved point.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sweeps/{encode_path_param(sweep_id)}/impedance",
            method="POST",
            params={
                "complex": complex_,
            },
            json={
                "frequency": frequency,
                "complex": complex_request_complex,
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
                    Complex,
                    parse_obj_as(
                        type_=Complex,
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

    async def calibrate(
        self,
        *,
        complex_: typing.Optional[bool] = None,
        calibration_complex: typing.Optional[float] = OMIT,
        gain: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        complex_ : typing.Optional[bool]
            Apply the correction to the complex plane only.

        calibration_complex : typing.Optional[float]
            Phase correction, in degrees.

        gain : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "calibrations",
            method="PUT",
            params={
                "complex": complex_,
            },
            json={
                "complex": calibration_complex,
                "gain": gain,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def get_range(
        self, sweep_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Range]:
        """
        Parameters
        ----------
        sweep_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Range]
            The frequency span the sweep covered.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sweeps/{encode_path_param(sweep_id)}/range",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Range,
                    parse_obj_as(
                        type_=Range,
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
