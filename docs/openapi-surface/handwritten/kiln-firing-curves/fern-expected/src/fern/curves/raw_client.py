

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.curve import Curve
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCurvesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def record_curve(
        self,
        *,
        tolerance: float,
        glaze: float,
        readings: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Curve]:
        """
        Parameters
        ----------
        tolerance : float

        glaze : float

        readings : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Curve]
            The curve was recorded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "curves",
            method="POST",
            params={
                "tolerance": tolerance,
            },
            json={
                "glaze": glaze,
                "readings": readings,
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
                    Curve,
                    parse_obj_as(
                        type_=Curve,
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


class AsyncRawCurvesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def record_curve(
        self,
        *,
        tolerance: float,
        glaze: float,
        readings: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Curve]:
        """
        Parameters
        ----------
        tolerance : float

        glaze : float

        readings : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Curve]
            The curve was recorded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "curves",
            method="POST",
            params={
                "tolerance": tolerance,
            },
            json={
                "glaze": glaze,
                "readings": readings,
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
                    Curve,
                    parse_obj_as(
                        type_=Curve,
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
