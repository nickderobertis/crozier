

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted import Deleted
from ..types.group import Group
from ..types.patch import Patch
from .raw_client import AsyncRawGroupsClient, RawGroupsClient


OMIT = typing.cast(typing.Any, ...)


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

    def all_service_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Group]:
        """
        Get all service groups

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.all_service_groups()
        """
        _response = self._raw_client.all_service_groups(request_options=request_options)
        return _response.data

    def create_group(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new service group

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.create_group(
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.create_group(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def service_group(self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.service_group(
            service_group_id="serviceGroupId",
        )
        """
        _response = self._raw_client.service_group(service_group_id, request_options=request_options)
        return _response.data

    def update_group(
        self,
        service_group_id: str,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Update a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.update_group(
            service_group_id="serviceGroupId",
            id="a string value",
            name="a string value",
        )
        """
        _response = self._raw_client.update_group(
            service_group_id, id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def delete_group(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.delete_group(
            service_group_id="serviceGroupId",
        )
        """
        _response = self._raw_client.delete_group(service_group_id, request_options=request_options)
        return _response.data

    def patch_group(
        self, service_group_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Update a service group with a diff

        Parameters
        ----------
        service_group_id : str
            The service group id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.patch_group(
            service_group_id="serviceGroupId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_group(service_group_id, request=request, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

    async def all_service_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Group]:
        """
        Get all service groups

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.all_service_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_service_groups(request_options=request_options)
        return _response.data

    async def create_group(
        self,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new service group

        Parameters
        ----------
        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.create_group(
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(
            id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def service_group(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Get a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.service_group(
                service_group_id="serviceGroupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_group(service_group_id, request_options=request_options)
        return _response.data

    async def update_group(
        self,
        service_group_id: str,
        *,
        id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Update a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        id : str
            The unique id of the group. Usually 64 random alpha numerical characters, but can be anything

        name : str
            The name of the group

        description : typing.Optional[str]
            The descriptoin of the group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.update_group(
                service_group_id="serviceGroupId",
                id="a string value",
                name="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group(
            service_group_id, id=id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def delete_group(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a service group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.delete_group(
                service_group_id="serviceGroupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(service_group_id, request_options=request_options)
        return _response.data

    async def patch_group(
        self, service_group_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Group:
        """
        Update a service group with a diff

        Parameters
        ----------
        service_group_id : str
            The service group id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.patch_group(
                service_group_id="serviceGroupId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_group(
            service_group_id, request=request, request_options=request_options
        )
        return _response.data
