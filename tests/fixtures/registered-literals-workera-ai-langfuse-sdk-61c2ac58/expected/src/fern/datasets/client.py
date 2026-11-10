

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset import Dataset
from ..types.dataset_run_with_items import DatasetRunWithItems
from ..types.delete_dataset_run_response import DeleteDatasetRunResponse
from ..types.paginated_dataset_runs import PaginatedDatasetRuns
from ..types.paginated_datasets import PaginatedDatasets
from .raw_client import AsyncRawDatasetsClient, RawDatasetsClient


OMIT = typing.cast(typing.Any, ...)


class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        Get all datasets

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.list()
        """
        _response = self._raw_client.list(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Create a dataset

        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.create(
            name="name",
        )
        """
        _response = self._raw_client.create(
            name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    def get(self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dataset:
        """
        Get a dataset

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get(
            dataset_name="datasetName",
        )
        """
        _response = self._raw_client.get(dataset_name, request_options=request_options)
        return _response.data

    def getrun(
        self, dataset_name: str, run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetRunWithItems:
        """
        Get a dataset run and its items

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunWithItems


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.getrun(
            dataset_name="datasetName",
            run_name="runName",
        )
        """
        _response = self._raw_client.getrun(dataset_name, run_name, request_options=request_options)
        return _response.data

    def deleterun(
        self, dataset_name: str, run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDatasetRunResponse:
        """
        Delete a dataset run and all its run items. This action is irreversible.

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetRunResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.deleterun(
            dataset_name="datasetName",
            run_name="runName",
        )
        """
        _response = self._raw_client.deleterun(dataset_name, run_name, request_options=request_options)
        return _response.data

    def getruns(
        self,
        dataset_name: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetRuns:
        """
        Get dataset runs

        Parameters
        ----------
        dataset_name : str

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetRuns


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.getruns(
            dataset_name="datasetName",
        )
        """
        _response = self._raw_client.getruns(dataset_name, page=page, limit=limit, request_options=request_options)
        return _response.data


class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        Get all datasets

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets


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
            await client.datasets.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Create a dataset

        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset


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
            await client.datasets.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name, description=description, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def get(self, dataset_name: str, *, request_options: typing.Optional[RequestOptions] = None) -> Dataset:
        """
        Get a dataset

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset


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
            await client.datasets.get(
                dataset_name="datasetName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(dataset_name, request_options=request_options)
        return _response.data

    async def getrun(
        self, dataset_name: str, run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetRunWithItems:
        """
        Get a dataset run and its items

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunWithItems


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
            await client.datasets.getrun(
                dataset_name="datasetName",
                run_name="runName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrun(dataset_name, run_name, request_options=request_options)
        return _response.data

    async def deleterun(
        self, dataset_name: str, run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteDatasetRunResponse:
        """
        Delete a dataset run and all its run items. This action is irreversible.

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetRunResponse


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
            await client.datasets.deleterun(
                dataset_name="datasetName",
                run_name="runName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleterun(dataset_name, run_name, request_options=request_options)
        return _response.data

    async def getruns(
        self,
        dataset_name: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetRuns:
        """
        Get dataset runs

        Parameters
        ----------
        dataset_name : str

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetRuns


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
            await client.datasets.getruns(
                dataset_name="datasetName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getruns(
            dataset_name, page=page, limit=limit, request_options=request_options
        )
        return _response.data
