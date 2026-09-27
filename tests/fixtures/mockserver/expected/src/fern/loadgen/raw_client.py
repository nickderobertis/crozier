

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.conflict_error_body import ConflictErrorBody
from ..types.http_request import HttpRequest
from ..types.load_feeder import LoadFeeder
from ..types.load_pacing import LoadPacing
from ..types.load_profile import LoadProfile
from ..types.load_scenario_list_entry import LoadScenarioListEntry
from ..types.load_scenario_report import LoadScenarioReport
from ..types.load_scenario_step_selection import LoadScenarioStepSelection
from ..types.load_scenario_template_type import LoadScenarioTemplateType
from ..types.load_step import LoadStep
from ..types.load_threshold import LoadThreshold
from .types.delete_mockserver_load_scenario_name_response import DeleteMockserverLoadScenarioNameResponse
from .types.delete_mockserver_load_scenario_response import DeleteMockserverLoadScenarioResponse
from .types.get_mockserver_load_scenario_name_report_request_format import (
    GetMockserverLoadScenarioNameReportRequestFormat,
)
from .types.get_mockserver_load_scenario_response import GetMockserverLoadScenarioResponse
from .types.put_mockserver_load_scenario_generate_from_open_api_request_target import (
    PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
)
from .types.put_mockserver_load_scenario_generate_from_open_api_response import (
    PutMockserverLoadScenarioGenerateFromOpenApiResponse,
)
from .types.put_mockserver_load_scenario_generate_from_recording_request_mode import (
    PutMockserverLoadScenarioGenerateFromRecordingRequestMode,
)
from .types.put_mockserver_load_scenario_generate_from_recording_request_target import (
    PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
)
from .types.put_mockserver_load_scenario_generate_from_recording_response import (
    PutMockserverLoadScenarioGenerateFromRecordingResponse,
)
from .types.put_mockserver_load_scenario_response import PutMockserverLoadScenarioResponse
from .types.put_mockserver_load_scenario_start_response import PutMockserverLoadScenarioStartResponse
from .types.put_mockserver_load_scenario_stop_response import PutMockserverLoadScenarioStopResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLoadgenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_registered_load_scenarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverLoadScenarioResponse]:
        """
        Lists every registered load scenario with its lifecycle state (LOADED / PENDING / RUNNING / COMPLETED / STOPPED), startDelayMillis, full definition, and — when active or recently run — the live status fields (stage, virtual users, request counts, latency percentiles, run id, timestamps).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverLoadScenarioResponse]
            registered load scenarios listed
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=GetMockserverLoadScenarioResponse,
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

    def load_register_a_load_scenario_into_the_registry(
        self,
        *,
        name: str,
        profile: LoadProfile,
        steps: typing.Sequence[LoadStep],
        template_type: typing.Optional[LoadScenarioTemplateType] = OMIT,
        max_requests: typing.Optional[int] = OMIT,
        start_delay_millis: typing.Optional[int] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        thresholds: typing.Optional[typing.Sequence[LoadThreshold]] = OMIT,
        abort_on_fail: typing.Optional[bool] = OMIT,
        abort_grace_millis: typing.Optional[int] = OMIT,
        pacing: typing.Optional[LoadPacing] = OMIT,
        feeder: typing.Optional[LoadFeeder] = OMIT,
        step_selection: typing.Optional[LoadScenarioStepSelection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverLoadScenarioResponse]:
        """
        Loads (registers) an API load scenario into the named registry under its "name" (the unique registry key). Loading does NOT run the scenario — it is staged in the LOADED state, ready to be triggered by PUT /mockserver/loadScenario/start. Loading the same name replaces the prior definition. A scenario is an ordered list of templated request steps driven through a sequence of stages (a load profile): a stage holds/ramps virtual users (VU, closed model), holds/ramps an arrival rate in iterations/second (RATE, open model), or pauses; an optional startDelayMillis defers the start after a trigger. Loading is allowed even when loadGenerationEnabled is false (no traffic is generated). Hard caps validated at load time: max 50 virtual users, max 5000 iterations/second, max 20 stages, max 50 steps, max 1h total duration.

        Parameters
        ----------
        name : str
            scenario name — the unique registry key. Loading the same name replaces the prior definition.

        profile : LoadProfile

        steps : typing.Sequence[LoadStep]
            ordered list of request steps. Under SEQUENTIAL stepSelection (default) all steps are fired in sequence each iteration; under WEIGHTED one step is chosen per iteration by weight (max 50)

        template_type : typing.Optional[LoadScenarioTemplateType]
            template engine used to render the per-iteration request path and body; only VELOCITY and MUSTACHE are supported for load steps (JAVASCRIPT is rejected)

        max_requests : typing.Optional[int]
            optional hard cap on the total number of requests dispatched

        start_delay_millis : typing.Optional[int]
            delay in milliseconds, applied after this scenario is triggered to start, before its iterations begin. A positive value means the scenario is PENDING until the delay elapses, then RUNNING; 0 (default) starts immediately on trigger. Lets several triggered scenarios begin at staggered offsets.

        labels : typing.Optional[typing.Dict[str, str]]
            optional scenario-level custom annotation labels; exported as OpenTelemetry attributes on every load measurement and (for keys named in the loadGenerationMetricLabels allowlist) as extra Prometheus labels

        thresholds : typing.Optional[typing.Sequence[LoadThreshold]]
            optional in-run pass/fail thresholds; the run carries a PASS verdict iff all hold, FAIL otherwise. Empty/omitted means no verdict is computed.

        abort_on_fail : typing.Optional[bool]
            when true, a FAIL verdict aborts the run early (terminal STOPPED state, abortedByThreshold set); default false (the run always finishes its stages and carries a final verdict)

        abort_grace_millis : typing.Optional[int]
            suppress abortOnFail for the first N milliseconds of the run so noisy startup samples cannot trigger a premature abort (thresholds are still evaluated and a verdict still reported during the grace window — only the abort action is deferred)

        pacing : typing.Optional[LoadPacing]

        feeder : typing.Optional[LoadFeeder]

        step_selection : typing.Optional[LoadScenarioStepSelection]
            how each iteration selects which steps to run: SEQUENTIAL (default) runs ALL steps in declared order (a multi-step user journey); WEIGHTED runs exactly ONE step per iteration chosen at random proportional to each step's weight (mixed-workload modelling, e.g. 70% browse / 20% search / 10% checkout). Cross-step captures are meaningful only under SEQUENTIAL (a WEIGHTED iteration runs a single step); feeder data and pacing apply to both.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverLoadScenarioResponse]
            load scenario loaded (registered)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="PUT",
            json={
                "name": name,
                "templateType": template_type,
                "maxRequests": max_requests,
                "startDelayMillis": start_delay_millis,
                "labels": labels,
                "thresholds": convert_and_respect_annotation_metadata(
                    object_=thresholds, annotation=typing.Sequence[LoadThreshold], direction="write"
                ),
                "abortOnFail": abort_on_fail,
                "abortGraceMillis": abort_grace_millis,
                "pacing": convert_and_respect_annotation_metadata(
                    object_=pacing, annotation=LoadPacing, direction="write"
                ),
                "feeder": convert_and_respect_annotation_metadata(
                    object_=feeder, annotation=LoadFeeder, direction="write"
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
                ),
                "stepSelection": step_selection,
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[LoadStep], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioResponse,
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

    def clear_the_load_scenario_registry(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMockserverLoadScenarioResponse]:
        """
        Removes ALL registered load scenarios, stopping any that are running. Idempotent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMockserverLoadScenarioResponse]
            load scenario registry cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=DeleteMockserverLoadScenarioResponse,
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

    def retrieve_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LoadScenarioListEntry]:
        """
        Returns a single registered load scenario (definition + state + live/terminal status). 404 if not registered.

        Parameters
        ----------
        name : str
            the registered load scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoadScenarioListEntry]
            load scenario returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoadScenarioListEntry,
                    parse_obj_as(
                        type_=LoadScenarioListEntry,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def remove_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMockserverLoadScenarioNameResponse]:
        """
        Removes a single load scenario from the registry, stopping it first if it is running.

        Parameters
        ----------
        name : str
            the registered load scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMockserverLoadScenarioNameResponse]
            load scenario removed (or absent)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverLoadScenarioNameResponse,
                    parse_obj_as(
                        type_=DeleteMockserverLoadScenarioNameResponse,
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

    def end_of_run_summary_report_for_a_load_scenario_run(
        self,
        name: str,
        *,
        format: typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LoadScenarioReport]:
        """
        Returns an end-of-run summary report derived from the run's status snapshot — the live snapshot while running, or the retained terminal snapshot once finished. The default JSON form carries counts, latency percentiles, the threshold verdict and per-threshold results. With ?format=junit the same data is rendered as a JUnit-XML <testsuite> (one <testcase> per threshold, a <failure> per breach, plus a "run completed" testcase) so CI consumers render per-threshold pass/fail. 404 if the scenario never ran.

        Parameters
        ----------
        name : str
            the load scenario name

        format : typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat]
            report format. Omit (or any value other than "junit") for the JSON report; "junit" returns a JUnit-XML <testsuite> (Content-Type application/xml) so a load run becomes a first-class CI test artifact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LoadScenarioReport]
            report returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}/report",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoadScenarioReport,
                    parse_obj_as(
                        type_=LoadScenarioReport,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def seed_a_load_scenario_from_an_open_api_specification(
        self,
        *,
        name: str,
        spec_url_or_payload: str,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverLoadScenarioGenerateFromOpenApiResponse]:
        """
        Generates an editable load scenario from an OpenAPI spec and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. One step is produced per OpenAPI operation (in a stable path-then-method order), each with the operation's method and server-prefixed path, a representative request-body example, and a Content-Type header. The spec is accepted identically to PUT /mockserver/openapi/expectation — an inline JSON/YAML payload, a URL, or a file/classpath reference. Target precedence for where each request is sent (carried as the request's Host header and secure flag): an explicit "target" wins, else the spec's servers[0] URL, else the request is left path-only for the operator to edit. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.

        Parameters
        ----------
        name : str
            the generated scenario name (the unique registry key)

        spec_url_or_payload : str
            the OpenAPI spec as an inline JSON/YAML payload, a URL, or a file/classpath reference

        target : typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget]
            explicit network target for every generated step (overrides the spec's servers[0])

        profile : typing.Optional[LoadProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverLoadScenarioGenerateFromOpenApiResponse]
            load scenario generated and loaded (registered)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/generateFromOpenAPI",
            method="PUT",
            json={
                "name": name,
                "specUrlOrPayload": spec_url_or_payload,
                "target": convert_and_respect_annotation_metadata(
                    object_=target,
                    annotation=PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
                    direction="write",
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
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
                    PutMockserverLoadScenarioGenerateFromOpenApiResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioGenerateFromOpenApiResponse,
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

    def seed_a_load_scenario_from_recorded_proxy_traffic(
        self,
        *,
        name: str,
        mode: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestMode] = OMIT,
        request_filter: typing.Optional[HttpRequest] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverLoadScenarioGenerateFromRecordingResponse]:
        """
        Generates an editable load scenario from traffic previously recorded by MockServer in proxy/recording mode (the requests held by the event log) and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. Two modes control how recorded requests become steps. VERBATIM (the default) emits one step per recorded request, in recorded order, preserving the concrete path, body and headers — with an optional "maxSteps" cap. TEMPLATIZED deduplicates recorded requests by (method, templatised-path) — id-shaped path segments such as /orders/123 collapse to /orders/{id} — keeping one representative example per unique route, ordered by descending hit frequency (most-hit routes first); each step's "weight" is set to its route's observed hit count and the scenario uses "stepSelection": "WEIGHTED" so replay reproduces the recorded traffic mix. An optional "requestFilter" (an HttpRequest matcher) selects which recorded requests to include; absent means all recorded requests. An optional "target" is applied to every step (overriding each recorded request's own Host/secure routing); absent leaves each recorded request's routing untouched. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.

        Parameters
        ----------
        name : str
            the generated scenario name (the unique registry key)

        mode : typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestMode]
            VERBATIM = one step per recorded request; TEMPLATIZED = one step per unique (method, templatised-path) route, ordered by descending frequency

        request_filter : typing.Optional[HttpRequest]

        max_steps : typing.Optional[int]
            optional cap on the number of VERBATIM steps (keeps the first N recorded requests)

        target : typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTarget]
            explicit network target applied to every generated step (overrides each recorded request's own Host/secure routing)

        profile : typing.Optional[LoadProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverLoadScenarioGenerateFromRecordingResponse]
            load scenario generated and loaded (registered)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/generateFromRecording",
            method="PUT",
            json={
                "name": name,
                "mode": mode,
                "requestFilter": convert_and_respect_annotation_metadata(
                    object_=request_filter, annotation=HttpRequest, direction="write"
                ),
                "maxSteps": max_steps,
                "target": convert_and_respect_annotation_metadata(
                    object_=target,
                    annotation=PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
                    direction="write",
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
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
                    PutMockserverLoadScenarioGenerateFromRecordingResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioGenerateFromRecordingResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
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

    def trigger_registered_load_scenario_s_to_run(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverLoadScenarioStartResponse]:
        """
        Triggers one or more registered load scenarios to start running concurrently. Each gets a fresh run id and honours its own startDelayMillis (a positive delay → the scenario is PENDING until the delay elapses, then RUNNING). Requires loadGenerationEnabled=true (else 403). 404 if a name is not registered. Rejected with 400 if it would exceed loadGenerationMaxConcurrentScenarios (default 10). Re-triggering an already-active name replaces that run.

        Parameters
        ----------
        names : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverLoadScenarioStartResponse]
            load scenario(s) triggered
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/start",
            method="PUT",
            json={
                "names": names,
                "name": name,
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
                    PutMockserverLoadScenarioStartResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioStartResponse,
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

    def stop_running_load_scenario_s(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        all_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverLoadScenarioStopResponse]:
        """
        Stops one or more running load scenarios. Body is {"names":[...]}, {"all":true}, or an empty body (stop all running). Stopped scenarios stay registered (state STOPPED) and can be re-triggered.

        Parameters
        ----------
        names : typing.Optional[typing.Sequence[str]]

        all_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverLoadScenarioStopResponse]
            load scenario(s) stopped
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/stop",
            method="PUT",
            json={
                "names": names,
                "all": all_,
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
                    PutMockserverLoadScenarioStopResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioStopResponse,
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


class AsyncRawLoadgenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_registered_load_scenarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverLoadScenarioResponse]:
        """
        Lists every registered load scenario with its lifecycle state (LOADED / PENDING / RUNNING / COMPLETED / STOPPED), startDelayMillis, full definition, and — when active or recently run — the live status fields (stage, virtual users, request counts, latency percentiles, run id, timestamps).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverLoadScenarioResponse]
            registered load scenarios listed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=GetMockserverLoadScenarioResponse,
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

    async def load_register_a_load_scenario_into_the_registry(
        self,
        *,
        name: str,
        profile: LoadProfile,
        steps: typing.Sequence[LoadStep],
        template_type: typing.Optional[LoadScenarioTemplateType] = OMIT,
        max_requests: typing.Optional[int] = OMIT,
        start_delay_millis: typing.Optional[int] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        thresholds: typing.Optional[typing.Sequence[LoadThreshold]] = OMIT,
        abort_on_fail: typing.Optional[bool] = OMIT,
        abort_grace_millis: typing.Optional[int] = OMIT,
        pacing: typing.Optional[LoadPacing] = OMIT,
        feeder: typing.Optional[LoadFeeder] = OMIT,
        step_selection: typing.Optional[LoadScenarioStepSelection] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverLoadScenarioResponse]:
        """
        Loads (registers) an API load scenario into the named registry under its "name" (the unique registry key). Loading does NOT run the scenario — it is staged in the LOADED state, ready to be triggered by PUT /mockserver/loadScenario/start. Loading the same name replaces the prior definition. A scenario is an ordered list of templated request steps driven through a sequence of stages (a load profile): a stage holds/ramps virtual users (VU, closed model), holds/ramps an arrival rate in iterations/second (RATE, open model), or pauses; an optional startDelayMillis defers the start after a trigger. Loading is allowed even when loadGenerationEnabled is false (no traffic is generated). Hard caps validated at load time: max 50 virtual users, max 5000 iterations/second, max 20 stages, max 50 steps, max 1h total duration.

        Parameters
        ----------
        name : str
            scenario name — the unique registry key. Loading the same name replaces the prior definition.

        profile : LoadProfile

        steps : typing.Sequence[LoadStep]
            ordered list of request steps. Under SEQUENTIAL stepSelection (default) all steps are fired in sequence each iteration; under WEIGHTED one step is chosen per iteration by weight (max 50)

        template_type : typing.Optional[LoadScenarioTemplateType]
            template engine used to render the per-iteration request path and body; only VELOCITY and MUSTACHE are supported for load steps (JAVASCRIPT is rejected)

        max_requests : typing.Optional[int]
            optional hard cap on the total number of requests dispatched

        start_delay_millis : typing.Optional[int]
            delay in milliseconds, applied after this scenario is triggered to start, before its iterations begin. A positive value means the scenario is PENDING until the delay elapses, then RUNNING; 0 (default) starts immediately on trigger. Lets several triggered scenarios begin at staggered offsets.

        labels : typing.Optional[typing.Dict[str, str]]
            optional scenario-level custom annotation labels; exported as OpenTelemetry attributes on every load measurement and (for keys named in the loadGenerationMetricLabels allowlist) as extra Prometheus labels

        thresholds : typing.Optional[typing.Sequence[LoadThreshold]]
            optional in-run pass/fail thresholds; the run carries a PASS verdict iff all hold, FAIL otherwise. Empty/omitted means no verdict is computed.

        abort_on_fail : typing.Optional[bool]
            when true, a FAIL verdict aborts the run early (terminal STOPPED state, abortedByThreshold set); default false (the run always finishes its stages and carries a final verdict)

        abort_grace_millis : typing.Optional[int]
            suppress abortOnFail for the first N milliseconds of the run so noisy startup samples cannot trigger a premature abort (thresholds are still evaluated and a verdict still reported during the grace window — only the abort action is deferred)

        pacing : typing.Optional[LoadPacing]

        feeder : typing.Optional[LoadFeeder]

        step_selection : typing.Optional[LoadScenarioStepSelection]
            how each iteration selects which steps to run: SEQUENTIAL (default) runs ALL steps in declared order (a multi-step user journey); WEIGHTED runs exactly ONE step per iteration chosen at random proportional to each step's weight (mixed-workload modelling, e.g. 70% browse / 20% search / 10% checkout). Cross-step captures are meaningful only under SEQUENTIAL (a WEIGHTED iteration runs a single step); feeder data and pacing apply to both.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverLoadScenarioResponse]
            load scenario loaded (registered)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="PUT",
            json={
                "name": name,
                "templateType": template_type,
                "maxRequests": max_requests,
                "startDelayMillis": start_delay_millis,
                "labels": labels,
                "thresholds": convert_and_respect_annotation_metadata(
                    object_=thresholds, annotation=typing.Sequence[LoadThreshold], direction="write"
                ),
                "abortOnFail": abort_on_fail,
                "abortGraceMillis": abort_grace_millis,
                "pacing": convert_and_respect_annotation_metadata(
                    object_=pacing, annotation=LoadPacing, direction="write"
                ),
                "feeder": convert_and_respect_annotation_metadata(
                    object_=feeder, annotation=LoadFeeder, direction="write"
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
                ),
                "stepSelection": step_selection,
                "steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[LoadStep], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioResponse,
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

    async def clear_the_load_scenario_registry(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMockserverLoadScenarioResponse]:
        """
        Removes ALL registered load scenarios, stopping any that are running. Idempotent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMockserverLoadScenarioResponse]
            load scenario registry cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverLoadScenarioResponse,
                    parse_obj_as(
                        type_=DeleteMockserverLoadScenarioResponse,
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

    async def retrieve_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LoadScenarioListEntry]:
        """
        Returns a single registered load scenario (definition + state + live/terminal status). 404 if not registered.

        Parameters
        ----------
        name : str
            the registered load scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoadScenarioListEntry]
            load scenario returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoadScenarioListEntry,
                    parse_obj_as(
                        type_=LoadScenarioListEntry,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def remove_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMockserverLoadScenarioNameResponse]:
        """
        Removes a single load scenario from the registry, stopping it first if it is running.

        Parameters
        ----------
        name : str
            the registered load scenario name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMockserverLoadScenarioNameResponse]
            load scenario removed (or absent)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverLoadScenarioNameResponse,
                    parse_obj_as(
                        type_=DeleteMockserverLoadScenarioNameResponse,
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

    async def end_of_run_summary_report_for_a_load_scenario_run(
        self,
        name: str,
        *,
        format: typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LoadScenarioReport]:
        """
        Returns an end-of-run summary report derived from the run's status snapshot — the live snapshot while running, or the retained terminal snapshot once finished. The default JSON form carries counts, latency percentiles, the threshold verdict and per-threshold results. With ?format=junit the same data is rendered as a JUnit-XML <testsuite> (one <testcase> per threshold, a <failure> per breach, plus a "run completed" testcase) so CI consumers render per-threshold pass/fail. 404 if the scenario never ran.

        Parameters
        ----------
        name : str
            the load scenario name

        format : typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat]
            report format. Omit (or any value other than "junit") for the JSON report; "junit" returns a JUnit-XML <testsuite> (Content-Type application/xml) so a load run becomes a first-class CI test artifact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LoadScenarioReport]
            report returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/loadScenario/{encode_path_param(name)}/report",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LoadScenarioReport,
                    parse_obj_as(
                        type_=LoadScenarioReport,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def seed_a_load_scenario_from_an_open_api_specification(
        self,
        *,
        name: str,
        spec_url_or_payload: str,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverLoadScenarioGenerateFromOpenApiResponse]:
        """
        Generates an editable load scenario from an OpenAPI spec and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. One step is produced per OpenAPI operation (in a stable path-then-method order), each with the operation's method and server-prefixed path, a representative request-body example, and a Content-Type header. The spec is accepted identically to PUT /mockserver/openapi/expectation — an inline JSON/YAML payload, a URL, or a file/classpath reference. Target precedence for where each request is sent (carried as the request's Host header and secure flag): an explicit "target" wins, else the spec's servers[0] URL, else the request is left path-only for the operator to edit. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.

        Parameters
        ----------
        name : str
            the generated scenario name (the unique registry key)

        spec_url_or_payload : str
            the OpenAPI spec as an inline JSON/YAML payload, a URL, or a file/classpath reference

        target : typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget]
            explicit network target for every generated step (overrides the spec's servers[0])

        profile : typing.Optional[LoadProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverLoadScenarioGenerateFromOpenApiResponse]
            load scenario generated and loaded (registered)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/generateFromOpenAPI",
            method="PUT",
            json={
                "name": name,
                "specUrlOrPayload": spec_url_or_payload,
                "target": convert_and_respect_annotation_metadata(
                    object_=target,
                    annotation=PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
                    direction="write",
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
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
                    PutMockserverLoadScenarioGenerateFromOpenApiResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioGenerateFromOpenApiResponse,
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

    async def seed_a_load_scenario_from_recorded_proxy_traffic(
        self,
        *,
        name: str,
        mode: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestMode] = OMIT,
        request_filter: typing.Optional[HttpRequest] = OMIT,
        max_steps: typing.Optional[int] = OMIT,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverLoadScenarioGenerateFromRecordingResponse]:
        """
        Generates an editable load scenario from traffic previously recorded by MockServer in proxy/recording mode (the requests held by the event log) and loads (registers) it into the registry under "name" in the LOADED state — exactly like PUT /mockserver/loadScenario, it generates no traffic and is allowed even when loadGenerationEnabled is false. Two modes control how recorded requests become steps. VERBATIM (the default) emits one step per recorded request, in recorded order, preserving the concrete path, body and headers — with an optional "maxSteps" cap. TEMPLATIZED deduplicates recorded requests by (method, templatised-path) — id-shaped path segments such as /orders/123 collapse to /orders/{id} — keeping one representative example per unique route, ordered by descending hit frequency (most-hit routes first); each step's "weight" is set to its route's observed hit count and the scenario uses "stepSelection": "WEIGHTED" so replay reproduces the recorded traffic mix. An optional "requestFilter" (an HttpRequest matcher) selects which recorded requests to include; absent means all recorded requests. An optional "target" is applied to every step (overriding each recorded request's own Host/secure routing); absent leaves each recorded request's routing untouched. When no "profile" is supplied a conservative default is applied (one short constant-VU stage) so the scenario is immediately runnable yet safe — the operator edits it before scaling up. The generated scenario is returned so a client/UI can show and edit it before triggering a run.

        Parameters
        ----------
        name : str
            the generated scenario name (the unique registry key)

        mode : typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestMode]
            VERBATIM = one step per recorded request; TEMPLATIZED = one step per unique (method, templatised-path) route, ordered by descending frequency

        request_filter : typing.Optional[HttpRequest]

        max_steps : typing.Optional[int]
            optional cap on the number of VERBATIM steps (keeps the first N recorded requests)

        target : typing.Optional[PutMockserverLoadScenarioGenerateFromRecordingRequestTarget]
            explicit network target applied to every generated step (overrides each recorded request's own Host/secure routing)

        profile : typing.Optional[LoadProfile]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverLoadScenarioGenerateFromRecordingResponse]
            load scenario generated and loaded (registered)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/generateFromRecording",
            method="PUT",
            json={
                "name": name,
                "mode": mode,
                "requestFilter": convert_and_respect_annotation_metadata(
                    object_=request_filter, annotation=HttpRequest, direction="write"
                ),
                "maxSteps": max_steps,
                "target": convert_and_respect_annotation_metadata(
                    object_=target,
                    annotation=PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
                    direction="write",
                ),
                "profile": convert_and_respect_annotation_metadata(
                    object_=profile, annotation=LoadProfile, direction="write"
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
                    PutMockserverLoadScenarioGenerateFromRecordingResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioGenerateFromRecordingResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ConflictErrorBody,
                        parse_obj_as(
                            type_=ConflictErrorBody,
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

    async def trigger_registered_load_scenario_s_to_run(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverLoadScenarioStartResponse]:
        """
        Triggers one or more registered load scenarios to start running concurrently. Each gets a fresh run id and honours its own startDelayMillis (a positive delay → the scenario is PENDING until the delay elapses, then RUNNING). Requires loadGenerationEnabled=true (else 403). 404 if a name is not registered. Rejected with 400 if it would exceed loadGenerationMaxConcurrentScenarios (default 10). Re-triggering an already-active name replaces that run.

        Parameters
        ----------
        names : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverLoadScenarioStartResponse]
            load scenario(s) triggered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/start",
            method="PUT",
            json={
                "names": names,
                "name": name,
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
                    PutMockserverLoadScenarioStartResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioStartResponse,
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

    async def stop_running_load_scenario_s(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        all_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverLoadScenarioStopResponse]:
        """
        Stops one or more running load scenarios. Body is {"names":[...]}, {"all":true}, or an empty body (stop all running). Stopped scenarios stay registered (state STOPPED) and can be re-triggered.

        Parameters
        ----------
        names : typing.Optional[typing.Sequence[str]]

        all_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverLoadScenarioStopResponse]
            load scenario(s) stopped
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/loadScenario/stop",
            method="PUT",
            json={
                "names": names,
                "all": all_,
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
                    PutMockserverLoadScenarioStopResponse,
                    parse_obj_as(
                        type_=PutMockserverLoadScenarioStopResponse,
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
