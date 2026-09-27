

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.excel_status import ExcelStatus
from ..types.report import Report
from .raw_client import AsyncRawExcelReportsClient, RawExcelReportsClient
from .types.download_excel_report_request_report_type import DownloadExcelReportRequestReportType
from .types.generate_excel_report_request_report_type import GenerateExcelReportRequestReportType
from .types.get_accounting_marketing_metrics_request_period_unit import GetAccountingMarketingMetricsRequestPeriodUnit
from .types.get_excel_report_generation_status_request_report_type import (
    GetExcelReportGenerationStatusRequestReportType,
)
from .types.get_excel_report_request_report_type import GetExcelReportRequestReportType


class ExcelReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExcelReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExcelReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExcelReportsClient
        """
        return self._raw_client

    def get_excel_report_generation_status(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportGenerationStatusRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExcelStatus:
        """
        Returns the status of the latest report requested.

        Parameters
        ----------
        company_id : str

        report_type : GetExcelReportGenerationStatusRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExcelStatus
            OK

        Examples
        --------
        from fern.excel_reports import GetExcelReportGenerationStatusRequestReportType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.excel_reports.get_excel_report_generation_status(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            report_type=GetExcelReportGenerationStatusRequestReportType.AUDIT,
        )
        """
        _response = self._raw_client.get_excel_report_generation_status(
            company_id, report_type=report_type, request_options=request_options
        )
        return _response.data

    def generate_excel_report(
        self,
        company_id: str,
        *,
        report_type: GenerateExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExcelStatus:
        """
        Generate an Excel report which can subsequently be downloaded.

        Parameters
        ----------
        company_id : str

        report_type : GenerateExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExcelStatus
            OK

        Examples
        --------
        from fern.excel_reports import GenerateExcelReportRequestReportType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.excel_reports.generate_excel_report(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            report_type=GenerateExcelReportRequestReportType.AUDIT,
        )
        """
        _response = self._raw_client.generate_excel_report(
            company_id, report_type=report_type, request_options=request_options
        )
        return _response.data

    def get_excel_report(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Download the previously generated Excel report to a local drive.

        Parameters
        ----------
        company_id : str

        report_type : GetExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK
        """
        with self._raw_client.get_excel_report(
            company_id, report_type=report_type, request_options=request_options
        ) as r:
            yield from r.data

    def download_excel_report(
        self,
        company_id: str,
        *,
        report_type: DownloadExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Download the previously generated Excel report to a local drive.

        Parameters
        ----------
        company_id : str

        report_type : DownloadExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK
        """
        with self._raw_client.download_excel_report(
            company_id, report_type=report_type, request_options=request_options
        ) as r:
            yield from r.data

    def get_accounting_marketing_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetAccountingMarketingMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        show_input_values: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Request an Excel report for download.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetAccountingMarketingMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        show_input_values : typing.Optional[bool]
            If set to true, then the system includes the input values within the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        from fern.excel_reports import GetAccountingMarketingMetricsRequestPeriodUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.excel_reports.get_accounting_marketing_metrics(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            report_date="29-09-2020",
            period_length=1,
            number_of_periods=1,
            period_unit=GetAccountingMarketingMetricsRequestPeriodUnit.DAY,
        )
        """
        _response = self._raw_client.get_accounting_marketing_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            show_input_values=show_input_values,
            request_options=request_options,
        )
        return _response.data


class AsyncExcelReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExcelReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExcelReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExcelReportsClient
        """
        return self._raw_client

    async def get_excel_report_generation_status(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportGenerationStatusRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExcelStatus:
        """
        Returns the status of the latest report requested.

        Parameters
        ----------
        company_id : str

        report_type : GetExcelReportGenerationStatusRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExcelStatus
            OK

        Examples
        --------
        import asyncio

        from fern.excel_reports import GetExcelReportGenerationStatusRequestReportType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.excel_reports.get_excel_report_generation_status(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                report_type=GetExcelReportGenerationStatusRequestReportType.AUDIT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_excel_report_generation_status(
            company_id, report_type=report_type, request_options=request_options
        )
        return _response.data

    async def generate_excel_report(
        self,
        company_id: str,
        *,
        report_type: GenerateExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExcelStatus:
        """
        Generate an Excel report which can subsequently be downloaded.

        Parameters
        ----------
        company_id : str

        report_type : GenerateExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExcelStatus
            OK

        Examples
        --------
        import asyncio

        from fern.excel_reports import GenerateExcelReportRequestReportType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.excel_reports.generate_excel_report(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                report_type=GenerateExcelReportRequestReportType.AUDIT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_excel_report(
            company_id, report_type=report_type, request_options=request_options
        )
        return _response.data

    async def get_excel_report(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Download the previously generated Excel report to a local drive.

        Parameters
        ----------
        company_id : str

        report_type : GetExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK
        """
        async with self._raw_client.get_excel_report(
            company_id, report_type=report_type, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def download_excel_report(
        self,
        company_id: str,
        *,
        report_type: DownloadExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Download the previously generated Excel report to a local drive.

        Parameters
        ----------
        company_id : str

        report_type : DownloadExcelReportRequestReportType
            The type of report you want to generate and download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            OK
        """
        async with self._raw_client.download_excel_report(
            company_id, report_type=report_type, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_accounting_marketing_metrics(
        self,
        company_id: str,
        connection_id: str,
        *,
        report_date: str,
        period_length: int,
        number_of_periods: int,
        period_unit: GetAccountingMarketingMetricsRequestPeriodUnit,
        include_display_names: typing.Optional[bool] = None,
        show_input_values: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Report:
        """
        Request an Excel report for download.

        Parameters
        ----------
        company_id : str

        connection_id : str

        report_date : str
            The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month.

        period_length : int
            The number of months per period. E.g. 2 = 2 months per period.

        number_of_periods : int
            The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods.

        period_unit : GetAccountingMarketingMetricsRequestPeriodUnit
            The period unit of time returned.

        include_display_names : typing.Optional[bool]
            Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable.

        show_input_values : typing.Optional[bool]
            If set to true, then the system includes the input values within the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Report
            OK

        Examples
        --------
        import asyncio

        from fern.excel_reports import GetAccountingMarketingMetricsRequestPeriodUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.excel_reports.get_accounting_marketing_metrics(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                report_date="29-09-2020",
                period_length=1,
                number_of_periods=1,
                period_unit=GetAccountingMarketingMetricsRequestPeriodUnit.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_accounting_marketing_metrics(
            company_id,
            connection_id,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
            show_input_values=show_input_values,
            request_options=request_options,
        )
        return _response.data
