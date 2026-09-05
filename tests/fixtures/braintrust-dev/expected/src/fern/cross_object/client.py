

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cross_object_insert_response import CrossObjectInsertResponse
from .raw_client import AsyncRawCrossObjectClient, RawCrossObjectClient
from .types.cross_object_insert_request_dataset_value import CrossObjectInsertRequestDatasetValue
from .types.cross_object_insert_request_experiment_value import CrossObjectInsertRequestExperimentValue
from .types.cross_object_insert_request_project_logs_value import CrossObjectInsertRequestProjectLogsValue


OMIT = typing.cast(typing.Any, ...)


class CrossObjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrossObjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrossObjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrossObjectClient
        """
        return self._raw_client

    def post_cross_object_insert(
        self,
        *,
        experiment: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]] = OMIT,
        dataset: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]] = OMIT,
        project_logs: typing.Optional[
            typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrossObjectInsertResponse:
        """
        Insert events and feedback across object types

        Parameters
        ----------
        experiment : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]]
            A mapping from experiment id to a set of log events and feedback items to insert

        dataset : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]]
            A mapping from dataset id to a set of log events and feedback items to insert

        project_logs : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]]
            A mapping from project id to a set of log events and feedback items to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrossObjectInsertResponse
            Returns the inserted row ids for the events on each individual object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cross_object.post_cross_object_insert()
        """
        _response = self._raw_client.post_cross_object_insert(
            experiment=experiment, dataset=dataset, project_logs=project_logs, request_options=request_options
        )
        return _response.data


class AsyncCrossObjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrossObjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrossObjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrossObjectClient
        """
        return self._raw_client

    async def post_cross_object_insert(
        self,
        *,
        experiment: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]] = OMIT,
        dataset: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]] = OMIT,
        project_logs: typing.Optional[
            typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrossObjectInsertResponse:
        """
        Insert events and feedback across object types

        Parameters
        ----------
        experiment : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]]
            A mapping from experiment id to a set of log events and feedback items to insert

        dataset : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]]
            A mapping from dataset id to a set of log events and feedback items to insert

        project_logs : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]]
            A mapping from project id to a set of log events and feedback items to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrossObjectInsertResponse
            Returns the inserted row ids for the events on each individual object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cross_object.post_cross_object_insert()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_cross_object_insert(
            experiment=experiment, dataset=dataset, project_logs=project_logs, request_options=request_options
        )
        return _response.data
