

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v2extract_options import V2ExtractOptions
from .raw_client import AsyncRawExtractClient, RawExtractClient
from .types.v2extract_create_job_request_service_tier import V2ExtractCreateJobRequestServiceTier
from .types.v2extract_create_job_response import V2ExtractCreateJobResponse
from .types.v2extract_get_job_response import V2ExtractGetJobResponse
from .types.v2extract_list_jobs_response import V2ExtractListJobsResponse
from .types.v2extract_run_sync_response import V2ExtractRunSyncResponse


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

    def v2extract_run_sync(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractRunSyncResponse:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs synchronously and returns the result inline.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractRunSyncResponse
            v2-extract result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.v2extract_run_sync(
            schema={
                "properties": {
                    "revenue": {"description": "Q1 revenue figure", "type": "string"},
                    "summary": {"description": "Executive summary", "type": "string"},
                },
                "type": "object",
            },
        )
        """
        _response = self._raw_client.v2extract_run_sync(
            schema=schema,
            markdown=markdown,
            markdown_url=markdown_url,
            model=model,
            options=options,
            request_options=request_options,
        )
        return _response.data

    def v2extract_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractListJobsResponse:
        """
        List your Extract jobs, newest first.

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
        V2ExtractListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.v2extract_list_jobs()
        """
        _response = self._raw_client.v2extract_list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    def v2extract_create_job(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[V2ExtractCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractCreateJobResponse:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        output_save_url : typing.Optional[str]
            URL to save the result to — e.g. a presigned S3 PUT URL. Async jobs only. When set, the finished result is delivered (HTTP PUT) to this URL and the completed job reports ``output_url`` instead of an inline ``result``. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        service_tier : typing.Optional[V2ExtractCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractCreateJobResponse
            Job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.v2extract_create_job(
            schema={
                "properties": {
                    "revenue": {"description": "Q1 revenue figure", "type": "string"},
                    "summary": {"description": "Executive summary", "type": "string"},
                },
                "type": "object",
            },
        )
        """
        _response = self._raw_client.v2extract_create_job(
            schema=schema,
            markdown=markdown,
            markdown_url=markdown_url,
            model=model,
            options=options,
            output_save_url=output_save_url,
            service_tier=service_tier,
            request_options=request_options,
        )
        return _response.data

    def v2extract_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2ExtractGetJobResponse:
        """
        Get the status of an async Extract job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractGetJobResponse
            Job status / result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.extract.v2extract_get_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.v2extract_get_job(job_id, request_options=request_options)
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

    async def v2extract_run_sync(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractRunSyncResponse:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs synchronously and returns the result inline.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractRunSyncResponse
            v2-extract result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.v2extract_run_sync(
                schema={
                    "properties": {
                        "revenue": {
                            "description": "Q1 revenue figure",
                            "type": "string",
                        },
                        "summary": {
                            "description": "Executive summary",
                            "type": "string",
                        },
                    },
                    "type": "object",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2extract_run_sync(
            schema=schema,
            markdown=markdown,
            markdown_url=markdown_url,
            model=model,
            options=options,
            request_options=request_options,
        )
        return _response.data

    async def v2extract_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractListJobsResponse:
        """
        List your Extract jobs, newest first.

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
        V2ExtractListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.v2extract_list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.v2extract_list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    async def v2extract_create_job(
        self,
        *,
        schema: typing.Dict[str, typing.Any],
        markdown: typing.Optional[str] = OMIT,
        markdown_url: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        options: typing.Optional[V2ExtractOptions] = OMIT,
        output_save_url: typing.Optional[str] = OMIT,
        service_tier: typing.Optional[V2ExtractCreateJobRequestServiceTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2ExtractCreateJobResponse:
        """
        Extract structured data from a Markdown document according to a JSON schema, with character-span grounding into the source Markdown. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        schema : typing.Dict[str, typing.Any]
            JSON Schema describing the fields to extract. The schema must be an object type with a ``properties`` map of field names to their types and descriptions.

        markdown : typing.Optional[str]
            Markdown string to extract from, or a multipart FILE part carrying the markdown (large inputs — uploads are staged by the gateway). Can come from any source — LandingAI parse output, a third-party parser, or hand-authored text. When the markdown was produced by ``POST /v2/parse``, it ends with a ``<!-- doc_id=<id> -->`` comment that the service reads automatically and echoes as ``metadata.doc_id``.

        markdown_url : typing.Optional[str]
            URL to fetch the markdown from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        model : typing.Optional[str]
            The version of the model to use for extraction. Use ``extract-latest`` to use the latest version.

        options : typing.Optional[V2ExtractOptions]
            Extraction options (``strict``). Omit for defaults.

        output_save_url : typing.Optional[str]
            URL to save the result to — e.g. a presigned S3 PUT URL. Async jobs only. When set, the finished result is delivered (HTTP PUT) to this URL and the completed job reports ``output_url`` instead of an inline ``result``. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.

        service_tier : typing.Optional[V2ExtractCreateJobRequestServiceTier]
            Async service tier. ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractCreateJobResponse
            Job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.v2extract_create_job(
                schema={
                    "properties": {
                        "revenue": {
                            "description": "Q1 revenue figure",
                            "type": "string",
                        },
                        "summary": {
                            "description": "Executive summary",
                            "type": "string",
                        },
                    },
                    "type": "object",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2extract_create_job(
            schema=schema,
            markdown=markdown,
            markdown_url=markdown_url,
            model=model,
            options=options,
            output_save_url=output_save_url,
            service_tier=service_tier,
            request_options=request_options,
        )
        return _response.data

    async def v2extract_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2ExtractGetJobResponse:
        """
        Get the status of an async Extract job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2ExtractGetJobResponse
            Job status / result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.extract.v2extract_get_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2extract_get_job(job_id, request_options=request_options)
        return _response.data
