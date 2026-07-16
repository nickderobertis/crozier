

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_employees_response import ListEmployeesResponse
from ..types.retrieve_employee_response import RetrieveEmployeeResponse
from .raw_client import AsyncRawEmployeesClient, RawEmployeesClient


class EmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmployeesClient
        """
        return self._raw_client

    def list_employees(
        self,
        *,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEmployeesResponse:
        """


        Parameters
        ----------
        location_id : typing.Optional[str]


        status : typing.Optional[str]
            Specifies the EmployeeStatus to filter the employee by.

        limit : typing.Optional[int]
            The number of employees to be returned on each page.

        cursor : typing.Optional[str]
            The token required to retrieve the specified page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmployeesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.employees.list_employees()
        """
        _response = self._raw_client.list_employees(
            location_id=location_id, status=status, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def retrieve_employee(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveEmployeeResponse:
        """


        Parameters
        ----------
        id : str
            UUID for the employee that was requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveEmployeeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.employees.retrieve_employee(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_employee(id, request_options=request_options)
        return _response.data


class AsyncEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmployeesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmployeesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmployeesClient
        """
        return self._raw_client

    async def list_employees(
        self,
        *,
        location_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEmployeesResponse:
        """


        Parameters
        ----------
        location_id : typing.Optional[str]


        status : typing.Optional[str]
            Specifies the EmployeeStatus to filter the employee by.

        limit : typing.Optional[int]
            The number of employees to be returned on each page.

        cursor : typing.Optional[str]
            The token required to retrieve the specified page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEmployeesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.employees.list_employees()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_employees(
            location_id=location_id, status=status, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def retrieve_employee(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveEmployeeResponse:
        """


        Parameters
        ----------
        id : str
            UUID for the employee that was requested.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveEmployeeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.employees.retrieve_employee(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_employee(id, request_options=request_options)
        return _response.data
