

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
from ..errors.not_acceptable_error import NotAcceptableError
from ..types.slo_objective import SloObjective
from ..types.slo_verdict import SloVerdict
from .types.slo_criteria_window import SloCriteriaWindow
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSloClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def verify_a_service_level_objective_over_a_window(
        self,
        *,
        objectives: typing.Sequence[SloObjective],
        name: typing.Optional[str] = OMIT,
        window: typing.Optional[SloCriteriaWindow] = OMIT,
        minimum_sample_count: typing.Optional[int] = OMIT,
        upstream_hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SloVerdict]:
        """
        Evaluates a named set of objectives (latency percentiles, error rate) over a time window against the recorded forward-path SLI samples and returns a PASS / FAIL / INCONCLUSIVE verdict. The HTTP status encodes the verdict so a CI or chaos gate can assert on the status code alone: 200 when the verdict is PASS or INCONCLUSIVE, 406 when it is FAIL. A criteria PASSes only when all objectives hold (logical AND); it is INCONCLUSIVE when an indicator cannot be computed or the window holds fewer than minimumSampleCount samples. Off by default — returns 400 until sloTrackingEnabled=true.

        Parameters
        ----------
        objectives : typing.Sequence[SloObjective]

        name : typing.Optional[str]
            human-readable criteria name, echoed back in the verdict

        window : typing.Optional[SloCriteriaWindow]
            the time window to evaluate over

        minimum_sample_count : typing.Optional[int]
            minimum samples required in the window; below this the verdict is INCONCLUSIVE

        upstream_hosts : typing.Optional[typing.Sequence[str]]
            optional list of upstream hosts to restrict the evaluation to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SloVerdict]
            verdict is PASS or INCONCLUSIVE
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/verifySLO",
            method="PUT",
            json={
                "name": name,
                "window": convert_and_respect_annotation_metadata(
                    object_=window, annotation=SloCriteriaWindow, direction="write"
                ),
                "minimumSampleCount": minimum_sample_count,
                "upstreamHosts": upstream_hosts,
                "objectives": convert_and_respect_annotation_metadata(
                    object_=objectives, annotation=typing.Sequence[SloObjective], direction="write"
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
                    SloVerdict,
                    parse_obj_as(
                        type_=SloVerdict,
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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


class AsyncRawSloClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def verify_a_service_level_objective_over_a_window(
        self,
        *,
        objectives: typing.Sequence[SloObjective],
        name: typing.Optional[str] = OMIT,
        window: typing.Optional[SloCriteriaWindow] = OMIT,
        minimum_sample_count: typing.Optional[int] = OMIT,
        upstream_hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SloVerdict]:
        """
        Evaluates a named set of objectives (latency percentiles, error rate) over a time window against the recorded forward-path SLI samples and returns a PASS / FAIL / INCONCLUSIVE verdict. The HTTP status encodes the verdict so a CI or chaos gate can assert on the status code alone: 200 when the verdict is PASS or INCONCLUSIVE, 406 when it is FAIL. A criteria PASSes only when all objectives hold (logical AND); it is INCONCLUSIVE when an indicator cannot be computed or the window holds fewer than minimumSampleCount samples. Off by default — returns 400 until sloTrackingEnabled=true.

        Parameters
        ----------
        objectives : typing.Sequence[SloObjective]

        name : typing.Optional[str]
            human-readable criteria name, echoed back in the verdict

        window : typing.Optional[SloCriteriaWindow]
            the time window to evaluate over

        minimum_sample_count : typing.Optional[int]
            minimum samples required in the window; below this the verdict is INCONCLUSIVE

        upstream_hosts : typing.Optional[typing.Sequence[str]]
            optional list of upstream hosts to restrict the evaluation to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SloVerdict]
            verdict is PASS or INCONCLUSIVE
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/verifySLO",
            method="PUT",
            json={
                "name": name,
                "window": convert_and_respect_annotation_metadata(
                    object_=window, annotation=SloCriteriaWindow, direction="write"
                ),
                "minimumSampleCount": minimum_sample_count,
                "upstreamHosts": upstream_hosts,
                "objectives": convert_and_respect_annotation_metadata(
                    object_=objectives, annotation=typing.Sequence[SloObjective], direction="write"
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
                    SloVerdict,
                    parse_obj_as(
                        type_=SloVerdict,
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
            if _response.status_code == 406:
                raise NotAcceptableError(
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
