

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.app_limit_param import AppLimitParam
from ..types.dataset_snapshot import DatasetSnapshot
from ..types.dataset_snapshot_id_param import DatasetSnapshotIdParam
from ..types.dataset_snapshot_name import DatasetSnapshotName
from ..types.ending_before import EndingBefore
from ..types.ids import Ids
from ..types.org_name import OrgName
from ..types.starting_after import StartingAfter
from .raw_client import AsyncRawDatasetSnapshotsClient, RawDatasetSnapshotsClient
from .types.get_dataset_snapshot_response import GetDatasetSnapshotResponse


OMIT = typing.cast(typing.Any, ...)


class DatasetSnapshotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetSnapshotsClient
        """
        return self._raw_client

    def get_dataset_snapshot(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        dataset_snapshot_name: typing.Optional[DatasetSnapshotName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDatasetSnapshotResponse:
        """
        List out all dataset_snapshots. The dataset_snapshots are sorted by creation date, with the most recently-created dataset_snapshots coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        dataset_snapshot_name : typing.Optional[DatasetSnapshotName]
            Name of the dataset_snapshot to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDatasetSnapshotResponse
            Returns a list of dataset_snapshot objects

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.get_dataset_snapshot()
        """
        _response = self._raw_client.get_dataset_snapshot(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            dataset_snapshot_name=dataset_snapshot_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    def post_dataset_snapshot(
        self,
        *,
        dataset_id: str,
        name: str,
        xact_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Create a new dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will return the existing dataset_snapshot unmodified

        Parameters
        ----------
        dataset_id : str
            Unique identifier for the dataset that this snapshot belongs to

        name : str
            Name of the dataset snapshot

        xact_id : str
            Transaction id of the brainstore version at the time of the snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the new dataset_snapshot object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.post_dataset_snapshot(
            dataset_id="dataset_id",
            name="name",
            xact_id="xact_id",
        )
        """
        _response = self._raw_client.post_dataset_snapshot(
            dataset_id=dataset_id, name=name, xact_id=xact_id, description=description, request_options=request_options
        )
        return _response.data

    def put_dataset_snapshot(
        self,
        *,
        dataset_id: str,
        name: str,
        xact_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Create or replace dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will replace the existing dataset_snapshot with the provided fields

        Parameters
        ----------
        dataset_id : str
            Unique identifier for the dataset that this snapshot belongs to

        name : str
            Name of the dataset snapshot

        xact_id : str
            Transaction id of the brainstore version at the time of the snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the new dataset_snapshot object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.put_dataset_snapshot(
            dataset_id="dataset_id",
            name="name",
            xact_id="xact_id",
        )
        """
        _response = self._raw_client.put_dataset_snapshot(
            dataset_id=dataset_id, name=name, xact_id=xact_id, description=description, request_options=request_options
        )
        return _response.data

    def get_dataset_snapshot_id(
        self, dataset_snapshot_id: DatasetSnapshotIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetSnapshot:
        """
        Get a dataset_snapshot object by its id

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the dataset_snapshot object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.get_dataset_snapshot_id(
            dataset_snapshot_id="dataset_snapshot_id",
        )
        """
        _response = self._raw_client.get_dataset_snapshot_id(dataset_snapshot_id, request_options=request_options)
        return _response.data

    def delete_dataset_snapshot_id(
        self, dataset_snapshot_id: DatasetSnapshotIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetSnapshot:
        """
        Delete a dataset_snapshot object by its id

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the deleted dataset_snapshot object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.delete_dataset_snapshot_id(
            dataset_snapshot_id="dataset_snapshot_id",
        )
        """
        _response = self._raw_client.delete_dataset_snapshot_id(dataset_snapshot_id, request_options=request_options)
        return _response.data

    def patch_dataset_snapshot_id(
        self,
        dataset_snapshot_id: DatasetSnapshotIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Partially update a dataset_snapshot object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        name : typing.Optional[str]
            Name of the dataset snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the dataset_snapshot object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dataset_snapshots.patch_dataset_snapshot_id(
            dataset_snapshot_id="dataset_snapshot_id",
        )
        """
        _response = self._raw_client.patch_dataset_snapshot_id(
            dataset_snapshot_id, name=name, description=description, request_options=request_options
        )
        return _response.data


class AsyncDatasetSnapshotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetSnapshotsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetSnapshotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetSnapshotsClient
        """
        return self._raw_client

    async def get_dataset_snapshot(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        dataset_snapshot_name: typing.Optional[DatasetSnapshotName] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDatasetSnapshotResponse:
        """
        List out all dataset_snapshots. The dataset_snapshots are sorted by creation date, with the most recently-created dataset_snapshots coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        dataset_snapshot_name : typing.Optional[DatasetSnapshotName]
            Name of the dataset_snapshot to search for

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDatasetSnapshotResponse
            Returns a list of dataset_snapshot objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.get_dataset_snapshot()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dataset_snapshot(
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            ids=ids,
            dataset_snapshot_name=dataset_snapshot_name,
            org_name=org_name,
            request_options=request_options,
        )
        return _response.data

    async def post_dataset_snapshot(
        self,
        *,
        dataset_id: str,
        name: str,
        xact_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Create a new dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will return the existing dataset_snapshot unmodified

        Parameters
        ----------
        dataset_id : str
            Unique identifier for the dataset that this snapshot belongs to

        name : str
            Name of the dataset snapshot

        xact_id : str
            Transaction id of the brainstore version at the time of the snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the new dataset_snapshot object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.post_dataset_snapshot(
                dataset_id="dataset_id",
                name="name",
                xact_id="xact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_dataset_snapshot(
            dataset_id=dataset_id, name=name, xact_id=xact_id, description=description, request_options=request_options
        )
        return _response.data

    async def put_dataset_snapshot(
        self,
        *,
        dataset_id: str,
        name: str,
        xact_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Create or replace dataset_snapshot. If there is an existing dataset_snapshot with the same name as the one specified in the request, will replace the existing dataset_snapshot with the provided fields

        Parameters
        ----------
        dataset_id : str
            Unique identifier for the dataset that this snapshot belongs to

        name : str
            Name of the dataset snapshot

        xact_id : str
            Transaction id of the brainstore version at the time of the snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the new dataset_snapshot object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.put_dataset_snapshot(
                dataset_id="dataset_id",
                name="name",
                xact_id="xact_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_dataset_snapshot(
            dataset_id=dataset_id, name=name, xact_id=xact_id, description=description, request_options=request_options
        )
        return _response.data

    async def get_dataset_snapshot_id(
        self, dataset_snapshot_id: DatasetSnapshotIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetSnapshot:
        """
        Get a dataset_snapshot object by its id

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the dataset_snapshot object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.get_dataset_snapshot_id(
                dataset_snapshot_id="dataset_snapshot_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dataset_snapshot_id(dataset_snapshot_id, request_options=request_options)
        return _response.data

    async def delete_dataset_snapshot_id(
        self, dataset_snapshot_id: DatasetSnapshotIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DatasetSnapshot:
        """
        Delete a dataset_snapshot object by its id

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the deleted dataset_snapshot object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.delete_dataset_snapshot_id(
                dataset_snapshot_id="dataset_snapshot_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dataset_snapshot_id(
            dataset_snapshot_id, request_options=request_options
        )
        return _response.data

    async def patch_dataset_snapshot_id(
        self,
        dataset_snapshot_id: DatasetSnapshotIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetSnapshot:
        """
        Partially update a dataset_snapshot object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        dataset_snapshot_id : DatasetSnapshotIdParam
            DatasetSnapshot id

        name : typing.Optional[str]
            Name of the dataset snapshot

        description : typing.Optional[str]
            Textual description of the dataset snapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetSnapshot
            Returns the dataset_snapshot object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dataset_snapshots.patch_dataset_snapshot_id(
                dataset_snapshot_id="dataset_snapshot_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_dataset_snapshot_id(
            dataset_snapshot_id, name=name, description=description, request_options=request_options
        )
        return _response.data
