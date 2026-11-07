

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_task_association import CommonTaskAssociation
from ..types.crm_create_or_update_task_response import CrmCreateOrUpdateTaskResponse
from ..types.crm_get_task_response import CrmGetTaskResponse
from ..types.crm_get_tasks_response import CrmGetTasksResponse
from ..types.crm_search_tasks_response import CrmSearchTasksResponse
from .raw_client import AsyncRawCrmTaskClient, RawCrmTaskClient


OMIT = typing.cast(typing.Any, ...)


class CrmTaskClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmTaskClient
        """
        return self._raw_client

    def crm_task_get_task(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetTaskResponse:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_task.crm_task_get_task(
            id="id",
        )
        """
        _response = self._raw_client.crm_task_get_task(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_task_update_task(
        self,
        id: str,
        *,
        additional: typing.Any,
        associations: typing.Optional[CommonTaskAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters
        ----------
        id : str

        additional : typing.Any

        associations : typing.Optional[CommonTaskAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_task.crm_task_update_task(
            id="id",
            additional={"key": "value"},
        )
        """
        _response = self._raw_client.crm_task_update_task(
            id, additional=additional, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetTasksResponse:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetTasksResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_task.crm_task_get_tasks()
        """
        _response = self._raw_client.crm_task_get_tasks(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_task_create_task(
        self,
        *,
        additional: typing.Any,
        associations: typing.Optional[CommonTaskAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateTaskResponse:
        """
        Create a new task

        Parameters
        ----------
        additional : typing.Any

        associations : typing.Optional[CommonTaskAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateTaskResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_task.crm_task_create_task(
            additional={"key": "value"},
        )
        """
        _response = self._raw_client.crm_task_create_task(
            additional=additional, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_task_search_tasks(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchTasksResponse:
        """
        Search for tasks

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchTasksResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_task.crm_task_search_tasks(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_task_search_tasks(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmTaskClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmTaskClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmTaskClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmTaskClient
        """
        return self._raw_client

    async def crm_task_get_task(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetTaskResponse:
        """
        Get details of a task

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_task.crm_task_get_task(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_task_get_task(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_task_update_task(
        self,
        id: str,
        *,
        additional: typing.Any,
        associations: typing.Optional[CommonTaskAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateTaskResponse:
        """
        Update a task

        Parameters
        ----------
        id : str

        additional : typing.Any

        associations : typing.Optional[CommonTaskAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_task.crm_task_update_task(
                id="id",
                additional={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_task_update_task(
            id, additional=additional, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_task_get_tasks(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetTasksResponse:
        """
        Get all the tasks

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetTasksResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_task.crm_task_get_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_task_get_tasks(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_task_create_task(
        self,
        *,
        additional: typing.Any,
        associations: typing.Optional[CommonTaskAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateTaskResponse:
        """
        Create a new task

        Parameters
        ----------
        additional : typing.Any

        associations : typing.Optional[CommonTaskAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateTaskResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_task.crm_task_create_task(
                additional={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_task_create_task(
            additional=additional, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_task_search_tasks(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchTasksResponse:
        """
        Search for tasks

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchTasksResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_task.crm_task_search_tasks(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_task_search_tasks(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
