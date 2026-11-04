

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.parse_response import ParseResponse
from .raw_client import AsyncRawParseClient, RawParseClient
from .types.parse_create_job_request_options import ParseCreateJobRequestOptions
from .types.parse_create_job_request_service_tier import ParseCreateJobRequestServiceTier
from .types.parse_create_job_response import ParseCreateJobResponse
from .types.parse_get_job_response import ParseGetJobResponse
from .types.parse_list_jobs_response import ParseListJobsResponse
from .types.parse_run_sync_request_options import ParseRunSyncRequestOptions


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

    def run_sync(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseRunSyncRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResponse:
        """
        Parse a document and return the parse response inline.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseRunSyncRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseResponse
            The parse response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.parse.run_sync()
        """
        _response = self._raw_client.run_sync(
            document=document, document_url=document_url, model=model, options=options, request_options=request_options
        )
        return _response.data

    def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseListJobsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.parse.list_jobs()
        """
        _response = self._raw_client.list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    def create_job(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseCreateJobRequestOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[ParseCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseCreateJobResponse:
        """
        Parse a document asynchronously. Returns a job ID; use it to poll for the job's status and retrieve the parse result once processing completes.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseCreateJobRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        output_save_url : typing.Optional[str]
            Public URL the full response is delivered to; the API response then carries ``output_url`` instead of inline data.

        service_tier : typing.Optional[ParseCreateJobRequestServiceTier]
            Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseCreateJobResponse
            Job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.parse.create_job()
        """
        _response = self._raw_client.create_job(
            document=document,
            document_url=document_url,
            model=model,
            options=options,
            output_save_url=output_save_url,
            service_tier=service_tier,
            request_options=request_options,
        )
        return _response.data

    def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ParseGetJobResponse:
        """
        Get the status of an async parse job. Once the job has ``completed``, ``result`` carries the parse response (or ``output_url`` when ``output_save_url`` was set). Partial success (some pages failed) is reported in ``result.metadata.failed_pages``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseGetJobResponse
            Job status / result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.parse.get_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_job(job_id, request_options=request_options)
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

    async def run_sync(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseRunSyncRequestOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseResponse:
        """
        Parse a document and return the parse response inline.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseRunSyncRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseResponse
            The parse response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.parse.run_sync()


        asyncio.run(main())
        """
        _response = await self._raw_client.run_sync(
            document=document, document_url=document_url, model=model, options=options, request_options=request_options
        )
        return _response.data

    async def list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseListJobsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number (0-indexed).

        page_size : typing.Optional[int]
            Number of items per page.

        status : typing.Optional[str]
            Filter by job status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.parse.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    async def create_job(
        self,
        *,
        document: typing.Optional[core.File] = OMIT,
        document_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[ParseCreateJobRequestOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[ParseCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParseCreateJobResponse:
        """
        Parse a document asynchronously. Returns a job ID; use it to poll for the job's status and retrieve the parse result once processing completes.

        Parameters
        ----------
        document : typing.Optional[core.File]
            See core.File for more documentation

        document_url : typing.Optional[str]
            A publicly accessible URL to the file to parse. The file must be a PDF or image; see the list of [supported file types](https://docs.landing.ai/dpt3/file-types). Provide either `document` or `document_url`, not both.

        model : typing.Optional[str]
            The DPT-3 model snapshot to use for this request. Accepts a dated snapshot (for example, `dpt-3-pro-20260710`), the `dpt-3-pro-latest` alias, or the bare `dpt-3-pro` family name (equivalent to `dpt-3-pro-latest`). Defaults to the latest DPT-3 Pro snapshot.

        options : typing.Optional[ParseCreateJobRequestOptions]
            Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.

        output_save_url : typing.Optional[str]
            Public URL the full response is delivered to; the API response then carries ``output_url`` instead of inline data.

        service_tier : typing.Optional[ParseCreateJobRequestServiceTier]
            Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseCreateJobResponse
            Job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.parse.create_job()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_job(
            document=document,
            document_url=document_url,
            model=model,
            options=options,
            output_save_url=output_save_url,
            service_tier=service_tier,
            request_options=request_options,
        )
        return _response.data

    async def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ParseGetJobResponse:
        """
        Get the status of an async parse job. Once the job has ``completed``, ``result`` carries the parse response (or ``output_url`` when ``output_save_url`` was set). Partial success (some pages failed) is reported in ``result.metadata.failed_pages``.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParseGetJobResponse
            Job status / result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.parse.get_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data
