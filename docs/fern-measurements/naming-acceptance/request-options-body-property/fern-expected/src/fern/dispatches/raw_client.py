

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.dispatch import Dispatch
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDispatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_dispatch(
        self,
        *,
        request_options: str,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dispatch]:
        """
        Parameters
        ----------
        request_options : str

        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dispatch]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "dispatches",
            method="POST",
            json={
                "kwargs": kwargs_,
                "request_options": request_options,
                "self": self_,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    def update_dispatch(
        self,
        dispatch_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dispatch]:
        """
        Parameters
        ----------
        dispatch_id : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dispatch]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dispatches/{encode_path_param(dispatch_id)}",
            method="PUT",
            json={
                "note": note,
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
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    def add_note(
        self, dispatch_id: str, *, request_options: str, _request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : str

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**_request_options, "max_retries": 0} if _request_options is not None else {"max_retries": 0}
        )
        _response = self._client_wrapper.httpx_client.request(
            f"dispatches/{encode_path_param(dispatch_id)}/notes",
            method="POST",
            data={
                "request_options": request_options,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=_request_options_with_retries_disabled,
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

    @contextlib.contextmanager
    def download_manifest(
        self,
        dispatch_id: str,
        *,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            the manifest
        """
        with self._client_wrapper.httpx_client.stream(
            f"dispatches/{encode_path_param(dispatch_id)}/manifest",
            method="GET",
            params={
                "request_options": request_options,
            },
            request_options=_request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = _request_options.get("chunk_size", None) if _request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawDispatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_dispatch(
        self,
        *,
        request_options: str,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dispatch]:
        """
        Parameters
        ----------
        request_options : str

        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dispatch]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dispatches",
            method="POST",
            json={
                "kwargs": kwargs_,
                "request_options": request_options,
                "self": self_,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=_request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    async def update_dispatch(
        self,
        dispatch_id: str,
        *,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dispatch]:
        """
        Parameters
        ----------
        dispatch_id : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dispatch]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dispatches/{encode_path_param(dispatch_id)}",
            method="PUT",
            json={
                "note": note,
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
                    Dispatch,
                    parse_obj_as(
                        type_=Dispatch,
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

    async def add_note(
        self, dispatch_id: str, *, request_options: str, _request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : str

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _request_options_with_retries_disabled: typing.Optional[RequestOptions] = (
            {**_request_options, "max_retries": 0} if _request_options is not None else {"max_retries": 0}
        )
        _response = await self._client_wrapper.httpx_client.request(
            f"dispatches/{encode_path_param(dispatch_id)}/notes",
            method="POST",
            data={
                "request_options": request_options,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=_request_options_with_retries_disabled,
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

    @contextlib.asynccontextmanager
    async def download_manifest(
        self,
        dispatch_id: str,
        *,
        request_options: typing.Optional[str] = None,
        _request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        dispatch_id : str

        request_options : typing.Optional[str]

        _request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            the manifest
        """
        async with self._client_wrapper.httpx_client.stream(
            f"dispatches/{encode_path_param(dispatch_id)}/manifest",
            method="GET",
            params={
                "request_options": request_options,
            },
            request_options=_request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = _request_options.get("chunk_size", None) if _request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
