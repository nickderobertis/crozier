

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.trim_hedge_request_finish import TrimHedgeRequestFinish
from .types.trim_hedge_response import TrimHedgeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawYewWalkClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def trim_hedge(
        self,
        *,
        length: float,
        finish: typing.Optional[TrimHedgeRequestFinish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TrimHedgeResponse]:
        """
        Parameters
        ----------
        length : float

        finish : typing.Optional[TrimHedgeRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrimHedgeResponse]
            The trimmed hedge.
        """
        _response = self._client_wrapper.httpx_client.request(
            "yew-walk/hedges",
            method="POST",
            json={
                "length": length,
                "finish": finish,
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
                    TrimHedgeResponse,
                    parse_obj_as(
                        type_=TrimHedgeResponse,
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


class AsyncRawYewWalkClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def trim_hedge(
        self,
        *,
        length: float,
        finish: typing.Optional[TrimHedgeRequestFinish] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TrimHedgeResponse]:
        """
        Parameters
        ----------
        length : float

        finish : typing.Optional[TrimHedgeRequestFinish]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrimHedgeResponse]
            The trimmed hedge.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "yew-walk/hedges",
            method="POST",
            json={
                "length": length,
                "finish": finish,
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
                    TrimHedgeResponse,
                    parse_obj_as(
                        type_=TrimHedgeResponse,
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
