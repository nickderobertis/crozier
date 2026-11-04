

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGroundClient, RawGroundClient
from .types.v2ground_create_job_response import V2GroundCreateJobResponse
from .types.v2ground_get_job_response import V2GroundGetJobResponse
from .types.v2ground_list_jobs_response import V2GroundListJobsResponse
from .types.v2ground_run_sync_response import V2GroundRunSyncResponse


OMIT = typing.cast(typing.Any, ...)


class GroundClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroundClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroundClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroundClient
        """
        return self._raw_client

    def v2ground_run_sync(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundRunSyncResponse:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs synchronously and returns the result inline.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundRunSyncResponse
            v2-ground result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ground.v2ground_run_sync(
            extraction_metadata={
                "invoice_number": {
                    "ranges": [{"end": 31, "start": 13}],
                    "value": "INV-042",
                }
            },
            structure={"key": "value"},
        )
        """
        _response = self._raw_client.v2ground_run_sync(
            extraction_metadata=extraction_metadata, structure=structure, request_options=request_options
        )
        return _response.data

    def v2ground_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundListJobsResponse:
        """
        List your Ground jobs, newest first.

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
        V2GroundListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ground.v2ground_list_jobs()
        """
        _response = self._raw_client.v2ground_list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    def v2ground_create_job(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundCreateJobResponse:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundCreateJobResponse
            Job created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ground.v2ground_create_job(
            extraction_metadata={
                "invoice_number": {
                    "ranges": [{"end": 31, "start": 13}],
                    "value": "INV-042",
                }
            },
            structure={"key": "value"},
        )
        """
        _response = self._raw_client.v2ground_create_job(
            extraction_metadata=extraction_metadata, structure=structure, request_options=request_options
        )
        return _response.data

    def v2ground_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2GroundGetJobResponse:
        """
        Get the status of an async Ground job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundGetJobResponse
            Job status / result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ground.v2ground_get_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.v2ground_get_job(job_id, request_options=request_options)
        return _response.data


class AsyncGroundClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroundClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroundClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroundClient
        """
        return self._raw_client

    async def v2ground_run_sync(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundRunSyncResponse:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs synchronously and returns the result inline.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundRunSyncResponse
            v2-ground result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ground.v2ground_run_sync(
                extraction_metadata={
                    "invoice_number": {
                        "ranges": [{"end": 31, "start": 13}],
                        "value": "INV-042",
                    }
                },
                structure={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2ground_run_sync(
            extraction_metadata=extraction_metadata, structure=structure, request_options=request_options
        )
        return _response.data

    async def v2ground_list_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundListJobsResponse:
        """
        List your Ground jobs, newest first.

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
        V2GroundListJobsResponse
            The caller's jobs, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ground.v2ground_list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.v2ground_list_jobs(
            page=page, page_size=page_size, status=status, request_options=request_options
        )
        return _response.data

    async def v2ground_create_job(
        self,
        *,
        extraction_metadata: typing.Dict[str, typing.Any],
        structure: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GroundCreateJobResponse:
        """
        Map extracted fields to the document blocks they were quoted from. Takes the extraction_metadata from an extract call and the structure tree from the parse call the markdown came from, and returns, for every extracted field, the overlapping blocks with their ids, page numbers, and bounding boxes. Runs asynchronously and returns a job ID; use it to poll for status and retrieve the result once processing completes.

        Parameters
        ----------
        extraction_metadata : typing.Dict[str, typing.Any]
            The ``extraction_metadata`` object returned by ``POST /v2/extract`` (or the pipeline's extract step): a tree mirroring your extraction schema whose leaves are ``{value, ranges}`` objects, where ``ranges`` are ``{start, end}`` Unicode code point offsets into the parse markdown.

        structure : typing.Dict[str, typing.Any]
            The ``structure`` tree from the parse response the extraction was produced from. Every block in the tree carries its ``grounding`` (``{page, range, box}``) inline; block ids in the response resolve against this exact tree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundCreateJobResponse
            Job created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ground.v2ground_create_job(
                extraction_metadata={
                    "invoice_number": {
                        "ranges": [{"end": 31, "start": 13}],
                        "value": "INV-042",
                    }
                },
                structure={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2ground_create_job(
            extraction_metadata=extraction_metadata, structure=structure, request_options=request_options
        )
        return _response.data

    async def v2ground_get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V2GroundGetJobResponse:
        """
        Get the status of an async Ground job, including its result once the job has completed.

        Parameters
        ----------
        job_id : str
            The identifier of the job to retrieve, as returned by the create-job request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GroundGetJobResponse
            Job status / result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ground.v2ground_get_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v2ground_get_job(job_id, request_options=request_options)
        return _response.data
