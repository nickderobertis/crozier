

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feedback_type import FeedbackType
from ..types.provider_trace import ProviderTrace
from ..types.step import Step
from ..types.step_metrics import StepMetrics
from .raw_client import AsyncRawStepsClient, RawStepsClient
from .types.list_messages_for_step_request_order import ListMessagesForStepRequestOrder
from .types.list_messages_for_step_request_order_by import ListMessagesForStepRequestOrderBy
from .types.list_messages_for_step_response_item import ListMessagesForStepResponseItem
from .types.list_steps_request_feedback import ListStepsRequestFeedback
from .types.list_steps_request_order import ListStepsRequestOrder
from .types.list_steps_request_order_by import ListStepsRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class StepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStepsClient
        """
        return self._raw_client

    def list_steps(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsRequestOrder] = None,
        order_by: typing.Optional[ListStepsRequestOrderBy] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Sequence[str]] = None,
        feedback: typing.Optional[ListStepsRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        List steps with optional pagination and date filters.

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[ListStepsRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsRequestOrderBy]
            Field to sort by

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Sequence[str]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[ListStepsRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        project : typing.Optional[str]
            Filter by project slug to associate with the group (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.list_steps()
        """
        _response = self._raw_client.list_steps(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            start_date=start_date,
            end_date=end_date,
            model=model,
            agent_id=agent_id,
            trace_ids=trace_ids,
            feedback=feedback,
            has_feedback=has_feedback,
            tags=tags,
            project_id=project_id,
            project=project,
            request_options=request_options,
        )
        return _response.data

    def retrieve_step(self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Step:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.retrieve_step(
            step_id="step-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_step(step_id, request_options=request_options)
        return _response.data

    def retrieve_metrics_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StepMetrics:
        """
        Get step metrics by step ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StepMetrics
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.retrieve_metrics_for_step(
            step_id="step-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_metrics_for_step(step_id, request_options=request_options)
        return _response.data

    def retrieve_trace_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProviderTrace]:
        """
        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProviderTrace]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.retrieve_trace_for_step(
            step_id="step-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_trace_for_step(step_id, request_options=request_options)
        return _response.data

    def modify_feedback_for_step(
        self,
        step_id: str,
        *,
        feedback: typing.Optional[FeedbackType] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Step:
        """
        Modify feedback for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        feedback : typing.Optional[FeedbackType]
            Whether this feedback is positive or negative

        tags : typing.Optional[typing.Sequence[str]]
            Feedback tags to add to the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.modify_feedback_for_step(
            step_id="step-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.modify_feedback_for_step(
            step_id, feedback=feedback, tags=tags, request_options=request_options
        )
        return _response.data

    def list_messages_for_step(
        self,
        step_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForStepRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForStepRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListMessagesForStepResponseItem]:
        """
        List messages for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForStepRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForStepRequestOrderBy]
            Sort by field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListMessagesForStepResponseItem]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.steps.list_messages_for_step(
            step_id="step-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_messages_for_step(
            step_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data


class AsyncStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStepsClient
        """
        return self._raw_client

    async def list_steps(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsRequestOrder] = None,
        order_by: typing.Optional[ListStepsRequestOrderBy] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Sequence[str]] = None,
        feedback: typing.Optional[ListStepsRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        List steps with optional pagination and date filters.

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[ListStepsRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsRequestOrderBy]
            Field to sort by

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Sequence[str]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[ListStepsRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Sequence[str]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        project : typing.Optional[str]
            Filter by project slug to associate with the group (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.list_steps()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_steps(
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            start_date=start_date,
            end_date=end_date,
            model=model,
            agent_id=agent_id,
            trace_ids=trace_ids,
            feedback=feedback,
            has_feedback=has_feedback,
            tags=tags,
            project_id=project_id,
            project=project,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_step(self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Step:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.retrieve_step(
                step_id="step-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_step(step_id, request_options=request_options)
        return _response.data

    async def retrieve_metrics_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StepMetrics:
        """
        Get step metrics by step ID.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StepMetrics
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.retrieve_metrics_for_step(
                step_id="step-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_metrics_for_step(step_id, request_options=request_options)
        return _response.data

    async def retrieve_trace_for_step(
        self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ProviderTrace]:
        """
        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[ProviderTrace]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.retrieve_trace_for_step(
                step_id="step-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_trace_for_step(step_id, request_options=request_options)
        return _response.data

    async def modify_feedback_for_step(
        self,
        step_id: str,
        *,
        feedback: typing.Optional[FeedbackType] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Step:
        """
        Modify feedback for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        feedback : typing.Optional[FeedbackType]
            Whether this feedback is positive or negative

        tags : typing.Optional[typing.Sequence[str]]
            Feedback tags to add to the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.modify_feedback_for_step(
                step_id="step-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_feedback_for_step(
            step_id, feedback=feedback, tags=tags, request_options=request_options
        )
        return _response.data

    async def list_messages_for_step(
        self,
        step_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForStepRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForStepRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ListMessagesForStepResponseItem]:
        """
        List messages for a given step.

        Parameters
        ----------
        step_id : str
            The ID of the step in the format 'step-<uuid4>'

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForStepRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForStepRequestOrderBy]
            Sort by field

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListMessagesForStepResponseItem]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.steps.list_messages_for_step(
                step_id="step-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages_for_step(
            step_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data
