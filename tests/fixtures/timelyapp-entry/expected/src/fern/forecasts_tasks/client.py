

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1forecast import V1Forecast
from ..types.v1forecast_summary import V1ForecastSummary
from .raw_client import AsyncRawForecastsTasksClient, RawForecastsTasksClient
from .types.list_task_summaries_request_completed import ListTaskSummariesRequestCompleted
from .types.list_task_summaries_request_resource import ListTaskSummariesRequestResource
from .types.list_tasks_request_completed import ListTasksRequestCompleted
from .types.list_tasks_request_order import ListTasksRequestOrder
from .types.list_tasks_request_sort import ListTasksRequestSort
from .types.v1forecasts_create_forecast import V1ForecastsCreateForecast
from .types.v1forecasts_update_forecast import V1ForecastsUpdateForecast


OMIT = typing.cast(typing.Any, ...)


class ForecastsTasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawForecastsTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawForecastsTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawForecastsTasksClient
        """
        return self._raw_client

    def list_tasks(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTasksRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTasksRequestSort] = None,
        order: typing.Optional[ListTasksRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Forecast]:
        """
        List all tasks in the account. Tasks are returned in a paginated format with optional filtering by date range, user, project, and completion status.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Filter tasks from this date (inclusive)

        upto : typing.Optional[dt.date]
            Filter tasks up to this date (inclusive)

        completed : typing.Optional[ListTasksRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs, or "active"/"archived" to filter by project status

        forecast_ids : typing.Optional[str]
            Comma-separated list of task IDs to filter by

        sort : typing.Optional[ListTasksRequestSort]
            Field to sort by (default: updated_at)

        order : typing.Optional[ListTasksRequestOrder]
            Sort order (default: desc)

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Forecast]
            Tasks list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.list_tasks(
            account_id=1,
        )
        """
        _response = self._raw_client.list_tasks(
            account_id,
            since=since,
            upto=upto,
            completed=completed,
            user_ids=user_ids,
            project_ids=project_ids,
            forecast_ids=forecast_ids,
            sort=sort,
            order=order,
            per_page=per_page,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def create_task(
        self,
        account_id: int,
        *,
        forecast: V1ForecastsCreateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Forecast:
        """
        Create a new task. Requires the Planning feature to be enabled.

        Parameters
        ----------
        account_id : int
            Account ID

        forecast : V1ForecastsCreateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task created

        Examples
        --------
        from fern.forecasts_tasks import V1ForecastsCreateForecast

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.create_task(
            account_id=1,
            forecast=V1ForecastsCreateForecast(
                title="Implement API documentation",
                from_="2024-01-01",
                to="2024-01-08",
                project_id=1,
                estimated_minutes=480,
            ),
        )
        """
        _response = self._raw_client.create_task(account_id, forecast=forecast, request_options=request_options)
        return _response.data

    def show_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Forecast:
        """
        Retrieve details for a specific task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.show_task(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.show_task(account_id, id, request_options=request_options)
        return _response.data

    def delete_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Task deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.delete_task(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_task(account_id, id, request_options=request_options)
        return _response.data

    def update_task(
        self,
        account_id: int,
        id: int,
        *,
        forecast: V1ForecastsUpdateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Forecast:
        """
        Update an existing task. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        forecast : V1ForecastsUpdateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task updated

        Examples
        --------
        from fern.forecasts_tasks import V1ForecastsUpdateForecast

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.update_task(
            account_id=1,
            id=1,
            forecast=V1ForecastsUpdateForecast(
                title="Updated task title",
            ),
        )
        """
        _response = self._raw_client.update_task(account_id, id, forecast=forecast, request_options=request_options)
        return _response.data

    def list_task_summaries(
        self,
        account_id: int,
        resource: ListTaskSummariesRequestResource,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTaskSummariesRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ForecastSummary]:
        """
        Get task summaries grouped by resource type (users or projects). Returns aggregate counts and duration totals.

        Parameters
        ----------
        account_id : int
            Account ID

        resource : ListTaskSummariesRequestResource
            Resource type to group summaries by

        since : typing.Optional[dt.date]
            Filter tasks from this date

        until : typing.Optional[dt.date]
            Filter tasks up to this date

        completed : typing.Optional[ListTaskSummariesRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated project IDs to filter by

        forecast_ids : typing.Optional[str]
            Comma-separated task IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ForecastSummary]
            Task summaries

        Examples
        --------
        from fern.forecasts_tasks import ListTaskSummariesRequestResource

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.forecasts_tasks.list_task_summaries(
            account_id=1,
            resource=ListTaskSummariesRequestResource.USERS,
        )
        """
        _response = self._raw_client.list_task_summaries(
            account_id,
            resource,
            since=since,
            until=until,
            completed=completed,
            user_ids=user_ids,
            project_ids=project_ids,
            forecast_ids=forecast_ids,
            request_options=request_options,
        )
        return _response.data


class AsyncForecastsTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawForecastsTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawForecastsTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawForecastsTasksClient
        """
        return self._raw_client

    async def list_tasks(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTasksRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTasksRequestSort] = None,
        order: typing.Optional[ListTasksRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Forecast]:
        """
        List all tasks in the account. Tasks are returned in a paginated format with optional filtering by date range, user, project, and completion status.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Filter tasks from this date (inclusive)

        upto : typing.Optional[dt.date]
            Filter tasks up to this date (inclusive)

        completed : typing.Optional[ListTasksRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs, or "active"/"archived" to filter by project status

        forecast_ids : typing.Optional[str]
            Comma-separated list of task IDs to filter by

        sort : typing.Optional[ListTasksRequestSort]
            Field to sort by (default: updated_at)

        order : typing.Optional[ListTasksRequestOrder]
            Sort order (default: desc)

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Forecast]
            Tasks list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.list_tasks(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tasks(
            account_id,
            since=since,
            upto=upto,
            completed=completed,
            user_ids=user_ids,
            project_ids=project_ids,
            forecast_ids=forecast_ids,
            sort=sort,
            order=order,
            per_page=per_page,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def create_task(
        self,
        account_id: int,
        *,
        forecast: V1ForecastsCreateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Forecast:
        """
        Create a new task. Requires the Planning feature to be enabled.

        Parameters
        ----------
        account_id : int
            Account ID

        forecast : V1ForecastsCreateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task created

        Examples
        --------
        import asyncio

        from fern.forecasts_tasks import V1ForecastsCreateForecast

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.create_task(
                account_id=1,
                forecast=V1ForecastsCreateForecast(
                    title="Implement API documentation",
                    from_="2024-01-01",
                    to="2024-01-08",
                    project_id=1,
                    estimated_minutes=480,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_task(account_id, forecast=forecast, request_options=request_options)
        return _response.data

    async def show_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Forecast:
        """
        Retrieve details for a specific task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.show_task(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_task(account_id, id, request_options=request_options)
        return _response.data

    async def delete_task(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a task.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Task deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.delete_task(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_task(account_id, id, request_options=request_options)
        return _response.data

    async def update_task(
        self,
        account_id: int,
        id: int,
        *,
        forecast: V1ForecastsUpdateForecast,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Forecast:
        """
        Update an existing task. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Task ID

        forecast : V1ForecastsUpdateForecast

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Forecast
            Task updated

        Examples
        --------
        import asyncio

        from fern.forecasts_tasks import V1ForecastsUpdateForecast

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.update_task(
                account_id=1,
                id=1,
                forecast=V1ForecastsUpdateForecast(
                    title="Updated task title",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_task(
            account_id, id, forecast=forecast, request_options=request_options
        )
        return _response.data

    async def list_task_summaries(
        self,
        account_id: int,
        resource: ListTaskSummariesRequestResource,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        completed: typing.Optional[ListTaskSummariesRequestCompleted] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        forecast_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ForecastSummary]:
        """
        Get task summaries grouped by resource type (users or projects). Returns aggregate counts and duration totals.

        Parameters
        ----------
        account_id : int
            Account ID

        resource : ListTaskSummariesRequestResource
            Resource type to group summaries by

        since : typing.Optional[dt.date]
            Filter tasks from this date

        until : typing.Optional[dt.date]
            Filter tasks up to this date

        completed : typing.Optional[ListTaskSummariesRequestCompleted]
            Filter by completion status

        user_ids : typing.Optional[str]
            Comma-separated user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated project IDs to filter by

        forecast_ids : typing.Optional[str]
            Comma-separated task IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ForecastSummary]
            Task summaries

        Examples
        --------
        import asyncio

        from fern.forecasts_tasks import ListTaskSummariesRequestResource

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.forecasts_tasks.list_task_summaries(
                account_id=1,
                resource=ListTaskSummariesRequestResource.USERS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_task_summaries(
            account_id,
            resource,
            since=since,
            until=until,
            completed=completed,
            user_ids=user_ids,
            project_ids=project_ids,
            forecast_ids=forecast_ids,
            request_options=request_options,
        )
        return _response.data
