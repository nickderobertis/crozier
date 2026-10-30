

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.introspection_request_token_type_hint import IntrospectionRequestTokenTypeHint
from ..types.introspection_response import IntrospectionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIntrospectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def introspect_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectionRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IntrospectionResponse]:
        """
        MUST be called by the permission pipeline before any invocation of a tool whose
        `is_irreversible = True`, regardless of local cache state (FR-007).

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[IntrospectionRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IntrospectionResponse]
            Introspection response.
        """
        _response = self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IntrospectionResponse,
                    parse_obj_as(
                        type_=IntrospectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawIntrospectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def introspect_delegation_token(
        self,
        *,
        token: str,
        token_type_hint: typing.Optional[IntrospectionRequestTokenTypeHint] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IntrospectionResponse]:
        """
        MUST be called by the permission pipeline before any invocation of a tool whose
        `is_irreversible = True`, regardless of local cache state (FR-007).

        Parameters
        ----------
        token : str

        token_type_hint : typing.Optional[IntrospectionRequestTokenTypeHint]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IntrospectionResponse]
            Introspection response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "introspect",
            method="POST",
            data={
                "token": token,
                "token_type_hint": token_type_hint,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IntrospectionResponse,
                    parse_obj_as(
                        type_=IntrospectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
