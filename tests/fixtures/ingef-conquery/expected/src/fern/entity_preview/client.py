

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connector_id import ConnectorId
from ..types.dataset_id import DatasetId
from ..types.date_range import DateRange
from ..types.entity_history_execution_status import EntityHistoryExecutionStatus
from ..types.filter_value import FilterValue
from .raw_client import AsyncRawEntityPreviewClient, RawEntityPreviewClient


OMIT = typing.cast(typing.Any, ...)


class EntityPreviewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntityPreviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntityPreviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntityPreviewClient
        """
        return self._raw_client

    def resolve_entities(
        self,
        dataset: DatasetId,
        *,
        request: typing.Sequence[FilterValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : typing.Sequence[FilterValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            List of tuple of ids.

        Examples
        --------
        from fern import FernApi, FilterValue_IntegerRange

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entity_preview.resolve_entities(
            dataset="dataset",
            request=[FilterValue_IntegerRange()],
        )
        """
        _response = self._raw_client.resolve_entities(dataset, request=request, request_options=request_options)
        return _response.data

    def get_entity_preview(
        self,
        dataset: DatasetId,
        *,
        id_kind: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        time: typing.Optional[DateRange] = OMIT,
        sources: typing.Optional[typing.Sequence[ConnectorId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityHistoryExecutionStatus:
        """
        Parameters
        ----------
        dataset : DatasetId

        id_kind : typing.Optional[str]
            The kind of the entity Id. Options are made available through `ColumnConfig#name`

        entity_id : typing.Optional[str]
            The Id of the entity.

        time : typing.Optional[DateRange]

        sources : typing.Optional[typing.Sequence[ConnectorId]]
            List of connectorIds to export their backing tables.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityHistoryExecutionStatus
            Description of the history of the entity.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.entity_preview.get_entity_preview(
            dataset="dataset",
        )
        """
        _response = self._raw_client.get_entity_preview(
            dataset, id_kind=id_kind, entity_id=entity_id, time=time, sources=sources, request_options=request_options
        )
        return _response.data


class AsyncEntityPreviewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntityPreviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntityPreviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntityPreviewClient
        """
        return self._raw_client

    async def resolve_entities(
        self,
        dataset: DatasetId,
        *,
        request: typing.Sequence[FilterValue],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        dataset : DatasetId

        request : typing.Sequence[FilterValue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            List of tuple of ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FilterValue_IntegerRange

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entity_preview.resolve_entities(
                dataset="dataset",
                request=[FilterValue_IntegerRange()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_entities(dataset, request=request, request_options=request_options)
        return _response.data

    async def get_entity_preview(
        self,
        dataset: DatasetId,
        *,
        id_kind: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        time: typing.Optional[DateRange] = OMIT,
        sources: typing.Optional[typing.Sequence[ConnectorId]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntityHistoryExecutionStatus:
        """
        Parameters
        ----------
        dataset : DatasetId

        id_kind : typing.Optional[str]
            The kind of the entity Id. Options are made available through `ColumnConfig#name`

        entity_id : typing.Optional[str]
            The Id of the entity.

        time : typing.Optional[DateRange]

        sources : typing.Optional[typing.Sequence[ConnectorId]]
            List of connectorIds to export their backing tables.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityHistoryExecutionStatus
            Description of the history of the entity.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.entity_preview.get_entity_preview(
                dataset="dataset",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entity_preview(
            dataset, id_kind=id_kind, entity_id=entity_id, time=time, sources=sources, request_options=request_options
        )
        return _response.data
