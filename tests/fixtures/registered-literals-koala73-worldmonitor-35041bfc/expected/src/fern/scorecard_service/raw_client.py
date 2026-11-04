

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.get_bloc_scorecard_response import GetBlocScorecardResponse
from ..types.get_five_factor_scorecard_response import GetFiveFactorScorecardResponse
from ..types.list_five_factor_scorecards_response import ListFiveFactorScorecardsResponse
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from pydantic import ValidationError


class RawScorecardServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_five_factor_scorecard(
        self,
        *,
        country_code: str,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetFiveFactorScorecardResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code for the requested scorecard.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFiveFactorScorecardResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/get-five-factor-scorecard",
            method="GET",
            params={
                "countryCode": country_code,
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFiveFactorScorecardResponse,
                    parse_obj_as(
                        type_=GetFiveFactorScorecardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def list_five_factor_scorecards(
        self, *, jmespath: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListFiveFactorScorecardsResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListFiveFactorScorecardsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/list-five-factor-scorecards",
            method="GET",
            params={
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFiveFactorScorecardsResponse,
                    parse_obj_as(
                        type_=ListFiveFactorScorecardsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    def get_bloc_scorecard(
        self,
        *,
        preset: typing.Optional[str] = None,
        members: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetBlocScorecardResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        preset : typing.Optional[str]
            Official bloc preset: USMCA, EU27, BRICS, GCC, ASEAN, or NATO. Values are case-sensitive. Omit when members is provided.

        members : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Custom list of 2-30 unique uppercase ISO 3166-1 alpha-2 members. Provide either preset or members; do not provide both.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBlocScorecardResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/get-bloc-scorecard",
            method="GET",
            params={
                "preset": preset,
                "members": members,
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBlocScorecardResponse,
                    parse_obj_as(
                        type_=GetBlocScorecardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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


class AsyncRawScorecardServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_five_factor_scorecard(
        self,
        *,
        country_code: str,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetFiveFactorScorecardResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        country_code : str
            ISO 3166-1 alpha-2 country code for the requested scorecard.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFiveFactorScorecardResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/get-five-factor-scorecard",
            method="GET",
            params={
                "countryCode": country_code,
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFiveFactorScorecardResponse,
                    parse_obj_as(
                        type_=GetFiveFactorScorecardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def list_five_factor_scorecards(
        self, *, jmespath: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListFiveFactorScorecardsResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListFiveFactorScorecardsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/list-five-factor-scorecards",
            method="GET",
            params={
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListFiveFactorScorecardsResponse,
                    parse_obj_as(
                        type_=ListFiveFactorScorecardsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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

    async def get_bloc_scorecard(
        self,
        *,
        preset: typing.Optional[str] = None,
        members: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        jmespath: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetBlocScorecardResponse]:
        """
        PRO-gated. Requires entitlement tier >= 1.

        Parameters
        ----------
        preset : typing.Optional[str]
            Official bloc preset: USMCA, EU27, BRICS, GCC, ASEAN, or NATO. Values are case-sensitive. Omit when members is provided.

        members : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Custom list of 2-30 unique uppercase ISO 3166-1 alpha-2 members. Provide either preset or members; do not provide both.

        jmespath : typing.Optional[str]
            Optional JMESPath expression applied server-side to project or reduce the JSON response before it is returned (mirrors the MCP jmespath argument). Invalid expressions, expressions larger than 1024 UTF-8 bytes, or projections that exceed the 256 KB output cap return HTTP 400 with a {_jmespath_error, original_keys} envelope. Grammar and worked examples: https://www.worldmonitor.app/docs/mcp-jmespath.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBlocScorecardResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/scorecard/v1/get-bloc-scorecard",
            method="GET",
            params={
                "preset": preset,
                "members": members,
                "jmespath": jmespath,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBlocScorecardResponse,
                    parse_obj_as(
                        type_=GetBlocScorecardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
