

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.expectation import Expectation
from ..types.request_definition import RequestDefinition
from .types.put_mockserver_traffic_validate_response import PutMockserverTrafficValidateResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTroubleshootingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def explain_why_recent_requests_did_not_match_any_expectation(
        self, *, limit: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns a diagnostic report for recently recorded unmatched requests, including the closest-matching expectations and the per-field differences that prevented a match. An optional 'limit' in the body bounds how many unmatched requests are analysed (default 10).

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent unmatched requests to analyse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            unmatched-request explanation returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/explainUnmatched",
            method="PUT",
            json={
                "limit": limit,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def return_per_expectation_mismatch_debug_information_for_a_request(
        self, *, request: RequestDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Evaluates the supplied HttpRequest against every active expectation and returns, for each, whether it matched and the per-field differences, plus a closest match. Only HttpRequest definitions are supported (not OpenAPI definitions).

        Parameters
        ----------
        request : RequestDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            mismatch debug information returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/debugMismatch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RequestDefinition, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diff_a_baseline_set_of_expectations_against_another(
        self,
        *,
        baseline: typing.Sequence[Expectation],
        current: typing.Optional[typing.Sequence[Expectation]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Compares a "baseline" array of expectations against a "current" array and returns a structured diff of what was added, removed and changed. When "current" is omitted the baseline is diffed against the instance's live active expectations, which makes this usable as a drift check against a committed baseline.

        Parameters
        ----------
        baseline : typing.Sequence[Expectation]

        current : typing.Optional[typing.Sequence[Expectation]]
            optional; when omitted the live active expectations are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            baseline diff report returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/baseline/compare",
            method="PUT",
            json={
                "baseline": convert_and_respect_annotation_metadata(
                    object_=baseline, annotation=typing.Sequence[Expectation], direction="write"
                ),
                "current": convert_and_respect_annotation_metadata(
                    object_=current, annotation=typing.Sequence[Expectation], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def validate_recorded_traffic_against_an_open_api_specification(
        self,
        *,
        spec: typing.Optional[str] = OMIT,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverTrafficValidateResponse]:
        """
        Validates the request/response pairs already recorded in the event log against an OpenAPI specification, and reports per-exchange which operation it matched and any request or response violations. Supply the spec as a URL, file path or inline JSON/YAML under "spec" (or its alias "specUrlOrPayload"). A spec fetched by URL is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). The traffic validated comes from the recorded event log, not from the request body.

        Parameters
        ----------
        spec : typing.Optional[str]
            OpenAPI spec as a URL, file path or inline JSON/YAML

        spec_url_or_payload : typing.Optional[str]
            accepted alias for "spec"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverTrafficValidateResponse]
            validation completed (inspect allPassed and the per-request results)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/trafficValidate",
            method="PUT",
            json={
                "spec": spec,
                "specUrlOrPayload": spec_url_or_payload,
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
                    PutMockserverTrafficValidateResponse,
                    parse_obj_as(
                        type_=PutMockserverTrafficValidateResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawTroubleshootingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def explain_why_recent_requests_did_not_match_any_expectation(
        self, *, limit: typing.Optional[int] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Returns a diagnostic report for recently recorded unmatched requests, including the closest-matching expectations and the per-field differences that prevented a match. An optional 'limit' in the body bounds how many unmatched requests are analysed (default 10).

        Parameters
        ----------
        limit : typing.Optional[int]
            maximum number of recent unmatched requests to analyse

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            unmatched-request explanation returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/explainUnmatched",
            method="PUT",
            json={
                "limit": limit,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def return_per_expectation_mismatch_debug_information_for_a_request(
        self, *, request: RequestDefinition, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Evaluates the supplied HttpRequest against every active expectation and returns, for each, whether it matched and the per-field differences, plus a closest match. Only HttpRequest definitions are supported (not OpenAPI definitions).

        Parameters
        ----------
        request : RequestDefinition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            mismatch debug information returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/debugMismatch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RequestDefinition, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diff_a_baseline_set_of_expectations_against_another(
        self,
        *,
        baseline: typing.Sequence[Expectation],
        current: typing.Optional[typing.Sequence[Expectation]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Compares a "baseline" array of expectations against a "current" array and returns a structured diff of what was added, removed and changed. When "current" is omitted the baseline is diffed against the instance's live active expectations, which makes this usable as a drift check against a committed baseline.

        Parameters
        ----------
        baseline : typing.Sequence[Expectation]

        current : typing.Optional[typing.Sequence[Expectation]]
            optional; when omitted the live active expectations are used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            baseline diff report returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/baseline/compare",
            method="PUT",
            json={
                "baseline": convert_and_respect_annotation_metadata(
                    object_=baseline, annotation=typing.Sequence[Expectation], direction="write"
                ),
                "current": convert_and_respect_annotation_metadata(
                    object_=current, annotation=typing.Sequence[Expectation], direction="write"
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def validate_recorded_traffic_against_an_open_api_specification(
        self,
        *,
        spec: typing.Optional[str] = OMIT,
        spec_url_or_payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverTrafficValidateResponse]:
        """
        Validates the request/response pairs already recorded in the event log against an OpenAPI specification, and reports per-exchange which operation it matched and any request or response violations. Supply the spec as a URL, file path or inline JSON/YAML under "spec" (or its alias "specUrlOrPayload"). A spec fetched by URL is subject to the SSRF policy (forwardProxyBlockPrivateNetworks). The traffic validated comes from the recorded event log, not from the request body.

        Parameters
        ----------
        spec : typing.Optional[str]
            OpenAPI spec as a URL, file path or inline JSON/YAML

        spec_url_or_payload : typing.Optional[str]
            accepted alias for "spec"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverTrafficValidateResponse]
            validation completed (inspect allPassed and the per-request results)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/trafficValidate",
            method="PUT",
            json={
                "spec": spec,
                "specUrlOrPayload": spec_url_or_payload,
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
                    PutMockserverTrafficValidateResponse,
                    parse_obj_as(
                        type_=PutMockserverTrafficValidateResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
