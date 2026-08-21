

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.context_uuid import ContextUuid
from ..types.export_ready_response import ExportReadyResponse
from ..types.export_request_response import ExportRequestResponse
from ..types.export_request_uuid import ExportRequestUuid
from ..types.supplied_auth import SuppliedAuth
from .raw_client import AsyncRawExportClient, RawExportClient


OMIT = typing.cast(typing.Any, ...)


class ExportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportClient
        """
        return self._raw_client

    def export_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRequestResponse:
        """
        Create an export request to export all personal data stored within a particular personal data context. This will only schedule an export. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to export.

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRequestResponse
            Export request queued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.export.export_personal_data(
            context_uuid="1234",
        )
        """
        _response = self._raw_client.export_personal_data(
            context_uuid, authenticated_identifiers=authenticated_identifiers, request_options=request_options
        )
        return _response.data

    def query_the_status_of_an_export_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        export_request_id: typing.Optional[ExportRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportReadyResponse:
        """
        Query the status of an export request. The status should be polled for until completed. The location of the exported content is communicated once the export request is completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        export_request_id : typing.Optional[ExportRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportReadyResponse
            Export ready

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.export.query_the_status_of_an_export_request(
            accept_language="fi_FI",
        )
        """
        _response = self._raw_client.query_the_status_of_an_export_request(
            accept_language=accept_language, export_request_id=export_request_id, request_options=request_options
        )
        return _response.data


class AsyncExportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportClient
        """
        return self._raw_client

    async def export_personal_data(
        self,
        context_uuid: ContextUuid,
        *,
        authenticated_identifiers: typing.Optional[SuppliedAuth] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportRequestResponse:
        """
        Create an export request to export all personal data stored within a particular personal data context. This will only schedule an export. The status and result must be polled for separately.

        Parameters
        ----------
        context_uuid : ContextUuid
            The personal data context (data category) to export.

        authenticated_identifiers : typing.Optional[SuppliedAuth]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportRequestResponse
            Export request queued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export.export_personal_data(
                context_uuid="1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_personal_data(
            context_uuid, authenticated_identifiers=authenticated_identifiers, request_options=request_options
        )
        return _response.data

    async def query_the_status_of_an_export_request(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        export_request_id: typing.Optional[ExportRequestUuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportReadyResponse:
        """
        Query the status of an export request. The status should be polled for until completed. The location of the exported content is communicated once the export request is completed.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        export_request_id : typing.Optional[ExportRequestUuid]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportReadyResponse
            Export ready

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export.query_the_status_of_an_export_request(
                accept_language="fi_FI",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_the_status_of_an_export_request(
            accept_language=accept_language, export_request_id=export_request_id, request_options=request_options
        )
        return _response.data
