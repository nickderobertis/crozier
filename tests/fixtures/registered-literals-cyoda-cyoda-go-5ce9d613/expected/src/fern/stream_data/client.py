

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.abstract_condition import AbstractCondition
from ..types.index_configuration_dto import IndexConfigurationDto
from ..types.query_plan_dto import QueryPlanDto
from ..types.report_alias_def import ReportAliasDef
from ..types.stream_data_config_def import StreamDataConfigDef
from ..types.stream_data_config_def_container import StreamDataConfigDefContainer
from ..types.stream_data_def import StreamDataDef
from ..types.stream_data_delete_result import StreamDataDeleteResult
from ..types.stream_data_fetch_result import StreamDataFetchResult
from .raw_client import AsyncRawStreamDataClient, RawStreamDataClient


OMIT = typing.cast(typing.Any, ...)


class StreamDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStreamDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStreamDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStreamDataClient
        """
        return self._raw_client

    def get_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamDataConfigDef:
        """
        Retrieves a specific stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDef
            The requested stream data configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.get_stream_data_config(
            config_id="configId",
        )
        """
        _response = self._raw_client.get_stream_data_config(config_id=config_id, request_options=request_options)
        return _response.data

    def save_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates and persists a new stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            UUID of the created configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.save_stream_data_config()
        """
        _response = self._raw_client.save_stream_data_config(
            stream_data_def=stream_data_def,
            name=name,
            description=description,
            create_date=create_date,
            owner=owner,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def update_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.update_stream_data_config()
        """
        _response = self._raw_client.update_stream_data_config(
            stream_data_def=stream_data_def,
            name=name,
            description=description,
            create_date=create_date,
            owner=owner,
            id=id,
            request_options=request_options,
        )
        return _response.data

    def delete_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.delete_stream_data_config(
            config_id="configId",
        )
        """
        _response = self._raw_client.delete_stream_data_config(config_id=config_id, request_options=request_options)
        return _response.data

    def get_all_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StreamDataConfigDef]:
        """
        Returns all available stream data configurations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StreamDataConfigDef]
            List of all stream data configurations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.get_all_configs()
        """
        _response = self._raw_client.get_all_configs(request_options=request_options)
        return _response.data

    def delete(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataDeleteResult:
        """
        Deletes entities matching the stream data request criteria.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataDeleteResult
            Deletion result with counts and any errors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.delete()
        """
        _response = self._raw_client.delete(
            sd_def=sd_def,
            point_time=point_time,
            offset=offset,
            length=length,
            from_pos_index=from_pos_index,
            request_options=request_options,
        )
        return _response.data

    def export_all1(self, *, request_options: typing.Optional[RequestOptions] = None) -> StreamDataConfigDefContainer:
        """
        Exports all stream data configurations as a container for backup or transfer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with all stream data configurations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.export_all1()
        """
        _response = self._raw_client.export_all1(request_options=request_options)
        return _response.data

    def export_all(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamDataConfigDefContainer:
        """
        Exports all stream data configurations associated with a specific entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with stream data configurations for the entity class

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.export_all(
            entity_class="com.example.MyEntity",
        )
        """
        _response = self._raw_client.export_all(entity_class=entity_class, request_options=request_options)
        return _response.data

    def export_by_ids(
        self,
        *,
        include_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataConfigDefContainer:
        """
        Exports specific stream data configurations identified by their UUIDs.

        Parameters
        ----------
        include_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of configuration UUIDs to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with the requested stream data configurations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.export_by_ids(
            include_ids=["includeIds"],
        )
        """
        _response = self._raw_client.export_by_ids(include_ids=include_ids, request_options=request_options)
        return _response.data

    def get_stream_data(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataFetchResult:
        """
        Retrieves paginated stream data based on the provided request definition, including conditions, columns, and pagination parameters.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataFetchResult
            Stream data fetch result containing rows and pagination info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.get_stream_data()
        """
        _response = self._raw_client.get_stream_data(
            sd_def=sd_def,
            point_time=point_time,
            offset=offset,
            length=length,
            from_pos_index=from_pos_index,
            request_options=request_options,
        )
        return _response.data

    def import_container(
        self,
        *,
        fail_on_exists: typing.Optional[bool] = None,
        data: typing.Optional[typing.Sequence[StreamDataConfigDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports stream data configurations from a container. Can optionally fail if configurations already exist.

        Parameters
        ----------
        fail_on_exists : typing.Optional[bool]
            If true, fail when a configuration already exists; if false, skip existing configurations

        data : typing.Optional[typing.Sequence[StreamDataConfigDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.import_container()
        """
        _response = self._raw_client.import_container(
            fail_on_exists=fail_on_exists, data=data, request_options=request_options
        )
        return _response.data

    def get_indexs(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IndexConfigurationDto]:
        """
        Returns all index configurations available for the specified entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IndexConfigurationDto]
            List of index configurations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.get_indexs(
            entity_class="com.example.MyEntity",
        )
        """
        _response = self._raw_client.get_indexs(entity_class=entity_class, request_options=request_options)
        return _response.data

    def get_query_plan(
        self,
        *,
        condition: typing.Optional[AbstractCondition] = OMIT,
        alias_defs: typing.Optional[typing.Sequence[ReportAliasDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryPlanDto:
        """
        Returns the original and optimized query execution plan for the given entity class, condition, and alias definitions.

        Parameters
        ----------
        condition : typing.Optional[AbstractCondition]

        alias_defs : typing.Optional[typing.Sequence[ReportAliasDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryPlanDto
            Query plan with original and optimized versions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.stream_data.get_query_plan()
        """
        _response = self._raw_client.get_query_plan(
            condition=condition, alias_defs=alias_defs, request_options=request_options
        )
        return _response.data


class AsyncStreamDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStreamDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStreamDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStreamDataClient
        """
        return self._raw_client

    async def get_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamDataConfigDef:
        """
        Retrieves a specific stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDef
            The requested stream data configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.get_stream_data_config(
                config_id="configId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_data_config(config_id=config_id, request_options=request_options)
        return _response.data

    async def save_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates and persists a new stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            UUID of the created configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.save_stream_data_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.save_stream_data_config(
            stream_data_def=stream_data_def,
            name=name,
            description=description,
            create_date=create_date,
            owner=owner,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def update_stream_data_config(
        self,
        *,
        stream_data_def: typing.Optional[StreamDataDef] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        create_date: typing.Optional[dt.datetime] = OMIT,
        owner: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an existing stream data configuration definition.

        Parameters
        ----------
        stream_data_def : typing.Optional[StreamDataDef]

        name : typing.Optional[str]

        description : typing.Optional[str]

        create_date : typing.Optional[dt.datetime]

        owner : typing.Optional[str]

        id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.update_stream_data_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_stream_data_config(
            stream_data_def=stream_data_def,
            name=name,
            description=description,
            create_date=create_date,
            owner=owner,
            id=id,
            request_options=request_options,
        )
        return _response.data

    async def delete_stream_data_config(
        self, *, config_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a stream data configuration by its UUID.

        Parameters
        ----------
        config_id : str
            UUID of the configuration to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.delete_stream_data_config(
                config_id="configId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_stream_data_config(
            config_id=config_id, request_options=request_options
        )
        return _response.data

    async def get_all_configs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StreamDataConfigDef]:
        """
        Returns all available stream data configurations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StreamDataConfigDef]
            List of all stream data configurations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.get_all_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_configs(request_options=request_options)
        return _response.data

    async def delete(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataDeleteResult:
        """
        Deletes entities matching the stream data request criteria.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataDeleteResult
            Deletion result with counts and any errors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            sd_def=sd_def,
            point_time=point_time,
            offset=offset,
            length=length,
            from_pos_index=from_pos_index,
            request_options=request_options,
        )
        return _response.data

    async def export_all1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamDataConfigDefContainer:
        """
        Exports all stream data configurations as a container for backup or transfer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with all stream data configurations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.export_all1()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_all1(request_options=request_options)
        return _response.data

    async def export_all(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamDataConfigDefContainer:
        """
        Exports all stream data configurations associated with a specific entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with stream data configurations for the entity class

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.export_all(
                entity_class="com.example.MyEntity",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_all(entity_class=entity_class, request_options=request_options)
        return _response.data

    async def export_by_ids(
        self,
        *,
        include_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataConfigDefContainer:
        """
        Exports specific stream data configurations identified by their UUIDs.

        Parameters
        ----------
        include_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            List of configuration UUIDs to export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataConfigDefContainer
            Container with the requested stream data configurations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.export_by_ids(
                include_ids=["includeIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_by_ids(include_ids=include_ids, request_options=request_options)
        return _response.data

    async def get_stream_data(
        self,
        *,
        sd_def: typing.Optional[StreamDataDef] = OMIT,
        point_time: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        length: typing.Optional[int] = OMIT,
        from_pos_index: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StreamDataFetchResult:
        """
        Retrieves paginated stream data based on the provided request definition, including conditions, columns, and pagination parameters.

        Parameters
        ----------
        sd_def : typing.Optional[StreamDataDef]

        point_time : typing.Optional[int]

        offset : typing.Optional[int]

        length : typing.Optional[int]

        from_pos_index : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamDataFetchResult
            Stream data fetch result containing rows and pagination info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.get_stream_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_data(
            sd_def=sd_def,
            point_time=point_time,
            offset=offset,
            length=length,
            from_pos_index=from_pos_index,
            request_options=request_options,
        )
        return _response.data

    async def import_container(
        self,
        *,
        fail_on_exists: typing.Optional[bool] = None,
        data: typing.Optional[typing.Sequence[StreamDataConfigDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Imports stream data configurations from a container. Can optionally fail if configurations already exist.

        Parameters
        ----------
        fail_on_exists : typing.Optional[bool]
            If true, fail when a configuration already exists; if false, skip existing configurations

        data : typing.Optional[typing.Sequence[StreamDataConfigDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.import_container()


        asyncio.run(main())
        """
        _response = await self._raw_client.import_container(
            fail_on_exists=fail_on_exists, data=data, request_options=request_options
        )
        return _response.data

    async def get_indexs(
        self, *, entity_class: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IndexConfigurationDto]:
        """
        Returns all index configurations available for the specified entity class.

        Parameters
        ----------
        entity_class : str
            Fully qualified class name of the entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IndexConfigurationDto]
            List of index configurations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.get_indexs(
                entity_class="com.example.MyEntity",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_indexs(entity_class=entity_class, request_options=request_options)
        return _response.data

    async def get_query_plan(
        self,
        *,
        condition: typing.Optional[AbstractCondition] = OMIT,
        alias_defs: typing.Optional[typing.Sequence[ReportAliasDef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> QueryPlanDto:
        """
        Returns the original and optimized query execution plan for the given entity class, condition, and alias definitions.

        Parameters
        ----------
        condition : typing.Optional[AbstractCondition]

        alias_defs : typing.Optional[typing.Sequence[ReportAliasDef]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        QueryPlanDto
            Query plan with original and optimized versions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.stream_data.get_query_plan()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_query_plan(
            condition=condition, alias_defs=alias_defs, request_options=request_options
        )
        return _response.data
