

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.chaos_experiment import ChaosExperiment
from ..types.chaos_experiment_stages_item import ChaosExperimentStagesItem
from ..types.preemption_status import PreemptionStatus
from .raw_client import AsyncRawChaosClient, RawChaosClient
from .types.delete_mockserver_chaos_experiment_profiles_name_response import (
    DeleteMockserverChaosExperimentProfilesNameResponse,
)
from .types.delete_mockserver_chaos_experiment_response import DeleteMockserverChaosExperimentResponse
from .types.delete_mockserver_preemption_response import DeleteMockserverPreemptionResponse
from .types.get_mockserver_chaos_experiment_history_response import GetMockserverChaosExperimentHistoryResponse
from .types.get_mockserver_chaos_experiment_profiles_response import GetMockserverChaosExperimentProfilesResponse
from .types.get_mockserver_chaos_experiment_response import GetMockserverChaosExperimentResponse
from .types.post_mockserver_chaos_experiment_apply_name_response import PostMockserverChaosExperimentApplyNameResponse
from .types.preemption_request_mode import PreemptionRequestMode
from .types.put_mockserver_chaos_experiment_profiles_name_response import (
    PutMockserverChaosExperimentProfilesNameResponse,
)
from .types.put_mockserver_chaos_experiment_request_stages_item import PutMockserverChaosExperimentRequestStagesItem
from .types.put_mockserver_chaos_experiment_response import PutMockserverChaosExperimentResponse


OMIT = typing.cast(typing.Any, ...)


class ChaosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChaosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChaosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChaosClient
        """
        return self._raw_client

    def list_registered_service_scoped_http_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered service-scoped chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered service-scoped chaos returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.list_registered_service_scoped_http_chaos()
        """
        _response = self._raw_client.list_registered_service_scoped_http_chaos(request_options=request_options)
        return _response.data

    def register_remove_or_clear_service_scoped_http_chaos(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers an HTTP chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all service-scoped chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        host : typing.Optional[str]
            downstream host the chaos profile applies to (mutually exclusive with clear)

        chaos : typing.Optional[typing.Dict[str, typing.Any]]
            HTTP chaos profile (fault types, probabilities, error status, etc.); omit (or set remove:true) to remove the host's profile

        remove : typing.Optional[bool]
            when true, removes the named host's chaos profile

        clear : typing.Optional[bool]
            when true, clears all service-scoped chaos (mutually exclusive with host)

        ttl_millis : typing.Optional[int]
            optional time-to-live in milliseconds after which the registration auto-reverts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.register_remove_or_clear_service_scoped_http_chaos(
            host="payments.internal:8443",
            chaos={
                "errorStatus": 503,
                "errorProbability": 0.3,
                "latency": {"timeUnit": "MILLISECONDS", "value": 200},
            },
            ttl_millis=60000,
        )
        """
        _response = self._raw_client.register_remove_or_clear_service_scoped_http_chaos(
            host=host, chaos=chaos, remove=remove, clear=clear, ttl_millis=ttl_millis, request_options=request_options
        )
        return _response.data

    def update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered service-scoped chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        host : typing.Optional[str]
            downstream host the chaos profile applies to (mutually exclusive with clear)

        chaos : typing.Optional[typing.Dict[str, typing.Any]]
            HTTP chaos profile (fault types, probabilities, error status, etc.); omit (or set remove:true) to remove the host's profile

        remove : typing.Optional[bool]
            when true, removes the named host's chaos profile

        clear : typing.Optional[bool]
            when true, clears all service-scoped chaos (mutually exclusive with host)

        ttl_millis : typing.Optional[int]
            optional time-to-live in milliseconds after which the registration auto-reverts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
            host="payments.internal:8443",
            chaos={"errorProbability": 0.5},
        )
        """
        _response = self._raw_client.update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
            host=host, chaos=chaos, remove=remove, clear=clear, ttl_millis=ttl_millis, request_options=request_options
        )
        return _response.data

    def list_registered_tcp_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered TCP chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered TCP chaos returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.list_registered_tcp_chaos()
        """
        _response = self._raw_client.list_registered_tcp_chaos(request_options=request_options)
        return _response.data

    def register_remove_or_clear_tcp_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers a TCP-layer chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all TCP chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.register_remove_or_clear_tcp_chaos(
            request={
                "host": "slow-api.example.com",
                "chaos": {"bandwidthBytesPerSec": 1024, "latencyMs": 50},
                "ttlMillis": 30000,
            },
        )
        """
        _response = self._raw_client.register_remove_or_clear_tcp_chaos(
            request=request, request_options=request_options
        )
        return _response.data

    def update_an_existing_tcp_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered TCP chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.update_an_existing_tcp_chaos_profile_json_merge_patch(
            request={"host": "slow-api.example.com", "chaos": {"slicerChunkSize": 256}},
        )
        """
        _response = self._raw_client.update_an_existing_tcp_chaos_profile_json_merge_patch(
            request=request, request_options=request_options
        )
        return _response.data

    def list_registered_g_rpc_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered gRPC chaos profiles keyed by service, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered gRPC chaos returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.list_registered_g_rpc_chaos()
        """
        _response = self._raw_client.list_registered_g_rpc_chaos(request_options=request_options)
        return _response.data

    def register_remove_or_clear_g_rpc_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers a gRPC chaos / fault-injection profile for a service, removes a service's profile, or clears all gRPC chaos. Supply a 'service' with a 'chaos' object to register, 'service' with 'remove':true (or no 'chaos') to remove a single service, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.register_remove_or_clear_g_rpc_chaos(
            request={
                "service": "com.example.OrderService",
                "chaos": {
                    "errorStatusCode": "UNAVAILABLE",
                    "errorMessage": "service maintenance",
                    "errorProbability": 0.5,
                    "latencyMs": 100,
                },
            },
        )
        """
        _response = self._raw_client.register_remove_or_clear_g_rpc_chaos(
            request=request, request_options=request_options
        )
        return _response.data

    def update_an_existing_g_rpc_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered gRPC chaos profile for a service, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.update_an_existing_g_rpc_chaos_profile_json_merge_patch(
            request={
                "service": "com.example.OrderService",
                "chaos": {"errorProbability": 0.8},
            },
        )
        """
        _response = self._raw_client.update_an_existing_g_rpc_chaos_profile_json_merge_patch(
            request=request, request_options=request_options
        )
        return _response.data

    def get_the_status_of_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentResponse:
        """
        Returns the current experiment status including name, running status (running/completed/halted_by_auto_halt/stopped), current stage index, total stages, elapsed/remaining time, loop iteration count, and the full experiment definition. Returns null/empty when no experiment is or was recently active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentResponse
            experiment status (or empty if none active)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.get_the_status_of_the_current_chaos_experiment()
        """
        _response = self._raw_client.get_the_status_of_the_current_chaos_experiment(request_options=request_options)
        return _response.data

    def start_a_scheduled_multi_stage_chaos_experiment(
        self,
        *,
        name: str,
        stages: typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverChaosExperimentResponse:
        """
        Starts a chaos experiment with an ordered sequence of stages, each applying service-scoped chaos profiles to one or more hosts for a specified duration. Stages progress automatically. Only one experiment may be active at a time; starting a new one stops the previous one. Safety limits: max 50 stages, max 24h per stage duration, auto-halt integration.

        Parameters
        ----------
        name : str
            human-readable experiment name

        stages : typing.Sequence[PutMockserverChaosExperimentRequestStagesItem]
            ordered sequence of stages

        loop : typing.Optional[bool]
            whether to loop back to stage 0 after the last stage completes (default false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverChaosExperimentResponse
            experiment started

        Examples
        --------
        from fern.chaos import PutMockserverChaosExperimentRequestStagesItem

        from fern import FernApi, HttpChaosProfile

        client = FernApi()
        client.chaos.start_a_scheduled_multi_stage_chaos_experiment(
            name="gradual-degradation",
            stages=[
                PutMockserverChaosExperimentRequestStagesItem(
                    duration_millis=10000,
                    profiles={
                        "api.example.com": HttpChaosProfile(
                            error_status=500,
                            error_probability=0.1,
                        )
                    },
                ),
                PutMockserverChaosExperimentRequestStagesItem(
                    duration_millis=10000,
                    profiles={
                        "api.example.com": HttpChaosProfile(
                            error_status=500,
                            error_probability=0.5,
                        )
                    },
                ),
            ],
        )
        """
        _response = self._raw_client.start_a_scheduled_multi_stage_chaos_experiment(
            name=name, stages=stages, loop=loop, request_options=request_options
        )
        return _response.data

    def stop_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverChaosExperimentResponse:
        """
        Stops the current experiment and clears all chaos from the service registry. Idempotent — no-op if no experiment is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverChaosExperimentResponse
            experiment stopped (or no experiment was running)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.stop_the_current_chaos_experiment()
        """
        _response = self._raw_client.stop_the_current_chaos_experiment(request_options=request_options)
        return _response.data

    def retrieve_the_current_preemption_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreemptionStatus:
        """
        Returns the current cordon/drain status: state (inactive / draining / drained), the number of in-flight requests, the remaining drain window in milliseconds and the active signalling mode.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreemptionStatus
            preemption status returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.retrieve_the_current_preemption_status()
        """
        _response = self._raw_client.retrieve_the_current_preemption_status(request_options=request_options)
        return _response.data

    def cordon_and_drain_the_server_preemption_simulation(
        self,
        *,
        mode: typing.Optional[PreemptionRequestMode] = OMIT,
        drain_millis: typing.Optional[int] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        last_stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreemptionStatus:
        """
        Simulates a connection-lifecycle preemption (e.g. a Kubernetes node drain or spot reclamation). While cordoned, new exchanges are signalled to back off — by a 503 + Connection: close, an HTTP/2 GOAWAY frame, or both — while in-flight requests are allowed to drain. The simulation is server-scoped and does not stop the JVM. An empty body uses defaults (mode "both", drainMillis from stopDrainMillis, no TTL). drainMillis and ttlMillis are clamped to preemptionSimulationMaxDrainMillis.

        Parameters
        ----------
        mode : typing.Optional[PreemptionRequestMode]
            how draining is signalled: reject503 = 503 + Connection: close; goaway = HTTP/2 GOAWAY frame; both = both

        drain_millis : typing.Optional[int]
            how long in-flight requests are allowed to drain; defaults to the stopDrainMillis property, clamped to preemptionSimulationMaxDrainMillis

        ttl_millis : typing.Optional[int]
            auto-uncordon after this many milliseconds (dead-man's switch); 0 (default) means no auto-uncordon

        last_stream_id : typing.Optional[int]
            HTTP/2 GOAWAY last_stream_id to advertise; -1 (default) lets the server choose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreemptionStatus
            preemption simulation started or replaced

        Examples
        --------
        from fern.chaos import PreemptionRequestMode

        from fern import FernApi

        client = FernApi()
        client.chaos.cordon_and_drain_the_server_preemption_simulation(
            mode=PreemptionRequestMode.BOTH,
            drain_millis=10000,
            ttl_millis=60000,
            last_stream_id=3,
        )
        """
        _response = self._raw_client.cordon_and_drain_the_server_preemption_simulation(
            mode=mode,
            drain_millis=drain_millis,
            ttl_millis=ttl_millis,
            last_stream_id=last_stream_id,
            request_options=request_options,
        )
        return _response.data

    def uncordon_the_server_clear_preemption(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverPreemptionResponse:
        """
        Explicitly clears any active preemption simulation, returning the server to normal operation. Idempotent — returns 200 whether or not a simulation was active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverPreemptionResponse
            preemption cleared

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.uncordon_the_server_clear_preemption()
        """
        _response = self._raw_client.uncordon_the_server_clear_preemption(request_options=request_options)
        return _response.data

    def list_saved_chaos_profile_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentProfilesResponse:
        """
        returns the names of all saved chaos experiment profiles, sorted ascending

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentProfilesResponse
            saved profile names returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.list_saved_chaos_profile_names()
        """
        _response = self._raw_client.list_saved_chaos_profile_names(request_options=request_options)
        return _response.data

    def retrieve_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChaosExperiment:
        """
        returns the full saved chaos experiment definition stored under the given name

        Parameters
        ----------
        name : str
            the profile name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaosExperiment
            saved profile returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.retrieve_a_saved_chaos_profile(
            name="name",
        )
        """
        _response = self._raw_client.retrieve_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    def save_a_chaos_experiment_profile(
        self,
        name_: str,
        *,
        stages: typing.Sequence[ChaosExperimentStagesItem],
        name: typing.Optional[str] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverChaosExperimentProfilesNameResponse:
        """
        Saves a chaos experiment definition (the same body shape as PUT /mockserver/chaosExperiment) under the given name so it can be applied later with POST /mockserver/chaosExperiment/apply/{name}. The name in the path is authoritative; any name field in the body is ignored. The name must be 1-128 characters of letters, digits, space, dot, underscore or hyphen with no leading/trailing space.

        Parameters
        ----------
        name_ : str
            the profile name to save under

        stages : typing.Sequence[ChaosExperimentStagesItem]
            ordered sequence of stages

        name : typing.Optional[str]
            human-readable experiment name (ignored when saved under a path {name})

        loop : typing.Optional[bool]
            whether to loop back to stage 0 after the last stage completes (default false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverChaosExperimentProfilesNameResponse
            profile saved

        Examples
        --------
        from fern import ChaosExperimentStagesItem, FernApi, HttpChaosProfile

        client = FernApi()
        client.chaos.save_a_chaos_experiment_profile(
            name_="name",
            stages=[
                ChaosExperimentStagesItem(
                    duration_millis=30000,
                    profiles={
                        "payments.svc": HttpChaosProfile(
                            error_status=503,
                            error_probability=0.5,
                        )
                    },
                )
            ],
        )
        """
        _response = self._raw_client.save_a_chaos_experiment_profile(
            name_, stages=stages, name=name, loop=loop, request_options=request_options
        )
        return _response.data

    def delete_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverChaosExperimentProfilesNameResponse:
        """
        Removes the saved chaos profile with the given name. Idempotent — returns 200 with status "deleted" when the profile existed, or "absent" when it did not.

        Parameters
        ----------
        name : str
            the profile name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverChaosExperimentProfilesNameResponse
            deletion processed

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.delete_a_saved_chaos_profile(
            name="name",
        )
        """
        _response = self._raw_client.delete_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    def apply_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMockserverChaosExperimentApplyNameResponse:
        """
        Starts the chaos experiment previously saved under the given name (as if its definition had been sent to PUT /mockserver/chaosExperiment). The request body is ignored.

        Parameters
        ----------
        name : str
            the saved profile name to apply

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMockserverChaosExperimentApplyNameResponse
            saved profile applied (experiment started)

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.apply_a_saved_chaos_profile(
            name="name",
        )
        """
        _response = self._raw_client.apply_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    def retrieve_completed_chaos_experiment_history(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentHistoryResponse:
        """
        Returns the record of chaos experiments that have run, most recent first, bounded by a fixed in-memory history size that is not caller-controllable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentHistoryResponse
            chaos experiment history returned

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.chaos.retrieve_completed_chaos_experiment_history()
        """
        _response = self._raw_client.retrieve_completed_chaos_experiment_history(request_options=request_options)
        return _response.data


class AsyncChaosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChaosClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChaosClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChaosClient
        """
        return self._raw_client

    async def list_registered_service_scoped_http_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered service-scoped chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered service-scoped chaos returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.list_registered_service_scoped_http_chaos()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_registered_service_scoped_http_chaos(request_options=request_options)
        return _response.data

    async def register_remove_or_clear_service_scoped_http_chaos(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers an HTTP chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all service-scoped chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        host : typing.Optional[str]
            downstream host the chaos profile applies to (mutually exclusive with clear)

        chaos : typing.Optional[typing.Dict[str, typing.Any]]
            HTTP chaos profile (fault types, probabilities, error status, etc.); omit (or set remove:true) to remove the host's profile

        remove : typing.Optional[bool]
            when true, removes the named host's chaos profile

        clear : typing.Optional[bool]
            when true, clears all service-scoped chaos (mutually exclusive with host)

        ttl_millis : typing.Optional[int]
            optional time-to-live in milliseconds after which the registration auto-reverts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.register_remove_or_clear_service_scoped_http_chaos(
                host="payments.internal:8443",
                chaos={
                    "errorStatus": 503,
                    "errorProbability": 0.3,
                    "latency": {"timeUnit": "MILLISECONDS", "value": 200},
                },
                ttl_millis=60000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_remove_or_clear_service_scoped_http_chaos(
            host=host, chaos=chaos, remove=remove, clear=clear, ttl_millis=ttl_millis, request_options=request_options
        )
        return _response.data

    async def update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered service-scoped chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        host : typing.Optional[str]
            downstream host the chaos profile applies to (mutually exclusive with clear)

        chaos : typing.Optional[typing.Dict[str, typing.Any]]
            HTTP chaos profile (fault types, probabilities, error status, etc.); omit (or set remove:true) to remove the host's profile

        remove : typing.Optional[bool]
            when true, removes the named host's chaos profile

        clear : typing.Optional[bool]
            when true, clears all service-scoped chaos (mutually exclusive with host)

        ttl_millis : typing.Optional[int]
            optional time-to-live in milliseconds after which the registration auto-reverts

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
                host="payments.internal:8443",
                chaos={"errorProbability": 0.5},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
            host=host, chaos=chaos, remove=remove, clear=clear, ttl_millis=ttl_millis, request_options=request_options
        )
        return _response.data

    async def list_registered_tcp_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered TCP chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered TCP chaos returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.list_registered_tcp_chaos()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_registered_tcp_chaos(request_options=request_options)
        return _response.data

    async def register_remove_or_clear_tcp_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers a TCP-layer chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all TCP chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.register_remove_or_clear_tcp_chaos(
                request={
                    "host": "slow-api.example.com",
                    "chaos": {"bandwidthBytesPerSec": 1024, "latencyMs": 50},
                    "ttlMillis": 30000,
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_remove_or_clear_tcp_chaos(
            request=request, request_options=request_options
        )
        return _response.data

    async def update_an_existing_tcp_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered TCP chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.update_an_existing_tcp_chaos_profile_json_merge_patch(
                request={
                    "host": "slow-api.example.com",
                    "chaos": {"slicerChunkSize": 256},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_an_existing_tcp_chaos_profile_json_merge_patch(
            request=request, request_options=request_options
        )
        return _response.data

    async def list_registered_g_rpc_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        returns all registered gRPC chaos profiles keyed by service, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            registered gRPC chaos returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.list_registered_g_rpc_chaos()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_registered_g_rpc_chaos(request_options=request_options)
        return _response.data

    async def register_remove_or_clear_g_rpc_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Registers a gRPC chaos / fault-injection profile for a service, removes a service's profile, or clears all gRPC chaos. Supply a 'service' with a 'chaos' object to register, 'service' with 'remove':true (or no 'chaos') to remove a single service, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos registered, removed, patched or cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.register_remove_or_clear_g_rpc_chaos(
                request={
                    "service": "com.example.OrderService",
                    "chaos": {
                        "errorStatusCode": "UNAVAILABLE",
                        "errorMessage": "service maintenance",
                        "errorProbability": 0.5,
                        "latencyMs": 100,
                    },
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_remove_or_clear_g_rpc_chaos(
            request=request, request_options=request_options
        )
        return _response.data

    async def update_an_existing_g_rpc_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Applies a JSON Merge Patch to an already-registered gRPC chaos profile for a service, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            chaos profile patched

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.update_an_existing_g_rpc_chaos_profile_json_merge_patch(
                request={
                    "service": "com.example.OrderService",
                    "chaos": {"errorProbability": 0.8},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_an_existing_g_rpc_chaos_profile_json_merge_patch(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_the_status_of_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentResponse:
        """
        Returns the current experiment status including name, running status (running/completed/halted_by_auto_halt/stopped), current stage index, total stages, elapsed/remaining time, loop iteration count, and the full experiment definition. Returns null/empty when no experiment is or was recently active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentResponse
            experiment status (or empty if none active)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.get_the_status_of_the_current_chaos_experiment()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_status_of_the_current_chaos_experiment(
            request_options=request_options
        )
        return _response.data

    async def start_a_scheduled_multi_stage_chaos_experiment(
        self,
        *,
        name: str,
        stages: typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverChaosExperimentResponse:
        """
        Starts a chaos experiment with an ordered sequence of stages, each applying service-scoped chaos profiles to one or more hosts for a specified duration. Stages progress automatically. Only one experiment may be active at a time; starting a new one stops the previous one. Safety limits: max 50 stages, max 24h per stage duration, auto-halt integration.

        Parameters
        ----------
        name : str
            human-readable experiment name

        stages : typing.Sequence[PutMockserverChaosExperimentRequestStagesItem]
            ordered sequence of stages

        loop : typing.Optional[bool]
            whether to loop back to stage 0 after the last stage completes (default false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverChaosExperimentResponse
            experiment started

        Examples
        --------
        import asyncio

        from fern.chaos import PutMockserverChaosExperimentRequestStagesItem

        from fern import AsyncFernApi, HttpChaosProfile

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.start_a_scheduled_multi_stage_chaos_experiment(
                name="gradual-degradation",
                stages=[
                    PutMockserverChaosExperimentRequestStagesItem(
                        duration_millis=10000,
                        profiles={
                            "api.example.com": HttpChaosProfile(
                                error_status=500,
                                error_probability=0.1,
                            )
                        },
                    ),
                    PutMockserverChaosExperimentRequestStagesItem(
                        duration_millis=10000,
                        profiles={
                            "api.example.com": HttpChaosProfile(
                                error_status=500,
                                error_probability=0.5,
                            )
                        },
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_a_scheduled_multi_stage_chaos_experiment(
            name=name, stages=stages, loop=loop, request_options=request_options
        )
        return _response.data

    async def stop_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverChaosExperimentResponse:
        """
        Stops the current experiment and clears all chaos from the service registry. Idempotent — no-op if no experiment is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverChaosExperimentResponse
            experiment stopped (or no experiment was running)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.stop_the_current_chaos_experiment()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_the_current_chaos_experiment(request_options=request_options)
        return _response.data

    async def retrieve_the_current_preemption_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreemptionStatus:
        """
        Returns the current cordon/drain status: state (inactive / draining / drained), the number of in-flight requests, the remaining drain window in milliseconds and the active signalling mode.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreemptionStatus
            preemption status returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.retrieve_the_current_preemption_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_the_current_preemption_status(request_options=request_options)
        return _response.data

    async def cordon_and_drain_the_server_preemption_simulation(
        self,
        *,
        mode: typing.Optional[PreemptionRequestMode] = OMIT,
        drain_millis: typing.Optional[int] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        last_stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreemptionStatus:
        """
        Simulates a connection-lifecycle preemption (e.g. a Kubernetes node drain or spot reclamation). While cordoned, new exchanges are signalled to back off — by a 503 + Connection: close, an HTTP/2 GOAWAY frame, or both — while in-flight requests are allowed to drain. The simulation is server-scoped and does not stop the JVM. An empty body uses defaults (mode "both", drainMillis from stopDrainMillis, no TTL). drainMillis and ttlMillis are clamped to preemptionSimulationMaxDrainMillis.

        Parameters
        ----------
        mode : typing.Optional[PreemptionRequestMode]
            how draining is signalled: reject503 = 503 + Connection: close; goaway = HTTP/2 GOAWAY frame; both = both

        drain_millis : typing.Optional[int]
            how long in-flight requests are allowed to drain; defaults to the stopDrainMillis property, clamped to preemptionSimulationMaxDrainMillis

        ttl_millis : typing.Optional[int]
            auto-uncordon after this many milliseconds (dead-man's switch); 0 (default) means no auto-uncordon

        last_stream_id : typing.Optional[int]
            HTTP/2 GOAWAY last_stream_id to advertise; -1 (default) lets the server choose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreemptionStatus
            preemption simulation started or replaced

        Examples
        --------
        import asyncio

        from fern.chaos import PreemptionRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.cordon_and_drain_the_server_preemption_simulation(
                mode=PreemptionRequestMode.BOTH,
                drain_millis=10000,
                ttl_millis=60000,
                last_stream_id=3,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cordon_and_drain_the_server_preemption_simulation(
            mode=mode,
            drain_millis=drain_millis,
            ttl_millis=ttl_millis,
            last_stream_id=last_stream_id,
            request_options=request_options,
        )
        return _response.data

    async def uncordon_the_server_clear_preemption(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverPreemptionResponse:
        """
        Explicitly clears any active preemption simulation, returning the server to normal operation. Idempotent — returns 200 whether or not a simulation was active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverPreemptionResponse
            preemption cleared

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.uncordon_the_server_clear_preemption()


        asyncio.run(main())
        """
        _response = await self._raw_client.uncordon_the_server_clear_preemption(request_options=request_options)
        return _response.data

    async def list_saved_chaos_profile_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentProfilesResponse:
        """
        returns the names of all saved chaos experiment profiles, sorted ascending

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentProfilesResponse
            saved profile names returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.list_saved_chaos_profile_names()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_saved_chaos_profile_names(request_options=request_options)
        return _response.data

    async def retrieve_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChaosExperiment:
        """
        returns the full saved chaos experiment definition stored under the given name

        Parameters
        ----------
        name : str
            the profile name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChaosExperiment
            saved profile returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.retrieve_a_saved_chaos_profile(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    async def save_a_chaos_experiment_profile(
        self,
        name_: str,
        *,
        stages: typing.Sequence[ChaosExperimentStagesItem],
        name: typing.Optional[str] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutMockserverChaosExperimentProfilesNameResponse:
        """
        Saves a chaos experiment definition (the same body shape as PUT /mockserver/chaosExperiment) under the given name so it can be applied later with POST /mockserver/chaosExperiment/apply/{name}. The name in the path is authoritative; any name field in the body is ignored. The name must be 1-128 characters of letters, digits, space, dot, underscore or hyphen with no leading/trailing space.

        Parameters
        ----------
        name_ : str
            the profile name to save under

        stages : typing.Sequence[ChaosExperimentStagesItem]
            ordered sequence of stages

        name : typing.Optional[str]
            human-readable experiment name (ignored when saved under a path {name})

        loop : typing.Optional[bool]
            whether to loop back to stage 0 after the last stage completes (default false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutMockserverChaosExperimentProfilesNameResponse
            profile saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChaosExperimentStagesItem, HttpChaosProfile

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.save_a_chaos_experiment_profile(
                name_="name",
                stages=[
                    ChaosExperimentStagesItem(
                        duration_millis=30000,
                        profiles={
                            "payments.svc": HttpChaosProfile(
                                error_status=503,
                                error_probability=0.5,
                            )
                        },
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_a_chaos_experiment_profile(
            name_, stages=stages, name=name, loop=loop, request_options=request_options
        )
        return _response.data

    async def delete_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteMockserverChaosExperimentProfilesNameResponse:
        """
        Removes the saved chaos profile with the given name. Idempotent — returns 200 with status "deleted" when the profile existed, or "absent" when it did not.

        Parameters
        ----------
        name : str
            the profile name to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteMockserverChaosExperimentProfilesNameResponse
            deletion processed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.delete_a_saved_chaos_profile(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    async def apply_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostMockserverChaosExperimentApplyNameResponse:
        """
        Starts the chaos experiment previously saved under the given name (as if its definition had been sent to PUT /mockserver/chaosExperiment). The request body is ignored.

        Parameters
        ----------
        name : str
            the saved profile name to apply

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostMockserverChaosExperimentApplyNameResponse
            saved profile applied (experiment started)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.apply_a_saved_chaos_profile(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply_a_saved_chaos_profile(name, request_options=request_options)
        return _response.data

    async def retrieve_completed_chaos_experiment_history(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMockserverChaosExperimentHistoryResponse:
        """
        Returns the record of chaos experiments that have run, most recent first, bounded by a fixed in-memory history size that is not caller-controllable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMockserverChaosExperimentHistoryResponse
            chaos experiment history returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.chaos.retrieve_completed_chaos_experiment_history()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_completed_chaos_experiment_history(request_options=request_options)
        return _response.data
