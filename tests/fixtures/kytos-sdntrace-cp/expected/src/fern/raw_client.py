

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.failed_dependency_error import FailedDependencyError
from .types.put_v1trace_request_trace import PutV1TraceRequestTrace
from .types.put_v1trace_response import PutV1TraceResponse
from .types.put_v1traces_request_item import PutV1TracesRequestItem
from .types.put_v1traces_response import PutV1TracesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def trace_a_path(
        self,
        *,
        trace: typing.Optional[PutV1TraceRequestTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutV1TraceResponse]:
        """
        Trace a path starting with the switch given with the parameters given. The trace is done entirely in control plane.

        Parameters
        ----------
        trace : typing.Optional[PutV1TraceRequestTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutV1TraceResponse]
            Ok.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trace",
            method="PUT",
            json={
                "trace": convert_and_respect_annotation_metadata(
                    object_=trace, annotation=PutV1TraceRequestTrace, direction="write"
                ),
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
                    PutV1TraceResponse,
                    parse_obj_as(
                        type_=PutV1TraceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 424:
                raise FailedDependencyError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trace_paths_given_switches(
        self,
        *,
        request: typing.Sequence[PutV1TracesRequestItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutV1TracesResponse]:
        """
        Trace a path starting with each switch given in a list as parameter.

        Parameters
        ----------
        request : typing.Sequence[PutV1TracesRequestItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutV1TracesResponse]
            Ok.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/traces",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PutV1TracesRequestItem], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutV1TracesResponse,
                    parse_obj_as(
                        type_=PutV1TracesResponse,
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

    async def trace_a_path(
        self,
        *,
        trace: typing.Optional[PutV1TraceRequestTrace] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutV1TraceResponse]:
        """
        Trace a path starting with the switch given with the parameters given. The trace is done entirely in control plane.

        Parameters
        ----------
        trace : typing.Optional[PutV1TraceRequestTrace]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutV1TraceResponse]
            Ok.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trace",
            method="PUT",
            json={
                "trace": convert_and_respect_annotation_metadata(
                    object_=trace, annotation=PutV1TraceRequestTrace, direction="write"
                ),
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
                    PutV1TraceResponse,
                    parse_obj_as(
                        type_=PutV1TraceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 424:
                raise FailedDependencyError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trace_paths_given_switches(
        self,
        *,
        request: typing.Sequence[PutV1TracesRequestItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutV1TracesResponse]:
        """
        Trace a path starting with each switch given in a list as parameter.

        Parameters
        ----------
        request : typing.Sequence[PutV1TracesRequestItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutV1TracesResponse]
            Ok.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/traces",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[PutV1TracesRequestItem], direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutV1TracesResponse,
                    parse_obj_as(
                        type_=PutV1TracesResponse,
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
