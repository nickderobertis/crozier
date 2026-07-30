

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
from ..types.check_output import CheckOutput
from ..types.destination_output import DestinationOutput
from ..types.discover_output import DiscoverOutput
from ..types.eof_payload import EofPayload
from ..types.message import Message
from ..types.pipeline_config import PipelineConfig
from ..types.setup_output import SetupOutput
from ..types.sync_output import SyncOutput
from ..types.sync_state import SyncState
from ..types.teardown_output import TeardownOutput
from .types.pipeline_check_request_only import PipelineCheckRequestOnly
from .types.pipeline_setup_request_only import PipelineSetupRequestOnly
from .types.pipeline_teardown_request_only import PipelineTeardownRequestOnly
from .types.source_discover_request_source import SourceDiscoverRequestSource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStatelessSyncApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def pipeline_check(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineCheckRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckOutput]:
        """
        Validates the source/destination config and tests connectivity. Streams NDJSON messages (connection_status, log, trace) tagged with _emitted_by. Pass only=source or only=destination to check a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineCheckRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckOutput]
            NDJSON stream of check messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_check",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    CheckOutput,
                    parse_obj_as(
                        type_=CheckOutput,
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

    def pipeline_setup(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineSetupRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SetupOutput]:
        """
        Creates destination tables and applies migrations. Streams NDJSON messages (control, log, trace) tagged with _emitted_by. Pass only=destination to run destination setup alone (e.g. optimistic table creation) or only=source to isolate the source.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineSetupRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SetupOutput]
            NDJSON stream of setup messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_setup",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    SetupOutput,
                    parse_obj_as(
                        type_=SetupOutput,
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

    def pipeline_teardown(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineTeardownRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TeardownOutput]:
        """
        Drops destination tables. Streams NDJSON messages (log, trace) tagged with _emitted_by. Pass only=destination or only=source to run a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineTeardownRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeardownOutput]
            NDJSON stream of teardown messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_teardown",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    TeardownOutput,
                    parse_obj_as(
                        type_=TeardownOutput,
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

    def source_discover(
        self, *, source: SourceDiscoverRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DiscoverOutput]:
        """
        Streams NDJSON messages (catalog, logs, traces) for the configured source.

        Parameters
        ----------
        source : SourceDiscoverRequestSource
            Source config ({ type, ...config })

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DiscoverOutput]
            NDJSON stream of discover messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "source_discover",
            method="POST",
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceDiscoverRequestSource, direction="write"
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
                    DiscoverOutput,
                    parse_obj_as(
                        type_=DiscoverOutput,
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

    def pipeline_read(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Message]:
        """
        Streams NDJSON messages (records, state, catalog).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Message]
            NDJSON stream of sync messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_read",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "time_limit": time_limit,
                "soft_time_limit": soft_time_limit,
                "run_id": run_id,
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
                ),
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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
                    Message,
                    parse_obj_as(
                        type_=Message,
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

    def pipeline_write(
        self,
        *,
        pipeline: PipelineConfig,
        stdin: typing.Sequence[Message],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationOutput]:
        """
        Writes messages to the destination. Pass an array of messages in the request body.

        Parameters
        ----------
        pipeline : PipelineConfig

        stdin : typing.Sequence[Message]
            Array of messages to write to the destination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationOutput]
            NDJSON stream of write result messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_write",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
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
                    DestinationOutput,
                    parse_obj_as(
                        type_=DestinationOutput,
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

    def pipeline_sync(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SyncOutput]:
        """
        Reads from the source connector and writes to the destination (backfill mode).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SyncOutput]
            NDJSON stream of sync messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_sync",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "time_limit": time_limit,
                "soft_time_limit": soft_time_limit,
                "run_id": run_id,
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
                ),
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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
                    SyncOutput,
                    parse_obj_as(
                        type_=SyncOutput,
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

    def pipeline_sync_batch(
        self,
        *,
        pipeline: PipelineConfig,
        run_id: typing.Optional[str] = OMIT,
        state_limit: typing.Optional[int] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EofPayload]:
        """
        Runs the full read → write pipeline and returns the final EofPayload as a single JSON response.

        Parameters
        ----------
        pipeline : PipelineConfig

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        state_limit : typing.Optional[int]
            Stop after yielding N source_state messages, inclusive.

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EofPayload]
            Sync result
        """
        _response = self._client_wrapper.httpx_client.request(
            "pipeline_sync_batch",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "run_id": run_id,
                "state_limit": state_limit,
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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


class AsyncRawStatelessSyncApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def pipeline_check(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineCheckRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckOutput]:
        """
        Validates the source/destination config and tests connectivity. Streams NDJSON messages (connection_status, log, trace) tagged with _emitted_by. Pass only=source or only=destination to check a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineCheckRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckOutput]
            NDJSON stream of check messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_check",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    CheckOutput,
                    parse_obj_as(
                        type_=CheckOutput,
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

    async def pipeline_setup(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineSetupRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SetupOutput]:
        """
        Creates destination tables and applies migrations. Streams NDJSON messages (control, log, trace) tagged with _emitted_by. Pass only=destination to run destination setup alone (e.g. optimistic table creation) or only=source to isolate the source.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineSetupRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SetupOutput]
            NDJSON stream of setup messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_setup",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    SetupOutput,
                    parse_obj_as(
                        type_=SetupOutput,
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

    async def pipeline_teardown(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineTeardownRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TeardownOutput]:
        """
        Drops destination tables. Streams NDJSON messages (log, trace) tagged with _emitted_by. Pass only=destination or only=source to run a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineTeardownRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeardownOutput]
            NDJSON stream of teardown messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_teardown",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "only": only,
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
                    TeardownOutput,
                    parse_obj_as(
                        type_=TeardownOutput,
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

    async def source_discover(
        self, *, source: SourceDiscoverRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DiscoverOutput]:
        """
        Streams NDJSON messages (catalog, logs, traces) for the configured source.

        Parameters
        ----------
        source : SourceDiscoverRequestSource
            Source config ({ type, ...config })

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DiscoverOutput]
            NDJSON stream of discover messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "source_discover",
            method="POST",
            json={
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=SourceDiscoverRequestSource, direction="write"
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
                    DiscoverOutput,
                    parse_obj_as(
                        type_=DiscoverOutput,
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

    async def pipeline_read(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Message]:
        """
        Streams NDJSON messages (records, state, catalog).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Message]
            NDJSON stream of sync messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_read",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "time_limit": time_limit,
                "soft_time_limit": soft_time_limit,
                "run_id": run_id,
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
                ),
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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
                    Message,
                    parse_obj_as(
                        type_=Message,
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

    async def pipeline_write(
        self,
        *,
        pipeline: PipelineConfig,
        stdin: typing.Sequence[Message],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationOutput]:
        """
        Writes messages to the destination. Pass an array of messages in the request body.

        Parameters
        ----------
        pipeline : PipelineConfig

        stdin : typing.Sequence[Message]
            Array of messages to write to the destination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationOutput]
            NDJSON stream of write result messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_write",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
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
                    DestinationOutput,
                    parse_obj_as(
                        type_=DestinationOutput,
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

    async def pipeline_sync(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SyncOutput]:
        """
        Reads from the source connector and writes to the destination (backfill mode).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SyncOutput]
            NDJSON stream of sync messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_sync",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "time_limit": time_limit,
                "soft_time_limit": soft_time_limit,
                "run_id": run_id,
                "stdin": convert_and_respect_annotation_metadata(
                    object_=stdin, annotation=typing.Sequence[Message], direction="write"
                ),
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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
                    SyncOutput,
                    parse_obj_as(
                        type_=SyncOutput,
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

    async def pipeline_sync_batch(
        self,
        *,
        pipeline: PipelineConfig,
        run_id: typing.Optional[str] = OMIT,
        state_limit: typing.Optional[int] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EofPayload]:
        """
        Runs the full read → write pipeline and returns the final EofPayload as a single JSON response.

        Parameters
        ----------
        pipeline : PipelineConfig

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        state_limit : typing.Optional[int]
            Stop after yielding N source_state messages, inclusive.

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EofPayload]
            Sync result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pipeline_sync_batch",
            method="POST",
            json={
                "pipeline": convert_and_respect_annotation_metadata(
                    object_=pipeline, annotation=PipelineConfig, direction="write"
                ),
                "run_id": run_id,
                "state_limit": state_limit,
                "state": convert_and_respect_annotation_metadata(
                    object_=state, annotation=SyncState, direction="write"
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
