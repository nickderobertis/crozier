

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset import Dataset
from ..types.dataset_collection import DatasetCollection
from ..types.dataset_event_collection import DatasetEventCollection
from .raw_client import AsyncRawDatasetClient, RawDatasetClient


class DatasetClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetClient
        """
        return self._raw_client

    def get_datasets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        uri_pattern: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        uri_pattern : typing.Optional[str]
            If set, only return datasets with uris matching this pattern.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dataset.get_datasets()
        """
        _response = self._raw_client.get_datasets(
            limit=limit, offset=offset, order_by=order_by, uri_pattern=uri_pattern, request_options=request_options
        )
        return _response.data

    def get_dataset_events(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        dataset_id: typing.Optional[int] = None,
        source_dag_id: typing.Optional[str] = None,
        source_task_id: typing.Optional[str] = None,
        source_run_id: typing.Optional[str] = None,
        source_map_index: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetEventCollection:
        """
        Get dataset events

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        dataset_id : typing.Optional[int]
            The Dataset ID that updated the dataset.

        source_dag_id : typing.Optional[str]
            The DAG ID that updated the dataset.

        source_task_id : typing.Optional[str]
            The task ID that updated the dataset.

        source_run_id : typing.Optional[str]
            The DAG run ID that updated the dataset.

        source_map_index : typing.Optional[int]
            The map index that updated the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetEventCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dataset.get_dataset_events()
        """
        _response = self._raw_client.get_dataset_events(
            limit=limit,
            offset=offset,
            order_by=order_by,
            dataset_id=dataset_id,
            source_dag_id=source_dag_id,
            source_task_id=source_task_id,
            source_run_id=source_run_id,
            source_map_index=source_map_index,
            request_options=request_options,
        )
        return _response.data

    def get_dataset(self, uri: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dataset:
        """
        Get a dataset by uri.

        Parameters
        ----------
        uri : str
            The encoded Dataset URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dataset.get_dataset(
            uri="uri",
        )
        """
        _response = self._raw_client.get_dataset(uri, request_options=request_options)
        return _response.data


class AsyncDatasetClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetClient
        """
        return self._raw_client

    async def get_datasets(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        uri_pattern: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetCollection:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        uri_pattern : typing.Optional[str]
            If set, only return datasets with uris matching this pattern.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dataset.get_datasets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_datasets(
            limit=limit, offset=offset, order_by=order_by, uri_pattern=uri_pattern, request_options=request_options
        )
        return _response.data

    async def get_dataset_events(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        dataset_id: typing.Optional[int] = None,
        source_dag_id: typing.Optional[str] = None,
        source_task_id: typing.Optional[str] = None,
        source_run_id: typing.Optional[str] = None,
        source_map_index: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetEventCollection:
        """
        Get dataset events

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        dataset_id : typing.Optional[int]
            The Dataset ID that updated the dataset.

        source_dag_id : typing.Optional[str]
            The DAG ID that updated the dataset.

        source_task_id : typing.Optional[str]
            The task ID that updated the dataset.

        source_run_id : typing.Optional[str]
            The DAG run ID that updated the dataset.

        source_map_index : typing.Optional[int]
            The map index that updated the dataset.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetEventCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dataset.get_dataset_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dataset_events(
            limit=limit,
            offset=offset,
            order_by=order_by,
            dataset_id=dataset_id,
            source_dag_id=source_dag_id,
            source_task_id=source_task_id,
            source_run_id=source_run_id,
            source_map_index=source_map_index,
            request_options=request_options,
        )
        return _response.data

    async def get_dataset(self, uri: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dataset:
        """
        Get a dataset by uri.

        Parameters
        ----------
        uri : str
            The encoded Dataset URI

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dataset.get_dataset(
                uri="uri",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dataset(uri, request_options=request_options)
        return _response.data
