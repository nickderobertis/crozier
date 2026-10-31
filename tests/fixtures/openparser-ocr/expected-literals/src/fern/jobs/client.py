

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.extraction_review import ExtractionReview
from ..types.job import Job
from ..types.job_id import JobId
from ..types.job_list_response import JobListResponse
from ..types.job_operation import JobOperation
from ..types.job_status import JobStatus
from ..types.ocr_output_format import OcrOutputFormat
from ..types.parse_result import ParseResult
from .raw_client import AsyncRawJobsClient, RawJobsClient
from .types.complete_extraction_review_request_status import CompleteExtractionReviewRequestStatus
from .types.update_extraction_review_request_confirmations_item import UpdateExtractionReviewRequestConfirmationsItem
from .types.update_extraction_review_request_retractions_item import UpdateExtractionReviewRequestRetractionsItem


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def list_jobs(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobStatus] = None,
        operation: typing.Optional[JobOperation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobListResponse:
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
        JobListResponse
            Page of job summaries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.list_jobs()
        """
        _response = self._raw_client.list_jobs(
            cursor=cursor, limit=limit, status=status, operation=operation, request_options=request_options
        )
        return _response.data

    def get_job(
        self,
        id: JobId,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
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
        Job
            Job status, progress, and result when available

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
        )
        """
        _response = self._raw_client.get_job(id, cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    def get_extraction_review(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionReview:
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
        ExtractionReview
            Current extraction review

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_extraction_review(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
        )
        """
        _response = self._raw_client.get_extraction_review(id, request_options=request_options)
        return _response.data

    def update_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        confirmations: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]] = OMIT,
        retractions: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionReview:
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
        ExtractionReview
            Updated extraction review

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.update_extraction_review(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
            expected_version=1,
        )
        """
        _response = self._raw_client.update_extraction_review(
            id,
            expected_version=expected_version,
            confirmations=confirmations,
            retractions=retractions,
            request_options=request_options,
        )
        return _response.data

    def complete_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        status: CompleteExtractionReviewRequestStatus,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionReview:
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
        ExtractionReview
            Completed extraction review

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.complete_extraction_review(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
            expected_version=1,
            status="approved",
        )
        """
        _response = self._raw_client.complete_extraction_review(
            id, expected_version=expected_version, status=status, note=note, request_options=request_options
        )
        return _response.data

    def reopen_extraction_review(
        self, id: JobId, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionReview:
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
        ExtractionReview
            Reopened extraction review, now pending

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.reopen_extraction_review(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
            expected_version=1,
        )
        """
        _response = self._raw_client.reopen_extraction_review(
            id, expected_version=expected_version, request_options=request_options
        )
        return _response.data

    def get_job_result(
        self,
        id: JobId,
        *,
        format: typing.Optional[OcrOutputFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResult:
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
        ParseResult
            Selected parse representation (`ParsedDocument` or `RawParseResult`)

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_result(
            id="opj_V1StGXR8_Z5jdHi6B-myT",
        )
        """
        _response = self._raw_client.get_job_result(id, format=format, request_options=request_options)
        return _response.data

    def get_job_source(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
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
        typing.Iterator[bytes]
            Full retained source document

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_source(
            id="id",
        )
        """
        with self._raw_client.get_job_source(id, request_options=request_options) as r:
            yield from r.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def list_jobs(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        status: typing.Optional[JobStatus] = None,
        operation: typing.Optional[JobOperation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobListResponse:
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
        JobListResponse
            Page of job summaries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(
            cursor=cursor, limit=limit, status=status, operation=operation, request_options=request_options
        )
        return _response.data

    async def get_job(
        self,
        id: JobId,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
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
        Job
            Job status, progress, and result when available

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(id, cursor=cursor, limit=limit, request_options=request_options)
        return _response.data

    async def get_extraction_review(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionReview:
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
        ExtractionReview
            Current extraction review

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_extraction_review(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_extraction_review(id, request_options=request_options)
        return _response.data

    async def update_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        confirmations: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestConfirmationsItem]] = OMIT,
        retractions: typing.Optional[typing.Sequence[UpdateExtractionReviewRequestRetractionsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionReview:
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
        ExtractionReview
            Updated extraction review

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.update_extraction_review(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_extraction_review(
            id,
            expected_version=expected_version,
            confirmations=confirmations,
            retractions=retractions,
            request_options=request_options,
        )
        return _response.data

    async def complete_extraction_review(
        self,
        id: JobId,
        *,
        expected_version: int,
        status: CompleteExtractionReviewRequestStatus,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionReview:
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
        ExtractionReview
            Completed extraction review

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.complete_extraction_review(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
                expected_version=1,
                status="approved",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_extraction_review(
            id, expected_version=expected_version, status=status, note=note, request_options=request_options
        )
        return _response.data

    async def reopen_extraction_review(
        self, id: JobId, *, expected_version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionReview:
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
        ExtractionReview
            Reopened extraction review, now pending

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.reopen_extraction_review(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
                expected_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reopen_extraction_review(
            id, expected_version=expected_version, request_options=request_options
        )
        return _response.data

    async def get_job_result(
        self,
        id: JobId,
        *,
        format: typing.Optional[OcrOutputFormat] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResult:
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
        ParseResult
            Selected parse representation (`ParsedDocument` or `RawParseResult`)

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_result(
                id="opj_V1StGXR8_Z5jdHi6B-myT",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_result(id, format=format, request_options=request_options)
        return _response.data

    async def get_job_source(
        self, id: JobId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
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
        typing.AsyncIterator[bytes]
            Full retained source document

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_source(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_job_source(id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
