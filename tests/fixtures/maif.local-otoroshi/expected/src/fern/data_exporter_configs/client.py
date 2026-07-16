

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_exporter_config import DataExporterConfig
from ..types.data_exporter_config_config import DataExporterConfigConfig
from ..types.data_exporter_config_typ import DataExporterConfigTyp
from ..types.deleted import Deleted
from ..types.filtering import Filtering
from ..types.location import Location
from ..types.patch import Patch
from .raw_client import AsyncRawDataExporterConfigsClient, RawDataExporterConfigsClient
from .types.create_bulk_data_exporter_configs_response_item import CreateBulkDataExporterConfigsResponseItem
from .types.deletebulk_data_exporter_config_response_item import DeletebulkDataExporterConfigResponseItem
from .types.patch_bulk_data_exporter_config_response_item import PatchBulkDataExporterConfigResponseItem
from .types.update_bulk_data_exporter_config_response_item import UpdateBulkDataExporterConfigResponseItem


OMIT = typing.cast(typing.Any, ...)


class DataExporterConfigsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataExporterConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataExporterConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataExporterConfigsClient
        """
        return self._raw_client

    def find_all_data_exporters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DataExporterConfig]:
        """
        Get all data exporter configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataExporterConfig]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.find_all_data_exporters()
        """
        _response = self._raw_client.find_all_data_exporters(request_options=request_options)
        return _response.data

    def create_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExporterConfig:
        """
        Create a new data exporter config

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.create_data_exporter_config()
        """
        _response = self._raw_client.create_data_exporter_config(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    def create_bulk_data_exporter_configs(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateBulkDataExporterConfigsResponseItem]:
        """
        Create a new data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateBulkDataExporterConfigsResponseItem]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.create_bulk_data_exporter_configs()
        """
        _response = self._raw_client.create_bulk_data_exporter_configs(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    def update_bulk_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UpdateBulkDataExporterConfigResponseItem]:
        """
        Update a data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UpdateBulkDataExporterConfigResponseItem]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.update_bulk_data_exporter_config()
        """
        _response = self._raw_client.update_bulk_data_exporter_config(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    def deletebulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeletebulkDataExporterConfigResponseItem]:
        """
        Delete a data exporter config

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeletebulkDataExporterConfigResponseItem]
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.deletebulk_data_exporter_config(
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.deletebulk_data_exporter_config(request=request, request_options=request_options)
        return _response.data

    def patch_bulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PatchBulkDataExporterConfigResponseItem]:
        """
        Update a data exporter configs with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PatchBulkDataExporterConfigResponseItem]
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.patch_bulk_data_exporter_config(
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_bulk_data_exporter_config(request=request, request_options=request_options)
        return _response.data

    def data_exporter_template(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Get all data exporter configs

        Parameters
        ----------
        type : typing.Optional[str]
            The data exporter config type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.data_exporter_template()
        """
        _response = self._raw_client.data_exporter_template(type=type, request_options=request_options)
        return _response.data

    def find_data_exporter_config_by_id(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Get a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.find_data_exporter_config_by_id(
            data_exporter_config_id="dataExporterConfigId",
        )
        """
        _response = self._raw_client.find_data_exporter_config_by_id(
            data_exporter_config_id, request_options=request_options
        )
        return _response.data

    def update_data_exporter_config(
        self,
        data_exporter_config_id: str,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExporterConfig:
        """
        Update a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.update_data_exporter_config(
            data_exporter_config_id="dataExporterConfigId",
        )
        """
        _response = self._raw_client.update_data_exporter_config(
            data_exporter_config_id,
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    def delete_data_exporter_config(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

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
        client.data_exporter_configs.delete_data_exporter_config(
            data_exporter_config_id="dataExporterConfigId",
        )
        """
        _response = self._raw_client.delete_data_exporter_config(
            data_exporter_config_id, request_options=request_options
        )
        return _response.data

    def patch_data_exporter_config(
        self, data_exporter_config_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Update a data exporter config with a diff

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_exporter_configs.patch_data_exporter_config(
            data_exporter_config_id="dataExporterConfigId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_data_exporter_config(
            data_exporter_config_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncDataExporterConfigsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataExporterConfigsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataExporterConfigsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataExporterConfigsClient
        """
        return self._raw_client

    async def find_all_data_exporters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DataExporterConfig]:
        """
        Get all data exporter configs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DataExporterConfig]
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
            await client.data_exporter_configs.find_all_data_exporters()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_data_exporters(request_options=request_options)
        return _response.data

    async def create_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExporterConfig:
        """
        Create a new data exporter config

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
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
            await client.data_exporter_configs.create_data_exporter_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_data_exporter_config(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    async def create_bulk_data_exporter_configs(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CreateBulkDataExporterConfigsResponseItem]:
        """
        Create a new data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CreateBulkDataExporterConfigsResponseItem]
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
            await client.data_exporter_configs.create_bulk_data_exporter_configs()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_bulk_data_exporter_configs(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    async def update_bulk_data_exporter_config(
        self,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UpdateBulkDataExporterConfigResponseItem]:
        """
        Update a data exporter configs

        Parameters
        ----------
        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UpdateBulkDataExporterConfigResponseItem]
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
            await client.data_exporter_configs.update_bulk_data_exporter_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_bulk_data_exporter_config(
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    async def deletebulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeletebulkDataExporterConfigResponseItem]:
        """
        Delete a data exporter config

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeletebulkDataExporterConfigResponseItem]
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
            await client.data_exporter_configs.deletebulk_data_exporter_config(
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletebulk_data_exporter_config(
            request=request, request_options=request_options
        )
        return _response.data

    async def patch_bulk_data_exporter_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PatchBulkDataExporterConfigResponseItem]:
        """
        Update a data exporter configs with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PatchBulkDataExporterConfigResponseItem]
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
            await client.data_exporter_configs.patch_bulk_data_exporter_config(
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_bulk_data_exporter_config(
            request=request, request_options=request_options
        )
        return _response.data

    async def data_exporter_template(
        self, *, type: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Get all data exporter configs

        Parameters
        ----------
        type : typing.Optional[str]
            The data exporter config type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
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
            await client.data_exporter_configs.data_exporter_template()


        asyncio.run(main())
        """
        _response = await self._raw_client.data_exporter_template(type=type, request_options=request_options)
        return _response.data

    async def find_data_exporter_config_by_id(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Get a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
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
            await client.data_exporter_configs.find_data_exporter_config_by_id(
                data_exporter_config_id="dataExporterConfigId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_data_exporter_config_by_id(
            data_exporter_config_id, request_options=request_options
        )
        return _response.data

    async def update_data_exporter_config(
        self,
        data_exporter_config_id: str,
        *,
        buffer_size: typing.Optional[int] = OMIT,
        config: typing.Optional[DataExporterConfigConfig] = OMIT,
        desc: typing.Optional[str] = OMIT,
        enabled: typing.Optional[str] = OMIT,
        filtering: typing.Optional[Filtering] = OMIT,
        group_duration: typing.Optional[int] = OMIT,
        group_size: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        json_workers: typing.Optional[int] = OMIT,
        location: typing.Optional[Location] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        projection: typing.Optional[typing.Dict[str, str]] = OMIT,
        send_workers: typing.Optional[int] = OMIT,
        typ: typing.Optional[DataExporterConfigTyp] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExporterConfig:
        """
        Update a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        buffer_size : typing.Optional[int]
            buffer size

        config : typing.Optional[DataExporterConfigConfig]
            Data Exporter config

        desc : typing.Optional[str]
            Description

        enabled : typing.Optional[str]
            Boolean

        filtering : typing.Optional[Filtering]
            filtering

        group_duration : typing.Optional[int]
            duration

        group_size : typing.Optional[int]
            Group size

        id : typing.Optional[str]
            Id

        json_workers : typing.Optional[int]
            nb workers

        location : typing.Optional[Location]
            location

        metadata : typing.Optional[typing.Dict[str, str]]
            Metadata

        name : typing.Optional[str]
            Name

        projection : typing.Optional[typing.Dict[str, str]]
            projection

        send_workers : typing.Optional[int]
            send workers

        typ : typing.Optional[DataExporterConfigTyp]
            Type of data exporter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
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
            await client.data_exporter_configs.update_data_exporter_config(
                data_exporter_config_id="dataExporterConfigId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_data_exporter_config(
            data_exporter_config_id,
            buffer_size=buffer_size,
            config=config,
            desc=desc,
            enabled=enabled,
            filtering=filtering,
            group_duration=group_duration,
            group_size=group_size,
            id=id,
            json_workers=json_workers,
            location=location,
            metadata=metadata,
            name=name,
            projection=projection,
            send_workers=send_workers,
            typ=typ,
            request_options=request_options,
        )
        return _response.data

    async def delete_data_exporter_config(
        self, data_exporter_config_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a data exporter config

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

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
            await client.data_exporter_configs.delete_data_exporter_config(
                data_exporter_config_id="dataExporterConfigId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_data_exporter_config(
            data_exporter_config_id, request_options=request_options
        )
        return _response.data

    async def patch_data_exporter_config(
        self, data_exporter_config_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> DataExporterConfig:
        """
        Update a data exporter config with a diff

        Parameters
        ----------
        data_exporter_config_id : str
            The data exporter config id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExporterConfig
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
            await client.data_exporter_configs.patch_data_exporter_config(
                data_exporter_config_id="dataExporterConfigId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_data_exporter_config(
            data_exporter_config_id, request=request, request_options=request_options
        )
        return _response.data
