

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.window_plan import WindowPlan
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def plan_windows(
        self,
        *,
        windows: typing.Sequence[typing.Sequence[typing.Optional[dt.datetime]]],
        soundings: typing.Optional[typing.Sequence[typing.Sequence[typing.Optional[float]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WindowPlan]:
        """
        Parameters
        ----------
        windows : typing.Sequence[typing.Sequence[typing.Optional[dt.datetime]]]

        soundings : typing.Optional[typing.Sequence[typing.Sequence[typing.Optional[float]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WindowPlan]
            The plan as stored.
        """
        _response = self._client_wrapper.httpx_client.request(
            "windows",
            method="POST",
            json={
                "windows": windows,
                "soundings": soundings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WindowPlan,
                    parse_obj_as(
                        type_=WindowPlan,
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

    async def plan_windows(
        self,
        *,
        windows: typing.Sequence[typing.Sequence[typing.Optional[dt.datetime]]],
        soundings: typing.Optional[typing.Sequence[typing.Sequence[typing.Optional[float]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WindowPlan]:
        """
        Parameters
        ----------
        windows : typing.Sequence[typing.Sequence[typing.Optional[dt.datetime]]]

        soundings : typing.Optional[typing.Sequence[typing.Sequence[typing.Optional[float]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WindowPlan]
            The plan as stored.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "windows",
            method="POST",
            json={
                "windows": windows,
                "soundings": soundings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WindowPlan,
                    parse_obj_as(
                        type_=WindowPlan,
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
