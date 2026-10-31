

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_extraction_pipeline_response import DeleteExtractionPipelineResponse
from ..types.extraction_pipeline import ExtractionPipeline
from ..types.extraction_pipeline_id import ExtractionPipelineId
from ..types.extraction_pipeline_list_response import ExtractionPipelineListResponse
from .raw_client import AsyncRawPipelinesClient, RawPipelinesClient
from .types.create_extraction_pipeline_request_grounding import CreateExtractionPipelineRequestGrounding
from .types.create_extraction_pipeline_request_llm_options import CreateExtractionPipelineRequestLlmOptions
from .types.update_extraction_pipeline_request_grounding import UpdateExtractionPipelineRequestGrounding
from .types.update_extraction_pipeline_request_llm_options import UpdateExtractionPipelineRequestLlmOptions


OMIT = typing.cast(typing.Any, ...)


class PipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipelinesClient
        """
        return self._raw_client

    def list_extraction_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionPipelineListResponse:
        """
        Return active (non-deleted) pipelines for the authenticated tenant, newest updates first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipelineListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.list_extraction_pipelines()
        """
        _response = self._raw_client.list_extraction_pipelines(request_options=request_options)
        return _response.data

    def create_extraction_pipeline(
        self,
        *,
        name: str,
        ocr_model: str,
        llm_model: str,
        schema: typing.Dict[str, typing.Any],
        slug: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_options: typing.Optional[CreateExtractionPipelineRequestLlmOptions] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[CreateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionPipeline:
        """
        Persist a tenant-scoped extraction configuration (OCR model, LLM model, schema,
        repair/grounding/reasoning). Validated with the same admission gates as extract.
        Playground tokens and `ocr:full` keys are both accepted.

        Parameters
        ----------
        name : str

        ocr_model : str

        llm_model : str

        schema : typing.Dict[str, typing.Any]
            JSON Schema object describing fields to extract. Root must be an object schema with
            explicit `properties` and at least one named property. Admission applies the same
            strict structured-output normalization as extract.

        slug : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_options : typing.Optional[CreateExtractionPipelineRequestLlmOptions]

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[CreateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.create_extraction_pipeline(
            name="name",
            ocr_model="ocr_model",
            llm_model="llm_model",
            schema={"key": "value"},
        )
        """
        _response = self._raw_client.create_extraction_pipeline(
            name=name,
            ocr_model=ocr_model,
            llm_model=llm_model,
            schema=schema,
            slug=slug,
            ocr_options=ocr_options,
            llm_options=llm_options,
            repair_attempts=repair_attempts,
            grounding=grounding,
            request_options=request_options,
        )
        return _response.data

    def get_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionPipeline:
        """
        Return one active pipeline. Missing, deleted, and cross-tenant ids return
        `404 pipeline_not_found`.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.get_extraction_pipeline(
            id="id",
        )
        """
        _response = self._raw_client.get_extraction_pipeline(id, request_options=request_options)
        return _response.data

    def delete_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteExtractionPipelineResponse:
        """
        Marks the pipeline deleted. Subsequent extract admits with that id return
        `404 pipeline_not_found`. Historical jobs retain snapshotted config.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteExtractionPipelineResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.delete_extraction_pipeline(
            id="id",
        )
        """
        _response = self._raw_client.delete_extraction_pipeline(id, request_options=request_options)
        return _response.data

    def update_extraction_pipeline(
        self,
        id: ExtractionPipelineId,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        ocr_model: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_model: typing.Optional[str] = OMIT,
        llm_options: typing.Optional[UpdateExtractionPipelineRequestLlmOptions] = OMIT,
        schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[UpdateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionPipeline:
        """
        Patch one or more fields, re-validate the effective merged config, and atomically
        increment `version`. In-flight and completed jobs keep their admit-time snapshots.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        name : typing.Optional[str]

        slug : typing.Optional[str]

        ocr_model : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_model : typing.Optional[str]

        llm_options : typing.Optional[UpdateExtractionPipelineRequestLlmOptions]

        schema : typing.Optional[typing.Dict[str, typing.Any]]
            Replacement extraction schema. Root must be an object schema with explicit `properties`
            and at least one named property. Merged pipeline config is re-validated on every update.

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[UpdateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.update_extraction_pipeline(
            id="id",
        )
        """
        _response = self._raw_client.update_extraction_pipeline(
            id,
            name=name,
            slug=slug,
            ocr_model=ocr_model,
            ocr_options=ocr_options,
            llm_model=llm_model,
            llm_options=llm_options,
            schema=schema,
            repair_attempts=repair_attempts,
            grounding=grounding,
            request_options=request_options,
        )
        return _response.data


class AsyncPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipelinesClient
        """
        return self._raw_client

    async def list_extraction_pipelines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionPipelineListResponse:
        """
        Return active (non-deleted) pipelines for the authenticated tenant, newest updates first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipelineListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.list_extraction_pipelines()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_extraction_pipelines(request_options=request_options)
        return _response.data

    async def create_extraction_pipeline(
        self,
        *,
        name: str,
        ocr_model: str,
        llm_model: str,
        schema: typing.Dict[str, typing.Any],
        slug: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_options: typing.Optional[CreateExtractionPipelineRequestLlmOptions] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[CreateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionPipeline:
        """
        Persist a tenant-scoped extraction configuration (OCR model, LLM model, schema,
        repair/grounding/reasoning). Validated with the same admission gates as extract.
        Playground tokens and `ocr:full` keys are both accepted.

        Parameters
        ----------
        name : str

        ocr_model : str

        llm_model : str

        schema : typing.Dict[str, typing.Any]
            JSON Schema object describing fields to extract. Root must be an object schema with
            explicit `properties` and at least one named property. Admission applies the same
            strict structured-output normalization as extract.

        slug : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_options : typing.Optional[CreateExtractionPipelineRequestLlmOptions]

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[CreateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.create_extraction_pipeline(
                name="name",
                ocr_model="ocr_model",
                llm_model="llm_model",
                schema={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_extraction_pipeline(
            name=name,
            ocr_model=ocr_model,
            llm_model=llm_model,
            schema=schema,
            slug=slug,
            ocr_options=ocr_options,
            llm_options=llm_options,
            repair_attempts=repair_attempts,
            grounding=grounding,
            request_options=request_options,
        )
        return _response.data

    async def get_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExtractionPipeline:
        """
        Return one active pipeline. Missing, deleted, and cross-tenant ids return
        `404 pipeline_not_found`.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.get_extraction_pipeline(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_extraction_pipeline(id, request_options=request_options)
        return _response.data

    async def delete_extraction_pipeline(
        self, id: ExtractionPipelineId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteExtractionPipelineResponse:
        """
        Marks the pipeline deleted. Subsequent extract admits with that id return
        `404 pipeline_not_found`. Historical jobs retain snapshotted config.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteExtractionPipelineResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.delete_extraction_pipeline(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_extraction_pipeline(id, request_options=request_options)
        return _response.data

    async def update_extraction_pipeline(
        self,
        id: ExtractionPipelineId,
        *,
        name: typing.Optional[str] = OMIT,
        slug: typing.Optional[str] = OMIT,
        ocr_model: typing.Optional[str] = OMIT,
        ocr_options: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        llm_model: typing.Optional[str] = OMIT,
        llm_options: typing.Optional[UpdateExtractionPipelineRequestLlmOptions] = OMIT,
        schema: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        repair_attempts: typing.Optional[int] = OMIT,
        grounding: typing.Optional[UpdateExtractionPipelineRequestGrounding] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExtractionPipeline:
        """
        Patch one or more fields, re-validate the effective merged config, and atomically
        increment `version`. In-flight and completed jobs keep their admit-time snapshots.

        Parameters
        ----------
        id : ExtractionPipelineId
            Tenant-scoped saved extraction pipeline identifier (`oppl_…`).

        name : typing.Optional[str]

        slug : typing.Optional[str]

        ocr_model : typing.Optional[str]

        ocr_options : typing.Optional[typing.Dict[str, typing.Any]]

        llm_model : typing.Optional[str]

        llm_options : typing.Optional[UpdateExtractionPipelineRequestLlmOptions]

        schema : typing.Optional[typing.Dict[str, typing.Any]]
            Replacement extraction schema. Root must be an object schema with explicit `properties`
            and at least one named property. Merged pipeline config is re-validated on every update.

        repair_attempts : typing.Optional[int]

        grounding : typing.Optional[UpdateExtractionPipelineRequestGrounding]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExtractionPipeline
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.update_extraction_pipeline(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_extraction_pipeline(
            id,
            name=name,
            slug=slug,
            ocr_model=ocr_model,
            ocr_options=ocr_options,
            llm_model=llm_model,
            llm_options=llm_options,
            schema=schema,
            repair_attempts=repair_attempts,
            grounding=grounding,
            request_options=request_options,
        )
        return _response.data
