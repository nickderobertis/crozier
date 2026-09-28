

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.otoroshi_models_data_exporter_config import OtoroshiModelsDataExporterConfig
from .raw_client import AsyncRawDataExportersClient, RawDataExportersClient


OMIT = typing.cast(typing.Any, ...)


class DataExportersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataExportersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataExportersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataExportersClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config(
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
        client.data_exporters.otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsDataExporterConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsDataExporterConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsDataExporterConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
            request=[OtoroshiModelsDataExporterConfig()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsDataExporterConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsDataExporterConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsDataExporterConfig

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
            request=[OtoroshiModelsDataExporterConfig()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action(
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
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
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
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = (
            self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
                id, request_options=request_options
            )
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
        self,
        id_: str,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
            id_,
            desc=desc,
            loc=loc,
            buffer_size=buffer_size,
            json_workers=json_workers,
            group_duration=group_duration,
            group_size=group_size,
            type=type,
            tags=tags,
            send_workers=send_workers,
            id=id,
            name=name,
            metadata=metadata,
            config=config,
            projection=projection,
            enabled=enabled,
            filtering=filtering,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
        self,
        id_: str,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
            id_,
            desc=desc,
            loc=loc,
            buffer_size=buffer_size,
            json_workers=json_workers,
            group_duration=group_duration,
            group_size=group_size,
            type=type,
            tags=tags,
            send_workers=send_workers,
            id=id,
            name=name,
            metadata=metadata,
            config=config,
            projection=projection,
            enabled=enabled,
            filtering=filtering,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsDataExporterConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsDataExporterConfig]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action()
        """
        _response = (
            self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action(
                request_options=request_options
            )
        )
        return _response.data

    def otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(
        self,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(
            desc=desc,
            loc=loc,
            buffer_size=buffer_size,
            json_workers=json_workers,
            group_duration=group_duration,
            group_size=group_size,
            type=type,
            tags=tags,
            send_workers=send_workers,
            id=id,
            name=name,
            metadata=metadata,
            config=config,
            projection=projection,
            enabled=enabled,
            filtering=filtering,
            request_options=request_options,
        )
        return _response.data


class AsyncDataExportersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataExportersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataExportersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataExportersClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config(
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
            await client.data_exporters.otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_data_exporter_config(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsDataExporterConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsDataExporterConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsDataExporterConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
                request=[OtoroshiModelsDataExporterConfig()],
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_create_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsDataExporterConfig],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsDataExporterConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsDataExporterConfig

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
                request=[OtoroshiModelsDataExporterConfig()],
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_update_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action(
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_delete_action(
                request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_bulk_patch_action(
                request=request, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
        self,
        id_: str,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_update_entity_action(
                id_,
                desc=desc,
                loc=loc,
                buffer_size=buffer_size,
                json_workers=json_workers,
                group_duration=group_duration,
                group_size=group_size,
                type=type,
                tags=tags,
                send_workers=send_workers,
                id=id,
                name=name,
                metadata=metadata,
                config=config,
                projection=projection,
                enabled=enabled,
                filtering=filtering,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_delete_entity_action(
                id, request_options=request_options
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
        self,
        id_: str,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_patch_entity_action(
                id_,
                desc=desc,
                loc=loc,
                buffer_size=buffer_size,
                json_workers=json_workers,
                group_duration=group_duration,
                group_size=group_size,
                type=type,
                tags=tags,
                send_workers=send_workers,
                id=id,
                name=name,
                metadata=metadata,
                config=config,
                projection=projection,
                enabled=enabled,
                filtering=filtering,
                request_options=request_options,
            )
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsDataExporterConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsDataExporterConfig]
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(
        self,
        *,
        desc: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        buffer_size: typing.Optional[int] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        group_duration: typing.Optional[float] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        type: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        config: typing.Optional[typing.Any] = OMIT,
        projection: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        filtering: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsDataExporterConfig:
        """
        Parameters
        ----------
        desc : typing.Optional[str]
            ???

        loc : typing.Optional[typing.Any]

        buffer_size : typing.Optional[int]
            ???

        json_workers : typing.Optional[int]
            ???

        group_duration : typing.Optional[float]
            ???

        group_size : typing.Optional[int]
            ???

        type : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        send_workers : typing.Optional[int]
            ???

        id : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        config : typing.Optional[typing.Any]

        projection : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        enabled : typing.Optional[bool]
            ???

        filtering : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsDataExporterConfig
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
            await client.data_exporters.otoroshi_controllers_adminapi_data_exporter_config_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_data_exporter_config_controller_create_action(
            desc=desc,
            loc=loc,
            buffer_size=buffer_size,
            json_workers=json_workers,
            group_duration=group_duration,
            group_size=group_size,
            type=type,
            tags=tags,
            send_workers=send_workers,
            id=id,
            name=name,
            metadata=metadata,
            config=config,
            projection=projection,
            enabled=enabled,
            filtering=filtering,
            request_options=request_options,
        )
        return _response.data
