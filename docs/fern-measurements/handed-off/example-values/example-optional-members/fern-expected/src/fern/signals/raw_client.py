

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.lamp_code import LampCode
from ..types.moment import Moment
from ..types.quoted_moment import QuotedMoment
from pydantic import ValidationError


class RawSignalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_signals(
        self,
        *,
        observed_to: Moment,
        observed_from: typing.Optional[Moment] = None,
        quoted_from: typing.Optional[QuotedMoment] = None,
        lamp: typing.Optional[LampCode] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        observed_to : Moment

        observed_from : typing.Optional[Moment]

        quoted_from : typing.Optional[QuotedMoment]

        lamp : typing.Optional[LampCode]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Signals
        """
        _response = self._client_wrapper.httpx_client.request(
            "signals",
            method="GET",
            params={
                "observedFrom": serialize_datetime(observed_from) if observed_from is not None else None,
                "quotedFrom": serialize_datetime(quoted_from) if quoted_from is not None else None,
                "lamp": lamp,
                "observedTo": serialize_datetime(observed_to),
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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


class AsyncRawSignalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_signals(
        self,
        *,
        observed_to: Moment,
        observed_from: typing.Optional[Moment] = None,
        quoted_from: typing.Optional[QuotedMoment] = None,
        lamp: typing.Optional[LampCode] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        observed_to : Moment

        observed_from : typing.Optional[Moment]

        quoted_from : typing.Optional[QuotedMoment]

        lamp : typing.Optional[LampCode]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Signals
        """
        _response = await self._client_wrapper.httpx_client.request(
            "signals",
            method="GET",
            params={
                "observedFrom": serialize_datetime(observed_from) if observed_from is not None else None,
                "quotedFrom": serialize_datetime(quoted_from) if quoted_from is not None else None,
                "lamp": lamp,
                "observedTo": serialize_datetime(observed_to),
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
