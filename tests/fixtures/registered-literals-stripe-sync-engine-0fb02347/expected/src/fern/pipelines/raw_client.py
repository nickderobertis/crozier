

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
from ..errors.not_found_error import NotFoundError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.conflict_error_body import ConflictErrorBody
from ..types.destination_config import DestinationConfig
from ..types.eof_payload import EofPayload
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.pipeline import Pipeline
from ..types.source_config import SourceConfig
from ..types.sync_state import SyncState
from .types.pipelines_check_request_only import PipelinesCheckRequestOnly
from .types.pipelines_create_request_streams_item import PipelinesCreateRequestStreamsItem
from .types.pipelines_delete_response import PipelinesDeleteResponse
from .types.pipelines_list_response import PipelinesListResponse
from .types.pipelines_setup_request_only import PipelinesSetupRequestOnly
from .types.pipelines_sync_batch_request_streams_item import PipelinesSyncBatchRequestStreamsItem
from .types.pipelines_sync_request_streams_item import PipelinesSyncRequestStreamsItem
from .types.pipelines_sync_workflow_test_response import PipelinesSyncWorkflowTestResponse
from .types.pipelines_teardown_request_only import PipelinesTeardownRequestOnly
from .types.pipelines_update_request_desired_status import PipelinesUpdateRequestDesiredStatus
from .types.pipelines_update_request_streams_item import PipelinesUpdateRequestStreamsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[PipelinesListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesListResponse]
            List of pipelines
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListResponse,
                    parse_obj_as(
                        type_=PipelinesListResponse,
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

    def create(
        self,
        *,
        source: SourceConfig,
        destination: DestinationConfig,
        skip_check: typing.Optional[bool] = None,
        id: typing.Optional[str] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pipeline]:
        """
        Parameters
        ----------
        source : SourceConfig

        destination : DestinationConfig

        skip_check : typing.Optional[bool]
            Skip connector validation checks

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        streams : typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pipeline]
            Created pipeline
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipelines",
            method="POST",
            params={
                "skip_check": skip_check,
            },
            json={
                "id": id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesCreateRequestStreamsItem], direction="write"
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
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Pipeline]:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pipeline]
            Retrieved pipeline with status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelinesDeleteResponse]:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesDeleteResponse]
            Deleted pipeline
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesDeleteResponse,
                    parse_obj_as(
                        type_=PipelinesDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def update(
        self,
        id_path_param: str,
        *,
        id: typing.Optional[str] = OMIT,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]] = OMIT,
        desired_status: typing.Optional[PipelinesUpdateRequestDesiredStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Pipeline]:
        """
        Parameters
        ----------
        id_path_param : str
            Unique pipeline identifier (e.g. pipe_abc123).

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        desired_status : typing.Optional[PipelinesUpdateRequestDesiredStatus]
            Set to "paused" to pause, "active" to resume, "deleted" to tear down.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Pipeline]
            Updated pipeline
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id_path_param)}",
            method="PATCH",
            json={
                "id": id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesUpdateRequestStreamsItem], direction="write"
                ),
                "desired_status": desired_status,
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
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def sync(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Triggers an ad-hoc sync run for the pipeline and streams NDJSON messages (records, state, progress, eof) back to the client. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Stop after N seconds

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON sync output
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync",
            method="POST",
            params={
                "time_limit": time_limit,
                "run_id": run_id,
                "reset_state": reset_state,
            },
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesSyncRequestStreamsItem], direction="write"
                ),
                "sync_state": convert_and_respect_annotation_metadata(
                    object_=sync_state, annotation=SyncState, direction="write"
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def sync_batch(
        self,
        id: str,
        *,
        state_limit: typing.Optional[int] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EofPayload]:
        """
        Runs the full sync pipeline and returns the final EofPayload as a single JSON response. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        state_limit : typing.Optional[int]
            Stop after N source_state messages

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EofPayload]
            Sync result
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync_batch",
            method="POST",
            params={
                "state_limit": state_limit,
                "run_id": run_id,
                "reset_state": reset_state,
            },
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesSyncBatchRequestStreamsItem], direction="write"
                ),
                "sync_state": convert_and_respect_annotation_metadata(
                    object_=sync_state, annotation=SyncState, direction="write"
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
                    EofPayload,
                    parse_obj_as(
                        type_=EofPayload,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def check(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesCheckRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `check()` method on source and/or destination connectors and streams back NDJSON messages (connection_status, log, trace). Pass ?only=source or ?only=destination to check a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesCheckRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON check output
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/check",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def setup(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesSetupRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `setup()` method on source and/or destination connectors (e.g. creating destination tables). Streams NDJSON messages (control, log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesSetupRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON setup output
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/setup",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def teardown(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesTeardownRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `teardown()` method on source and/or destination connectors (e.g. dropping destination tables). Streams NDJSON messages (log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesTeardownRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON teardown output
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/teardown",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def simulate_webhook_sync(
        self,
        id: str,
        *,
        created_after: typing.Optional[float] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Fetches events from /v1/events using the pipeline's Stripe API key, then pipes them as input into the sync engine's push mode. This exercises the same code path as real webhooks without needing webhook delivery.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        created_after : typing.Optional[float]
            Only fetch events created after this Unix timestamp (default: 24 hours ago)

        limit : typing.Optional[int]
            Max events to fetch (default: all)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON sync output
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/simulate_webhook_sync",
            method="POST",
            params={
                "created_after": created_after,
                "limit": limit,
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
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def sync_workflow_test(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesSyncWorkflowTestResponse]:
        """
        Exercises the same backfill loop code that the Temporal workflow uses, but runs inline without a Temporal server. Useful for testing the full workflow logic end-to-end.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Time limit per iteration (seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesSyncWorkflowTestResponse]
            Backfill result with final eof and sync state
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync_workflow_test",
            method="POST",
            params={
                "time_limit": time_limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesSyncWorkflowTestResponse,
                    parse_obj_as(
                        type_=PipelinesSyncWorkflowTestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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


class AsyncRawPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesListResponse]
            List of pipelines
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipelines",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListResponse,
                    parse_obj_as(
                        type_=PipelinesListResponse,
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

    async def create(
        self,
        *,
        source: SourceConfig,
        destination: DestinationConfig,
        skip_check: typing.Optional[bool] = None,
        id: typing.Optional[str] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pipeline]:
        """
        Parameters
        ----------
        source : SourceConfig

        destination : DestinationConfig

        skip_check : typing.Optional[bool]
            Skip connector validation checks

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        streams : typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pipeline]
            Created pipeline
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipelines",
            method="POST",
            params={
                "skip_check": skip_check,
            },
            json={
                "id": id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesCreateRequestStreamsItem], direction="write"
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
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
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

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Pipeline]:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pipeline]
            Retrieved pipeline with status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesDeleteResponse]:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesDeleteResponse]
            Deleted pipeline
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesDeleteResponse,
                    parse_obj_as(
                        type_=PipelinesDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def update(
        self,
        id_path_param: str,
        *,
        id: typing.Optional[str] = OMIT,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]] = OMIT,
        desired_status: typing.Optional[PipelinesUpdateRequestDesiredStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Pipeline]:
        """
        Parameters
        ----------
        id_path_param : str
            Unique pipeline identifier (e.g. pipe_abc123).

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        desired_status : typing.Optional[PipelinesUpdateRequestDesiredStatus]
            Set to "paused" to pause, "active" to resume, "deleted" to tear down.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Pipeline]
            Updated pipeline
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id_path_param)}",
            method="PATCH",
            json={
                "id": id,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesUpdateRequestStreamsItem], direction="write"
                ),
                "desired_status": desired_status,
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
                    Pipeline,
                    parse_obj_as(
                        type_=Pipeline,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def sync(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Triggers an ad-hoc sync run for the pipeline and streams NDJSON messages (records, state, progress, eof) back to the client. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Stop after N seconds

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON sync output
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync",
            method="POST",
            params={
                "time_limit": time_limit,
                "run_id": run_id,
                "reset_state": reset_state,
            },
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesSyncRequestStreamsItem], direction="write"
                ),
                "sync_state": convert_and_respect_annotation_metadata(
                    object_=sync_state, annotation=SyncState, direction="write"
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def sync_batch(
        self,
        id: str,
        *,
        state_limit: typing.Optional[int] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EofPayload]:
        """
        Runs the full sync pipeline and returns the final EofPayload as a single JSON response. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        state_limit : typing.Optional[int]
            Stop after N source_state messages

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EofPayload]
            Sync result
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync_batch",
            method="POST",
            params={
                "state_limit": state_limit,
                "run_id": run_id,
                "reset_state": reset_state,
            },
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceConfig, direction="write"
                ),
                "destination": convert_and_respect_annotation_metadata(
                    object_=destination, annotation=DestinationConfig, direction="write"
                ),
                "streams": convert_and_respect_annotation_metadata(
                    object_=streams, annotation=typing.Sequence[PipelinesSyncBatchRequestStreamsItem], direction="write"
                ),
                "sync_state": convert_and_respect_annotation_metadata(
                    object_=sync_state, annotation=SyncState, direction="write"
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
                    EofPayload,
                    parse_obj_as(
                        type_=EofPayload,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def check(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesCheckRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `check()` method on source and/or destination connectors and streams back NDJSON messages (connection_status, log, trace). Pass ?only=source or ?only=destination to check a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesCheckRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON check output
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/check",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def setup(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesSetupRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `setup()` method on source and/or destination connectors (e.g. creating destination tables). Streams NDJSON messages (control, log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesSetupRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON setup output
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/setup",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def teardown(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesTeardownRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Runs the `teardown()` method on source and/or destination connectors (e.g. dropping destination tables). Streams NDJSON messages (log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesTeardownRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON teardown output
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/teardown",
            method="POST",
            params={
                "only": only,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def simulate_webhook_sync(
        self,
        id: str,
        *,
        created_after: typing.Optional[float] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Fetches events from /v1/events using the pipeline's Stripe API key, then pipes them as input into the sync engine's push mode. This exercises the same code path as real webhooks without needing webhook delivery.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        created_after : typing.Optional[float]
            Only fetch events created after this Unix timestamp (default: 24 hours ago)

        limit : typing.Optional[int]
            Max events to fetch (default: all)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Streaming NDJSON sync output
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/simulate_webhook_sync",
            method="POST",
            params={
                "created_after": created_after,
                "limit": limit,
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
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def sync_workflow_test(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesSyncWorkflowTestResponse]:
        """
        Exercises the same backfill loop code that the Temporal workflow uses, but runs inline without a Temporal server. Useful for testing the full workflow logic end-to-end.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Time limit per iteration (seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesSyncWorkflowTestResponse]
            Backfill result with final eof and sync state
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pipelines/{encode_path_param(id)}/sync_workflow_test",
            method="POST",
            params={
                "time_limit": time_limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesSyncWorkflowTestResponse,
                    parse_obj_as(
                        type_=PipelinesSyncWorkflowTestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
