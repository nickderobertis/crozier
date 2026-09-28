

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawLoadgenClient, RawLoadgenClient
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


OMIT = typing.cast(typing.Any, ...)


class LoadgenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoadgenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoadgenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoadgenClient
        """
        return self._raw_client

    def list_all_registered_load_scenarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverLoadScenarioResponse:
        """
        Lists every registered load scenario with its lifecycle state (LOADED / PENDING / RUNNING / COMPLETED / STOPPED), startDelayMillis, full definition, and — when active or recently run — the live status fields (stage, virtual users, request counts, latency percentiles, run id, timestamps).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverLoadScenarioResponse
            registered load scenarios listed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.list_all_registered_load_scenarios()
        """
        _response = self._raw_client.list_all_registered_load_scenarios(request_options=request_options)
        return _response.data

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
    ) -> PutMockserverLoadScenarioResponse:
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
        PutMockserverLoadScenarioResponse
            load scenario loaded (registered)

        Examples
        --------
        from fern import (
            FernApi,
            HttpRequest,
            KeyToMultiValueZeroItem,
            LoadProfile,
            LoadScenarioTemplateType,
            LoadStage,
            LoadStageType,
            LoadStep,
            LoadStepThinkTime,
            RampCurve,
            SocketAddress,
            SocketAddressScheme,
        )

        client = FernApi()
        client.loadgen.load_register_a_load_scenario_into_the_registry(
            name="checkout-load",
            template_type=LoadScenarioTemplateType.VELOCITY,
            max_requests=5000,
            start_delay_millis=0,
            profile=LoadProfile(
                stages=[
                    LoadStage(
                        type=LoadStageType.VU,
                        duration_millis=30000,
                        curve=RampCurve.LINEAR,
                        start_vus=1,
                        end_vus=10,
                    ),
                    LoadStage(
                        type=LoadStageType.VU,
                        duration_millis=60000,
                        vus=10,
                    ),
                ],
            ),
            steps=[
                LoadStep(
                    request=HttpRequest(
                        method="GET",
                        path="/api/item/$iteration.index",
                        headers=[KeyToMultiValueZeroItem()],
                        socket_address=SocketAddress(
                            host="target.svc",
                            port=8080,
                            scheme=SocketAddressScheme.HTTP,
                        ),
                    ),
                    think_time=LoadStepThinkTime(
                        time_unit="MILLISECONDS",
                        value=20,
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.load_register_a_load_scenario_into_the_registry(
            name=name,
            profile=profile,
            steps=steps,
            template_type=template_type,
            max_requests=max_requests,
            start_delay_millis=start_delay_millis,
            labels=labels,
            thresholds=thresholds,
            abort_on_fail=abort_on_fail,
            abort_grace_millis=abort_grace_millis,
            pacing=pacing,
            feeder=feeder,
            step_selection=step_selection,
            request_options=request_options,
        )
        return _response.data

    def clear_the_load_scenario_registry(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverLoadScenarioResponse:
        """
        Removes ALL registered load scenarios, stopping any that are running. Idempotent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverLoadScenarioResponse
            load scenario registry cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.clear_the_load_scenario_registry()
        """
        _response = self._raw_client.clear_the_load_scenario_registry(request_options=request_options)
        return _response.data

    def retrieve_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoadScenarioListEntry:
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
        LoadScenarioListEntry
            load scenario returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.retrieve_one_registered_load_scenario(
            name="name",
        )
        """
        _response = self._raw_client.retrieve_one_registered_load_scenario(name, request_options=request_options)
        return _response.data

    def remove_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverLoadScenarioNameResponse:
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
        DeleteMockserverLoadScenarioNameResponse
            load scenario removed (or absent)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.remove_one_registered_load_scenario(
            name="name",
        )
        """
        _response = self._raw_client.remove_one_registered_load_scenario(name, request_options=request_options)
        return _response.data

    def end_of_run_summary_report_for_a_load_scenario_run(
        self,
        name: str,
        *,
        format: typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoadScenarioReport:
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
        LoadScenarioReport
            report returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.end_of_run_summary_report_for_a_load_scenario_run(
            name="name",
        )
        """
        _response = self._raw_client.end_of_run_summary_report_for_a_load_scenario_run(
            name, format=format, request_options=request_options
        )
        return _response.data

    def seed_a_load_scenario_from_an_open_api_specification(
        self,
        *,
        name: str,
        spec_url_or_payload: str,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioGenerateFromOpenApiResponse:
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
        PutMockserverLoadScenarioGenerateFromOpenApiResponse
            load scenario generated and loaded (registered)

        Examples
        --------
        from fern.loadgen import (
            PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
            PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme,
        )

        from fern import FernApi

        client = FernApi()
        client.loadgen.seed_a_load_scenario_from_an_open_api_specification(
            name="petstore-load",
            spec_url_or_payload='openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        "200":\n          description: a list of pets',
            target=PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget(
                host="petstore.svc",
                port=8080,
                scheme=PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme.HTTP,
            ),
        )
        """
        _response = self._raw_client.seed_a_load_scenario_from_an_open_api_specification(
            name=name,
            spec_url_or_payload=spec_url_or_payload,
            target=target,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PutMockserverLoadScenarioGenerateFromRecordingResponse:
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
        PutMockserverLoadScenarioGenerateFromRecordingResponse
            load scenario generated and loaded (registered)

        Examples
        --------
        from fern.loadgen import (
            PutMockserverLoadScenarioGenerateFromRecordingRequestMode,
            PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
            PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme,
        )

        from fern import FernApi

        client = FernApi()
        client.loadgen.seed_a_load_scenario_from_recorded_proxy_traffic(
            name="replay-prod-traffic",
            mode=PutMockserverLoadScenarioGenerateFromRecordingRequestMode.TEMPLATIZED,
            target=PutMockserverLoadScenarioGenerateFromRecordingRequestTarget(
                host="staging.svc",
                port=8080,
                scheme=PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme.HTTP,
            ),
        )
        """
        _response = self._raw_client.seed_a_load_scenario_from_recorded_proxy_traffic(
            name=name,
            mode=mode,
            request_filter=request_filter,
            max_steps=max_steps,
            target=target,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

    def trigger_registered_load_scenario_s_to_run(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioStartResponse:
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
        PutMockserverLoadScenarioStartResponse
            load scenario(s) triggered

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.trigger_registered_load_scenario_s_to_run(
            names=["checkout-load", "background-poller"],
        )
        """
        _response = self._raw_client.trigger_registered_load_scenario_s_to_run(
            names=names, name=name, request_options=request_options
        )
        return _response.data

    def stop_running_load_scenario_s(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        all_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioStopResponse:
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
        PutMockserverLoadScenarioStopResponse
            load scenario(s) stopped

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.loadgen.stop_running_load_scenario_s(
            names=["checkout-load"],
        )
        """
        _response = self._raw_client.stop_running_load_scenario_s(
            names=names, all_=all_, request_options=request_options
        )
        return _response.data


class AsyncLoadgenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoadgenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoadgenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoadgenClient
        """
        return self._raw_client

    async def list_all_registered_load_scenarios(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverLoadScenarioResponse:
        """
        Lists every registered load scenario with its lifecycle state (LOADED / PENDING / RUNNING / COMPLETED / STOPPED), startDelayMillis, full definition, and — when active or recently run — the live status fields (stage, virtual users, request counts, latency percentiles, run id, timestamps).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverLoadScenarioResponse
            registered load scenarios listed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.list_all_registered_load_scenarios()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_registered_load_scenarios(request_options=request_options)
        return _response.data

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
    ) -> PutMockserverLoadScenarioResponse:
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
        PutMockserverLoadScenarioResponse
            load scenario loaded (registered)

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            HttpRequest,
            KeyToMultiValueZeroItem,
            LoadProfile,
            LoadScenarioTemplateType,
            LoadStage,
            LoadStageType,
            LoadStep,
            LoadStepThinkTime,
            RampCurve,
            SocketAddress,
            SocketAddressScheme,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.load_register_a_load_scenario_into_the_registry(
                name="checkout-load",
                template_type=LoadScenarioTemplateType.VELOCITY,
                max_requests=5000,
                start_delay_millis=0,
                profile=LoadProfile(
                    stages=[
                        LoadStage(
                            type=LoadStageType.VU,
                            duration_millis=30000,
                            curve=RampCurve.LINEAR,
                            start_vus=1,
                            end_vus=10,
                        ),
                        LoadStage(
                            type=LoadStageType.VU,
                            duration_millis=60000,
                            vus=10,
                        ),
                    ],
                ),
                steps=[
                    LoadStep(
                        request=HttpRequest(
                            method="GET",
                            path="/api/item/$iteration.index",
                            headers=[KeyToMultiValueZeroItem()],
                            socket_address=SocketAddress(
                                host="target.svc",
                                port=8080,
                                scheme=SocketAddressScheme.HTTP,
                            ),
                        ),
                        think_time=LoadStepThinkTime(
                            time_unit="MILLISECONDS",
                            value=20,
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.load_register_a_load_scenario_into_the_registry(
            name=name,
            profile=profile,
            steps=steps,
            template_type=template_type,
            max_requests=max_requests,
            start_delay_millis=start_delay_millis,
            labels=labels,
            thresholds=thresholds,
            abort_on_fail=abort_on_fail,
            abort_grace_millis=abort_grace_millis,
            pacing=pacing,
            feeder=feeder,
            step_selection=step_selection,
            request_options=request_options,
        )
        return _response.data

    async def clear_the_load_scenario_registry(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverLoadScenarioResponse:
        """
        Removes ALL registered load scenarios, stopping any that are running. Idempotent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverLoadScenarioResponse
            load scenario registry cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.clear_the_load_scenario_registry()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_the_load_scenario_registry(request_options=request_options)
        return _response.data

    async def retrieve_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LoadScenarioListEntry:
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
        LoadScenarioListEntry
            load scenario returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.retrieve_one_registered_load_scenario(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_one_registered_load_scenario(name, request_options=request_options)
        return _response.data

    async def remove_one_registered_load_scenario(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverLoadScenarioNameResponse:
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
        DeleteMockserverLoadScenarioNameResponse
            load scenario removed (or absent)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.remove_one_registered_load_scenario(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_one_registered_load_scenario(name, request_options=request_options)
        return _response.data

    async def end_of_run_summary_report_for_a_load_scenario_run(
        self,
        name: str,
        *,
        format: typing.Optional[GetMockserverLoadScenarioNameReportRequestFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LoadScenarioReport:
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
        LoadScenarioReport
            report returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.end_of_run_summary_report_for_a_load_scenario_run(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_of_run_summary_report_for_a_load_scenario_run(
            name, format=format, request_options=request_options
        )
        return _response.data

    async def seed_a_load_scenario_from_an_open_api_specification(
        self,
        *,
        name: str,
        spec_url_or_payload: str,
        target: typing.Optional[PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget] = OMIT,
        profile: typing.Optional[LoadProfile] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioGenerateFromOpenApiResponse:
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
        PutMockserverLoadScenarioGenerateFromOpenApiResponse
            load scenario generated and loaded (registered)

        Examples
        --------
        import asyncio

        from fern.loadgen import (
            PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
            PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.seed_a_load_scenario_from_an_open_api_specification(
                name="petstore-load",
                spec_url_or_payload='openapi: 3.0.0\ninfo:\n  title: Petstore\n  version: 1.0.0\npaths:\n  /pets:\n    get:\n      operationId: listPets\n      responses:\n        "200":\n          description: a list of pets',
                target=PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget(
                    host="petstore.svc",
                    port=8080,
                    scheme=PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme.HTTP,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.seed_a_load_scenario_from_an_open_api_specification(
            name=name,
            spec_url_or_payload=spec_url_or_payload,
            target=target,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PutMockserverLoadScenarioGenerateFromRecordingResponse:
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
        PutMockserverLoadScenarioGenerateFromRecordingResponse
            load scenario generated and loaded (registered)

        Examples
        --------
        import asyncio

        from fern.loadgen import (
            PutMockserverLoadScenarioGenerateFromRecordingRequestMode,
            PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
            PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.seed_a_load_scenario_from_recorded_proxy_traffic(
                name="replay-prod-traffic",
                mode=PutMockserverLoadScenarioGenerateFromRecordingRequestMode.TEMPLATIZED,
                target=PutMockserverLoadScenarioGenerateFromRecordingRequestTarget(
                    host="staging.svc",
                    port=8080,
                    scheme=PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme.HTTP,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.seed_a_load_scenario_from_recorded_proxy_traffic(
            name=name,
            mode=mode,
            request_filter=request_filter,
            max_steps=max_steps,
            target=target,
            profile=profile,
            request_options=request_options,
        )
        return _response.data

    async def trigger_registered_load_scenario_s_to_run(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioStartResponse:
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
        PutMockserverLoadScenarioStartResponse
            load scenario(s) triggered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.trigger_registered_load_scenario_s_to_run(
                names=["checkout-load", "background-poller"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trigger_registered_load_scenario_s_to_run(
            names=names, name=name, request_options=request_options
        )
        return _response.data

    async def stop_running_load_scenario_s(
        self,
        *,
        names: typing.Optional[typing.Sequence[str]] = OMIT,
        all_: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverLoadScenarioStopResponse:
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
        PutMockserverLoadScenarioStopResponse
            load scenario(s) stopped

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.loadgen.stop_running_load_scenario_s(
                names=["checkout-load"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_running_load_scenario_s(
            names=names, all_=all_, request_options=request_options
        )
        return _response.data
