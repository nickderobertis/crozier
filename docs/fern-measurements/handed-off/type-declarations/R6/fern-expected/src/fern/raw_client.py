

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.passage import Passage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_passages(
        self,
        lock_id: str,
        *,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Passage]]:
        """
        Parameters
        ----------
        lock_id : str

                    The lock to read, by its painted number.
                    (ex. /L7)


        direction : typing.Optional[str]

            Upstream or downstream.

        limit : typing.Optional[int]
            Plain description without a leading break.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Passage]]
            The passages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"locks/{encode_path_param(lock_id)}/passages",
            method="GET",
            params={
                "direction": direction,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    def book_passage(
        self,
        lock_id: str,
        *,
        boat_name: str,
        draught: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Passage]:
        """
        Parameters
        ----------
        lock_id : str

        boat_name : str

                    The boat's registered name.


        draught : typing.Optional[float]

            Depth below the waterline, in metres.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Passage]
            The booked passage
        """
        _response = self._client_wrapper.httpx_client.request(
            f"locks/{encode_path_param(lock_id)}/passages",
            method="POST",
            json={
                "boatName": boat_name,
                "draught": draught,
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
                    Passage,
                    parse_obj_as(
                        type_=Passage,
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

    async def list_passages(
        self,
        lock_id: str,
        *,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Passage]]:
        """
        Parameters
        ----------
        lock_id : str

                    The lock to read, by its painted number.
                    (ex. /L7)


        direction : typing.Optional[str]

            Upstream or downstream.

        limit : typing.Optional[int]
            Plain description without a leading break.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Passage]]
            The passages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"locks/{encode_path_param(lock_id)}/passages",
            method="GET",
            params={
                "direction": direction,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Passage],
                    parse_obj_as(
                        type_=typing.List[Passage],
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

    async def book_passage(
        self,
        lock_id: str,
        *,
        boat_name: str,
        draught: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Passage]:
        """
        Parameters
        ----------
        lock_id : str

        boat_name : str

                    The boat's registered name.


        draught : typing.Optional[float]

            Depth below the waterline, in metres.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Passage]
            The booked passage
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"locks/{encode_path_param(lock_id)}/passages",
            method="POST",
            json={
                "boatName": boat_name,
                "draught": draught,
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
                    Passage,
                    parse_obj_as(
                        type_=Passage,
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
