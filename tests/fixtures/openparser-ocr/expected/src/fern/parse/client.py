

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_job_accepted import BatchJobAccepted
from ..types.job_accepted import JobAccepted
from ..types.parse_batch_request import ParseBatchRequest
from ..types.parse_request import ParseRequest
from ..types.parse_result import ParseResult
from .raw_client import AsyncRawParseClient, RawParseClient


OMIT = typing.cast(typing.Any, ...)


class ParseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawParseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawParseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawParseClient
        """
        return self._raw_client

    def sync(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResult:
        """
        Admit a parse job, wait up to the sync wait limit, and return the selected terminal parse
        representation when ready. `output_format` defaults to the versioned provider-neutral
        `openparser@1`; `raw` returns a stable provider envelope around the selected provider's
        untouched successful result. Terminal `failed` within the wait window returns `422`
        `ErrorResponse`; terminal `indeterminate` returns `504` `ErrorResponse`. Returns `202`
        with a durable job reference and `Location` if the wait limit expires first.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        ParseResult
            Terminal parse result in the selected `openparser@1` or `raw` representation
        
        Examples
        --------
        from fern import FernApi, ParseRequest
        
        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.parse.sync(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ParseRequest(
                ocr_model="ocr_model",
            ),
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
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobAccepted:
        """
        Admit a durable parse job and return immediately.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse/async' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
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
        from fern import FernApi, ParseRequest
        
        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.parse.async_(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ParseRequest(
                ocr_model="ocr_model",
            ),
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
        request: ParseBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJobAccepted:
        """
        Admit up to 100 parse child jobs in one durable batch. Every uploaded file must be mapped
        exactly once by `file_index`. Partial child failures are preserved in batch results.
        Parent status derivation for mixed outcomes is defined on `JobStatus`.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ParseBatchRequest

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
        from fern import FernApi, ParseBatchRequest, ParseBatchRequestItemsItem

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.parse.batch(
            idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
            request=ParseBatchRequest(
                items=[
                    ParseBatchRequestItemsItem(
                        client_item_id="client_item_id",
                        ocr_model="ocr_model",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.batch(
            idempotency_key=idempotency_key, request=request, files=files, request_options=request_options
        )
        return _response.data


class AsyncParseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawParseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawParseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawParseClient
        """
        return self._raw_client

    async def sync(
        self,
        *,
        idempotency_key: str,
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResult:
        """
        Admit a parse job, wait up to the sync wait limit, and return the selected terminal parse
        representation when ready. `output_format` defaults to the versioned provider-neutral
        `openparser@1`; `raw` returns a stable provider envelope around the selected provider's
        untouched successful result. Terminal `failed` within the wait window returns `422`
        `ErrorResponse`; terminal `indeterminate` returns `504` `ErrorResponse`. Returns `202`
        with a durable job reference and `Location` if the wait limit expires first.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
        file : typing.Optional[core.File]
            See core.File for more documentation
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        ParseResult
            Terminal parse result in the selected `openparser@1` or `raw` representation
        
        Examples
        --------
        import asyncio
        
        from fern import AsyncFernApi, ParseRequest
        
        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )
        
        
        async def main() -> None:
            await client.parse.sync(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ParseRequest(
                    ocr_model="ocr_model",
                ),
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
        request: ParseRequest,
        file: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobAccepted:
        """
        Admit a durable parse job and return immediately.
        
        Example (`multipart/form-data`):
        
        ```bash
        curl -X POST 'https://api.openparser.dev/parse/async' \\
          -H 'Authorization: Bearer YOUR_API_KEY' \\
          -H "Idempotency-Key: $(uuidgen 2>/dev/null || openssl rand -hex 16)" \\
          -F 'request={"ocr_model":"paddleocr-vl-1.6","output_format":"openparser@1"};type=application/json' \\
          -F 'file=@./document.pdf'
        ```
        
        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.
        
        request : ParseRequest
        
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
        
        from fern import AsyncFernApi, ParseRequest
        
        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )
        
        
        async def main() -> None:
            await client.parse.async_(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ParseRequest(
                    ocr_model="ocr_model",
                ),
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
        request: ParseBatchRequest,
        files: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchJobAccepted:
        """
        Admit up to 100 parse child jobs in one durable batch. Every uploaded file must be mapped
        exactly once by `file_index`. Partial child failures are preserved in batch results.
        Parent status derivation for mixed outcomes is defined on `JobStatus`.

        Parameters
        ----------
        idempotency_key : str
            Client-supplied idempotency key. Required on every parse or extract `POST`. Must be unique per distinct
            request body for a given tenant and operation.

        request : ParseBatchRequest

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

        from fern import AsyncFernApi, ParseBatchRequest, ParseBatchRequestItemsItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.parse.batch(
                idempotency_key="7f9f2f3d-0f8a-4f0a-9a2b-2f6f0a7d2c11",
                request=ParseBatchRequest(
                    items=[
                        ParseBatchRequestItemsItem(
                            client_item_id="client_item_id",
                            ocr_model="ocr_model",
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
