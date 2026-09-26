

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_team import OtoroshiModelsTeam
from .raw_client import AsyncRawTeamsClient, RawTeamsClient


OMIT = typing.cast(typing.Any, ...)


class TeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTeamsClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_team(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_templates_controller_initiate_team()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_team(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsTeam], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsTeam]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsTeam

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
            request=[OtoroshiModelsTeam()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsTeam], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsTeam]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsTeam

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
            request=[OtoroshiModelsTeam()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_bulk_delete_action(
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
        client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
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
        client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_update_entity_action(
        self,
        id_: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_update_entity_action(
            id_,
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
        self,
        id_: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
            id_,
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsTeam]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsTeam]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_teams_controller_create_action(
        self,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.teams.otoroshi_controllers_adminapi_teams_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_teams_controller_create_action(
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data


class AsyncTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTeamsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTeamsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTeamsClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_team(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
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
            await client.teams.otoroshi_controllers_adminapi_templates_controller_initiate_team()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_team(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
        self, *, request: typing.Sequence[OtoroshiModelsTeam], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsTeam]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsTeam

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
                request=[OtoroshiModelsTeam()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
        self, *, request: typing.Sequence[OtoroshiModelsTeam], request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsTeam]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsTeam

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
                request=[OtoroshiModelsTeam()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_bulk_delete_action(
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_update_entity_action(
        self,
        id_: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_update_entity_action(
            id_,
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
        self,
        id_: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_patch_entity_action(
            id_,
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsTeam]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsTeam]
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_teams_controller_create_action(
        self,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tenant: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        id: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTeam:
        """
        Parameters
        ----------
        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        name : typing.Optional[str]
            Entity name

        description : typing.Optional[str]
            Entity description

        tenant : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        id : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTeam
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
            await client.teams.otoroshi_controllers_adminapi_teams_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_teams_controller_create_action(
            tags=tags,
            name=name,
            description=description,
            tenant=tenant,
            metadata=metadata,
            id=id,
            request_options=request_options,
        )
        return _response.data
