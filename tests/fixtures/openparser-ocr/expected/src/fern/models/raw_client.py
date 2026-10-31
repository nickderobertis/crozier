

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.ocr_llm_models_response import OcrLlmModelsResponse
from ..types.ocr_models_response import OcrModelsResponse
from .types.list_llm_models_request_mode import ListLlmModelsRequestMode
from pydantic import ValidationError


class RawModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_ocr_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OcrModelsResponse]:
        """
        Returns the hosted OCR model registry with current capabilities, option defaults,
        retail page prices, and availability. Clients should discover this endpoint instead of
        hard-coding model IDs or provider-specific options.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OcrModelsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "models/ocr",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrModelsResponse,
                    parse_obj_as(
                        type_=OcrModelsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def list_llm_models(
        self,
        *,
        mode: typing.Optional[ListLlmModelsRequestMode] = None,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OcrLlmModelsResponse]:
        """
        Returns a cached, normalized OpenRouter catalog filtered to models that advertise
        strict structured output (`structured_outputs` + `response_format`), have valid finite
        provider-list cost (internally) that is converted to customer retail rates, produce text, and are not expired.

        Default `mode=suggested` returns a short recommended subset. `mode=search` discovers the
        full compatible catalog with optional `q` / pagination. Field grounding and schema
        suggestion remain restricted to certified models.

        Parameters
        ----------
        mode : typing.Optional[ListLlmModelsRequestMode]
            `suggested` (default): short recommended subset.
            `search`: full compatible catalog filtered by `q`.

        q : typing.Optional[str]
            Case-insensitive substring match against id, label, or provider. Used with `mode=search`.

        page : typing.Optional[int]
            1-based page index when paginating search results.

        limit : typing.Optional[int]
            Page size for search; ignored for suggested mode (bounded server-side).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OcrLlmModelsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "models/llm",
            method="GET",
            params={
                "mode": mode,
                "q": q,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrLlmModelsResponse,
                    parse_obj_as(
                        type_=OcrLlmModelsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_ocr_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OcrModelsResponse]:
        """
        Returns the hosted OCR model registry with current capabilities, option defaults,
        retail page prices, and availability. Clients should discover this endpoint instead of
        hard-coding model IDs or provider-specific options.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OcrModelsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "models/ocr",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrModelsResponse,
                    parse_obj_as(
                        type_=OcrModelsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def list_llm_models(
        self,
        *,
        mode: typing.Optional[ListLlmModelsRequestMode] = None,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OcrLlmModelsResponse]:
        """
        Returns a cached, normalized OpenRouter catalog filtered to models that advertise
        strict structured output (`structured_outputs` + `response_format`), have valid finite
        provider-list cost (internally) that is converted to customer retail rates, produce text, and are not expired.

        Default `mode=suggested` returns a short recommended subset. `mode=search` discovers the
        full compatible catalog with optional `q` / pagination. Field grounding and schema
        suggestion remain restricted to certified models.

        Parameters
        ----------
        mode : typing.Optional[ListLlmModelsRequestMode]
            `suggested` (default): short recommended subset.
            `search`: full compatible catalog filtered by `q`.

        q : typing.Optional[str]
            Case-insensitive substring match against id, label, or provider. Used with `mode=search`.

        page : typing.Optional[int]
            1-based page index when paginating search results.

        limit : typing.Optional[int]
            Page size for search; ignored for suggested mode (bounded server-side).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OcrLlmModelsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "models/llm",
            method="GET",
            params={
                "mode": mode,
                "q": q,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrLlmModelsResponse,
                    parse_obj_as(
                        type_=OcrLlmModelsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
