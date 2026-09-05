

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_with_default_param import AppLimitWithDefaultParam
from ..types.comparison_experiment_id import ComparisonExperimentId
from ..types.ending_before import EndingBefore
from ..types.experiment import Experiment
from ..types.experiment_id_param import ExperimentIdParam
from ..types.experiment_name import ExperimentName
from ..types.feedback_experiment_item import FeedbackExperimentItem
from ..types.feedback_response_schema import FeedbackResponseSchema
from ..types.fetch_experiment_events_response import FetchExperimentEventsResponse
from ..types.fetch_limit import FetchLimit
from ..types.fetch_limit_param import FetchLimitParam
from ..types.fetch_pagination_cursor import FetchPaginationCursor
from ..types.ids import Ids
from ..types.insert_events_response import InsertEventsResponse
from ..types.insert_experiment_event import InsertExperimentEvent
from ..types.max_root_span_id import MaxRootSpanId
from ..types.max_xact_id import MaxXactId
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.repo_info import RepoInfo
from ..types.starting_after import StartingAfter
from ..types.summarize_experiment_response import SummarizeExperimentResponse
from ..types.summarize_scores import SummarizeScores
from ..types.version import Version
from .raw_client import AsyncRawExperimentsClient, RawExperimentsClient
from .types.get_experiment_response import GetExperimentResponse


OMIT = typing.cast(typing.Any, ...)


class ExperimentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExperimentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExperimentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExperimentsClient
        """
        return self._raw_client

    def get_experiment(
        self,
        *,
        limit: typing.Optional[AppLimitWithDefaultParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        experiment_name: typing.Optional[ExperimentName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetExperimentResponse:
        """
        List out all experiments. The experiments are sorted by creation date, with the most recently-created experiments coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitWithDefaultParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        experiment_name : typing.Optional[ExperimentName]
            Name of the experiment to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExperimentResponse
            Returns a list of experiment objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.get_experiment()
        """
        _response = self._raw_client.get_experiment(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            experiment_name=experiment_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_experiment(
        self,
        *,
        project_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        repo_info: typing.Optional[RepoInfo] = OMIT,
        base_exp_id: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        dataset_version: typing.Optional[str] = OMIT,
        parameters_id: typing.Optional[str] = OMIT,
        parameters_version: typing.Optional[str] = OMIT,
        public: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        ensure_new: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Experiment:
        """
        Create a new experiment. If there is an existing experiment in the project with the same name as the one specified in the request, will return the existing experiment unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the experiment belongs under

        name : typing.Optional[str]
            Name of the experiment. Within a project, experiment names are unique

        description : typing.Optional[str]
            Textual description of the experiment

        repo_info : typing.Optional[RepoInfo]

        base_exp_id : typing.Optional[str]
            Id of default base experiment to compare against when viewing this experiment

        dataset_id : typing.Optional[str]
            Identifier of the linked dataset, or null if the experiment is not linked to a dataset

        dataset_version : typing.Optional[str]
            Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.

        parameters_id : typing.Optional[str]
            Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters

        parameters_version : typing.Optional[str]
            Version number of the linked saved parameters object the experiment was run against.

        public : typing.Optional[bool]
            Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the experiment

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the experiment

        ensure_new : typing.Optional[bool]
            Normally, creating an experiment with the same name as an existing experiment will return the existing one un-modified. But if `ensure_new` is true, registration will generate a new experiment with a unique name in case of a conflict.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the new experiment object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.post_experiment(
            project_id="project_id",
        )
        """
        _response = self._raw_client.post_experiment(
            project_id=project_id,
            name=name,
            description=description,
            repo_info=repo_info,
            base_exp_id=base_exp_id,
            dataset_id=dataset_id,
            dataset_version=dataset_version,
            parameters_id=parameters_id,
            parameters_version=parameters_version,
            public=public,
            metadata=metadata,
            tags=tags,
            ensure_new=ensure_new,
            request_options=request_options,
        )
        return _response.data

    def get_experiment_id(
        self, experiment_id: ExperimentIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Experiment:
        """
        Get an experiment object by its id

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the experiment object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.get_experiment_id(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.get_experiment_id(experiment_id, request_options=request_options)
        return _response.data

    def delete_experiment_id(
        self, experiment_id: ExperimentIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Experiment:
        """
        Delete an experiment object by its id

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the deleted experiment object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.delete_experiment_id(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.delete_experiment_id(experiment_id, request_options=request_options)
        return _response.data

    def patch_experiment_id(
        self,
        experiment_id: ExperimentIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        repo_info: typing.Optional[RepoInfo] = OMIT,
        base_exp_id: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        dataset_version: typing.Optional[str] = OMIT,
        parameters_id: typing.Optional[str] = OMIT,
        parameters_version: typing.Optional[str] = OMIT,
        public: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Experiment:
        """
        Partially update an experiment object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        name : typing.Optional[str]
            Name of the experiment. Within a project, experiment names are unique

        description : typing.Optional[str]
            Textual description of the experiment

        repo_info : typing.Optional[RepoInfo]

        base_exp_id : typing.Optional[str]
            Id of default base experiment to compare against when viewing this experiment

        dataset_id : typing.Optional[str]
            Identifier of the linked dataset, or null if the experiment is not linked to a dataset

        dataset_version : typing.Optional[str]
            Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.

        parameters_id : typing.Optional[str]
            Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters

        parameters_version : typing.Optional[str]
            Version number of the linked saved parameters object the experiment was run against.

        public : typing.Optional[bool]
            Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the experiment

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the experiment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the experiment object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.patch_experiment_id(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.patch_experiment_id(
            experiment_id,
            name=name,
            description=description,
            repo_info=repo_info,
            base_exp_id=base_exp_id,
            dataset_id=dataset_id,
            dataset_version=dataset_version,
            parameters_id=parameters_id,
            parameters_version=parameters_version,
            public=public,
            metadata=metadata,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def post_experiment_id_insert(
        self,
        experiment_id: ExperimentIdParam,
        *,
        events: typing.Sequence[InsertExperimentEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the experiment

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        events : typing.Sequence[InsertExperimentEvent]
            A list of experiment events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsertEventsResponse
            Returns the inserted row ids

        Examples
        --------
        from fern import FernApi, InsertExperimentEvent

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.post_experiment_id_insert(
            experiment_id="experiment_id",
            events=[InsertExperimentEvent()],
        )
        """
        _response = self._raw_client.post_experiment_id_insert(
            experiment_id, events=events, request_options=request_options
        )
        return _response.data

    def get_experiment_id_fetch(
        self,
        experiment_id: ExperimentIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchExperimentEventsResponse:
        """
        Fetch the events in an experiment. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchExperimentEventsResponse
            Returns the fetched rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.get_experiment_id_fetch(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.get_experiment_id_fetch(
            experiment_id,
            limit=limit,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def post_experiment_id_fetch(
        self,
        experiment_id: ExperimentIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchExperimentEventsResponse:
        """
        Fetch the events in an experiment. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchExperimentEventsResponse
            Returns the fetched rows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.post_experiment_id_fetch(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.post_experiment_id_fetch(
            experiment_id,
            limit=limit,
            cursor=cursor,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def post_experiment_id_feedback(
        self,
        experiment_id: ExperimentIdParam,
        *,
        feedback: typing.Sequence[FeedbackExperimentItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of experiment events

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        feedback : typing.Sequence[FeedbackExperimentItem]
            A list of experiment feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponseSchema
            Returns a success status

        Examples
        --------
        from fern import FeedbackExperimentItem, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.post_experiment_id_feedback(
            experiment_id="experiment_id",
            feedback=[
                FeedbackExperimentItem(
                    id="id",
                )
            ],
        )
        """
        _response = self._raw_client.post_experiment_id_feedback(
            experiment_id, feedback=feedback, request_options=request_options
        )
        return _response.data

    def get_experiment_id_summarize(
        self,
        experiment_id: ExperimentIdParam,
        *,
        summarize_scores: typing.Optional[SummarizeScores] = None,
        comparison_experiment_id: typing.Optional[ComparisonExperimentId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeExperimentResponse:
        """
        Summarize experiment

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        summarize_scores : typing.Optional[SummarizeScores]
            Whether to summarize the scores and metrics. If false (or omitted), only the metadata will be returned.

        comparison_experiment_id : typing.Optional[ComparisonExperimentId]
            The experiment to compare against, if summarizing scores and metrics. If omitted, will fall back to the `base_exp_id` stored in the experiment metadata, and then to the most recent experiment run in the same project. Must pass `summarize_scores=true` for this id to be used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeExperimentResponse
            Experiment summary

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.experiments.get_experiment_id_summarize(
            experiment_id="experiment_id",
        )
        """
        _response = self._raw_client.get_experiment_id_summarize(
            experiment_id,
            summarize_scores=summarize_scores,
            comparison_experiment_id=comparison_experiment_id,
            request_options=request_options,
        )
        return _response.data


class AsyncExperimentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExperimentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExperimentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExperimentsClient
        """
        return self._raw_client

    async def get_experiment(
        self,
        *,
        limit: typing.Optional[AppLimitWithDefaultParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        experiment_name: typing.Optional[ExperimentName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetExperimentResponse:
        """
        List out all experiments. The experiments are sorted by creation date, with the most recently-created experiments coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitWithDefaultParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        experiment_name : typing.Optional[ExperimentName]
            Name of the experiment to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExperimentResponse
            Returns a list of experiment objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.get_experiment()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_experiment(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            experiment_name=experiment_name,
            project_name=project_name,
            project_id=project_id,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_experiment(
        self,
        *,
        project_id: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        repo_info: typing.Optional[RepoInfo] = OMIT,
        base_exp_id: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        dataset_version: typing.Optional[str] = OMIT,
        parameters_id: typing.Optional[str] = OMIT,
        parameters_version: typing.Optional[str] = OMIT,
        public: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        ensure_new: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Experiment:
        """
        Create a new experiment. If there is an existing experiment in the project with the same name as the one specified in the request, will return the existing experiment unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the experiment belongs under

        name : typing.Optional[str]
            Name of the experiment. Within a project, experiment names are unique

        description : typing.Optional[str]
            Textual description of the experiment

        repo_info : typing.Optional[RepoInfo]

        base_exp_id : typing.Optional[str]
            Id of default base experiment to compare against when viewing this experiment

        dataset_id : typing.Optional[str]
            Identifier of the linked dataset, or null if the experiment is not linked to a dataset

        dataset_version : typing.Optional[str]
            Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.

        parameters_id : typing.Optional[str]
            Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters

        parameters_version : typing.Optional[str]
            Version number of the linked saved parameters object the experiment was run against.

        public : typing.Optional[bool]
            Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the experiment

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the experiment

        ensure_new : typing.Optional[bool]
            Normally, creating an experiment with the same name as an existing experiment will return the existing one un-modified. But if `ensure_new` is true, registration will generate a new experiment with a unique name in case of a conflict.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the new experiment object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.post_experiment(
                project_id="project_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_experiment(
            project_id=project_id,
            name=name,
            description=description,
            repo_info=repo_info,
            base_exp_id=base_exp_id,
            dataset_id=dataset_id,
            dataset_version=dataset_version,
            parameters_id=parameters_id,
            parameters_version=parameters_version,
            public=public,
            metadata=metadata,
            tags=tags,
            ensure_new=ensure_new,
            request_options=request_options,
        )
        return _response.data

    async def get_experiment_id(
        self, experiment_id: ExperimentIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Experiment:
        """
        Get an experiment object by its id

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the experiment object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.get_experiment_id(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_experiment_id(experiment_id, request_options=request_options)
        return _response.data

    async def delete_experiment_id(
        self, experiment_id: ExperimentIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Experiment:
        """
        Delete an experiment object by its id

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the deleted experiment object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.delete_experiment_id(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_experiment_id(experiment_id, request_options=request_options)
        return _response.data

    async def patch_experiment_id(
        self,
        experiment_id: ExperimentIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        repo_info: typing.Optional[RepoInfo] = OMIT,
        base_exp_id: typing.Optional[str] = OMIT,
        dataset_id: typing.Optional[str] = OMIT,
        dataset_version: typing.Optional[str] = OMIT,
        parameters_id: typing.Optional[str] = OMIT,
        parameters_version: typing.Optional[str] = OMIT,
        public: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Experiment:
        """
        Partially update an experiment object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        name : typing.Optional[str]
            Name of the experiment. Within a project, experiment names are unique

        description : typing.Optional[str]
            Textual description of the experiment

        repo_info : typing.Optional[RepoInfo]

        base_exp_id : typing.Optional[str]
            Id of default base experiment to compare against when viewing this experiment

        dataset_id : typing.Optional[str]
            Identifier of the linked dataset, or null if the experiment is not linked to a dataset

        dataset_version : typing.Optional[str]
            Version number of the linked dataset the experiment was run against. This can be used to reproduce the experiment after the dataset has been modified.

        parameters_id : typing.Optional[str]
            Identifier of the linked saved parameters object, or null if the experiment is not linked to saved parameters

        parameters_version : typing.Optional[str]
            Version number of the linked saved parameters object the experiment was run against.

        public : typing.Optional[bool]
            Whether or not the experiment is public. Public experiments can be viewed by anybody inside or outside the organization

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the experiment

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the experiment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Experiment
            Returns the experiment object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.patch_experiment_id(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_experiment_id(
            experiment_id,
            name=name,
            description=description,
            repo_info=repo_info,
            base_exp_id=base_exp_id,
            dataset_id=dataset_id,
            dataset_version=dataset_version,
            parameters_id=parameters_id,
            parameters_version=parameters_version,
            public=public,
            metadata=metadata,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def post_experiment_id_insert(
        self,
        experiment_id: ExperimentIdParam,
        *,
        events: typing.Sequence[InsertExperimentEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the experiment

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        events : typing.Sequence[InsertExperimentEvent]
            A list of experiment events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InsertEventsResponse
            Returns the inserted row ids

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, InsertExperimentEvent

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.post_experiment_id_insert(
                experiment_id="experiment_id",
                events=[InsertExperimentEvent()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_experiment_id_insert(
            experiment_id, events=events, request_options=request_options
        )
        return _response.data

    async def get_experiment_id_fetch(
        self,
        experiment_id: ExperimentIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchExperimentEventsResponse:
        """
        Fetch the events in an experiment. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchExperimentEventsResponse
            Returns the fetched rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.get_experiment_id_fetch(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_experiment_id_fetch(
            experiment_id,
            limit=limit,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def post_experiment_id_fetch(
        self,
        experiment_id: ExperimentIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FetchExperimentEventsResponse:
        """
        Fetch the events in an experiment. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FetchExperimentEventsResponse
            Returns the fetched rows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.post_experiment_id_fetch(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_experiment_id_fetch(
            experiment_id,
            limit=limit,
            cursor=cursor,
            max_xact_id=max_xact_id,
            max_root_span_id=max_root_span_id,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def post_experiment_id_feedback(
        self,
        experiment_id: ExperimentIdParam,
        *,
        feedback: typing.Sequence[FeedbackExperimentItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of experiment events

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        feedback : typing.Sequence[FeedbackExperimentItem]
            A list of experiment feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeedbackResponseSchema
            Returns a success status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FeedbackExperimentItem

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.post_experiment_id_feedback(
                experiment_id="experiment_id",
                feedback=[
                    FeedbackExperimentItem(
                        id="id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_experiment_id_feedback(
            experiment_id, feedback=feedback, request_options=request_options
        )
        return _response.data

    async def get_experiment_id_summarize(
        self,
        experiment_id: ExperimentIdParam,
        *,
        summarize_scores: typing.Optional[SummarizeScores] = None,
        comparison_experiment_id: typing.Optional[ComparisonExperimentId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SummarizeExperimentResponse:
        """
        Summarize experiment

        Parameters
        ----------
        experiment_id : ExperimentIdParam
            Experiment id

        summarize_scores : typing.Optional[SummarizeScores]
            Whether to summarize the scores and metrics. If false (or omitted), only the metadata will be returned.

        comparison_experiment_id : typing.Optional[ComparisonExperimentId]
            The experiment to compare against, if summarizing scores and metrics. If omitted, will fall back to the `base_exp_id` stored in the experiment metadata, and then to the most recent experiment run in the same project. Must pass `summarize_scores=true` for this id to be used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SummarizeExperimentResponse
            Experiment summary

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.experiments.get_experiment_id_summarize(
                experiment_id="experiment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_experiment_id_summarize(
            experiment_id,
            summarize_scores=summarize_scores,
            comparison_experiment_id=comparison_experiment_id,
            request_options=request_options,
        )
        return _response.data
