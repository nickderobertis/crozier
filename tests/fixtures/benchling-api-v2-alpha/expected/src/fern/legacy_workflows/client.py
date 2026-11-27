

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entry_external_file_by_id import EntryExternalFileById
from ..types.stage_entry import StageEntry
from .raw_client import AsyncRawLegacyWorkflowsClient, RawLegacyWorkflowsClient


class LegacyWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLegacyWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLegacyWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLegacyWorkflowsClient
        """
        return self._raw_client

    def get_stage_entry(
        self, stage_entry_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StageEntry:
        """
        Get a stage entry by ID

        Parameters
        ----------
        stage_entry_id : str
            ID of the stage entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageEntry
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.legacy_workflows.get_stage_entry(
            stage_entry_id="stage_entry_id",
        )
        """
        _response = self._raw_client.get_stage_entry(stage_entry_id, request_options=request_options)
        return _response.data

    def get_external_file_metadata(
        self, stage_entry_id: str, external_file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryExternalFileById:
        """
        Retrieves the metadata for an external file. Use the 'downloadURL' to download the actual file. (Expand the schema view for details)

        Parameters
        ----------
        stage_entry_id : str
            ID of the legacy workflow stage entry the file was uploaded to

        external_file_id : str
            ID of the external file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryExternalFileById
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.legacy_workflows.get_external_file_metadata(
            stage_entry_id="stage_entry_id",
            external_file_id="external_file_id",
        )
        """
        _response = self._raw_client.get_external_file_metadata(
            stage_entry_id, external_file_id, request_options=request_options
        )
        return _response.data


class AsyncLegacyWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLegacyWorkflowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLegacyWorkflowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLegacyWorkflowsClient
        """
        return self._raw_client

    async def get_stage_entry(
        self, stage_entry_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StageEntry:
        """
        Get a stage entry by ID

        Parameters
        ----------
        stage_entry_id : str
            ID of the stage entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageEntry
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.legacy_workflows.get_stage_entry(
                stage_entry_id="stage_entry_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stage_entry(stage_entry_id, request_options=request_options)
        return _response.data

    async def get_external_file_metadata(
        self, stage_entry_id: str, external_file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryExternalFileById:
        """
        Retrieves the metadata for an external file. Use the 'downloadURL' to download the actual file. (Expand the schema view for details)

        Parameters
        ----------
        stage_entry_id : str
            ID of the legacy workflow stage entry the file was uploaded to

        external_file_id : str
            ID of the external file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryExternalFileById
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.legacy_workflows.get_external_file_metadata(
                stage_entry_id="stage_entry_id",
                external_file_id="external_file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_external_file_metadata(
            stage_entry_id, external_file_id, request_options=request_options
        )
        return _response.data
