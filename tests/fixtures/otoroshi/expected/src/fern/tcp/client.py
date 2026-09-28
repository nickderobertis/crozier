

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.empty import Empty
from ..types.otoroshi_tcp_tcp_rule import OtoroshiTcpTcpRule
from ..types.otoroshi_tcp_tcp_service import OtoroshiTcpTcpService
from .raw_client import AsyncRawTcpClient, RawTcpClient


OMIT = typing.cast(typing.Any, ...)


class TcpClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTcpClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
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
        client.tcp.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiTcpTcpService

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
            request=[OtoroshiTcpTcpService()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiTcpTcpService

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
            request=[OtoroshiTcpTcpService()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
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
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
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
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
            id_,
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            loc=loc,
            name=name,
            tls=tls,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
            id_,
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            loc=loc,
            name=name,
            tls=tls,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiTcpTcpService]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            loc=loc,
            name=name,
            tls=tls,
            request_options=request_options,
        )
        return _response.data


class AsyncTcpClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTcpClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTcpClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTcpClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
        self, *, request: Empty, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        request : Empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_create_from_template_tcp(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
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
            await client.tcp.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_tcp_service_tcp(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiTcpTcpService

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
                request=[OtoroshiTcpTcpService()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiTcpTcpService],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiTcpTcpService]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiTcpTcpService

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
                request=[OtoroshiTcpTcpService()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_update_entity_action(
                id_,
                enabled=enabled,
                description=description,
                metadata=metadata,
                port=port,
                tags=tags,
                rules=rules,
                client_auth=client_auth,
                interface=interface,
                sni=sni,
                id=id,
                loc=loc,
                name=name,
                tls=tls,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_delete_entity_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
        self,
        id_: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_patch_entity_action(
            id_,
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            loc=loc,
            name=name,
            tls=tls,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiTcpTcpService]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiTcpTcpService]
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
        self,
        *,
        enabled: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        port: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        rules: typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]] = OMIT,
        client_auth: typing.Optional[typing.Any] = OMIT,
        interface: typing.Optional[str] = OMIT,
        sni: typing.Optional[typing.Any] = OMIT,
        id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        name: typing.Optional[str] = OMIT,
        tls: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiTcpTcpService:
        """
        Parameters
        ----------
        enabled : typing.Optional[bool]
            Service enabled

        description : typing.Optional[str]
            Entity description

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        port : typing.Optional[int]
            network port

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        rules : typing.Optional[typing.Sequence[OtoroshiTcpTcpRule]]
            Routing rules

        client_auth : typing.Optional[typing.Any]

        interface : typing.Optional[str]
            Network interface

        sni : typing.Optional[typing.Any]

        id : typing.Optional[str]
            Entity id

        loc : typing.Optional[typing.Any]

        name : typing.Optional[str]
            Entity name

        tls : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiTcpTcpService
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
            await client.tcp.otoroshi_controllers_adminapi_tcp_service_api_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_tcp_service_api_controller_create_action(
            enabled=enabled,
            description=description,
            metadata=metadata,
            port=port,
            tags=tags,
            rules=rules,
            client_auth=client_auth,
            interface=interface,
            sni=sni,
            id=id,
            loc=loc,
            name=name,
            tls=tls,
            request_options=request_options,
        )
        return _response.data
