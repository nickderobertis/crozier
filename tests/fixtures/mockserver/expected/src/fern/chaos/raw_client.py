

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
from ..errors.not_found_error import NotFoundError
from ..types.chaos_experiment import ChaosExperiment
from ..types.chaos_experiment_stages_item import ChaosExperimentStagesItem
from ..types.preemption_status import PreemptionStatus
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChaosClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_registered_service_scoped_http_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered service-scoped chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            registered service-scoped chaos returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_remove_or_clear_service_scoped_http_chaos(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
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
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="PUT",
            json={
                "host": host,
                "chaos": chaos,
                "remove": remove,
                "clear": clear,
                "ttlMillis": ttl_millis,
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

    def update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
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
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="PATCH",
            json={
                "host": host,
                "chaos": chaos,
                "remove": remove,
                "clear": clear,
                "ttlMillis": ttl_millis,
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

    def list_registered_tcp_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered TCP chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            registered TCP chaos returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_remove_or_clear_tcp_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Registers a TCP-layer chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all TCP chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="PUT",
            json=request,
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

    def update_an_existing_tcp_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Applies a JSON Merge Patch to an already-registered TCP chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="PATCH",
            json=request,
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

    def list_registered_g_rpc_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered gRPC chaos profiles keyed by service, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            registered gRPC chaos returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def register_remove_or_clear_g_rpc_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Registers a gRPC chaos / fault-injection profile for a service, removes a service's profile, or clears all gRPC chaos. Supply a 'service' with a 'chaos' object to register, 'service' with 'remove':true (or no 'chaos') to remove a single service, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="PUT",
            json=request,
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

    def update_an_existing_g_rpc_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Applies a JSON Merge Patch to an already-registered gRPC chaos profile for a service, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="PATCH",
            json=request,
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

    def get_the_status_of_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverChaosExperimentResponse]:
        """
        Returns the current experiment status including name, running status (running/completed/halted_by_auto_halt/stopped), current stage index, total stages, elapsed/remaining time, loop iteration count, and the full experiment definition. Returns null/empty when no experiment is or was recently active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverChaosExperimentResponse]
            experiment status (or empty if none active)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentResponse,
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

    def start_a_scheduled_multi_stage_chaos_experiment(
        self,
        *,
        name: str,
        stages: typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverChaosExperimentResponse]:
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
        HttpResponse[PutMockserverChaosExperimentResponse]
            experiment started
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="PUT",
            json={
                "name": name,
                "loop": loop,
                "stages": convert_and_respect_annotation_metadata(
                    object_=stages,
                    annotation=typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
                    direction="write",
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
                    PutMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=PutMockserverChaosExperimentResponse,
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

    def stop_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMockserverChaosExperimentResponse]:
        """
        Stops the current experiment and clears all chaos from the service registry. Idempotent — no-op if no experiment is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMockserverChaosExperimentResponse]
            experiment stopped (or no experiment was running)
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=DeleteMockserverChaosExperimentResponse,
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

    def retrieve_the_current_preemption_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PreemptionStatus]:
        """
        Returns the current cordon/drain status: state (inactive / draining / drained), the number of in-flight requests, the remaining drain window in milliseconds and the active signalling mode.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PreemptionStatus]
            preemption status returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreemptionStatus,
                    parse_obj_as(
                        type_=PreemptionStatus,
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

    def cordon_and_drain_the_server_preemption_simulation(
        self,
        *,
        mode: typing.Optional[PreemptionRequestMode] = OMIT,
        drain_millis: typing.Optional[int] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        last_stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PreemptionStatus]:
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
        HttpResponse[PreemptionStatus]
            preemption simulation started or replaced
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="PUT",
            json={
                "mode": mode,
                "drainMillis": drain_millis,
                "ttlMillis": ttl_millis,
                "lastStreamId": last_stream_id,
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
                    PreemptionStatus,
                    parse_obj_as(
                        type_=PreemptionStatus,
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

    def uncordon_the_server_clear_preemption(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMockserverPreemptionResponse]:
        """
        Explicitly clears any active preemption simulation, returning the server to normal operation. Idempotent — returns 200 whether or not a simulation was active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteMockserverPreemptionResponse]
            preemption cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverPreemptionResponse,
                    parse_obj_as(
                        type_=DeleteMockserverPreemptionResponse,
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

    def list_saved_chaos_profile_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverChaosExperimentProfilesResponse]:
        """
        returns the names of all saved chaos experiment profiles, sorted ascending

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverChaosExperimentProfilesResponse]
            saved profile names returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment/profiles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentProfilesResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentProfilesResponse,
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

    def retrieve_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChaosExperiment]:
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
        HttpResponse[ChaosExperiment]
            saved profile returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChaosExperiment,
                    parse_obj_as(
                        type_=ChaosExperiment,
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

    def save_a_chaos_experiment_profile(
        self,
        name_: str,
        *,
        stages: typing.Sequence[ChaosExperimentStagesItem],
        name: typing.Optional[str] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverChaosExperimentProfilesNameResponse]:
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
        HttpResponse[PutMockserverChaosExperimentProfilesNameResponse]
            profile saved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name_)}",
            method="PUT",
            json={
                "name": name,
                "loop": loop,
                "stages": convert_and_respect_annotation_metadata(
                    object_=stages, annotation=typing.Sequence[ChaosExperimentStagesItem], direction="write"
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
                    PutMockserverChaosExperimentProfilesNameResponse,
                    parse_obj_as(
                        type_=PutMockserverChaosExperimentProfilesNameResponse,
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

    def delete_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteMockserverChaosExperimentProfilesNameResponse]:
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
        HttpResponse[DeleteMockserverChaosExperimentProfilesNameResponse]
            deletion processed
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverChaosExperimentProfilesNameResponse,
                    parse_obj_as(
                        type_=DeleteMockserverChaosExperimentProfilesNameResponse,
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

    def apply_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostMockserverChaosExperimentApplyNameResponse]:
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
        HttpResponse[PostMockserverChaosExperimentApplyNameResponse]
            saved profile applied (experiment started)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/apply/{encode_path_param(name)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostMockserverChaosExperimentApplyNameResponse,
                    parse_obj_as(
                        type_=PostMockserverChaosExperimentApplyNameResponse,
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

    def retrieve_completed_chaos_experiment_history(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetMockserverChaosExperimentHistoryResponse]:
        """
        Returns the record of chaos experiments that have run, most recent first, bounded by a fixed in-memory history size that is not caller-controllable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverChaosExperimentHistoryResponse]
            chaos experiment history returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentHistoryResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentHistoryResponse,
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


class AsyncRawChaosClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_registered_service_scoped_http_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered service-scoped chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            registered service-scoped chaos returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_remove_or_clear_service_scoped_http_chaos(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
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
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="PUT",
            json={
                "host": host,
                "chaos": chaos,
                "remove": remove,
                "clear": clear,
                "ttlMillis": ttl_millis,
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

    async def update_an_existing_service_scoped_http_chaos_profile_json_merge_patch(
        self,
        *,
        host: typing.Optional[str] = OMIT,
        chaos: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        remove: typing.Optional[bool] = OMIT,
        clear: typing.Optional[bool] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
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
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/serviceChaos",
            method="PATCH",
            json={
                "host": host,
                "chaos": chaos,
                "remove": remove,
                "clear": clear,
                "ttlMillis": ttl_millis,
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

    async def list_registered_tcp_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered TCP chaos profiles keyed by host, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            registered TCP chaos returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_remove_or_clear_tcp_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Registers a TCP-layer chaos / fault-injection profile for a downstream host, removes a host's profile, or clears all TCP chaos. Supply a 'host' with a 'chaos' object to register, 'host' with 'remove':true (or no 'chaos') to remove a single host, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="PUT",
            json=request,
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

    async def update_an_existing_tcp_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Applies a JSON Merge Patch to an already-registered TCP chaos profile for a host, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/tcpChaos",
            method="PATCH",
            json=request,
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

    async def list_registered_g_rpc_chaos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        returns all registered gRPC chaos profiles keyed by service, plus any remaining time-to-live

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            registered gRPC chaos returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="GET",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def register_remove_or_clear_g_rpc_chaos(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Registers a gRPC chaos / fault-injection profile for a service, removes a service's profile, or clears all gRPC chaos. Supply a 'service' with a 'chaos' object to register, 'service' with 'remove':true (or no 'chaos') to remove a single service, or 'clear':true to clear all.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos registered, removed, patched or cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="PUT",
            json=request,
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

    async def update_an_existing_g_rpc_chaos_profile_json_merge_patch(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Applies a JSON Merge Patch to an already-registered gRPC chaos profile for a service, updating only the supplied fields and leaving the rest unchanged.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            chaos profile patched
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/grpcChaos",
            method="PATCH",
            json=request,
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

    async def get_the_status_of_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverChaosExperimentResponse]:
        """
        Returns the current experiment status including name, running status (running/completed/halted_by_auto_halt/stopped), current stage index, total stages, elapsed/remaining time, loop iteration count, and the full experiment definition. Returns null/empty when no experiment is or was recently active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverChaosExperimentResponse]
            experiment status (or empty if none active)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentResponse,
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

    async def start_a_scheduled_multi_stage_chaos_experiment(
        self,
        *,
        name: str,
        stages: typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverChaosExperimentResponse]:
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
        AsyncHttpResponse[PutMockserverChaosExperimentResponse]
            experiment started
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="PUT",
            json={
                "name": name,
                "loop": loop,
                "stages": convert_and_respect_annotation_metadata(
                    object_=stages,
                    annotation=typing.Sequence[PutMockserverChaosExperimentRequestStagesItem],
                    direction="write",
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
                    PutMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=PutMockserverChaosExperimentResponse,
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

    async def stop_the_current_chaos_experiment(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMockserverChaosExperimentResponse]:
        """
        Stops the current experiment and clears all chaos from the service registry. Idempotent — no-op if no experiment is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMockserverChaosExperimentResponse]
            experiment stopped (or no experiment was running)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverChaosExperimentResponse,
                    parse_obj_as(
                        type_=DeleteMockserverChaosExperimentResponse,
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

    async def retrieve_the_current_preemption_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PreemptionStatus]:
        """
        Returns the current cordon/drain status: state (inactive / draining / drained), the number of in-flight requests, the remaining drain window in milliseconds and the active signalling mode.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PreemptionStatus]
            preemption status returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PreemptionStatus,
                    parse_obj_as(
                        type_=PreemptionStatus,
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

    async def cordon_and_drain_the_server_preemption_simulation(
        self,
        *,
        mode: typing.Optional[PreemptionRequestMode] = OMIT,
        drain_millis: typing.Optional[int] = OMIT,
        ttl_millis: typing.Optional[int] = OMIT,
        last_stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PreemptionStatus]:
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
        AsyncHttpResponse[PreemptionStatus]
            preemption simulation started or replaced
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="PUT",
            json={
                "mode": mode,
                "drainMillis": drain_millis,
                "ttlMillis": ttl_millis,
                "lastStreamId": last_stream_id,
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
                    PreemptionStatus,
                    parse_obj_as(
                        type_=PreemptionStatus,
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

    async def uncordon_the_server_clear_preemption(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMockserverPreemptionResponse]:
        """
        Explicitly clears any active preemption simulation, returning the server to normal operation. Idempotent — returns 200 whether or not a simulation was active.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteMockserverPreemptionResponse]
            preemption cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/preemption",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverPreemptionResponse,
                    parse_obj_as(
                        type_=DeleteMockserverPreemptionResponse,
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

    async def list_saved_chaos_profile_names(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverChaosExperimentProfilesResponse]:
        """
        returns the names of all saved chaos experiment profiles, sorted ascending

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverChaosExperimentProfilesResponse]
            saved profile names returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment/profiles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentProfilesResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentProfilesResponse,
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

    async def retrieve_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChaosExperiment]:
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
        AsyncHttpResponse[ChaosExperiment]
            saved profile returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChaosExperiment,
                    parse_obj_as(
                        type_=ChaosExperiment,
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

    async def save_a_chaos_experiment_profile(
        self,
        name_: str,
        *,
        stages: typing.Sequence[ChaosExperimentStagesItem],
        name: typing.Optional[str] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverChaosExperimentProfilesNameResponse]:
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
        AsyncHttpResponse[PutMockserverChaosExperimentProfilesNameResponse]
            profile saved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name_)}",
            method="PUT",
            json={
                "name": name,
                "loop": loop,
                "stages": convert_and_respect_annotation_metadata(
                    object_=stages, annotation=typing.Sequence[ChaosExperimentStagesItem], direction="write"
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
                    PutMockserverChaosExperimentProfilesNameResponse,
                    parse_obj_as(
                        type_=PutMockserverChaosExperimentProfilesNameResponse,
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

    async def delete_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteMockserverChaosExperimentProfilesNameResponse]:
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
        AsyncHttpResponse[DeleteMockserverChaosExperimentProfilesNameResponse]
            deletion processed
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/profiles/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteMockserverChaosExperimentProfilesNameResponse,
                    parse_obj_as(
                        type_=DeleteMockserverChaosExperimentProfilesNameResponse,
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

    async def apply_a_saved_chaos_profile(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostMockserverChaosExperimentApplyNameResponse]:
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
        AsyncHttpResponse[PostMockserverChaosExperimentApplyNameResponse]
            saved profile applied (experiment started)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"mockserver/chaosExperiment/apply/{encode_path_param(name)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostMockserverChaosExperimentApplyNameResponse,
                    parse_obj_as(
                        type_=PostMockserverChaosExperimentApplyNameResponse,
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

    async def retrieve_completed_chaos_experiment_history(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetMockserverChaosExperimentHistoryResponse]:
        """
        Returns the record of chaos experiments that have run, most recent first, bounded by a fixed in-memory history size that is not caller-controllable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverChaosExperimentHistoryResponse]
            chaos experiment history returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/chaosExperiment/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverChaosExperimentHistoryResponse,
                    parse_obj_as(
                        type_=GetMockserverChaosExperimentHistoryResponse,
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
