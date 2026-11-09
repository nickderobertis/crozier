

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.info import Info
from .raw_client import AsyncRawReportClient, RawReportClient
from .types.upload_report_request_report_format import UploadReportRequestReportFormat


OMIT = typing.cast(typing.Any, ...)


class ReportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportClient
        """
        return self._raw_client

    def upload_report(
        self,
        *,
        upload: int,
        report_format: UploadReportRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import a report to an existing upload

        Parameters
        ----------
        upload : int
            Upload ID

        report_format : UploadReportRequestReportFormat
            Type of report being uploaded

        group_name : typing.Optional[str]
            The group name to chose while uploading report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            ReportImport job is scheduled successfully for the given upload.

        Examples
        --------
        from fern.report import UploadReportRequestReportFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.report.upload_report(
            upload=1,
            report_format=UploadReportRequestReportFormat.DECISIONIMPORTER,
        )
        """
        _response = self._raw_client.upload_report(
            upload=upload, report_format=report_format, group_name=group_name, request_options=request_options
        )
        return _response.data


class AsyncReportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportClient
        """
        return self._raw_client

    async def upload_report(
        self,
        *,
        upload: int,
        report_format: UploadReportRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import a report to an existing upload

        Parameters
        ----------
        upload : int
            Upload ID

        report_format : UploadReportRequestReportFormat
            Type of report being uploaded

        group_name : typing.Optional[str]
            The group name to chose while uploading report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            ReportImport job is scheduled successfully for the given upload.

        Examples
        --------
        import asyncio

        from fern.report import UploadReportRequestReportFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.report.upload_report(
                upload=1,
                report_format=UploadReportRequestReportFormat.DECISIONIMPORTER,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_report(
            upload=upload, report_format=report_format, group_name=group_name, request_options=request_options
        )
        return _response.data
