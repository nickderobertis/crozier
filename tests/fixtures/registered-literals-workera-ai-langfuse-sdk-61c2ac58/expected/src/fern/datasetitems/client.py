

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset_item import DatasetItem
from ..types.dataset_status import DatasetStatus
from ..types.delete_dataset_item_response import DeleteDatasetItemResponse
from ..types.paginated_dataset_items import PaginatedDatasetItems
from .raw_client import AsyncRawDatasetitemsClient, RawDatasetitemsClient


OMIT = typing.cast(typing.Any, ...)


class DatasetitemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetitemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetitemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetitemsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        dataset_name: typing.Optional[str] = None,
        source_trace_id: typing.Optional[str] = None,
        source_observation_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetItems:
        """
        Get dataset items

        Parameters
        ----------
        dataset_name : typing.Optional[str]

        source_trace_id : typing.Optional[str]

        source_observation_id : typing.Optional[str]

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetItems


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasetitems.list()
        """
        _response = self._raw_client.list(
            dataset_name=dataset_name,
            source_trace_id=source_trace_id,
            source_observation_id=source_observation_id,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        dataset_name: str,
        input: typing.Optional[typing.Any] = OMIT,
        expected_output: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        source_trace_id: typing.Optional[str] = OMIT,
        source_observation_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        status: typing.Optional[DatasetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetItem:
        """
        Create a dataset item

        Parameters
        ----------
        dataset_name : str

        input : typing.Optional[typing.Any]

        expected_output : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Any]

        source_trace_id : typing.Optional[str]

        source_observation_id : typing.Optional[str]

        id : typing.Optional[str]
            Dataset items are upserted on their id. Id needs to be unique (project-level) and cannot be reused across datasets.

        status : typing.Optional[DatasetStatus]
            Defaults to ACTIVE for newly created items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetItem


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasetitems.create(
            dataset_name="datasetName",
        )
        """
        _response = self._raw_client.create(
            dataset_name=dataset_name,
            input=input,
            expected_output=expected_output,
            metadata=metadata,
            source_trace_id=source_trace_id,
            source_observation_id=source_observation_id,
            id=id,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetItem:
        """
        Get a dataset item

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetItem


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasetitems.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteDatasetItemResponse:
        """
        Delete a dataset item and all its run items. This action is irreversible.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetItemResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasetitems.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data


class AsyncDatasetitemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetitemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetitemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetitemsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        dataset_name: typing.Optional[str] = None,
        source_trace_id: typing.Optional[str] = None,
        source_observation_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetItems:
        """
        Get dataset items

        Parameters
        ----------
        dataset_name : typing.Optional[str]

        source_trace_id : typing.Optional[str]

        source_observation_id : typing.Optional[str]

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetItems


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasetitems.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            dataset_name=dataset_name,
            source_trace_id=source_trace_id,
            source_observation_id=source_observation_id,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        dataset_name: str,
        input: typing.Optional[typing.Any] = OMIT,
        expected_output: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        source_trace_id: typing.Optional[str] = OMIT,
        source_observation_id: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        status: typing.Optional[DatasetStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetItem:
        """
        Create a dataset item

        Parameters
        ----------
        dataset_name : str

        input : typing.Optional[typing.Any]

        expected_output : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Any]

        source_trace_id : typing.Optional[str]

        source_observation_id : typing.Optional[str]

        id : typing.Optional[str]
            Dataset items are upserted on their id. Id needs to be unique (project-level) and cannot be reused across datasets.

        status : typing.Optional[DatasetStatus]
            Defaults to ACTIVE for newly created items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetItem


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasetitems.create(
                dataset_name="datasetName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            dataset_name=dataset_name,
            input=input,
            expected_output=expected_output,
            metadata=metadata,
            source_trace_id=source_trace_id,
            source_observation_id=source_observation_id,
            id=id,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetItem:
        """
        Get a dataset item

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetItem


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasetitems.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDatasetItemResponse:
        """
        Delete a dataset item and all its run items. This action is irreversible.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetItemResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasetitems.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data
