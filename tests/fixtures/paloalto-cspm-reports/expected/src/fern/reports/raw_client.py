

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..types.parsed_table_filter import ParsedTableFilter
from ..types.report_filter_suggestion import ReportFilterSuggestion
from ..types.report_generation_config_api_model import ReportGenerationConfigApiModel
from ..types.report_generation_config_api_model_cloud_type import ReportGenerationConfigApiModelCloudType
from ..types.report_generation_config_api_model_counts import ReportGenerationConfigApiModelCounts
from ..types.report_generation_config_api_model_target import ReportGenerationConfigApiModelTarget
from ..types.report_generation_config_api_model_type import ReportGenerationConfigApiModelType
from .types.base_report_generation_config_api_model_cloud_type import BaseReportGenerationConfigApiModelCloudType
from .types.base_report_generation_config_api_model_counts import BaseReportGenerationConfigApiModelCounts
from .types.base_report_generation_config_api_model_target import BaseReportGenerationConfigApiModelTarget
from .types.base_report_generation_config_api_model_type import BaseReportGenerationConfigApiModelType
from .types.list_reports_request_report_frequency import ListReportsRequestReportFrequency
from .types.list_reports_request_report_schedule import ListReportsRequestReportSchedule
from .types.list_reports_request_report_view import ListReportsRequestReportView
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[typing.List[ReportGenerationConfigApiModel]]:
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
        HttpResponse[typing.List[ReportGenerationConfigApiModel]]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "report",
            method="GET",
            params={
                "cloud.account": cloud_account,
                "cloud.type": cloud_type,
                "cloud.region": cloud_region,
                "account.group": account_group,
                "policy.complianceStandard": policy_compliance_standard,
                "report.frequency": report_frequency,
                "report.schedule": report_schedule,
                "report.email.recipients": report_email_recipients,
                "report_view": report_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportGenerationConfigApiModel],
                    parse_obj_as(
                        type_=typing.List[ReportGenerationConfigApiModel],
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
    ) -> HttpResponse[ReportGenerationConfigApiModel]:
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
        HttpResponse[ReportGenerationConfigApiModel]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "report",
            method="POST",
            json={
                "cloudType": cloud_type,
                "complianceStandardDeleted": compliance_standard_deleted,
                "complianceStandardId": compliance_standard_id,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=ReportGenerationConfigApiModelCounts, direction="write"
                ),
                "createdBy": created_by,
                "createdOn": created_on,
                "id": id,
                "lastModifiedBy": last_modified_by,
                "lastModifiedOn": last_modified_on,
                "lastScheduled": last_scheduled,
                "locale": locale,
                "name": name,
                "nextSchedule": next_schedule,
                "status": status,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ReportGenerationConfigApiModelTarget, direction="write"
                ),
                "totalInstanceCount": total_instance_count,
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ReportGenerationConfigApiModel]:
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
        HttpResponse[ReportGenerationConfigApiModel]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/report",
            method="POST",
            json={
                "cloudType": cloud_type,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=BaseReportGenerationConfigApiModelCounts, direction="write"
                ),
                "locale": locale,
                "name": name,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=BaseReportGenerationConfigApiModelTarget, direction="write"
                ),
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_report_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.List[str]]]:
        """
        Returns a list of the compliance report types and identifies which report types are available for each cloud type.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.List[str]]]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "report/type",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[str]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_specified_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReportGenerationConfigApiModel]:
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
        HttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ReportGenerationConfigApiModel]:
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
        HttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id_)}",
            method="PUT",
            json={
                "cloudType": cloud_type,
                "complianceStandardDeleted": compliance_standard_deleted,
                "complianceStandardId": compliance_standard_id,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=ReportGenerationConfigApiModelCounts, direction="write"
                ),
                "createdBy": created_by,
                "createdOn": created_on,
                "id": id,
                "lastModifiedBy": last_modified_by,
                "lastModifiedOn": last_modified_on,
                "lastScheduled": last_scheduled,
                "locale": locale,
                "name": name,
                "nextSchedule": next_schedule,
                "status": status,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ReportGenerationConfigApiModelTarget, direction="write"
                ),
                "totalInstanceCount": total_instance_count,
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_report(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def download_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_historical_report_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ReportGenerationConfigApiModel]]:
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
        HttpResponse[typing.List[ReportGenerationConfigApiModel]]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportGenerationConfigApiModel],
                    parse_obj_as(
                        type_=typing.List[ReportGenerationConfigApiModel],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_last_scheduled_report_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReportGenerationConfigApiModel]:
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
        HttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/{encode_path_param(last_scheduled)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def download_historical_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/{encode_path_param(last_scheduled)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_report_filters_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReportFilterSuggestion]:
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
        HttpResponse[ReportFilterSuggestion]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "filter/report/suggest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportFilterSuggestion,
                    parse_obj_as(
                        type_=ReportFilterSuggestion,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_report_posture_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ParsedTableFilter]:
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
        HttpResponse[ParsedTableFilter]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "filter/report/suggest",
            method="POST",
            json={
                "filterName": filter_name,
                "query": query,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParsedTableFilter,
                    parse_obj_as(
                        type_=ParsedTableFilter,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[typing.List[ReportGenerationConfigApiModel]]:
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
        AsyncHttpResponse[typing.List[ReportGenerationConfigApiModel]]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "report",
            method="GET",
            params={
                "cloud.account": cloud_account,
                "cloud.type": cloud_type,
                "cloud.region": cloud_region,
                "account.group": account_group,
                "policy.complianceStandard": policy_compliance_standard,
                "report.frequency": report_frequency,
                "report.schedule": report_schedule,
                "report.email.recipients": report_email_recipients,
                "report_view": report_view,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportGenerationConfigApiModel],
                    parse_obj_as(
                        type_=typing.List[ReportGenerationConfigApiModel],
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
    ) -> AsyncHttpResponse[ReportGenerationConfigApiModel]:
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
        AsyncHttpResponse[ReportGenerationConfigApiModel]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "report",
            method="POST",
            json={
                "cloudType": cloud_type,
                "complianceStandardDeleted": compliance_standard_deleted,
                "complianceStandardId": compliance_standard_id,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=ReportGenerationConfigApiModelCounts, direction="write"
                ),
                "createdBy": created_by,
                "createdOn": created_on,
                "id": id,
                "lastModifiedBy": last_modified_by,
                "lastModifiedOn": last_modified_on,
                "lastScheduled": last_scheduled,
                "locale": locale,
                "name": name,
                "nextSchedule": next_schedule,
                "status": status,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ReportGenerationConfigApiModelTarget, direction="write"
                ),
                "totalInstanceCount": total_instance_count,
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ReportGenerationConfigApiModel]:
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
        AsyncHttpResponse[ReportGenerationConfigApiModel]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/report",
            method="POST",
            json={
                "cloudType": cloud_type,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=BaseReportGenerationConfigApiModelCounts, direction="write"
                ),
                "locale": locale,
                "name": name,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=BaseReportGenerationConfigApiModelTarget, direction="write"
                ),
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_report_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.List[str]]]:
        """
        Returns a list of the compliance report types and identifies which report types are available for each cloud type.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.List[str]]]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "report/type",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[str]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_specified_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReportGenerationConfigApiModel]:
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
        AsyncHttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ReportGenerationConfigApiModel]:
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
        AsyncHttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id_)}",
            method="PUT",
            json={
                "cloudType": cloud_type,
                "complianceStandardDeleted": compliance_standard_deleted,
                "complianceStandardId": compliance_standard_id,
                "counts": convert_and_respect_annotation_metadata(
                    object_=counts, annotation=ReportGenerationConfigApiModelCounts, direction="write"
                ),
                "createdBy": created_by,
                "createdOn": created_on,
                "id": id,
                "lastModifiedBy": last_modified_by,
                "lastModifiedOn": last_modified_on,
                "lastScheduled": last_scheduled,
                "locale": locale,
                "name": name,
                "nextSchedule": next_schedule,
                "status": status,
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ReportGenerationConfigApiModelTarget, direction="write"
                ),
                "totalInstanceCount": total_instance_count,
                "type": type,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def download_report(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_historical_report_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ReportGenerationConfigApiModel]]:
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
        AsyncHttpResponse[typing.List[ReportGenerationConfigApiModel]]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportGenerationConfigApiModel],
                    parse_obj_as(
                        type_=typing.List[ReportGenerationConfigApiModel],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_last_scheduled_report_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReportGenerationConfigApiModel]:
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
        AsyncHttpResponse[ReportGenerationConfigApiModel]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/{encode_path_param(last_scheduled)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportGenerationConfigApiModel,
                    parse_obj_as(
                        type_=ReportGenerationConfigApiModel,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def download_historical_by_id(
        self, id: str, last_scheduled: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"report/{encode_path_param(id)}/{encode_path_param(last_scheduled)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_report_filters_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReportFilterSuggestion]:
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
        AsyncHttpResponse[ReportFilterSuggestion]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "filter/report/suggest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReportFilterSuggestion,
                    parse_obj_as(
                        type_=ReportFilterSuggestion,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_report_posture_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ParsedTableFilter]:
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
        AsyncHttpResponse[ParsedTableFilter]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "filter/report/suggest",
            method="POST",
            json={
                "filterName": filter_name,
                "query": query,
            },
            headers={
                "content-type": "application/json; charset=UTF-8",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ParsedTableFilter,
                    parse_obj_as(
                        type_=ParsedTableFilter,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
