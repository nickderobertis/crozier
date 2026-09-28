

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_next_models_ng_minimal_route import OtoroshiNextModelsNgMinimalRoute
from ..types.otoroshi_next_models_ng_route_composition import OtoroshiNextModelsNgRouteComposition
from .raw_client import AsyncRawRouteCompositionsClient, RawRouteCompositionsClient


OMIT = typing.cast(typing.Any, ...)


class RouteCompositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRouteCompositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRouteCompositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRouteCompositionsClient
        """
        return self._raw_client

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
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
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
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
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsNgRouteComposition

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
            request=[OtoroshiNextModelsNgRouteComposition()],
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiNextModelsNgRouteComposition

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
            request=[OtoroshiNextModelsNgRouteComposition()],
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
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
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action()
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
                request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
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
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
            id_="id",
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
                id_,
                capture=capture,
                id=id,
                debug_flow=debug_flow,
                routes=routes,
                enabled=enabled,
                description=description,
                metadata=metadata,
                export_reporting=export_reporting,
                tags=tags,
                name=name,
                loc=loc,
                client=client,
                groups=groups,
                request_options=request_options,
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
            id="id",
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
                id, request_options=request_options
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = (
            self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
                id_,
                capture=capture,
                id=id,
                debug_flow=debug_flow,
                routes=routes,
                enabled=enabled,
                description=description,
                metadata=metadata,
                export_reporting=export_reporting,
                tags=tags,
                name=name,
                loc=loc,
                client=client,
                groups=groups,
                request_options=request_options,
            )
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsNgRouteComposition]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
        self,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action()
        """
        _response = self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
            capture=capture,
            id=id,
            debug_flow=debug_flow,
            routes=routes,
            enabled=enabled,
            description=description,
            metadata=metadata,
            export_reporting=export_reporting,
            tags=tags,
            name=name,
            loc=loc,
            client=client,
            groups=groups,
            request_options=request_options,
        )
        return _response.data


class AsyncRouteCompositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRouteCompositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRouteCompositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRouteCompositionsClient
        """
        return self._raw_client

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_form(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_from_openapi(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_initiate_route_composition(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsNgRouteComposition

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
                request=[OtoroshiNextModelsNgRouteComposition()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiNextModelsNgRouteComposition],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiNextModelsNgRouteComposition]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiNextModelsNgRouteComposition

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
                request=[OtoroshiNextModelsNgRouteComposition()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_update_entity_action(
            id_,
            capture=capture,
            id=id,
            debug_flow=debug_flow,
            routes=routes,
            enabled=enabled,
            description=description,
            metadata=metadata,
            export_reporting=export_reporting,
            tags=tags,
            name=name,
            loc=loc,
            client=client,
            groups=groups,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
        self,
        id_: str,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_patch_entity_action(
            id_,
            capture=capture,
            id=id,
            debug_flow=debug_flow,
            routes=routes,
            enabled=enabled,
            description=description,
            metadata=metadata,
            export_reporting=export_reporting,
            tags=tags,
            name=name,
            loc=loc,
            client=client,
            groups=groups,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiNextModelsNgRouteComposition]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiNextModelsNgRouteComposition]
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
        self,
        *,
        capture: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        debug_flow: typing.Optional[bool] = OMIT,
        routes: typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        export_reporting: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        client: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiNextModelsNgRouteComposition:
        """
        Parameters
        ----------
        capture : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        debug_flow : typing.Optional[bool]
            ???

        routes : typing.Optional[typing.Sequence[OtoroshiNextModelsNgMinimalRoute]]
            ???

        enabled : typing.Optional[bool]
            ???

        description : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        export_reporting : typing.Optional[bool]
            ???

        tags : typing.Optional[typing.Sequence[str]]
            ???

        name : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        client : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiNextModelsNgRouteComposition
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
            await client.route_compositions.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_next_controllers_adminapi_ng_route_compositions_controller_create_action(
                capture=capture,
                id=id,
                debug_flow=debug_flow,
                routes=routes,
                enabled=enabled,
                description=description,
                metadata=metadata,
                export_reporting=export_reporting,
                tags=tags,
                name=name,
                loc=loc,
                client=client,
                groups=groups,
                request_options=request_options,
            )
        )
        return _response.data
