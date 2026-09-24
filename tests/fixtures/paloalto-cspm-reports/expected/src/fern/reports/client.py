

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.parsed_table_filter import ParsedTableFilter
from ..types.report_filter_suggestion import ReportFilterSuggestion
from ..types.report_generation_config_api_model import ReportGenerationConfigApiModel
from ..types.report_generation_config_api_model_cloud_type import ReportGenerationConfigApiModelCloudType
from ..types.report_generation_config_api_model_counts import ReportGenerationConfigApiModelCounts
from ..types.report_generation_config_api_model_target import ReportGenerationConfigApiModelTarget
from ..types.report_generation_config_api_model_type import ReportGenerationConfigApiModelType
from .raw_client import AsyncRawReportsClient, RawReportsClient
from .types.base_report_generation_config_api_model_cloud_type import BaseReportGenerationConfigApiModelCloudType
from .types.base_report_generation_config_api_model_counts import BaseReportGenerationConfigApiModelCounts
from .types.base_report_generation_config_api_model_target import BaseReportGenerationConfigApiModelTarget
from .types.base_report_generation_config_api_model_type import BaseReportGenerationConfigApiModelType
from .types.list_reports_request_report_frequency import ListReportsRequestReportFrequency
from .types.list_reports_request_report_schedule import ListReportsRequestReportSchedule
from .types.list_reports_request_report_view import ListReportsRequestReportView


OMIT = typing.cast(typing.Any, ...)


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def list_reports(
        self,
        *,
        cloud_account: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        report_frequency: typing.Optional[ListReportsRequestReportFrequency] = None,
        report_schedule: typing.Optional[ListReportsRequestReportSchedule] = None,
        report_email_recipients: typing.Optional[str] = None,
        report_view: typing.Optional[ListReportsRequestReportView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportGenerationConfigApiModel]:
        """
        Returns a list of compliance report generation configurations, including the ID for each configuration. Accepts query parameters to narrow the list.

        Optional query parameters are available to narrow the reports list request. See
        [Get Report Overview Filters and Options](/prisma-cloud/api/cspm/get-report-filters-and-options)
        for the REST API request to get the available query parameters.

        Parameters
        ----------
        cloud_account : typing.Optional[str]
            Cloud account

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        account_group : typing.Optional[str]
            Account group

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        report_frequency : typing.Optional[ListReportsRequestReportFrequency]
            Report frequency

        report_schedule : typing.Optional[ListReportsRequestReportSchedule]
            Report schedule

        report_email_recipients : typing.Optional[str]
            Report email recipients

        report_view : typing.Optional[ListReportsRequestReportView]
            Report type. Default is COMPLIANCE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportGenerationConfigApiModel]
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.list_reports()
        """
        _response = self._raw_client.list_reports(
            cloud_account=cloud_account,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            account_group=account_group,
            policy_compliance_standard=policy_compliance_standard,
            report_frequency=report_frequency,
            report_schedule=report_schedule,
            report_email_recipients=report_email_recipients,
            report_view=report_view,
            request_options=request_options,
        )
        return _response.data

    def save_report(
        self,
        *,
        cloud_type: ReportGenerationConfigApiModelCloudType,
        name: str,
        compliance_standard_deleted: typing.Optional[bool] = OMIT,
        compliance_standard_id: typing.Optional[str] = OMIT,
        counts: typing.Optional[ReportGenerationConfigApiModelCounts] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_on: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_modified_by: typing.Optional[str] = OMIT,
        last_modified_on: typing.Optional[int] = OMIT,
        last_scheduled: typing.Optional[int] = OMIT,
        locale: typing.Optional[str] = OMIT,
        next_schedule: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        target: typing.Optional[ReportGenerationConfigApiModelTarget] = OMIT,
        total_instance_count: typing.Optional[int] = OMIT,
        type: typing.Optional[ReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.
        :::info
         **Replacement  Endpoint: [Add Report Config V2](/prisma-cloud/api/cspm/save-report-v-2)**
        :::



        You can use the body parameters to specify whether the report is a one-time report
        or a recurring report. Specify a recurring report by providing a valid
        **target.schedule** body parameter.

        Parameters
        ----------
        cloud_type : ReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        compliance_standard_deleted : typing.Optional[bool]
            Compliance Standard Deleted

        compliance_standard_id : typing.Optional[str]
            Compliance standard ID

        counts : typing.Optional[ReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        created_by : typing.Optional[str]
            User who created this report

        created_on : typing.Optional[int]
            Report created on this timestamp

        id : typing.Optional[str]
            Report ID

        last_modified_by : typing.Optional[str]
            Last modified by

        last_modified_on : typing.Optional[int]
            Timestamp of last modification

        last_scheduled : typing.Optional[int]
            Timestamp of last generated report

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        next_schedule : typing.Optional[int]
            Timestamp of next scheduled report

        status : typing.Optional[str]
            Report generation status

        target : typing.Optional[ReportGenerationConfigApiModelTarget]
            Report definition

        total_instance_count : typing.Optional[int]
            Total number of reports for the report ID

        type : typing.Optional[ReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            successful operation

        Examples
        --------
        from fern import FernApi, ReportGenerationConfigApiModelCloudType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.save_report(
            cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
            name="name",
        )
        """
        _response = self._raw_client.save_report(
            cloud_type=cloud_type,
            name=name,
            compliance_standard_deleted=compliance_standard_deleted,
            compliance_standard_id=compliance_standard_id,
            counts=counts,
            created_by=created_by,
            created_on=created_on,
            id=id,
            last_modified_by=last_modified_by,
            last_modified_on=last_modified_on,
            last_scheduled=last_scheduled,
            locale=locale,
            next_schedule=next_schedule,
            status=status,
            target=target,
            total_instance_count=total_instance_count,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def save_report_v2(
        self,
        *,
        cloud_type: BaseReportGenerationConfigApiModelCloudType,
        name: str,
        counts: typing.Optional[BaseReportGenerationConfigApiModelCounts] = OMIT,
        locale: typing.Optional[str] = OMIT,
        target: typing.Optional[BaseReportGenerationConfigApiModelTarget] = OMIT,
        type: typing.Optional[BaseReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.

        You can use the body parameters to specify whether the report is a one-time report
        or a recurring report. Specify a recurring report by providing a valid
        **target.schedule** body parameter.

        **Note:** The `complianceStandardIds` parameter is not applicable to `COMPLIANCE` or `RIS` report types

        Parameters
        ----------
        cloud_type : BaseReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        counts : typing.Optional[BaseReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        target : typing.Optional[BaseReportGenerationConfigApiModelTarget]
            Report definition

        type : typing.Optional[BaseReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            successful operation

        Examples
        --------
        from fern.reports import BaseReportGenerationConfigApiModelCloudType

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.save_report_v2(
            cloud_type=BaseReportGenerationConfigApiModelCloudType.AWS,
            name="name",
        )
        """
        _response = self._raw_client.save_report_v2(
            cloud_type=cloud_type,
            name=name,
            counts=counts,
            locale=locale,
            target=target,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_report_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.List[str]]:
        """
        Returns a list of the compliance report types and identifies which report types are available for each cloud type.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[str]]
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_report_types()
        """
        _response = self._raw_client.get_report_types(request_options=request_options)
        return _response.data

    def get_specified_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportGenerationConfigApiModel:
        """
        Returns the compliance report generation configuration with the specified ID. The response includes pass/fail counts for this ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_specified_report(
            id="id",
        )
        """
        _response = self._raw_client.get_specified_report(id, request_options=request_options)
        return _response.data

    def update_report(
        self,
        id_: str,
        *,
        cloud_type: ReportGenerationConfigApiModelCloudType,
        name: str,
        compliance_standard_deleted: typing.Optional[bool] = OMIT,
        compliance_standard_id: typing.Optional[str] = OMIT,
        counts: typing.Optional[ReportGenerationConfigApiModelCounts] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_on: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_modified_by: typing.Optional[str] = OMIT,
        last_modified_on: typing.Optional[int] = OMIT,
        last_scheduled: typing.Optional[int] = OMIT,
        locale: typing.Optional[str] = OMIT,
        next_schedule: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        target: typing.Optional[ReportGenerationConfigApiModelTarget] = OMIT,
        total_instance_count: typing.Optional[int] = OMIT,
        type: typing.Optional[ReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Updates the compliance report generation configuration with the specified ID.

        You can update a recurring report schedule through this request.
        When using this request to update a report schedule, the only body
        parameter that is required is **target**.

        Parameters
        ----------
        id_ : str
            Report ID

        cloud_type : ReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        compliance_standard_deleted : typing.Optional[bool]
            Compliance Standard Deleted

        compliance_standard_id : typing.Optional[str]
            Compliance standard ID

        counts : typing.Optional[ReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        created_by : typing.Optional[str]
            User who created this report

        created_on : typing.Optional[int]
            Report created on this timestamp

        id : typing.Optional[str]
            Report ID

        last_modified_by : typing.Optional[str]
            Last modified by

        last_modified_on : typing.Optional[int]
            Timestamp of last modification

        last_scheduled : typing.Optional[int]
            Timestamp of last generated report

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        next_schedule : typing.Optional[int]
            Timestamp of next scheduled report

        status : typing.Optional[str]
            Report generation status

        target : typing.Optional[ReportGenerationConfigApiModelTarget]
            Report definition

        total_instance_count : typing.Optional[int]
            Total number of reports for the report ID

        type : typing.Optional[ReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        from fern import FernApi, ReportGenerationConfigApiModelCloudType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.update_report(
            id_="id",
            cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
            name="name",
        )
        """
        _response = self._raw_client.update_report(
            id_,
            cloud_type=cloud_type,
            name=name,
            compliance_standard_deleted=compliance_standard_deleted,
            compliance_standard_id=compliance_standard_id,
            counts=counts,
            created_by=created_by,
            created_on=created_on,
            id=id,
            last_modified_by=last_modified_by,
            last_modified_on=last_modified_on,
            last_scheduled=last_scheduled,
            locale=locale,
            next_schedule=next_schedule,
            status=status,
            target=target,
            total_instance_count=total_instance_count,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def delete_report(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the compliance report generation configuration with the specified ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.delete_report(
            id="id",
        )
        """
        _response = self._raw_client.delete_report(id, request_options=request_options)
        return _response.data

    def download_report(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the compliance report with the specified ID. If the report is scheduled, then the request downloads the latest generated report.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.download_report(
            id="id",
        )
        """
        _response = self._raw_client.download_report(id, request_options=request_options)
        return _response.data

    def get_historical_report_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReportGenerationConfigApiModel]:
        """
        Returns a list of metadata for the scheduled compliance reports that have been run for the specified report ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportGenerationConfigApiModel]
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_historical_report_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_historical_report_by_id(id, request_options=request_options)
        return _response.data

    def get_last_scheduled_report_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportGenerationConfigApiModel:
        """
        Returns metadata for the scheduled compliance report that has the specified report ID and was generated on the given timestamp. Returned data includes pass/fail counts.

        Parameters
        ----------
        id : str
            Report ID

        last_scheduled : int
            Timestamp of report generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_last_scheduled_report_by_id(
            id="id",
            last_scheduled=1000000,
        )
        """
        _response = self._raw_client.get_last_scheduled_report_by_id(
            id, last_scheduled, request_options=request_options
        )
        return _response.data

    def download_historical_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Downloads the compliance report that has the specified report ID and was generated on the specified timestamp.

        Parameters
        ----------
        id : str
            Report ID

        last_scheduled : int
            Timestamp of report generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.download_historical_by_id(
            id="id",
            last_scheduled=1000000,
        )
        """
        _response = self._raw_client.download_historical_by_id(id, last_scheduled, request_options=request_options)
        return _response.data

    def get_report_filters_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportFilterSuggestion:
        """
        Returns an object whose key/value pairs identify filter options for compliance posture data. The keys are supported filters, and the corresponding values identify the available and saved filter options.

        The keys in the response object are the filter names you can use in
        [List Report Overview Filter Autocomplete Suggestions](/prisma-cloud/api/cspm/get-report-posture-filter-options).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportFilterSuggestion
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_report_filters_and_options()
        """
        _response = self._raw_client.get_report_filters_and_options(request_options=request_options)
        return _response.data

    def get_report_posture_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParsedTableFilter:
        """
        Returns the available options for a specific report posture filter. Also supports fuzzy autocomplete search for easier filtering.

        You can find the available filter names through
        [Get Report Overview Filters and Options request](/prisma-cloud/api/cspm/get-report-filters-and-options).
        The keys in the response object from that GET request are
        the available filter names.

        Parameters
        ----------
        filter_name : str
            Filter name

        query : typing.Optional[str]
            Case-insensitive fuzzy search autocomplete filter. Includes only items that contain the query as a substring.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParsedTableFilter
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.reports.get_report_posture_filter_options(
            filter_name="filterName",
        )
        """
        _response = self._raw_client.get_report_posture_filter_options(
            filter_name=filter_name, query=query, request_options=request_options
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def list_reports(
        self,
        *,
        cloud_account: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        report_frequency: typing.Optional[ListReportsRequestReportFrequency] = None,
        report_schedule: typing.Optional[ListReportsRequestReportSchedule] = None,
        report_email_recipients: typing.Optional[str] = None,
        report_view: typing.Optional[ListReportsRequestReportView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportGenerationConfigApiModel]:
        """
        Returns a list of compliance report generation configurations, including the ID for each configuration. Accepts query parameters to narrow the list.

        Optional query parameters are available to narrow the reports list request. See
        [Get Report Overview Filters and Options](/prisma-cloud/api/cspm/get-report-filters-and-options)
        for the REST API request to get the available query parameters.

        Parameters
        ----------
        cloud_account : typing.Optional[str]
            Cloud account

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        account_group : typing.Optional[str]
            Account group

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        report_frequency : typing.Optional[ListReportsRequestReportFrequency]
            Report frequency

        report_schedule : typing.Optional[ListReportsRequestReportSchedule]
            Report schedule

        report_email_recipients : typing.Optional[str]
            Report email recipients

        report_view : typing.Optional[ListReportsRequestReportView]
            Report type. Default is COMPLIANCE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportGenerationConfigApiModel]
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.list_reports()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_reports(
            cloud_account=cloud_account,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            account_group=account_group,
            policy_compliance_standard=policy_compliance_standard,
            report_frequency=report_frequency,
            report_schedule=report_schedule,
            report_email_recipients=report_email_recipients,
            report_view=report_view,
            request_options=request_options,
        )
        return _response.data

    async def save_report(
        self,
        *,
        cloud_type: ReportGenerationConfigApiModelCloudType,
        name: str,
        compliance_standard_deleted: typing.Optional[bool] = OMIT,
        compliance_standard_id: typing.Optional[str] = OMIT,
        counts: typing.Optional[ReportGenerationConfigApiModelCounts] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_on: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_modified_by: typing.Optional[str] = OMIT,
        last_modified_on: typing.Optional[int] = OMIT,
        last_scheduled: typing.Optional[int] = OMIT,
        locale: typing.Optional[str] = OMIT,
        next_schedule: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        target: typing.Optional[ReportGenerationConfigApiModelTarget] = OMIT,
        total_instance_count: typing.Optional[int] = OMIT,
        type: typing.Optional[ReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.
        :::info
         **Replacement  Endpoint: [Add Report Config V2](/prisma-cloud/api/cspm/save-report-v-2)**
        :::



        You can use the body parameters to specify whether the report is a one-time report
        or a recurring report. Specify a recurring report by providing a valid
        **target.schedule** body parameter.

        Parameters
        ----------
        cloud_type : ReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        compliance_standard_deleted : typing.Optional[bool]
            Compliance Standard Deleted

        compliance_standard_id : typing.Optional[str]
            Compliance standard ID

        counts : typing.Optional[ReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        created_by : typing.Optional[str]
            User who created this report

        created_on : typing.Optional[int]
            Report created on this timestamp

        id : typing.Optional[str]
            Report ID

        last_modified_by : typing.Optional[str]
            Last modified by

        last_modified_on : typing.Optional[int]
            Timestamp of last modification

        last_scheduled : typing.Optional[int]
            Timestamp of last generated report

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        next_schedule : typing.Optional[int]
            Timestamp of next scheduled report

        status : typing.Optional[str]
            Report generation status

        target : typing.Optional[ReportGenerationConfigApiModelTarget]
            Report definition

        total_instance_count : typing.Optional[int]
            Total number of reports for the report ID

        type : typing.Optional[ReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ReportGenerationConfigApiModelCloudType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.save_report(
                cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_report(
            cloud_type=cloud_type,
            name=name,
            compliance_standard_deleted=compliance_standard_deleted,
            compliance_standard_id=compliance_standard_id,
            counts=counts,
            created_by=created_by,
            created_on=created_on,
            id=id,
            last_modified_by=last_modified_by,
            last_modified_on=last_modified_on,
            last_scheduled=last_scheduled,
            locale=locale,
            next_schedule=next_schedule,
            status=status,
            target=target,
            total_instance_count=total_instance_count,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def save_report_v2(
        self,
        *,
        cloud_type: BaseReportGenerationConfigApiModelCloudType,
        name: str,
        counts: typing.Optional[BaseReportGenerationConfigApiModelCounts] = OMIT,
        locale: typing.Optional[str] = OMIT,
        target: typing.Optional[BaseReportGenerationConfigApiModelTarget] = OMIT,
        type: typing.Optional[BaseReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Creates a compliance report generation configuration based on the specified parameters. Report generation can be either one-time or recurring.

        You can use the body parameters to specify whether the report is a one-time report
        or a recurring report. Specify a recurring report by providing a valid
        **target.schedule** body parameter.

        **Note:** The `complianceStandardIds` parameter is not applicable to `COMPLIANCE` or `RIS` report types

        Parameters
        ----------
        cloud_type : BaseReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        counts : typing.Optional[BaseReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        target : typing.Optional[BaseReportGenerationConfigApiModelTarget]
            Report definition

        type : typing.Optional[BaseReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            successful operation

        Examples
        --------
        import asyncio

        from fern.reports import BaseReportGenerationConfigApiModelCloudType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.save_report_v2(
                cloud_type=BaseReportGenerationConfigApiModelCloudType.AWS,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_report_v2(
            cloud_type=cloud_type,
            name=name,
            counts=counts,
            locale=locale,
            target=target,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_report_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.List[str]]:
        """
        Returns a list of the compliance report types and identifies which report types are available for each cloud type.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[str]]
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_report_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_report_types(request_options=request_options)
        return _response.data

    async def get_specified_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportGenerationConfigApiModel:
        """
        Returns the compliance report generation configuration with the specified ID. The response includes pass/fail counts for this ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_specified_report(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_specified_report(id, request_options=request_options)
        return _response.data

    async def update_report(
        self,
        id_: str,
        *,
        cloud_type: ReportGenerationConfigApiModelCloudType,
        name: str,
        compliance_standard_deleted: typing.Optional[bool] = OMIT,
        compliance_standard_id: typing.Optional[str] = OMIT,
        counts: typing.Optional[ReportGenerationConfigApiModelCounts] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_on: typing.Optional[int] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_modified_by: typing.Optional[str] = OMIT,
        last_modified_on: typing.Optional[int] = OMIT,
        last_scheduled: typing.Optional[int] = OMIT,
        locale: typing.Optional[str] = OMIT,
        next_schedule: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        target: typing.Optional[ReportGenerationConfigApiModelTarget] = OMIT,
        total_instance_count: typing.Optional[int] = OMIT,
        type: typing.Optional[ReportGenerationConfigApiModelType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportGenerationConfigApiModel:
        """
        Updates the compliance report generation configuration with the specified ID.

        You can update a recurring report schedule through this request.
        When using this request to update a report schedule, the only body
        parameter that is required is **target**.

        Parameters
        ----------
        id_ : str
            Report ID

        cloud_type : ReportGenerationConfigApiModelCloudType
            Cloud type

        name : str
            Report name

        compliance_standard_deleted : typing.Optional[bool]
            Compliance Standard Deleted

        compliance_standard_id : typing.Optional[str]
            Compliance standard ID

        counts : typing.Optional[ReportGenerationConfigApiModelCounts]
            Model for compliance aggregate count

        created_by : typing.Optional[str]
            User who created this report

        created_on : typing.Optional[int]
            Report created on this timestamp

        id : typing.Optional[str]
            Report ID

        last_modified_by : typing.Optional[str]
            Last modified by

        last_modified_on : typing.Optional[int]
            Timestamp of last modification

        last_scheduled : typing.Optional[int]
            Timestamp of last generated report

        locale : typing.Optional[str]
            Locale of caller (e.g. en_us, jp). Default is en_us.

        next_schedule : typing.Optional[int]
            Timestamp of next scheduled report

        status : typing.Optional[str]
            Report generation status

        target : typing.Optional[ReportGenerationConfigApiModelTarget]
            Report definition

        total_instance_count : typing.Optional[int]
            Total number of reports for the report ID

        type : typing.Optional[ReportGenerationConfigApiModelType]
            Report type. Default is COMPLIANCE.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ReportGenerationConfigApiModelCloudType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.update_report(
                id_="id",
                cloud_type=ReportGenerationConfigApiModelCloudType.AWS,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_report(
            id_,
            cloud_type=cloud_type,
            name=name,
            compliance_standard_deleted=compliance_standard_deleted,
            compliance_standard_id=compliance_standard_id,
            counts=counts,
            created_by=created_by,
            created_on=created_on,
            id=id,
            last_modified_by=last_modified_by,
            last_modified_on=last_modified_on,
            last_scheduled=last_scheduled,
            locale=locale,
            next_schedule=next_schedule,
            status=status,
            target=target,
            total_instance_count=total_instance_count,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def delete_report(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the compliance report generation configuration with the specified ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.delete_report(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_report(id, request_options=request_options)
        return _response.data

    async def download_report(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the compliance report with the specified ID. If the report is scheduled, then the request downloads the latest generated report.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.download_report(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_report(id, request_options=request_options)
        return _response.data

    async def get_historical_report_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ReportGenerationConfigApiModel]:
        """
        Returns a list of metadata for the scheduled compliance reports that have been run for the specified report ID.

        Parameters
        ----------
        id : str
            Report ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportGenerationConfigApiModel]
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_historical_report_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_historical_report_by_id(id, request_options=request_options)
        return _response.data

    async def get_last_scheduled_report_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportGenerationConfigApiModel:
        """
        Returns metadata for the scheduled compliance report that has the specified report ID and was generated on the given timestamp. Returned data includes pass/fail counts.

        Parameters
        ----------
        id : str
            Report ID

        last_scheduled : int
            Timestamp of report generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportGenerationConfigApiModel
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_last_scheduled_report_by_id(
                id="id",
                last_scheduled=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_last_scheduled_report_by_id(
            id, last_scheduled, request_options=request_options
        )
        return _response.data

    async def download_historical_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Downloads the compliance report that has the specified report ID and was generated on the specified timestamp.

        Parameters
        ----------
        id : str
            Report ID

        last_scheduled : int
            Timestamp of report generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.download_historical_by_id(
                id="id",
                last_scheduled=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_historical_by_id(
            id, last_scheduled, request_options=request_options
        )
        return _response.data

    async def get_report_filters_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReportFilterSuggestion:
        """
        Returns an object whose key/value pairs identify filter options for compliance posture data. The keys are supported filters, and the corresponding values identify the available and saved filter options.

        The keys in the response object are the filter names you can use in
        [List Report Overview Filter Autocomplete Suggestions](/prisma-cloud/api/cspm/get-report-posture-filter-options).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportFilterSuggestion
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_report_filters_and_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_report_filters_and_options(request_options=request_options)
        return _response.data

    async def get_report_posture_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParsedTableFilter:
        """
        Returns the available options for a specific report posture filter. Also supports fuzzy autocomplete search for easier filtering.

        You can find the available filter names through
        [Get Report Overview Filters and Options request](/prisma-cloud/api/cspm/get-report-filters-and-options).
        The keys in the response object from that GET request are
        the available filter names.

        Parameters
        ----------
        filter_name : str
            Filter name

        query : typing.Optional[str]
            Case-insensitive fuzzy search autocomplete filter. Includes only items that contain the query as a substring.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ParsedTableFilter
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.reports.get_report_posture_filter_options(
                filter_name="filterName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_report_posture_filter_options(
            filter_name=filter_name, query=query, request_options=request_options
        )
        return _response.data
