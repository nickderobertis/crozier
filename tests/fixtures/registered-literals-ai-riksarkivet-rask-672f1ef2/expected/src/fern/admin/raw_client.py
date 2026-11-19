

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.dlq_backlog import DlqBacklog
from ..types.dlq_replay_response import DlqReplayResponse
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


class RawAdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_dlq(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DlqBacklog]:
        """
        The outbox saturation snapshot + the visible at-risk events (oldest first, capped at ``limit``).

        ``depth``/``oldest_age_seconds`` are the raw system-health signal; ``events`` is the per-dataset-governed
        subset the caller may see. Requires an authenticated principal when FGA is on (else the raw depth would
        leak to an anonymous caller); the event list is then filtered by dataset visibility.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DlqBacklog]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "admin/dlq",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DlqBacklog,
                    parse_obj_as(
                        type_=DlqBacklog,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def replay_dlq(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DlqReplayResponse]:
        """
        Re-ingest one staged event on demand, re-publish it, then drop it — the manual twin of the reconcile relay's drain.

        A replay IS a re-ingest, so it carries the SAME authz as a fresh ingest, twice over: the relay's gate on
        the staged bytes (:func:`enforce_bus_authz` — signature and stamped author) and the ingest door's on the
        operator (:func:`enforce_output_authz` — ``can_write_data`` on the outputs, ``can_get_metadata`` on the
        inputs, fail-closed). Both doors are idempotent: a run MERGEs on its run id, a static change on its
        derived feed id, and the durable feed insert is ON CONFLICT DO NOTHING. The staged bytes are re-published
        to the lineage topic exactly as the relay re-publishes them, so subscribers hear of the event as well as
        the graph. The drop is only reached on success — a failed re-ingest or re-publish leaves the object
        staged for the relay to retry, and a failed re-publish answers 503 because the graph is already
        repaired.

        Non-disclosure (audit 2026-07-20): replay must not become an oracle for events ``list_dlq`` hid. So a
        run whose datasets the caller cannot SEE (or an unparseable poison object, which the governed list also
        hides) returns the SAME 404 as a missing run — never a distinct 422 or a 403 echoing hidden dataset
        names. Only an event the caller could have listed reaches ``enforce_output_authz``.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DlqReplayResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"admin/dlq/{encode_path_param(run_id)}/replay",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DlqReplayResponse,
                    parse_obj_as(
                        type_=DlqReplayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_dlq(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DlqBacklog]:
        """
        The outbox saturation snapshot + the visible at-risk events (oldest first, capped at ``limit``).

        ``depth``/``oldest_age_seconds`` are the raw system-health signal; ``events`` is the per-dataset-governed
        subset the caller may see. Requires an authenticated principal when FGA is on (else the raw depth would
        leak to an anonymous caller); the event list is then filtered by dataset visibility.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DlqBacklog]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "admin/dlq",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DlqBacklog,
                    parse_obj_as(
                        type_=DlqBacklog,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def replay_dlq(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DlqReplayResponse]:
        """
        Re-ingest one staged event on demand, re-publish it, then drop it — the manual twin of the reconcile relay's drain.

        A replay IS a re-ingest, so it carries the SAME authz as a fresh ingest, twice over: the relay's gate on
        the staged bytes (:func:`enforce_bus_authz` — signature and stamped author) and the ingest door's on the
        operator (:func:`enforce_output_authz` — ``can_write_data`` on the outputs, ``can_get_metadata`` on the
        inputs, fail-closed). Both doors are idempotent: a run MERGEs on its run id, a static change on its
        derived feed id, and the durable feed insert is ON CONFLICT DO NOTHING. The staged bytes are re-published
        to the lineage topic exactly as the relay re-publishes them, so subscribers hear of the event as well as
        the graph. The drop is only reached on success — a failed re-ingest or re-publish leaves the object
        staged for the relay to retry, and a failed re-publish answers 503 because the graph is already
        repaired.

        Non-disclosure (audit 2026-07-20): replay must not become an oracle for events ``list_dlq`` hid. So a
        run whose datasets the caller cannot SEE (or an unparseable poison object, which the governed list also
        hides) returns the SAME 404 as a missing run — never a distinct 422 or a 403 echoing hidden dataset
        names. Only an event the caller could have listed reaches ``enforce_output_authz``.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DlqReplayResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"admin/dlq/{encode_path_param(run_id)}/replay",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DlqReplayResponse,
                    parse_obj_as(
                        type_=DlqReplayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
