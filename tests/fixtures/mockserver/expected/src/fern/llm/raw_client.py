

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
from ..errors.internal_server_error import InternalServerError
from .types.get_mockserver_llm_optimisation_report_request_format import GetMockserverLlmOptimisationReportRequestFormat
from .types.put_mockserver_llm_diff_runs_request_after import PutMockserverLlmDiffRunsRequestAfter
from .types.put_mockserver_llm_diff_runs_request_before import PutMockserverLlmDiffRunsRequestBefore
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLlmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_the_llm_optimisation_report(
        self,
        *,
        format: typing.Optional[GetMockserverLlmOptimisationReportRequestFormat] = None,
        session: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Analyses captured LLM traffic and reports optimisation signals (cost, latency, token usage, prompt and response characteristics) with an overall verdict. The report can also be emitted in evaluation-dataset formats for downstream tooling. An empty capture is a 200 with an empty report, not an error.

        Parameters
        ----------
        format : typing.Optional[GetMockserverLlmOptimisationReportRequestFormat]
            output format; defaults to json. The dataset formats also accept the aliases `evals` (openai-evals) and `finetune` (fine-tune), and underscores in place of hyphens.

        session : typing.Optional[str]
            restrict the report to a single captured session

        host : typing.Optional[str]
            restrict the report to a single upstream host

        provider : typing.Optional[str]
            restrict the report to a single LLM provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            optimisation report returned in the requested format
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/llm/optimisationReport",
            method="GET",
            params={
                "format": format,
                "session": session,
                "host": host,
                "provider": provider,
            },
            request_options=request_options,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def diff_two_captured_llm_agent_runs(
        self,
        *,
        before: typing.Optional[PutMockserverLlmDiffRunsRequestBefore] = OMIT,
        after: typing.Optional[PutMockserverLlmDiffRunsRequestAfter] = OMIT,
        normalization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Compares two captured agent runs, each selected by session, host and/or provider, and reports where they diverge. Normalization options control which incidental differences are ignored before comparing. The request body is optional — an empty body is treated as an empty filter on both sides.

        Parameters
        ----------
        before : typing.Optional[PutMockserverLlmDiffRunsRequestBefore]

        after : typing.Optional[PutMockserverLlmDiffRunsRequestAfter]

        normalization : typing.Optional[typing.Dict[str, typing.Any]]
            options controlling which incidental differences are ignored

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            diff of the two runs returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/llm/diffRuns",
            method="PUT",
            json={
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=PutMockserverLlmDiffRunsRequestBefore, direction="write"
                ),
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=PutMockserverLlmDiffRunsRequestAfter, direction="write"
                ),
                "normalization": normalization,
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawLlmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_the_llm_optimisation_report(
        self,
        *,
        format: typing.Optional[GetMockserverLlmOptimisationReportRequestFormat] = None,
        session: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Analyses captured LLM traffic and reports optimisation signals (cost, latency, token usage, prompt and response characteristics) with an overall verdict. The report can also be emitted in evaluation-dataset formats for downstream tooling. An empty capture is a 200 with an empty report, not an error.

        Parameters
        ----------
        format : typing.Optional[GetMockserverLlmOptimisationReportRequestFormat]
            output format; defaults to json. The dataset formats also accept the aliases `evals` (openai-evals) and `finetune` (fine-tune), and underscores in place of hyphens.

        session : typing.Optional[str]
            restrict the report to a single captured session

        host : typing.Optional[str]
            restrict the report to a single upstream host

        provider : typing.Optional[str]
            restrict the report to a single LLM provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            optimisation report returned in the requested format
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/llm/optimisationReport",
            method="GET",
            params={
                "format": format,
                "session": session,
                "host": host,
                "provider": provider,
            },
            request_options=request_options,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def diff_two_captured_llm_agent_runs(
        self,
        *,
        before: typing.Optional[PutMockserverLlmDiffRunsRequestBefore] = OMIT,
        after: typing.Optional[PutMockserverLlmDiffRunsRequestAfter] = OMIT,
        normalization: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Compares two captured agent runs, each selected by session, host and/or provider, and reports where they diverge. Normalization options control which incidental differences are ignored before comparing. The request body is optional — an empty body is treated as an empty filter on both sides.

        Parameters
        ----------
        before : typing.Optional[PutMockserverLlmDiffRunsRequestBefore]

        after : typing.Optional[PutMockserverLlmDiffRunsRequestAfter]

        normalization : typing.Optional[typing.Dict[str, typing.Any]]
            options controlling which incidental differences are ignored

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            diff of the two runs returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/llm/diffRuns",
            method="PUT",
            json={
                "before": convert_and_respect_annotation_metadata(
                    object_=before, annotation=PutMockserverLlmDiffRunsRequestBefore, direction="write"
                ),
                "after": convert_and_respect_annotation_metadata(
                    object_=after, annotation=PutMockserverLlmDiffRunsRequestAfter, direction="write"
                ),
                "normalization": normalization,
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
            if _response.status_code == 500:
                raise InternalServerError(
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
