

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.excel_status import ExcelStatus
from ..types.report import Report
from .types.download_excel_report_request_report_type import DownloadExcelReportRequestReportType
from .types.generate_excel_report_request_report_type import GenerateExcelReportRequestReportType
from .types.get_accounting_marketing_metrics_request_period_unit import GetAccountingMarketingMetricsRequestPeriodUnit
from .types.get_excel_report_generation_status_request_report_type import (
    GetExcelReportGenerationStatusRequestReportType,
)
from .types.get_excel_report_request_report_type import GetExcelReportRequestReportType
from pydantic import ValidationError


class RawExcelReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_excel_report_generation_status(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportGenerationStatusRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExcelStatus]:
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
        HttpResponse[ExcelStatus]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/excel",
            method="GET",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExcelStatus,
                    parse_obj_as(
                        type_=ExcelStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def generate_excel_report(
        self,
        company_id: str,
        *,
        report_type: GenerateExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExcelStatus]:
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
        HttpResponse[ExcelStatus]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/excel",
            method="POST",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExcelStatus,
                    parse_obj_as(
                        type_=ExcelStatus,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_excel_report(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"data/companies/{encode_path_param(company_id)}/assess/excel/download",
            method="GET",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    @contextlib.contextmanager
    def download_excel_report(
        self,
        company_id: str,
        *,
        report_type: DownloadExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            OK
        """
        with self._client_wrapper.httpx_client.stream(
            f"data/companies/{encode_path_param(company_id)}/assess/excel/download",
            method="POST",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

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
    ) -> HttpResponse[Report]:
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
        HttpResponse[Report]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accountingMetrics/marketing",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
                "showInputValues": show_input_values,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawExcelReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_excel_report_generation_status(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportGenerationStatusRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExcelStatus]:
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
        AsyncHttpResponse[ExcelStatus]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/excel",
            method="GET",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExcelStatus,
                    parse_obj_as(
                        type_=ExcelStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def generate_excel_report(
        self,
        company_id: str,
        *,
        report_type: GenerateExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExcelStatus]:
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
        AsyncHttpResponse[ExcelStatus]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/assess/excel",
            method="POST",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExcelStatus,
                    parse_obj_as(
                        type_=ExcelStatus,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_excel_report(
        self,
        company_id: str,
        *,
        report_type: GetExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"data/companies/{encode_path_param(company_id)}/assess/excel/download",
            method="GET",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    @contextlib.asynccontextmanager
    async def download_excel_report(
        self,
        company_id: str,
        *,
        report_type: DownloadExcelReportRequestReportType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            OK
        """
        async with self._client_wrapper.httpx_client.stream(
            f"data/companies/{encode_path_param(company_id)}/assess/excel/download",
            method="POST",
            params={
                "reportType": report_type,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

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
    ) -> AsyncHttpResponse[Report]:
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
        AsyncHttpResponse[Report]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"data/companies/{encode_path_param(company_id)}/connections/{encode_path_param(connection_id)}/assess/accountingMetrics/marketing",
            method="GET",
            params={
                "reportDate": report_date,
                "periodLength": period_length,
                "numberOfPeriods": number_of_periods,
                "periodUnit": period_unit,
                "includeDisplayNames": include_display_names,
                "showInputValues": show_input_values,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Report,
                    parse_obj_as(
                        type_=Report,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
