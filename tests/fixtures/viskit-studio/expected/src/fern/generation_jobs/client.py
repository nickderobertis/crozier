

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.generation_job_created import GenerationJobCreated
from ..types.generation_job_list_response import GenerationJobListResponse
from ..types.generation_job_out import GenerationJobOut
from ..types.generation_job_start_response import GenerationJobStartResponse
from ..types.generation_job_stop_response import GenerationJobStopResponse
from ..types.generation_output_create import GenerationOutputCreate
from .raw_client import AsyncRawGenerationJobsClient, RawGenerationJobsClient
from .types.generation_job_create_locale import GenerationJobCreateLocale
from .types.list_generation_jobs_api_generation_jobs_get_request_status import (
    ListGenerationJobsApiGenerationJobsGetRequestStatus,
)


OMIT = typing.cast(typing.Any, ...)


class GenerationJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGenerationJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGenerationJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGenerationJobsClient
        """
        return self._raw_client

    def list_generation_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ListGenerationJobsApiGenerationJobsGetRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationJobListResponse:
        """
        Return recent durable generation jobs as queue/history records.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ListGenerationJobsApiGenerationJobsGetRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.list_generation_jobs()
        """
        _response = self._raw_client.list_generation_jobs(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    def create_generation_job(
        self,
        *,
        outputs: typing.Sequence[GenerationOutputCreate],
        source_image_ref: str,
        client_job_id: typing.Optional[str] = OMIT,
        locale: typing.Optional[GenerationJobCreateLocale] = OMIT,
        marketing_kit_id: typing.Optional[int] = OMIT,
        planner_payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        user_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationJobCreated:
        """
        Parameters
        ----------
        outputs : typing.Sequence[GenerationOutputCreate]

        source_image_ref : str

        client_job_id : typing.Optional[str]

        locale : typing.Optional[GenerationJobCreateLocale]

        marketing_kit_id : typing.Optional[int]

        planner_payload : typing.Optional[typing.Dict[str, typing.Any]]

        user_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobCreated
            Successful Response

        Examples
        --------
        from fern import FernApi, GenerationOutputCreate

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.create_generation_job(
            outputs=[
                GenerationOutputCreate(
                    output_key="output_key",
                    prompt="prompt",
                    template_ref="template_ref",
                )
            ],
            source_image_ref="source_image_ref",
        )
        """
        _response = self._raw_client.create_generation_job(
            outputs=outputs,
            source_image_ref=source_image_ref,
            client_job_id=client_job_id,
            locale=locale,
            marketing_kit_id=marketing_kit_id,
            planner_payload=planner_payload,
            user_prompt=user_prompt,
            request_options=request_options,
        )
        return _response.data

    def get_kit_slot_output_image(
        self, marketing_kit_id: int, slot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        marketing_kit_id : int

        slot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.get_kit_slot_output_image(
            marketing_kit_id=1,
            slot_id="slot_id",
        )
        """
        _response = self._raw_client.get_kit_slot_output_image(
            marketing_kit_id, slot_id, request_options=request_options
        )
        return _response.data

    def get_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobOut:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.get_generation_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.get_generation_job(job_id, request_options=request_options)
        return _response.data

    def generation_job_events(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.generation_job_events(
            job_id="job_id",
        )
        """
        _response = self._raw_client.generation_job_events(job_id, request_options=request_options)
        return _response.data

    def get_generation_output_image(
        self, job_id: str, output_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        job_id : str

        output_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.get_generation_output_image(
            job_id="job_id",
            output_id="output_id",
        )
        """
        _response = self._raw_client.get_generation_output_image(job_id, output_id, request_options=request_options)
        return _response.data

    def start_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobStartResponse:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobStartResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.start_generation_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.start_generation_job(job_id, request_options=request_options)
        return _response.data

    def stop_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobStopResponse:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobStopResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.generation_jobs.stop_generation_job(
            job_id="job_id",
        )
        """
        _response = self._raw_client.stop_generation_job(job_id, request_options=request_options)
        return _response.data


class AsyncGenerationJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGenerationJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGenerationJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGenerationJobsClient
        """
        return self._raw_client

    async def list_generation_jobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ListGenerationJobsApiGenerationJobsGetRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationJobListResponse:
        """
        Return recent durable generation jobs as queue/history records.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ListGenerationJobsApiGenerationJobsGetRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.list_generation_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_generation_jobs(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    async def create_generation_job(
        self,
        *,
        outputs: typing.Sequence[GenerationOutputCreate],
        source_image_ref: str,
        client_job_id: typing.Optional[str] = OMIT,
        locale: typing.Optional[GenerationJobCreateLocale] = OMIT,
        marketing_kit_id: typing.Optional[int] = OMIT,
        planner_payload: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        user_prompt: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationJobCreated:
        """
        Parameters
        ----------
        outputs : typing.Sequence[GenerationOutputCreate]

        source_image_ref : str

        client_job_id : typing.Optional[str]

        locale : typing.Optional[GenerationJobCreateLocale]

        marketing_kit_id : typing.Optional[int]

        planner_payload : typing.Optional[typing.Dict[str, typing.Any]]

        user_prompt : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobCreated
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GenerationOutputCreate

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.create_generation_job(
                outputs=[
                    GenerationOutputCreate(
                        output_key="output_key",
                        prompt="prompt",
                        template_ref="template_ref",
                    )
                ],
                source_image_ref="source_image_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_generation_job(
            outputs=outputs,
            source_image_ref=source_image_ref,
            client_job_id=client_job_id,
            locale=locale,
            marketing_kit_id=marketing_kit_id,
            planner_payload=planner_payload,
            user_prompt=user_prompt,
            request_options=request_options,
        )
        return _response.data

    async def get_kit_slot_output_image(
        self, marketing_kit_id: int, slot_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        marketing_kit_id : int

        slot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.get_kit_slot_output_image(
                marketing_kit_id=1,
                slot_id="slot_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_kit_slot_output_image(
            marketing_kit_id, slot_id, request_options=request_options
        )
        return _response.data

    async def get_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobOut:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.get_generation_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_generation_job(job_id, request_options=request_options)
        return _response.data

    async def generation_job_events(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.generation_job_events(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generation_job_events(job_id, request_options=request_options)
        return _response.data

    async def get_generation_output_image(
        self, job_id: str, output_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        job_id : str

        output_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.get_generation_output_image(
                job_id="job_id",
                output_id="output_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_generation_output_image(
            job_id, output_id, request_options=request_options
        )
        return _response.data

    async def start_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobStartResponse:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobStartResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.start_generation_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_generation_job(job_id, request_options=request_options)
        return _response.data

    async def stop_generation_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GenerationJobStopResponse:
        """
        Parameters
        ----------
        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GenerationJobStopResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generation_jobs.stop_generation_job(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_generation_job(job_id, request_options=request_options)
        return _response.data
