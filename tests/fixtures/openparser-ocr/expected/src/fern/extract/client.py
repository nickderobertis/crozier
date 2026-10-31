

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_job_accepted import BatchJobAccepted
from ..types.extract_batch_request import ExtractBatchRequest
from ..types.extract_request import ExtractRequest
from ..types.extraction_terminal_result import ExtractionTerminalResult
from ..types.job_accepted import JobAccepted
from ..types.suggest_schema_response import SuggestSchemaResponse
from .raw_client import AsyncRawExtractClient, RawExtractClient


OMIT = typing.cast(typing.Any, ...)


class ExtractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExtractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExtractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExtractClient
        """
        return self._raw_client

    def sync(
        self,
        *,
        idempotency_key: str,
        request: ExtractRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionTerminalResult:
        """
        Admit a single extract job from file bytes, `file_id`, or a tenant-owned succeeded
        `parse_job_id`, then run schema-constrained OpenRouter extraction via `llm_model`. A
        `parse_job_id` source reuses the canonical ParsedDocument (from dual artifacts or legacy
        `result_json`) without OCR or another page charge; historical raw-only parses return
        `422 canonical_result_unavailable`. Wait up to the sync wait limit and return
        `ExtractionTerminalResult` when ready. Terminal `failed` within the wait window returns
        `422`; terminal `indeterminate` returns `504`. Returns `202` with a durable job reference
        and `Location` if the wait expires.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractRequest

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionTerminalResult
            Terminal extraction result

        Examples
        --------
        from fern import ExtractRequest, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.extract.sync(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ExtractRequest(),
        )
        """
        _response = self._raw_client.sync(
            idempotency_key=idempotency_key, request=request, file=file, request_options=request_options
        )
        return _response.data

    def async_(
        self,
        *,
        idempotency_key: str,
        request: ExtractRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobAccepted:
        """
        Admit a durable single extract job from file bytes, `file_id`, or `parse_job_id` and
        return immediately. Parse reuse does not run OCR or add a page charge; OpenRouter usage
        remains billable.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractRequest

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobAccepted
            Durable non-terminal job admitted. Returned by async endpoints and by sync endpoints when
            the wait limit expires before a terminal status.

        Examples
        --------
        from fern import ExtractRequest, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.extract.async_(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ExtractRequest(),
        )
        """
        _response = self._raw_client.async_(
            idempotency_key=idempotency_key, request=request, file=file, request_options=request_options
        )
        return _response.data

    def batch(
        self,
        *,
        idempotency_key: str,
        request: ExtractBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJobAccepted:
        """
        Admit up to 100 file-backed extract child jobs in one durable batch. Every item uses
        `file_index` or `file_id`; `parse_job_id` reuse is single-extract-only and is not accepted
        in batch. Partial child failures are preserved. Parent status derivation follows
        `JobStatus`; billing is evaluated per child.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractBatchRequest

        files : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJobAccepted
            Durable batch job admitted. `Location` points at the parent batch job resource.

        Examples
        --------
        from fern import ExtractBatchRequest, ExtractBatchRequestItemsItem, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.extract.batch(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ExtractBatchRequest(
                items=[
                    ExtractBatchRequestItemsItem(
                        client_item_id="client_item_id",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.batch(
            idempotency_key=idempotency_key, request=request, files=files, request_options=request_options
        )
        return _response.data

    def suggest_schema(
        self,
        *,
        parse_job_id: str,
        hint: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuggestSchemaResponse:
        """
        Suggest an extraction JSON Schema from a tenant-owned succeeded parse result.
        Optional `hint` is capped at 500 characters. Definitive failures return
        `schema_suggestion_failed`.

        Parameters
        ----------
        parse_job_id : str
            Prefixed id (`opj_…`) of a succeeded `parse` job in the same tenant.

        hint : typing.Optional[str]
            Optional free-text guidance for the suggestion model (max 500 characters).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestSchemaResponse
            Suggested schema

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.extract.suggest_schema(
            parse_job_id="parse_job_id",
        )
        """
        _response = self._raw_client.suggest_schema(
            parse_job_id=parse_job_id, hint=hint, request_options=request_options
        )
        return _response.data


class AsyncExtractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExtractClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExtractClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExtractClient
        """
        return self._raw_client

    async def sync(
        self,
        *,
        idempotency_key: str,
        request: ExtractRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionTerminalResult:
        """
        Admit a single extract job from file bytes, `file_id`, or a tenant-owned succeeded
        `parse_job_id`, then run schema-constrained OpenRouter extraction via `llm_model`. A
        `parse_job_id` source reuses the canonical ParsedDocument (from dual artifacts or legacy
        `result_json`) without OCR or another page charge; historical raw-only parses return
        `422 canonical_result_unavailable`. Wait up to the sync wait limit and return
        `ExtractionTerminalResult` when ready. Terminal `failed` within the wait window returns
        `422`; terminal `indeterminate` returns `504`. Returns `202` with a durable job reference
        and `Location` if the wait expires.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractRequest

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionTerminalResult
            Terminal extraction result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExtractRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.extract.sync(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ExtractRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync(
            idempotency_key=idempotency_key, request=request, file=file, request_options=request_options
        )
        return _response.data

    async def async_(
        self,
        *,
        idempotency_key: str,
        request: ExtractRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobAccepted:
        """
        Admit a durable single extract job from file bytes, `file_id`, or `parse_job_id` and
        return immediately. Parse reuse does not run OCR or add a page charge; OpenRouter usage
        remains billable.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractRequest

        file : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobAccepted
            Durable non-terminal job admitted. Returned by async endpoints and by sync endpoints when
            the wait limit expires before a terminal status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExtractRequest

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.extract.async_(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ExtractRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.async_(
            idempotency_key=idempotency_key, request=request, file=file, request_options=request_options
        )
        return _response.data

    async def batch(
        self,
        *,
        idempotency_key: str,
        request: ExtractBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJobAccepted:
        """
        Admit up to 100 file-backed extract child jobs in one durable batch. Every item uses
        `file_index` or `file_id`; `parse_job_id` reuse is single-extract-only and is not accepted
        in batch. Partial child failures are preserved. Parent status derivation follows
        `JobStatus`; billing is evaluated per child.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ExtractBatchRequest

        files : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchJobAccepted
            Durable batch job admitted. `Location` points at the parent batch job resource.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExtractBatchRequest, ExtractBatchRequestItemsItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.extract.batch(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ExtractBatchRequest(
                    items=[
                        ExtractBatchRequestItemsItem(
                            client_item_id="client_item_id",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch(
            idempotency_key=idempotency_key, request=request, files=files, request_options=request_options
        )
        return _response.data

    async def suggest_schema(
        self,
        *,
        parse_job_id: str,
        hint: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SuggestSchemaResponse:
        """
        Suggest an extraction JSON Schema from a tenant-owned succeeded parse result.
        Optional `hint` is capped at 500 characters. Definitive failures return
        `schema_suggestion_failed`.

        Parameters
        ----------
        parse_job_id : str
            Prefixed id (`opj_…`) of a succeeded `parse` job in the same tenant.

        hint : typing.Optional[str]
            Optional free-text guidance for the suggestion model (max 500 characters).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuggestSchemaResponse
            Suggested schema

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.extract.suggest_schema(
                parse_job_id="parse_job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.suggest_schema(
            parse_job_id=parse_job_id, hint=hint, request_options=request_options
        )
        return _response.data
