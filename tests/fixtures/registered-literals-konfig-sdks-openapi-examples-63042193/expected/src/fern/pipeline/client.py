

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pipeline_continue_execution_response import PipelineContinueExecutionResponse
from ..types.pipeline_get_all_pipelines_response import PipelineGetAllPipelinesResponse
from ..types.pipeline_get_by_id_response import PipelineGetByIdResponse
from ..types.pipeline_get_by_number_response import PipelineGetByNumberResponse
from ..types.pipeline_get_configuration_by_id_response import PipelineGetConfigurationByIdResponse
from ..types.pipeline_list_recent_pipelines_response import PipelineListRecentPipelinesResponse
from ..types.pipeline_list_user_pipelines_response import PipelineListUserPipelinesResponse
from ..types.pipeline_list_workflows_response import PipelineListWorkflowsResponse
from ..types.pipeline_trigger_new_pipeline_response import PipelineTriggerNewPipelineResponse
from .raw_client import AsyncRawPipelineClient, RawPipelineClient
from .types.pipeline_continue_execution_request_parameters_value import PipelineContinueExecutionRequestParametersValue
from .types.pipeline_trigger_new_pipeline_request_parameters_value import (
    PipelineTriggerNewPipelineRequestParametersValue,
)


OMIT = typing.cast(typing.Any, ...)


class PipelineClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipelineClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipelineClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipelineClient
        """
        return self._raw_client

    def listrecentpipelines(
        self,
        *,
        org_slug: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListRecentPipelinesResponse:
        """
        Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

        Parameters
        ----------
        org_slug : typing.Optional[str]
            Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        mine : typing.Optional[bool]
            Only include entries created by your user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListRecentPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.listrecentpipelines(
            org_slug="gh/CircleCI-Public",
        )
        """
        _response = self._raw_client.listrecentpipelines(
            org_slug=org_slug, page_token=page_token, mine=mine, request_options=request_options
        )
        return _response.data

    def continueexecution(
        self,
        *,
        continuation_key: str,
        configuration: str,
        parameters: typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineContinueExecutionResponse:
        """
        Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.

        Parameters
        ----------
        continuation_key : str
            A pipeline continuation key.

        configuration : str
            A configuration string for the pipeline.

        parameters : typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]]
            An object containing pipeline parameters and their values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineContinueExecutionResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.continueexecution(
            continuation_key="continuation-key",
            configuration="configuration",
        )
        """
        _response = self._raw_client.continueexecution(
            continuation_key=continuation_key,
            configuration=configuration,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    def getbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetByIdResponse:
        """
        Returns a pipeline by the pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetByIdResponse
            A pipeline object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.getbyid(
            pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.getbyid(pipeline_id, request_options=request_options)
        return _response.data

    def getconfigurationbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetConfigurationByIdResponse:
        """
        Returns a pipeline's configuration by ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetConfigurationByIdResponse
            The configuration strings for the pipeline.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.getconfigurationbyid(
            pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.getconfigurationbyid(pipeline_id, request_options=request_options)
        return _response.data

    def listworkflows(
        self,
        pipeline_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListWorkflowsResponse:
        """
        Returns a paginated list of workflows by pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListWorkflowsResponse
            A paginated list of workflow objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.listworkflows(
            pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
        )
        """
        _response = self._raw_client.listworkflows(pipeline_id, page_token=page_token, request_options=request_options)
        return _response.data

    def getallpipelines(
        self,
        project_slug: str,
        *,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineGetAllPipelinesResponse:
        """
        Returns all pipelines for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        branch : typing.Optional[str]
            The name of a vcs branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetAllPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.getallpipelines(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getallpipelines(
            project_slug, branch=branch, page_token=page_token, request_options=request_options
        )
        return _response.data

    def triggernewpipeline(
        self,
        project_slug: str,
        *,
        parameters: typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]] = OMIT,
        branch: typing.Optional[str] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineTriggerNewPipelineResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]]
            An object containing pipeline parameters and their values.

        branch : typing.Optional[str]
            The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).

        tag : typing.Optional[str]
            The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineTriggerNewPipelineResponse
            The created pipeline.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.triggernewpipeline(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.triggernewpipeline(
            project_slug, parameters=parameters, branch=branch, tag=tag, request_options=request_options
        )
        return _response.data

    def listuserpipelines(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListUserPipelinesResponse:
        """
        Returns a sequence of all pipelines for this project triggered by the user.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListUserPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.listuserpipelines(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.listuserpipelines(
            project_slug, page_token=page_token, request_options=request_options
        )
        return _response.data

    def getbynumber(
        self, project_slug: str, pipeline_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetByNumberResponse:
        """
        Returns a pipeline by the pipeline number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        pipeline_number : typing.Any
            The number of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetByNumberResponse
            A pipeline object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pipeline.getbynumber(
            project_slug="project-slug",
            pipeline_number="pipeline-number",
        )
        """
        _response = self._raw_client.getbynumber(project_slug, pipeline_number, request_options=request_options)
        return _response.data


class AsyncPipelineClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipelineClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipelineClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipelineClient
        """
        return self._raw_client

    async def listrecentpipelines(
        self,
        *,
        org_slug: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListRecentPipelinesResponse:
        """
        Returns all pipelines for the most recently built projects (max 250) you follow in an organization.

        Parameters
        ----------
        org_slug : typing.Optional[str]
            Org slug in the form `vcs-slug/org-name`. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug` and replace the `org-name` with the organization ID (found in Organization Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        mine : typing.Optional[bool]
            Only include entries created by your user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListRecentPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.listrecentpipelines(
                org_slug="gh/CircleCI-Public",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listrecentpipelines(
            org_slug=org_slug, page_token=page_token, mine=mine, request_options=request_options
        )
        return _response.data

    async def continueexecution(
        self,
        *,
        continuation_key: str,
        configuration: str,
        parameters: typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineContinueExecutionResponse:
        """
        Continue a pipeline from the setup phase. For information on using pipeline parameters with dynamic configuration, see the [Pipeline values and parameters](https://circleci.com/docs/pipeline-variables/#pipeline-parameters-and-dynamic-configuration) docs.

        Parameters
        ----------
        continuation_key : str
            A pipeline continuation key.

        configuration : str
            A configuration string for the pipeline.

        parameters : typing.Optional[typing.Dict[str, PipelineContinueExecutionRequestParametersValue]]
            An object containing pipeline parameters and their values.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineContinueExecutionResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.continueexecution(
                continuation_key="continuation-key",
                configuration="configuration",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.continueexecution(
            continuation_key=continuation_key,
            configuration=configuration,
            parameters=parameters,
            request_options=request_options,
        )
        return _response.data

    async def getbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetByIdResponse:
        """
        Returns a pipeline by the pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetByIdResponse
            A pipeline object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.getbyid(
                pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbyid(pipeline_id, request_options=request_options)
        return _response.data

    async def getconfigurationbyid(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetConfigurationByIdResponse:
        """
        Returns a pipeline's configuration by ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetConfigurationByIdResponse
            The configuration strings for the pipeline.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.getconfigurationbyid(
                pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getconfigurationbyid(pipeline_id, request_options=request_options)
        return _response.data

    async def listworkflows(
        self,
        pipeline_id: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListWorkflowsResponse:
        """
        Returns a paginated list of workflows by pipeline ID.

        Parameters
        ----------
        pipeline_id : str
            The unique ID of the pipeline.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListWorkflowsResponse
            A paginated list of workflow objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.listworkflows(
                pipeline_id="5034460f-c7c4-4c43-9457-de07e2029e7b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listworkflows(
            pipeline_id, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def getallpipelines(
        self,
        project_slug: str,
        *,
        branch: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineGetAllPipelinesResponse:
        """
        Returns all pipelines for this project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        branch : typing.Optional[str]
            The name of a vcs branch.

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetAllPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.getallpipelines(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getallpipelines(
            project_slug, branch=branch, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def triggernewpipeline(
        self,
        project_slug: str,
        *,
        parameters: typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]] = OMIT,
        branch: typing.Optional[str] = OMIT,
        tag: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineTriggerNewPipelineResponse:
        """
        Not yet available to projects that use GitLab or GitHub App. Triggers a new pipeline on the project.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        parameters : typing.Optional[typing.Dict[str, PipelineTriggerNewPipelineRequestParametersValue]]
            An object containing pipeline parameters and their values.

        branch : typing.Optional[str]
            The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that `branch` and `tag` are mutually exclusive. To trigger a pipeline for a PR by number use `pull/<number>/head` for the PR ref or `pull/<number>/merge` for the merge ref (GitHub only).

        tag : typing.Optional[str]
            The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that `branch` and `tag` are mutually exclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineTriggerNewPipelineResponse
            The created pipeline.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.triggernewpipeline(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.triggernewpipeline(
            project_slug, parameters=parameters, branch=branch, tag=tag, request_options=request_options
        )
        return _response.data

    async def listuserpipelines(
        self,
        project_slug: str,
        *,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineListUserPipelinesResponse:
        """
        Returns a sequence of all pipelines for this project triggered by the user.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        page_token : typing.Optional[str]
            A token to retrieve the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineListUserPipelinesResponse
            A sequence of pipelines.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.listuserpipelines(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listuserpipelines(
            project_slug, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def getbynumber(
        self, project_slug: str, pipeline_number: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelineGetByNumberResponse:
        """
        Returns a pipeline by the pipeline number.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        pipeline_number : typing.Any
            The number of the pipeline.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelineGetByNumberResponse
            A pipeline object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pipeline.getbynumber(
                project_slug="project-slug",
                pipeline_number="pipeline-number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbynumber(project_slug, pipeline_number, request_options=request_options)
        return _response.data
