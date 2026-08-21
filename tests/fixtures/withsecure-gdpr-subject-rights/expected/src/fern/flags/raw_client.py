

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.contexts_response import ContextsResponse
from pydantic import ValidationError


class RawFlagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_personal_data_contexts(
        self, *, accept_language: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContextsResponse]:
        """
        The API exposes actions against contexts (logical groups) of personal data in the given system. The grouping should be based on usage, e.g., personal data used for marketing, personal data collected for usage analysis, or personal data processed for technical realisation of the service. The same personal data type (e.g., an email address) may be in several contexts; this does not imply it would be actually duplicated in the system, but it could be used in different contexts. Typically, a single context should not contain data that is processed under different basis of processing.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "contexts",
            method="GET",
            headers={
                "Accept-Language": str(accept_language) if accept_language is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextsResponse,
                    parse_obj_as(
                        type_=ContextsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawFlagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_personal_data_contexts(
        self, *, accept_language: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContextsResponse]:
        """
        The API exposes actions against contexts (logical groups) of personal data in the given system. The grouping should be based on usage, e.g., personal data used for marketing, personal data collected for usage analysis, or personal data processed for technical realisation of the service. The same personal data type (e.g., an email address) may be in several contexts; this does not imply it would be actually duplicated in the system, but it could be used in different contexts. Typically, a single context should not contain data that is processed under different basis of processing.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contexts",
            method="GET",
            headers={
                "Accept-Language": str(accept_language) if accept_language is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContextsResponse,
                    parse_obj_as(
                        type_=ContextsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
