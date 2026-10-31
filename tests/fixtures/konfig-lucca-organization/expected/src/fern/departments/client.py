

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDepartmentsClient, RawDepartmentsClient
from .types.get_api_v3departments_department_id_response import GetApiV3DepartmentsDepartmentIdResponse
from .types.get_api_v3departments_response import GetApiV3DepartmentsResponse
from .types.get_api_v3departments_tree_response import GetApiV3DepartmentsTreeResponse


class DepartmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepartmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDepartmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepartmentsClient
        """
        return self._raw_client

    def get_api_v3departments(
        self,
        *,
        paging: str,
        head_id: typing.Optional[int] = None,
        parent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3DepartmentsResponse:
        """
        List all Departments satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        head_id : typing.Optional[int]

        parent_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.departments.get_api_v3departments(
            paging="100,0",
        )
        """
        _response = self._raw_client.get_api_v3departments(
            paging=paging, head_id=head_id, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    def get_api_v3departments_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3DepartmentsTreeResponse:
        """
        List all departments as a tree.
        Remark: first node is always empty and represents the starting point of the tree as multiple departments might be set to the highest level.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsTreeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.departments.get_api_v3departments_tree()
        """
        _response = self._raw_client.get_api_v3departments_tree(request_options=request_options)
        return _response.data

    def get_api_v3departments_department_id(
        self, department_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3DepartmentsDepartmentIdResponse:
        """
        Retrieve a single Department by its unique identifier.

        Parameters
        ----------
        department_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsDepartmentIdResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.departments.get_api_v3departments_department_id(
            department_id=1,
        )
        """
        _response = self._raw_client.get_api_v3departments_department_id(department_id, request_options=request_options)
        return _response.data


class AsyncDepartmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepartmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDepartmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepartmentsClient
        """
        return self._raw_client

    async def get_api_v3departments(
        self,
        *,
        paging: str,
        head_id: typing.Optional[int] = None,
        parent_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApiV3DepartmentsResponse:
        """
        List all Departments satisfying query filters.

        Parameters
        ----------
        paging : str
            {offset},{limit}. Defaults to 0,1000.

        head_id : typing.Optional[int]

        parent_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.departments.get_api_v3departments(
                paging="100,0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3departments(
            paging=paging, head_id=head_id, parent_id=parent_id, request_options=request_options
        )
        return _response.data

    async def get_api_v3departments_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3DepartmentsTreeResponse:
        """
        List all departments as a tree.
        Remark: first node is always empty and represents the starting point of the tree as multiple departments might be set to the highest level.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsTreeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.departments.get_api_v3departments_tree()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3departments_tree(request_options=request_options)
        return _response.data

    async def get_api_v3departments_department_id(
        self, department_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV3DepartmentsDepartmentIdResponse:
        """
        Retrieve a single Department by its unique identifier.

        Parameters
        ----------
        department_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV3DepartmentsDepartmentIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.departments.get_api_v3departments_department_id(
                department_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v3departments_department_id(
            department_id, request_options=request_options
        )
        return _response.data
