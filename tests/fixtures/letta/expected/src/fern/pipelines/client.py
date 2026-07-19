

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pipelines_list_pipelines_request_offset import PipelinesListPipelinesRequestOffset
from .raw_client import AsyncRawPipelinesClient, RawPipelinesClient
from .types.pipelines_count_pipelines_response import PipelinesCountPipelinesResponse
from .types.pipelines_create_pipeline_request_integration_type import PipelinesCreatePipelineRequestIntegrationType
from .types.pipelines_create_pipeline_request_producer_config import PipelinesCreatePipelineRequestProducerConfig
from .types.pipelines_create_pipeline_response import PipelinesCreatePipelineResponse
from .types.pipelines_delete_pipeline_response import PipelinesDeletePipelineResponse
from .types.pipelines_get_pipeline_response import PipelinesGetPipelineResponse
from .types.pipelines_list_pipeline_sync_history_response import PipelinesListPipelineSyncHistoryResponse
from .types.pipelines_list_pipelines_response import PipelinesListPipelinesResponse
from .types.pipelines_preview_pipeline_request_integration_type import PipelinesPreviewPipelineRequestIntegrationType
from .types.pipelines_preview_pipeline_request_producer_config import PipelinesPreviewPipelineRequestProducerConfig
from .types.pipelines_preview_pipeline_response import PipelinesPreviewPipelineResponse
from .types.pipelines_sync_pipeline_response import PipelinesSyncPipelineResponse
from .types.pipelines_update_pipeline_response import PipelinesUpdatePipelineResponse


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

    def listpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        offset: typing.Optional[PipelinesListPipelinesRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesListPipelinesResponse:
        """
        List all pipelines for the organization with optional filtering

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        offset : typing.Optional[PipelinesListPipelinesRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListPipelinesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.listpipelines()
        """
        _response = self._raw_client.listpipelines(
            search=search,
            integration_type=integration_type,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def createpipeline(
        self,
        *,
        name: str,
        project_id: str,
        integration_type: PipelinesCreatePipelineRequestIntegrationType,
        producer_config: PipelinesCreatePipelineRequestProducerConfig,
        subscriber_agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        subscriber_cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesCreatePipelineResponse:
        """
        Create a new pipeline (producer + feed + optionally subscribers)

        Parameters
        ----------
        name : str

        project_id : str

        integration_type : PipelinesCreatePipelineRequestIntegrationType

        producer_config : PipelinesCreatePipelineRequestProducerConfig

        subscriber_agent_ids : typing.Optional[typing.Sequence[str]]

        subscriber_cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesCreatePipelineResponse
            200

        Examples
        --------
        from fern.pipelines import (
            PipelinesCreatePipelineRequestIntegrationType,
            PipelinesCreatePipelineRequestProducerConfig,
            PipelinesCreatePipelineRequestProducerConfigData,
            PipelinesCreatePipelineRequestProducerConfigDataChannelsItem,
            PipelinesCreatePipelineRequestProducerConfigType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.createpipeline(
            name="name",
            project_id="project_id",
            integration_type=PipelinesCreatePipelineRequestIntegrationType.SLACK,
            producer_config=PipelinesCreatePipelineRequestProducerConfig(
                type=PipelinesCreatePipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
                data=PipelinesCreatePipelineRequestProducerConfigData(
                    channels=[
                        PipelinesCreatePipelineRequestProducerConfigDataChannelsItem(
                            channel_id="channel_id",
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.createpipeline(
            name=name,
            project_id=project_id,
            integration_type=integration_type,
            producer_config=producer_config,
            subscriber_agent_ids=subscriber_agent_ids,
            subscriber_cron_schedule=subscriber_cron_schedule,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    def countpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesCountPipelinesResponse:
        """
        Get the total count of pipelines, optionally filtered by project and search

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesCountPipelinesResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.countpipelines()
        """
        _response = self._raw_client.countpipelines(
            search=search, integration_type=integration_type, request_options=request_options
        )
        return _response.data

    def getpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesGetPipelineResponse:
        """
        Get a single pipeline with details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesGetPipelineResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.getpipeline(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.getpipeline(pipeline_id, request_options=request_options)
        return _response.data

    def deletepipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesDeletePipelineResponse:
        """
        Soft delete a pipeline and cascade to feed + subscriptions

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesDeletePipelineResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.deletepipeline(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.deletepipeline(pipeline_id, request_options=request_options)
        return _response.data

    def updatepipeline(
        self,
        pipeline_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesUpdatePipelineResponse:
        """
        Update pipeline name or disable/enable it

        Parameters
        ----------
        pipeline_id : str

        name : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesUpdatePipelineResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.updatepipeline(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.updatepipeline(
            pipeline_id, name=name, disabled=disabled, request_options=request_options
        )
        return _response.data

    def previewpipeline(
        self,
        *,
        integration_type: PipelinesPreviewPipelineRequestIntegrationType,
        integration_id: str,
        producer_config: PipelinesPreviewPipelineRequestProducerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesPreviewPipelineResponse:
        """
        Fetch sample messages from integration to preview what agents will receive

        Parameters
        ----------
        integration_type : PipelinesPreviewPipelineRequestIntegrationType

        integration_id : str

        producer_config : PipelinesPreviewPipelineRequestProducerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesPreviewPipelineResponse
            200

        Examples
        --------
        from fern.pipelines import (
            PipelinesPreviewPipelineRequestIntegrationType,
            PipelinesPreviewPipelineRequestProducerConfig,
            PipelinesPreviewPipelineRequestProducerConfigData,
            PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem,
            PipelinesPreviewPipelineRequestProducerConfigType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.previewpipeline(
            integration_type=PipelinesPreviewPipelineRequestIntegrationType.SLACK,
            integration_id="integration_id",
            producer_config=PipelinesPreviewPipelineRequestProducerConfig(
                type=PipelinesPreviewPipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
                data=PipelinesPreviewPipelineRequestProducerConfigData(
                    channels=[
                        PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem(
                            channel_id="channel_id",
                        )
                    ],
                ),
            ),
        )
        """
        _response = self._raw_client.previewpipeline(
            integration_type=integration_type,
            integration_id=integration_id,
            producer_config=producer_config,
            request_options=request_options,
        )
        return _response.data

    def syncpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesSyncPipelineResponse:
        """
        Manually trigger a pipeline sync to fetch new messages immediately

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesSyncPipelineResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.syncpipeline(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.syncpipeline(pipeline_id, request_options=request_options)
        return _response.data

    def listpipelinesynchistory(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesListPipelineSyncHistoryResponse:
        """
        List the sync run history for a pipeline from Temporal with error details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListPipelineSyncHistoryResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pipelines.listpipelinesynchistory(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._raw_client.listpipelinesynchistory(pipeline_id, request_options=request_options)
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

    async def listpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        offset: typing.Optional[PipelinesListPipelinesRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesListPipelinesResponse:
        """
        List all pipelines for the organization with optional filtering

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        offset : typing.Optional[PipelinesListPipelinesRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListPipelinesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.listpipelines()


        asyncio.run(main())
        """
        _response = await self._raw_client.listpipelines(
            search=search,
            integration_type=integration_type,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def createpipeline(
        self,
        *,
        name: str,
        project_id: str,
        integration_type: PipelinesCreatePipelineRequestIntegrationType,
        producer_config: PipelinesCreatePipelineRequestProducerConfig,
        subscriber_agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        subscriber_cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesCreatePipelineResponse:
        """
        Create a new pipeline (producer + feed + optionally subscribers)

        Parameters
        ----------
        name : str

        project_id : str

        integration_type : PipelinesCreatePipelineRequestIntegrationType

        producer_config : PipelinesCreatePipelineRequestProducerConfig

        subscriber_agent_ids : typing.Optional[typing.Sequence[str]]

        subscriber_cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesCreatePipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern.pipelines import (
            PipelinesCreatePipelineRequestIntegrationType,
            PipelinesCreatePipelineRequestProducerConfig,
            PipelinesCreatePipelineRequestProducerConfigData,
            PipelinesCreatePipelineRequestProducerConfigDataChannelsItem,
            PipelinesCreatePipelineRequestProducerConfigType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.createpipeline(
                name="name",
                project_id="project_id",
                integration_type=PipelinesCreatePipelineRequestIntegrationType.SLACK,
                producer_config=PipelinesCreatePipelineRequestProducerConfig(
                    type=PipelinesCreatePipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
                    data=PipelinesCreatePipelineRequestProducerConfigData(
                        channels=[
                            PipelinesCreatePipelineRequestProducerConfigDataChannelsItem(
                                channel_id="channel_id",
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createpipeline(
            name=name,
            project_id=project_id,
            integration_type=integration_type,
            producer_config=producer_config,
            subscriber_agent_ids=subscriber_agent_ids,
            subscriber_cron_schedule=subscriber_cron_schedule,
            prompt_template=prompt_template,
            request_options=request_options,
        )
        return _response.data

    async def countpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesCountPipelinesResponse:
        """
        Get the total count of pipelines, optionally filtered by project and search

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesCountPipelinesResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.countpipelines()


        asyncio.run(main())
        """
        _response = await self._raw_client.countpipelines(
            search=search, integration_type=integration_type, request_options=request_options
        )
        return _response.data

    async def getpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesGetPipelineResponse:
        """
        Get a single pipeline with details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesGetPipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.getpipeline(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpipeline(pipeline_id, request_options=request_options)
        return _response.data

    async def deletepipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesDeletePipelineResponse:
        """
        Soft delete a pipeline and cascade to feed + subscriptions

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesDeletePipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.deletepipeline(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletepipeline(pipeline_id, request_options=request_options)
        return _response.data

    async def updatepipeline(
        self,
        pipeline_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesUpdatePipelineResponse:
        """
        Update pipeline name or disable/enable it

        Parameters
        ----------
        pipeline_id : str

        name : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesUpdatePipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.updatepipeline(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatepipeline(
            pipeline_id, name=name, disabled=disabled, request_options=request_options
        )
        return _response.data

    async def previewpipeline(
        self,
        *,
        integration_type: PipelinesPreviewPipelineRequestIntegrationType,
        integration_id: str,
        producer_config: PipelinesPreviewPipelineRequestProducerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesPreviewPipelineResponse:
        """
        Fetch sample messages from integration to preview what agents will receive

        Parameters
        ----------
        integration_type : PipelinesPreviewPipelineRequestIntegrationType

        integration_id : str

        producer_config : PipelinesPreviewPipelineRequestProducerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesPreviewPipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern.pipelines import (
            PipelinesPreviewPipelineRequestIntegrationType,
            PipelinesPreviewPipelineRequestProducerConfig,
            PipelinesPreviewPipelineRequestProducerConfigData,
            PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem,
            PipelinesPreviewPipelineRequestProducerConfigType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.previewpipeline(
                integration_type=PipelinesPreviewPipelineRequestIntegrationType.SLACK,
                integration_id="integration_id",
                producer_config=PipelinesPreviewPipelineRequestProducerConfig(
                    type=PipelinesPreviewPipelineRequestProducerConfigType.SLACK_CHANNEL_READER,
                    data=PipelinesPreviewPipelineRequestProducerConfigData(
                        channels=[
                            PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem(
                                channel_id="channel_id",
                            )
                        ],
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.previewpipeline(
            integration_type=integration_type,
            integration_id=integration_id,
            producer_config=producer_config,
            request_options=request_options,
        )
        return _response.data

    async def syncpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesSyncPipelineResponse:
        """
        Manually trigger a pipeline sync to fetch new messages immediately

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesSyncPipelineResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.syncpipeline(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.syncpipeline(pipeline_id, request_options=request_options)
        return _response.data

    async def listpipelinesynchistory(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesListPipelineSyncHistoryResponse:
        """
        List the sync run history for a pipeline from Temporal with error details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListPipelineSyncHistoryResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pipelines.listpipelinesynchistory(
                pipeline_id="pipeline_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listpipelinesynchistory(pipeline_id, request_options=request_options)
        return _response.data
