

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.obj1 import Obj1
from .types.obj3 import Obj3
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def put_some_path_id_template(
        self,
        id: float,
        *,
        first_name: str,
        last_name: str,
        n: typing.Optional[float] = None,
        middle_names: typing.Optional[typing.Sequence[str]] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Obj1]:
        """
        Parameters
        ----------
        id : float
            some parameter

        first_name : str

        last_name : str

        n : typing.Optional[float]

        middle_names : typing.Optional[typing.Sequence[str]]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Obj1]
            some content
        """
        _response = self._client_wrapper.httpx_client.request(
            f"some/path/{encode_path_param(id)}/template",
            method="PUT",
            params={
                "n": n,
            },
            json={
                "firstName": first_name,
                "lastName": last_name,
                "middleNames": middle_names,
                "email": email,
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
                    Obj1,
                    parse_obj_as(
                        type_=Obj1,
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

    def patch_some_path_id_template(
        self,
        id: float,
        *,
        first_name: str,
        last_name: str,
        n: typing.Optional[float] = None,
        middle_names: typing.Optional[typing.Sequence[str]] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Obj1]:
        """
        Parameters
        ----------
        id : float
            some parameter

        first_name : str

        last_name : str

        n : typing.Optional[float]

        middle_names : typing.Optional[typing.Sequence[str]]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Obj1]
            some content
        """
        _response = self._client_wrapper.httpx_client.request(
            f"some/path/{encode_path_param(id)}/template",
            method="PATCH",
            params={
                "n": n,
            },
            json={
                "firstName": first_name,
                "lastName": last_name,
                "middleNames": middle_names,
                "email": email,
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
                    Obj1,
                    parse_obj_as(
                        type_=Obj1,
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

    def get_something(
        self,
        *,
        q: str,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[Obj3]]:
        """
        Parameters
        ----------
        q : str

        if_none_match : typing.Optional[str]
            makes the request conditional

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[Obj3]]
            all good
        """
        _response = self._client_wrapper.httpx_client.request(
            "something",
            method="GET",
            params={
                "q": q,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Obj3],
                    parse_obj_as(
                        type_=typing.Optional[Obj3],
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

    async def put_some_path_id_template(
        self,
        id: float,
        *,
        first_name: str,
        last_name: str,
        n: typing.Optional[float] = None,
        middle_names: typing.Optional[typing.Sequence[str]] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Obj1]:
        """
        Parameters
        ----------
        id : float
            some parameter

        first_name : str

        last_name : str

        n : typing.Optional[float]

        middle_names : typing.Optional[typing.Sequence[str]]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Obj1]
            some content
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"some/path/{encode_path_param(id)}/template",
            method="PUT",
            params={
                "n": n,
            },
            json={
                "firstName": first_name,
                "lastName": last_name,
                "middleNames": middle_names,
                "email": email,
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
                    Obj1,
                    parse_obj_as(
                        type_=Obj1,
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

    async def patch_some_path_id_template(
        self,
        id: float,
        *,
        first_name: str,
        last_name: str,
        n: typing.Optional[float] = None,
        middle_names: typing.Optional[typing.Sequence[str]] = OMIT,
        email: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Obj1]:
        """
        Parameters
        ----------
        id : float
            some parameter

        first_name : str

        last_name : str

        n : typing.Optional[float]

        middle_names : typing.Optional[typing.Sequence[str]]

        email : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Obj1]
            some content
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"some/path/{encode_path_param(id)}/template",
            method="PATCH",
            params={
                "n": n,
            },
            json={
                "firstName": first_name,
                "lastName": last_name,
                "middleNames": middle_names,
                "email": email,
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
                    Obj1,
                    parse_obj_as(
                        type_=Obj1,
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

    async def get_something(
        self,
        *,
        q: str,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[Obj3]]:
        """
        Parameters
        ----------
        q : str

        if_none_match : typing.Optional[str]
            makes the request conditional

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[Obj3]]
            all good
        """
        _response = await self._client_wrapper.httpx_client.request(
            "something",
            method="GET",
            params={
                "q": q,
            },
            headers={
                "If-None-Match": str(if_none_match) if if_none_match is not None else None,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Obj3],
                    parse_obj_as(
                        type_=typing.Optional[Obj3],
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
