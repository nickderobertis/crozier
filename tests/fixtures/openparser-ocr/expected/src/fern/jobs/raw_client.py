

import contextlib
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
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.gateway_timeout_error import GatewayTimeoutError
from ..errors.not_found_error import NotFoundError
from ..errors.range_not_satisfiable_error import RangeNotSatisfiableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.extraction_review import ExtractionReview
from ..types.job import Job
from ..types.job_id import JobId
from ..types.job_list_response import JobListResponse
from ..types.job_operation import JobOperation
from ..types.job_status import JobStatus
from ..types.ocr_output_format import OcrOutputFormat
from ..types.parse_result import ParseResult
from .types.complete_extraction_review_request_status import CompleteExtractionReviewRequestStatus
from .types.update_extraction_review_request_confirmations_item import UpdateExtractionReviewRequestConfirmationsItem
from .types.update_extraction_review_request_retractions_item import UpdateExtractionReviewRequestRetractionsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_jobs(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobStatus] = None,
        operation: typing.Optional[JobOperation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobListResponse]:
        """
        Tenant-scoped chronological list of top-level OCR jobs (batch children are omitted).
        Returns lightweight summaries only — full results remain on `GET /jobs/{id}`.
        Cursor pagination is stable newest-first with an `id` tie-break. Optional `status`
        and `operation` filters are validated strictly; unknown values return `400`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Opaque pagination cursor from a prior `JobListResponse.next_cursor`. Jobs are
            returned newest-first (`created_at` descending, `id` descending tie-break).

        limit : typing.Optional[int]
            Maximum number of job summaries to return.

        status : typing.Optional[JobStatus]
            Optional filter by public job status. Admission-phase (`admitting`) jobs are
            never listed.

        operation : typing.Optional[JobOperation]
            Optional filter by job operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobListResponse]
            Page of job summaries
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "status": status,
                "operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobListResponse,
                    parse_obj_as(
                        type_=JobListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_job(
        self,
        id: JobId,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Job]:
        """
        Tenant-scoped durable job read. Jobs belonging to another tenant return `404`. Batch jobs
        include cursor-paginated child summaries. Playground tokens (`ocr:playground`) and `ocr:full`
        keys are both accepted. Successful parse jobs return the originally requested `output_format`
        in `result`; use `GET /jobs/{id}/result?format=` to select an alternate stored representation
        without re-running OCR.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        cursor : typing.Optional[str]
            Opaque pagination cursor for batch child summaries.

        limit : typing.Optional[int]
            Maximum number of batch child summaries to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Job]
            Job status, progress, and result when available
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_extraction_review(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExtractionReview]:
        """
        Return the immutable machine output beside the current corrected output and append-only
        review events. A succeeded extraction with no confirmations returns a synthesized pending review
        at version 0. Cross-tenant and unknown jobs return `404`.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionReview]
            Current extraction review
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def update_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        confirmations: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]] = OMIT,
        retractions: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtractionReview]:
        """
        Confirm that a field should say a given value, signed by the caller, without mutating the
        machine result. `expected_version` provides optimistic concurrency; stale writes return `409`.
        Every confirmation and retraction appends an actor- and timestamp-attributed event.

        A confirmation whose value matches what extraction produced is a plain sign-off; one that
        differs also corrects the field. There is no separate approval: who stands behind a value is
        derived from live confirmations. Retractions are applied first, then confirmations.

        A retraction peels the caller's own current tip on that path and restores the value the
        confirmation replaced. Two retractions of the same path undo two confirmations, in order. A
        retraction cannot be combined with a confirmation on the same or overlapping path. The tip is
        not retractable when someone else made it, or when a later overlapping confirmation named a
        different value. A co-signature of the same value becomes the tip, so only that co-signer can
        take it back. Completing the review still freezes everything. Provide at least one
        confirmation or retraction.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        confirmations : typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]]
            Fields the caller is signing. A value that matches the standing field is a sign-off; a different value also corrects it.

        retractions : typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]]
            JSON Pointers whose current tip the caller is taking back. Each entry peels one confirmation. The restored value is the one recorded on that confirmation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionReview]
            Updated extraction review
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review",
            method="PATCH",
            json={
                "expected_version": expected_version,
                "confirmations": convert_and_respect_annotation_metadata(
                    object_=confirmations,
                    annotation=typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem],
                    direction="write",
                ),
                "retractions": convert_and_respect_annotation_metadata(
                    object_=retractions,
                    annotation=typing.Sequence[UpdateExtractionReviewRequestRetractionsItem],
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def complete_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        status: CompleteExtractionReviewRequestStatus,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtractionReview]:
        """
        Finalize a pending review as approved or rejected. A completed review is frozen: field
        confirmations are rejected until it is reopened. Uses the same optimistic version check as
        field confirmations.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        status : CompleteExtractionReviewRequestStatus

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionReview]
            Completed extraction review
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review/complete",
            method="POST",
            json={
                "expected_version": expected_version,
                "status": status,
                "note": note,
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def reopen_extraction_review(
        self, id: JobId, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExtractionReview]:
        """
        Take a sign-off back so the run returns to `pending` and its fields can be reviewed again.
        Only the reviewer who completed the run may reopen it. Both events stay in the log, so the
        trail shows the run was signed off and then reopened, while the review status and the
        lineage decision follow the live completion. Uses the same optimistic version check as
        field confirmations.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtractionReview]
            Reopened extraction review, now pending
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review/reopen",
            method="POST",
            json={
                "expected_version": expected_version,
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_job_result(
        self,
        id: JobId,
        *,
        format: typing.Optional[OcrOutputFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParseResult]:
        """
        Return the selected parse wire body for a tenant-owned succeeded parse job.
        `format` defaults to the job's original `output_format`. Fresh dual-artifact parses
        can serve either `openparser@1` or `raw` from object storage without re-running HPS
        or charging pages. Historical jobs only serve the representation already present in
        `result_json`; unavailable alternates return `422 result_format_unavailable` with
        guidance. Non-terminal jobs return `409 job_not_terminal`. Playground tokens
        (`ocr:playground`) and `ocr:full` keys are both accepted.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        format : typing.Optional[OcrOutputFormat]
            Parse representation to return. Defaults to the job's original `output_format`
            when omitted. Fresh parses store both representations as immutable object-store
            artifacts; historical jobs only expose the representation already present in
            `result_json`. Requesting an unavailable alternate returns `422` and never
            re-runs OCR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ParseResult]
            Selected parse representation (`ParsedDocument` or `RawParseResult`)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/result",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResult,
                    parse_obj_as(
                        type_=ParseResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    @contextlib.contextmanager
    def get_job_source(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Stream the retained source document for a parse or single-document extract job. Jobs without
        retained source bytes return `404 source_not_available`. Check `has_source` on `GET /jobs/{id}`
        before calling. Playground tokens (`ocr:playground`) and `ocr:full` keys are both accepted,
        matching other job read routes. Optional `Range` requests may return `206` partial content or
        `416` when the range is unsatisfiable.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Full retained source document
        """
        with self._client_wrapper.httpx_client.stream(
            f"jobs/{encode_path_param(id)}/source",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_jobs(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobStatus] = None,
        operation: typing.Optional[JobOperation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobListResponse]:
        """
        Tenant-scoped chronological list of top-level OCR jobs (batch children are omitted).
        Returns lightweight summaries only — full results remain on `GET /jobs/{id}`.
        Cursor pagination is stable newest-first with an `id` tie-break. Optional `status`
        and `operation` filters are validated strictly; unknown values return `400`.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Opaque pagination cursor from a prior `JobListResponse.next_cursor`. Jobs are
            returned newest-first (`created_at` descending, `id` descending tie-break).

        limit : typing.Optional[int]
            Maximum number of job summaries to return.

        status : typing.Optional[JobStatus]
            Optional filter by public job status. Admission-phase (`admitting`) jobs are
            never listed.

        operation : typing.Optional[JobOperation]
            Optional filter by job operation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobListResponse]
            Page of job summaries
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "status": status,
                "operation": operation,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobListResponse,
                    parse_obj_as(
                        type_=JobListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_job(
        self,
        id: JobId,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Job]:
        """
        Tenant-scoped durable job read. Jobs belonging to another tenant return `404`. Batch jobs
        include cursor-paginated child summaries. Playground tokens (`ocr:playground`) and `ocr:full`
        keys are both accepted. Successful parse jobs return the originally requested `output_format`
        in `result`; use `GET /jobs/{id}/result?format=` to select an alternate stored representation
        without re-running OCR.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        cursor : typing.Optional[str]
            Opaque pagination cursor for batch child summaries.

        limit : typing.Optional[int]
            Maximum number of batch child summaries to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Job]
            Job status, progress, and result when available
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_extraction_review(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExtractionReview]:
        """
        Return the immutable machine output beside the current corrected output and append-only
        review events. A succeeded extraction with no confirmations returns a synthesized pending review
        at version 0. Cross-tenant and unknown jobs return `404`.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionReview]
            Current extraction review
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def update_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        confirmations: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]] = OMIT,
        retractions: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtractionReview]:
        """
        Confirm that a field should say a given value, signed by the caller, without mutating the
        machine result. `expected_version` provides optimistic concurrency; stale writes return `409`.
        Every confirmation and retraction appends an actor- and timestamp-attributed event.

        A confirmation whose value matches what extraction produced is a plain sign-off; one that
        differs also corrects the field. There is no separate approval: who stands behind a value is
        derived from live confirmations. Retractions are applied first, then confirmations.

        A retraction peels the caller's own current tip on that path and restores the value the
        confirmation replaced. Two retractions of the same path undo two confirmations, in order. A
        retraction cannot be combined with a confirmation on the same or overlapping path. The tip is
        not retractable when someone else made it, or when a later overlapping confirmation named a
        different value. A co-signature of the same value becomes the tip, so only that co-signer can
        take it back. Completing the review still freezes everything. Provide at least one
        confirmation or retraction.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        confirmations : typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]]
            Fields the caller is signing. A value that matches the standing field is a sign-off; a different value also corrects it.

        retractions : typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]]
            JSON Pointers whose current tip the caller is taking back. Each entry peels one confirmation. The restored value is the one recorded on that confirmation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionReview]
            Updated extraction review
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review",
            method="PATCH",
            json={
                "expected_version": expected_version,
                "confirmations": convert_and_respect_annotation_metadata(
                    object_=confirmations,
                    annotation=typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem],
                    direction="write",
                ),
                "retractions": convert_and_respect_annotation_metadata(
                    object_=retractions,
                    annotation=typing.Sequence[UpdateExtractionReviewRequestRetractionsItem],
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def complete_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        status: CompleteExtractionReviewRequestStatus,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtractionReview]:
        """
        Finalize a pending review as approved or rejected. A completed review is frozen: field
        confirmations are rejected until it is reopened. Uses the same optimistic version check as
        field confirmations.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        status : CompleteExtractionReviewRequestStatus

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionReview]
            Completed extraction review
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review/complete",
            method="POST",
            json={
                "expected_version": expected_version,
                "status": status,
                "note": note,
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def reopen_extraction_review(
        self, id: JobId, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExtractionReview]:
        """
        Take a sign-off back so the run returns to `pending` and its fields can be reviewed again.
        Only the reviewer who completed the run may reopen it. Both events stay in the log, so the
        trail shows the run was signed off and then reopened, while the review status and the
        lineage decision follow the live completion. Uses the same optimistic version check as
        field confirmations.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        expected_version : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtractionReview]
            Reopened extraction review, now pending
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/review/reopen",
            method="POST",
            json={
                "expected_version": expected_version,
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
                    ExtractionReview,
                    parse_obj_as(
                        type_=ExtractionReview,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_job_result(
        self,
        id: JobId,
        *,
        format: typing.Optional[OcrOutputFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParseResult]:
        """
        Return the selected parse wire body for a tenant-owned succeeded parse job.
        `format` defaults to the job's original `output_format`. Fresh dual-artifact parses
        can serve either `openparser@1` or `raw` from object storage without re-running HPS
        or charging pages. Historical jobs only serve the representation already present in
        `result_json`; unavailable alternates return `422 result_format_unavailable` with
        guidance. Non-terminal jobs return `409 job_not_terminal`. Playground tokens
        (`ocr:playground`) and `ocr:full` keys are both accepted.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        format : typing.Optional[OcrOutputFormat]
            Parse representation to return. Defaults to the job's original `output_format`
            when omitted. Fresh parses store both representations as immutable object-store
            artifacts; historical jobs only expose the representation already present in
            `result_json`. Requesting an unavailable alternate returns `422` and never
            re-runs OCR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ParseResult]
            Selected parse representation (`ParsedDocument` or `RawParseResult`)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"jobs/{encode_path_param(id)}/result",
            method="GET",
            params={
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParseResult,
                    parse_obj_as(
                        type_=ParseResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 504:
                raise GatewayTimeoutError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    @contextlib.asynccontextmanager
    async def get_job_source(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Stream the retained source document for a parse or single-document extract job. Jobs without
        retained source bytes return `404 source_not_available`. Check `has_source` on `GET /jobs/{id}`
        before calling. Playground tokens (`ocr:playground`) and `ocr:full` keys are both accepted,
        matching other job read routes. Optional `Range` requests may return `206` partial content or
        `416` when the range is unsatisfiable.

        Parameters
        ----------
        id : JobId
            Durable OCR job identifier (`opj_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Full retained source document
        """
        async with self._client_wrapper.httpx_client.stream(
            f"jobs/{encode_path_param(id)}/source",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 416:
                        raise RangeNotSatisfiableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
