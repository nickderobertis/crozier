

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_service_group import OtoroshiModelsServiceGroup
from ..types.service_descriptor_list import ServiceDescriptorList
from ..types.unknown import Unknown
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

    def otoroshi_controllers_adminapi_analytics_controller_group_status(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        group_id : str
            the groupId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_analytics_controller_group_status(
            group_id="groupId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_group_status(
            group_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceGroup],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsServiceGroup

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
            request=[OtoroshiModelsServiceGroup()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceGroup],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsServiceGroup

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
            request=[OtoroshiModelsServiceGroup()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_service_group_services(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceDescriptorList:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceDescriptorList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_service_group_services(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_service_group_services(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
            id_,
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
            id_,
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsServiceGroup]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsServiceGroup]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_service_group_controller_create_action(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.otoroshi_controllers_adminapi_service_group_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_service_group_controller_create_action(
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
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

    async def otoroshi_controllers_adminapi_analytics_controller_group_status(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        group_id : str
            the groupId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
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
            await client.groups.otoroshi_controllers_adminapi_analytics_controller_group_status(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_group_status(
            group_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_group_groups(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceGroup],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsServiceGroup

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
                request=[OtoroshiModelsServiceGroup()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceGroup],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsServiceGroup

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
                request=[OtoroshiModelsServiceGroup()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_service_group_services(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceDescriptorList:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceDescriptorList
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_service_group_services(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_service_group_services(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_update_entity_action(
            id_,
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
        self,
        id_: str,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_patch_entity_action(
            id_,
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsServiceGroup]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsServiceGroup]
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_service_group_controller_create_action(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceGroup:
        """
        Parameters
        ----------
        id : typing.Optional[str]
            A unique random string to identify your service

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            The name of your service. Only for debug and human readability purposes

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        description : typing.Optional[str]
            Entity description

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceGroup
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
            await client.groups.otoroshi_controllers_adminapi_service_group_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_service_group_controller_create_action(
            id=id,
            loc=loc,
            name=name,
            metadata=metadata,
            description=description,
            tags=tags,
            request_options=request_options,
        )
        return _response.data
