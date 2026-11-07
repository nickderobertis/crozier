

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.workflow_configuration_dto import WorkflowConfigurationDto
from ..types.workflow_export_response_dto import WorkflowExportResponseDto
from .raw_client import AsyncRawEntityModelWorkflowClient, RawEntityModelWorkflowClient
from .types.workflow_import_request_dto_import_mode import WorkflowImportRequestDtoImportMode


OMIT = typing.cast(typing.Any, ...)


class EntityModelWorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntityModelWorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntityModelWorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntityModelWorkflowClient
        """
        return self._raw_client

    def export_entity_model_workflow(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowExportResponseDto:
        """
        Exports all workflow configurations for a specific entity type.

        Since one entity type can have multiple workflows (selected by workflow-level conditions),
        this endpoint returns a collection of all workflows configured for the entity type.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowExportResponseDto
            Workflows exported successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model_workflow.export_entity_model_workflow(
            entity_name="entityName",
            model_version=1,
        )
        """
        _response = self._raw_client.export_entity_model_workflow(
            entity_name, model_version, request_options=request_options
        )
        return _response.data

    def import_entity_model_workflow(
        self,
        entity_name: str,
        model_version: int,
        *,
        workflows: typing.Sequence[WorkflowConfigurationDto],
        import_mode: typing.Optional[WorkflowImportRequestDtoImportMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports or updates workflow configurations for a specific entity type.

        Since workflow name must be unique per entity model, this endpoint will either create
        new workflow or update existing workflow with the same name.

        The workflow configuration structure is defined by versioned schemas and may vary
        depending on the version specified in the configuration.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        workflows : typing.Sequence[WorkflowConfigurationDto]
            Array of workflow configurations to import

        import_mode : typing.Optional[WorkflowImportRequestDtoImportMode]
            Import mode for handling existing workflows

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, StateDefinitionDto, WorkflowConfigurationDto

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_model_workflow.import_entity_model_workflow(
            entity_name="entityName",
            model_version=1,
            workflows=[
                WorkflowConfigurationDto(
                    version="version",
                    name="name",
                    initial_state="initialState",
                    states={"key": StateDefinitionDto()},
                )
            ],
        )
        """
        _response = self._raw_client.import_entity_model_workflow(
            entity_name, model_version, workflows=workflows, import_mode=import_mode, request_options=request_options
        )
        return _response.data


class AsyncEntityModelWorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntityModelWorkflowClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntityModelWorkflowClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntityModelWorkflowClient
        """
        return self._raw_client

    async def export_entity_model_workflow(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowExportResponseDto:
        """
        Exports all workflow configurations for a specific entity type.

        Since one entity type can have multiple workflows (selected by workflow-level conditions),
        this endpoint returns a collection of all workflows configured for the entity type.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkflowExportResponseDto
            Workflows exported successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model_workflow.export_entity_model_workflow(
                entity_name="entityName",
                model_version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_entity_model_workflow(
            entity_name, model_version, request_options=request_options
        )
        return _response.data

    async def import_entity_model_workflow(
        self,
        entity_name: str,
        model_version: int,
        *,
        workflows: typing.Sequence[WorkflowConfigurationDto],
        import_mode: typing.Optional[WorkflowImportRequestDtoImportMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports or updates workflow configurations for a specific entity type.

        Since workflow name must be unique per entity model, this endpoint will either create
        new workflow or update existing workflow with the same name.

        The workflow configuration structure is defined by versioned schemas and may vary
        depending on the version specified in the configuration.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        workflows : typing.Sequence[WorkflowConfigurationDto]
            Array of workflow configurations to import

        import_mode : typing.Optional[WorkflowImportRequestDtoImportMode]
            Import mode for handling existing workflows

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, StateDefinitionDto, WorkflowConfigurationDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_model_workflow.import_entity_model_workflow(
                entity_name="entityName",
                model_version=1,
                workflows=[
                    WorkflowConfigurationDto(
                        version="version",
                        name="name",
                        initial_state="initialState",
                        states={"key": StateDefinitionDto()},
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_entity_model_workflow(
            entity_name, model_version, workflows=workflows, import_mode=import_mode, request_options=request_options
        )
        return _response.data
