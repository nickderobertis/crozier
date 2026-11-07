

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ats_create_or_update_department_request import AtsCreateOrUpdateDepartmentRequest
from ..types.ats_create_or_update_department_response import AtsCreateOrUpdateDepartmentResponse
from ..types.ats_delete_department_response import AtsDeleteDepartmentResponse
from ..types.ats_get_department_response import AtsGetDepartmentResponse
from ..types.ats_get_departments_response import AtsGetDepartmentsResponse
from .raw_client import AsyncRawAtsDepartmentClient, RawAtsDepartmentClient


OMIT = typing.cast(typing.Any, ...)


class AtsDepartmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAtsDepartmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAtsDepartmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAtsDepartmentClient
        """
        return self._raw_client

    def ats_department_get_department(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetDepartmentResponse:
        """
        Get details of a department.

        Parameters
        ----------
        id : str
            The unique `id` of the department.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetDepartmentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_department.ats_department_get_department(
            id="id",
        )
        """
        _response = self._raw_client.ats_department_get_department(id, fields=fields, request_options=request_options)
        return _response.data

    def ats_department_delete_department(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteDepartmentResponse:
        """
        Delete details of an Department

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteDepartmentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_department.ats_department_delete_department(
            id="id",
        )
        """
        _response = self._raw_client.ats_department_delete_department(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    def ats_department_update_department(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateDepartmentRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateDepartmentResponse:
        """
        Update a Department

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateDepartmentRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateDepartmentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_department.ats_department_update_department(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_department_update_department(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    def ats_department_get_departments(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetDepartmentsResponse:
        """
        Get all the departments.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetDepartmentsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_department.ats_department_get_departments()
        """
        _response = self._raw_client.ats_department_get_departments(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    def ats_department_create_department(
        self,
        *,
        request: AtsCreateOrUpdateDepartmentRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateDepartmentResponse:
        """
        Create a new Department

        Parameters
        ----------
        request : AtsCreateOrUpdateDepartmentRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateDepartmentResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ats_department.ats_department_create_department(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.ats_department_create_department(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data


class AsyncAtsDepartmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAtsDepartmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAtsDepartmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAtsDepartmentClient
        """
        return self._raw_client

    async def ats_department_get_department(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsGetDepartmentResponse:
        """
        Get details of a department.

        Parameters
        ----------
        id : str
            The unique `id` of the department.

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetDepartmentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_department.ats_department_get_department(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_department_get_department(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_department_delete_department(
        self, id: str, *, fields: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AtsDeleteDepartmentResponse:
        """
        Delete details of an Department

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsDeleteDepartmentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_department.ats_department_delete_department(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_department_delete_department(
            id, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_department_update_department(
        self,
        id: str,
        *,
        request: AtsCreateOrUpdateDepartmentRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateDepartmentResponse:
        """
        Update a Department

        Parameters
        ----------
        id : str

        request : AtsCreateOrUpdateDepartmentRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateDepartmentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_department.ats_department_update_department(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_department_update_department(
            id, request=request, fields=fields, request_options=request_options
        )
        return _response.data

    async def ats_department_get_departments(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsGetDepartmentsResponse:
        """
        Get all the departments.

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsGetDepartmentsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_department.ats_department_get_departments()


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_department_get_departments(
            fields=fields, page_size=page_size, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def ats_department_create_department(
        self,
        *,
        request: AtsCreateOrUpdateDepartmentRequest,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AtsCreateOrUpdateDepartmentResponse:
        """
        Create a new Department

        Parameters
        ----------
        request : AtsCreateOrUpdateDepartmentRequest

        fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AtsCreateOrUpdateDepartmentResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ats_department.ats_department_create_department(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ats_department_create_department(
            request=request, fields=fields, request_options=request_options
        )
        return _response.data
