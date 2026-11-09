

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dataset_run_item import DatasetRunItem
from .raw_client import AsyncRawDatasetrunitemsClient, RawDatasetrunitemsClient


OMIT = typing.cast(typing.Any, ...)


class DatasetrunitemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetrunitemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetrunitemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetrunitemsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        run_name: str,
        dataset_item_id: str,
        run_description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        trace_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetRunItem:
        """
        Create a dataset run item

        Parameters
        ----------
        run_name : str

        dataset_item_id : str

        run_description : typing.Optional[str]
            Description of the run. If run exists, description will be updated.

        metadata : typing.Optional[typing.Any]
            Metadata of the dataset run, updates run if run already exists

        observation_id : typing.Optional[str]

        trace_id : typing.Optional[str]
            traceId should always be provided. For compatibility with older SDK versions it can also be inferred from the provided observationId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunItem


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasetrunitems.create(
            run_name="runName",
            dataset_item_id="datasetItemId",
        )
        """
        _response = self._raw_client.create(
            run_name=run_name,
            dataset_item_id=dataset_item_id,
            run_description=run_description,
            metadata=metadata,
            observation_id=observation_id,
            trace_id=trace_id,
            request_options=request_options,
        )
        return _response.data


class AsyncDatasetrunitemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetrunitemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetrunitemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetrunitemsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        run_name: str,
        dataset_item_id: str,
        run_description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Any] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        trace_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetRunItem:
        """
        Create a dataset run item

        Parameters
        ----------
        run_name : str

        dataset_item_id : str

        run_description : typing.Optional[str]
            Description of the run. If run exists, description will be updated.

        metadata : typing.Optional[typing.Any]
            Metadata of the dataset run, updates run if run already exists

        observation_id : typing.Optional[str]

        trace_id : typing.Optional[str]
            traceId should always be provided. For compatibility with older SDK versions it can also be inferred from the provided observationId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunItem


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
            await client.datasetrunitems.create(
                run_name="runName",
                dataset_item_id="datasetItemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            run_name=run_name,
            dataset_item_id=dataset_item_id,
            run_description=run_description,
            metadata=metadata,
            observation_id=observation_id,
            trace_id=trace_id,
            request_options=request_options,
        )
        return _response.data
