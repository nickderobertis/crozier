

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_models_permission import ApiModelsPermission
from ..types.api_models_permission_data_required import ApiModelsPermissionDataRequired
from ..types.api_paged_response_api_models_permission import ApiPagedResponseApiModelsPermission
from .raw_client import AsyncRawPermissionsClient, RawPermissionsClient


OMIT = typing.cast(typing.Any, ...)


class PermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermissionsClient
        """
        return self._raw_client

    def getpermissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        name : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsPermission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.getpermissions()
        """
        _response = self._raw_client.getpermissions(
            limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    def postpermission(
        self,
        *,
        data_required: ApiModelsPermissionDataRequired,
        name: str,
        data_description: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        data_required : ApiModelsPermissionDataRequired
            Indicates if data is required or optional

        name : str
            The name of the permission.

        data_description : typing.Optional[str]
            Description of data to be provided with Role Authorization

        description : typing.Optional[str]

        id : typing.Optional[int]
            The identifier of the permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import ApiModelsPermissionDataRequired, FernApi

        client = FernApi()
        client.permissions.postpermission(
            data_required=ApiModelsPermissionDataRequired.YES,
            name="Name",
        )
        """
        _response = self._raw_client.postpermission(
            data_required=data_required,
            name=name,
            data_description=data_description,
            description=description,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def getpermission(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            Id of Permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsPermission
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.getpermission(
            id=1,
        )
        """
        _response = self._raw_client.getpermission(id, request_options=request_options)
        return _response.data

    def putpermission(
        self,
        id_: int,
        *,
        data_required: ApiModelsPermissionDataRequired,
        name: str,
        data_description: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            Id of Permission

        data_required : ApiModelsPermissionDataRequired
            Indicates if data is required or optional

        name : str
            The name of the permission.

        data_description : typing.Optional[str]
            Description of data to be provided with Role Authorization

        description : typing.Optional[str]

        id : typing.Optional[int]
            The identifier of the permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ApiModelsPermissionDataRequired, FernApi

        client = FernApi()
        client.permissions.putpermission(
            id_=1,
            data_required=ApiModelsPermissionDataRequired.YES,
            name="Name",
        )
        """
        _response = self._raw_client.putpermission(
            id_,
            data_required=data_required,
            name=name,
            data_description=data_description,
            description=description,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def deletepermission(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            Id of Permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.deletepermission(
            id=1,
        )
        """
        _response = self._raw_client.deletepermission(id, request_options=request_options)
        return _response.data


class AsyncPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermissionsClient
        """
        return self._raw_client

    async def getpermissions(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        name : typing.Optional[str]
            Filter by permission name. Supports ending wildcard (*). Optional.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseApiModelsPermission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.getpermissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getpermissions(
            limit=limit, offset=offset, name=name, request_options=request_options
        )
        return _response.data

    async def postpermission(
        self,
        *,
        data_required: ApiModelsPermissionDataRequired,
        name: str,
        data_description: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        data_required : ApiModelsPermissionDataRequired
            Indicates if data is required or optional

        name : str
            The name of the permission.

        data_description : typing.Optional[str]
            Description of data to be provided with Role Authorization

        description : typing.Optional[str]

        id : typing.Optional[int]
            The identifier of the permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import ApiModelsPermissionDataRequired, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.postpermission(
                data_required=ApiModelsPermissionDataRequired.YES,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postpermission(
            data_required=data_required,
            name=name,
            data_description=data_description,
            description=description,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def getpermission(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiModelsPermission:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            Id of Permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiModelsPermission
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.getpermission(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpermission(id, request_options=request_options)
        return _response.data

    async def putpermission(
        self,
        id_: int,
        *,
        data_required: ApiModelsPermissionDataRequired,
        name: str,
        data_description: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : int
            Id of Permission

        data_required : ApiModelsPermissionDataRequired
            Indicates if data is required or optional

        name : str
            The name of the permission.

        data_description : typing.Optional[str]
            Description of data to be provided with Role Authorization

        description : typing.Optional[str]

        id : typing.Optional[int]
            The identifier of the permission.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import ApiModelsPermissionDataRequired, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.putpermission(
                id_=1,
                data_required=ApiModelsPermissionDataRequired.YES,
                name="Name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putpermission(
            id_,
            data_required=data_required,
            name=name,
            data_description=data_description,
            description=description,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def deletepermission(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : int
            Id of Permission

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.deletepermission(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletepermission(id, request_options=request_options)
        return _response.data
