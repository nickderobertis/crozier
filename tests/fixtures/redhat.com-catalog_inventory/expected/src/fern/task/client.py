

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.id import Id
from ..types.task import Task
from ..types.task_state import TaskState
from ..types.task_status import TaskStatus
from ..types.tasks_collection import TasksCollection
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawTaskClient, RawTaskClient


OMIT = typing.cast(typing.Any, ...)


class TaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaskClient
        """
        return self._raw_client

    def list_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksCollection:
        """
        Returns an array of Task objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TasksCollection
            Tasks collection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task.list_tasks()
        """
        _response = self._raw_client.list_tasks(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    def show_task(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Returns a Task object

        Parameters
        ----------
        id : str
            UUID of task

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task.show_task(
            id="id",
        )
        """
        _response = self._raw_client.show_task(id, request_options=request_options)
        return _response.data

    def update_task(
        self,
        id_: str,
        *,
        archived_at: typing.Optional[dt.datetime] = OMIT,
        child_task_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        controller_message_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Uuid] = OMIT,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        message: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        owner: typing.Optional[str] = OMIT,
        source_id: typing.Optional[Id] = OMIT,
        state: typing.Optional[TaskState] = OMIT,
        status: typing.Optional[TaskStatus] = OMIT,
        target_source_ref: typing.Optional[str] = OMIT,
        target_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Task object

        Parameters
        ----------
        id_ : str
            UUID of task

        archived_at : typing.Optional[dt.datetime]

        child_task_id : typing.Optional[str]

        completed_at : typing.Optional[dt.datetime]

        controller_message_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        id : typing.Optional[Uuid]

        input : typing.Optional[typing.Dict[str, typing.Any]]

        message : typing.Optional[str]

        name : typing.Optional[str]

        output : typing.Optional[typing.Dict[str, typing.Any]]

        owner : typing.Optional[str]

        source_id : typing.Optional[Id]

        state : typing.Optional[TaskState]

        status : typing.Optional[TaskStatus]

        target_source_ref : typing.Optional[str]

        target_type : typing.Optional[str]

        type : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.task.update_task(
            id_="id",
        )
        """
        _response = self._raw_client.update_task(
            id_,
            archived_at=archived_at,
            child_task_id=child_task_id,
            completed_at=completed_at,
            controller_message_id=controller_message_id,
            created_at=created_at,
            id=id,
            input=input,
            message=message,
            name=name,
            output=output,
            owner=owner,
            source_id=source_id,
            state=state,
            status=status,
            target_source_ref=target_source_ref,
            target_type=target_type,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data


class AsyncTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaskClient
        """
        return self._raw_client

    async def list_tasks(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TasksCollection:
        """
        Returns an array of Task objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TasksCollection
            Tasks collection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.task.list_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tasks(
            limit=limit, offset=offset, filter=filter, sort_by=sort_by, request_options=request_options
        )
        return _response.data

    async def show_task(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Returns a Task object

        Parameters
        ----------
        id : str
            UUID of task

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.task.show_task(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_task(id, request_options=request_options)
        return _response.data

    async def update_task(
        self,
        id_: str,
        *,
        archived_at: typing.Optional[dt.datetime] = OMIT,
        child_task_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        controller_message_id: typing.Optional[str] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Uuid] = OMIT,
        input: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        message: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        output: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        owner: typing.Optional[str] = OMIT,
        source_id: typing.Optional[Id] = OMIT,
        state: typing.Optional[TaskState] = OMIT,
        status: typing.Optional[TaskStatus] = OMIT,
        target_source_ref: typing.Optional[str] = OMIT,
        target_type: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Task object

        Parameters
        ----------
        id_ : str
            UUID of task

        archived_at : typing.Optional[dt.datetime]

        child_task_id : typing.Optional[str]

        completed_at : typing.Optional[dt.datetime]

        controller_message_id : typing.Optional[str]

        created_at : typing.Optional[dt.datetime]

        id : typing.Optional[Uuid]

        input : typing.Optional[typing.Dict[str, typing.Any]]

        message : typing.Optional[str]

        name : typing.Optional[str]

        output : typing.Optional[typing.Dict[str, typing.Any]]

        owner : typing.Optional[str]

        source_id : typing.Optional[Id]

        state : typing.Optional[TaskState]

        status : typing.Optional[TaskStatus]

        target_source_ref : typing.Optional[str]

        target_type : typing.Optional[str]

        type : typing.Optional[str]

        updated_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.task.update_task(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_task(
            id_,
            archived_at=archived_at,
            child_task_id=child_task_id,
            completed_at=completed_at,
            controller_message_id=controller_message_id,
            created_at=created_at,
            id=id,
            input=input,
            message=message,
            name=name,
            output=output,
            owner=owner,
            source_id=source_id,
            state=state,
            status=status,
            target_source_ref=target_source_ref,
            target_type=target_type,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data
