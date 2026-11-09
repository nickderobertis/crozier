

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_ticket_priority import CommonTicketPriority
from ..types.common_ticket_status import CommonTicketStatus
from ..types.ticket_create_or_update_task_response import TicketCreateOrUpdateTaskResponse
from ..types.ticket_get_task_response import TicketGetTaskResponse
from ..types.ticket_get_tasks_response import TicketGetTasksResponse
from .raw_client import AsyncRawTicketTaskClient, RawTicketTaskClient


OMIT = typing.cast(typing.Any, ...)


class TicketTaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketTaskClient
        """
        return self._raw_client

    def ticket_task_get_task(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetTaskResponse:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_task.ticket_task_get_task(
            id="id",
        )
        """
        _response = self._raw_client.ticket_task_get_task(id, fields=fields, request_options=request_options)
        return _response.data

    def ticket_task_update_task(
        self,
        id: str,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters
        ----------
        id : str

        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_task.ticket_task_update_task(
            id="id",
            name="name",
            assignees=["assignees"],
            description="description",
            status="open",
            priority="urgent",
            creator_id="creatorId",
            due_date="dueDate",
            completed_date="completedDate",
            parent_id="parentId",
            list_id="listId",
        )
        """
        _response = self._raw_client.ticket_task_update_task(
            id,
            name=name,
            assignees=assignees,
            description=description,
            status=status,
            priority=priority,
            creator_id=creator_id,
            due_date=due_date,
            completed_date=completed_date,
            parent_id=parent_id,
            list_id=list_id,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def ticket_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetTasksResponse:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetTasksResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_task.ticket_task_get_tasks()
        """
        _response = self._raw_client.ticket_task_get_tasks(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ticket_task_create_task(
        self,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateTaskResponse:
        """
        Parameters
        ----------
        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ticket_task.ticket_task_create_task(
            name="name",
            assignees=["assignees"],
            description="description",
            status="open",
            priority="urgent",
            creator_id="creatorId",
            due_date="dueDate",
            completed_date="completedDate",
            parent_id="parentId",
            list_id="listId",
        )
        """
        _response = self._raw_client.ticket_task_create_task(
            name=name,
            assignees=assignees,
            description=description,
            status=status,
            priority=priority,
            creator_id=creator_id,
            due_date=due_date,
            completed_date=completed_date,
            parent_id=parent_id,
            list_id=list_id,
            fields=fields,
            request_options=request_options,
        )
        return _response.data


class AsyncTicketTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketTaskClient
        """
        return self._raw_client

    async def ticket_task_get_task(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> TicketGetTaskResponse:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_task.ticket_task_get_task(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_task_get_task(id, fields=fields, request_options=request_options)
        return _response.data

    async def ticket_task_update_task(
        self,
        id: str,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters
        ----------
        id : str

        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_task.ticket_task_update_task(
                id="id",
                name="name",
                assignees=["assignees"],
                description="description",
                status="open",
                priority="urgent",
                creator_id="creatorId",
                due_date="dueDate",
                completed_date="completedDate",
                parent_id="parentId",
                list_id="listId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_task_update_task(
            id,
            name=name,
            assignees=assignees,
            description=description,
            status=status,
            priority=priority,
            creator_id=creator_id,
            due_date=due_date,
            completed_date=completed_date,
            parent_id=parent_id,
            list_id=list_id,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def ticket_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketGetTasksResponse:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketGetTasksResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_task.ticket_task_get_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_task_get_tasks(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ticket_task_create_task(
        self,
        *,
        name: str,
        assignees: typing.Sequence[str],
        description: str,
        status: CommonTicketStatus,
        priority: CommonTicketPriority,
        creator_id: str,
        due_date: str,
        completed_date: str,
        parent_id: str,
        list_id: str,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketCreateOrUpdateTaskResponse:
        """
        Parameters
        ----------
        name : str
            Name of the task.

        assignees : typing.Sequence[str]
            collection of IDs belonging to assignees.

        description : str
            Description of the task.

        status : CommonTicketStatus
            Current status of the task.

        priority : CommonTicketPriority
            Priority of the task.

        creator_id : str
            ID of the task creator.

        due_date : str
            Due date for the given task.

        completed_date : str
            Date at which task was completed.

        parent_id : str
            Id of the parent task.

        list_id : str
            Id of the list

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketCreateOrUpdateTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ticket_task.ticket_task_create_task(
                name="name",
                assignees=["assignees"],
                description="description",
                status="open",
                priority="urgent",
                creator_id="creatorId",
                due_date="dueDate",
                completed_date="completedDate",
                parent_id="parentId",
                list_id="listId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ticket_task_create_task(
            name=name,
            assignees=assignees,
            description=description,
            status=status,
            priority=priority,
            creator_id=creator_id,
            due_date=due_date,
            completed_date=completed_date,
            parent_id=parent_id,
            list_id=list_id,
            fields=fields,
            request_options=request_options,
        )
        return _response.data
