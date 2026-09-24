

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alert_filter_suggestion import AlertFilterSuggestion
from ..types.alert_model import AlertModel
from ..types.alert_status_change_request_model_dismissal_time_range import (
    AlertStatusChangeRequestModelDismissalTimeRange,
)
from ..types.alert_status_change_request_model_filter import AlertStatusChangeRequestModelFilter
from ..types.async_job import AsyncJob
from ..types.count_model import CountModel
from ..types.filter_model_time_range import FilterModelTimeRange
from ..types.paged_results_alert_model import PagedResultsAlertModel
from ..types.parsed_table_filter import ParsedTableFilter
from ..types.remediation_cli_model import RemediationCliModel
from ..types.require_dismissal_note_config_model import RequireDismissalNoteConfigModel
from ..types.ui_filter_model import UiFilterModel
from .raw_client import AsyncRawAlertsClient, RawAlertsClient
from .types.alerts_lookup_key_model_filter import AlertsLookupKeyModelFilter
from .types.get_alert_count_request_status import GetAlertCountRequestStatus
from .types.get_alerts_grouped_request_alert_status import GetAlertsGroupedRequestAlertStatus
from .types.get_alerts_grouped_request_policy_remediable import GetAlertsGroupedRequestPolicyRemediable
from .types.get_alerts_grouped_request_policy_severity import GetAlertsGroupedRequestPolicySeverity
from .types.get_alerts_grouped_request_policy_type import GetAlertsGroupedRequestPolicyType
from .types.get_alerts_request_alert_status import GetAlertsRequestAlertStatus
from .types.get_alerts_request_policy_remediable import GetAlertsRequestPolicyRemediable
from .types.get_alerts_request_policy_severity import GetAlertsRequestPolicySeverity
from .types.get_alerts_request_policy_type import GetAlertsRequestPolicyType
from .types.get_alerts_request_time_type import GetAlertsRequestTimeType
from .types.get_alerts_request_time_unit import GetAlertsRequestTimeUnit
from .types.get_alerts_v2request_alert_status import GetAlertsV2RequestAlertStatus
from .types.get_alerts_v2request_policy_remediable import GetAlertsV2RequestPolicyRemediable
from .types.get_alerts_v2request_policy_severity import GetAlertsV2RequestPolicySeverity
from .types.get_alerts_v2request_policy_type import GetAlertsV2RequestPolicyType
from .types.get_alerts_v2request_time_type import GetAlertsV2RequestTimeType
from .types.get_alerts_v2request_time_unit import GetAlertsV2RequestTimeUnit


OMIT = typing.cast(typing.Any, ...)


class AlertsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlertsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlertsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlertsClient
        """
        return self._raw_client

    def get_alert_filter_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertFilterSuggestion:
        """
        Returns an object whose keys are the available policy filters. The corresponding values are default or recently set filter options

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertFilterSuggestion
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alert_filter_and_options()
        """
        _response = self._raw_client.get_alert_filter_and_options(request_options=request_options)
        return _response.data

    def get_alert_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParsedTableFilter:
        """
        Returns available options for an alert filter key. Supports fuzzy autocomplete search. If you specify a **query** value in the request body parameters, the response includes only items that contain the **query** string.

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
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alert_filter_options(
            filter_name="filterName",
        )
        """
        _response = self._raw_client.get_alert_filter_options(
            filter_name=filter_name, query=query, request_options=request_options
        )
        return _response.data

    def get_alerts(
        self,
        *,
        time_type: GetAlertsRequestTimeType,
        time_amount: str,
        time_unit: GetAlertsRequestTimeUnit,
        detailed: bool,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsRequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsRequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsRequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsRequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns a list of alerts that match the constraints specified in the query parameters. Max 10k results. To get more, use **List Alerts V2 - GET**.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_type : GetAlertsRequestTimeType
            Time Type

        time_amount : str
            Number of **timeUnits**

        time_unit : GetAlertsRequestTimeUnit
            Time Unit

        detailed : bool
            true = Return detailed alert data.

        fields : typing.Optional[str]
            Comma-separated list of specific fields to retrieve. Allowed values: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity

        limit : typing.Optional[float]
            The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.

        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsRequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsRequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsRequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsRequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        from fern.alerts import GetAlertsRequestTimeType, GetAlertsRequestTimeUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alerts(
            time_type=GetAlertsRequestTimeType.RELATIVE,
            time_amount="timeAmount",
            time_unit=GetAlertsRequestTimeUnit.MINUTE,
            detailed=True,
        )
        """
        _response = self._raw_client.get_alerts(
            time_type=time_type,
            time_amount=time_amount,
            time_unit=time_unit,
            detailed=detailed,
            fields=fields,
            limit=limit,
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    def post_alerts(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns a list of alerts that matches the constraints specified in the body parameters. Max 10k results. To get more, use **List Alerts V2 - POST**.

        The **fields** body parameter allows you to request specific fields from the alert payload. These fields
        are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters** body parameter enables you to narrow your request for alerts. See
        [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.post_alerts()
        """
        _response = self._raw_client.post_alerts(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_alerts_v2(
        self,
        *,
        time_type: GetAlertsV2RequestTimeType,
        time_amount: str,
        time_unit: GetAlertsV2RequestTimeUnit,
        detailed: bool,
        fields: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page_token: typing.Optional[str] = None,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsV2RequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsV2RequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsV2RequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsV2RequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultsAlertModel:
        """
        Returns a paginated list of alerts from the Prisma Cloud platform.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_type : GetAlertsV2RequestTimeType
            Time Type

        time_amount : str
            Number of **timeUnits**

        time_unit : GetAlertsV2RequestTimeUnit
            Time Unit

        detailed : bool
            true = Return detailed alert data.

        fields : typing.Optional[str]
            Array of specific fields to return. Allowed fields: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity

        sort_by : typing.Optional[str]
            Response object property by which to sort response list. The valid values are in the response object attribute **sortAllowedColumns**. The format is **property:asc** for ascending and **property:desc** for descending sort

        limit : typing.Optional[float]
            The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.

        page_token : typing.Optional[str]
            Token that identifies the required page of data. When there are multiple pages of data in the response, set **pageToken** to the **nextPageToken** value from the previous API response to retrieve the next page of data.

        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsV2RequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsV2RequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsV2RequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsV2RequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultsAlertModel
            successful operation

        Examples
        --------
        from fern.alerts import GetAlertsV2RequestTimeType, GetAlertsV2RequestTimeUnit

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alerts_v2(
            time_type=GetAlertsV2RequestTimeType.RELATIVE,
            time_amount="timeAmount",
            time_unit=GetAlertsV2RequestTimeUnit.MINUTE,
            detailed=True,
            sort_by="sortBy=id:desc&sortBy=firstseen:asc,lastseen:desc",
        )
        """
        _response = self._raw_client.get_alerts_v2(
            time_type=time_type,
            time_amount=time_amount,
            time_unit=time_unit,
            detailed=detailed,
            fields=fields,
            sort_by=sort_by,
            limit=limit,
            page_token=page_token,
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    def post_alerts_v2(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultsAlertModel:
        """
        Returns a paginated list of alerts that matches the constraints specified in the body parameters.

        The **fields** request body parameter allows you to request specific fields from the alert payload.
        These fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters** request body parameter enables you to narrow your request for alerts. See
        [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        You can find the valid values for the **sortBy** request body parameter in the response
        object attribute **sortAllowedColumns**.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultsAlertModel
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.post_alerts_v2()
        """
        _response = self._raw_client.post_alerts_v2(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_alerts_grouped(
        self,
        *,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsGroupedRequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsGroupedRequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsGroupedRequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsGroupedRequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns alert counts grouped by policy. You can use query parameters to narrow the response.

        In the response object:

        * Property **alertRules** is not populated.
        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is not populated.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsGroupedRequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsGroupedRequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsGroupedRequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsGroupedRequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alerts_grouped()
        """
        _response = self._raw_client.get_alerts_grouped(
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    def post_alerts_grouped(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns alert counts grouped by policy. You can use body parameters to narrow the response.

        In the response object:

        * Property **alertRules** is not populated.
        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is not populated.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.post_alerts_grouped()
        """
        _response = self._raw_client.post_alerts_grouped(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_alert(
        self,
        id: str,
        *,
        detailed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertModel:
        """
        Returns information about an alert for the specified ID.

        In the response object, field **riskDetail** is deprecated.

        When `detailed` flag is set to **true**, following fields will be returned within the policy and response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        The `resource` response object will include `cloudAccountGroups` field when `detailed` is set to **true**

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 5/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        id : str
            Alert ID

        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertModel
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alert(
            id="id",
        )
        """
        _response = self._raw_client.get_alert(id, detailed=detailed, request_options=request_options)
        return _response.data

    def dismiss_alerts(
        self,
        *,
        filter: AlertStatusChangeRequestModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        dismissal_note: typing.Optional[str] = OMIT,
        dismissal_time_range: typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Dismisses one or more alerts on the Prisma Cloud platform. If the caller specifies a dismissal time range, then alerts will snooze for that time period rather than be dismissed.

        Parameters
        ----------
        filter : AlertStatusChangeRequestModelFilter
            Filter

        alerts : typing.Optional[typing.Sequence[str]]
            Alert IDs

        dismissal_note : typing.Optional[str]
            Reason for dismissal (this only applies to the dismiss alerts endpoint)

        dismissal_time_range : typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange]
            Dismissal Time Range

        policies : typing.Optional[typing.Sequence[str]]
            Policy IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import AlertStatusChangeRequestModelFilter, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.dismiss_alerts(
            filter=AlertStatusChangeRequestModelFilter(),
        )
        """
        _response = self._raw_client.dismiss_alerts(
            filter=filter,
            alerts=alerts,
            dismissal_note=dismissal_note,
            dismissal_time_range=dismissal_time_range,
            policies=policies,
            request_options=request_options,
        )
        return _response.data

    def is_dismissal_note_required(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequireDismissalNoteConfigModel:
        """
        Indicates whether or not the user is required to specify a reason (dismissal note) when dismissing an alert.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequireDismissalNoteConfigModel
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.is_dismissal_note_required()
        """
        _response = self._raw_client.is_dismissal_note_required(request_options=request_options)
        return _response.data

    def set_dismissal_note_required(
        self,
        *,
        require_dismissal_note: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Manages whether or not a user must provide a reason (dismissal note) when dismissing an alert on the Prisma Cloud platform.

        Parameters
        ----------
        require_dismissal_note : typing.Optional[bool]
            Require Dismissal Note

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
        client.alerts.set_dismissal_note_required()
        """
        _response = self._raw_client.set_dismissal_note_required(
            require_dismissal_note=require_dismissal_note, request_options=request_options
        )
        return _response.data

    def reopen_alerts(
        self,
        *,
        filter: AlertStatusChangeRequestModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        dismissal_note: typing.Optional[str] = OMIT,
        dismissal_time_range: typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sets the status of one or more dismissed or snoozed alerts on the Prisma Cloud platform to **open**.

        Parameters
        ----------
        filter : AlertStatusChangeRequestModelFilter
            Filter

        alerts : typing.Optional[typing.Sequence[str]]
            Alert IDs

        dismissal_note : typing.Optional[str]
            Reason for dismissal (this only applies to the dismiss alerts endpoint)

        dismissal_time_range : typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange]
            Dismissal Time Range

        policies : typing.Optional[typing.Sequence[str]]
            Policy IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import AlertStatusChangeRequestModelFilter, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.reopen_alerts(
            filter=AlertStatusChangeRequestModelFilter(),
        )
        """
        _response = self._raw_client.reopen_alerts(
            filter=filter,
            alerts=alerts,
            dismissal_note=dismissal_note,
            dismissal_time_range=dismissal_time_range,
            policies=policies,
            request_options=request_options,
        )
        return _response.data

    def get_alert_count(
        self, status: GetAlertCountRequestStatus, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CountModel:
        """
        Returns an alert count for the specified status.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        status : GetAlertCountRequestStatus
            Alert Status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountModel
            successful operation

        Examples
        --------
        from fern.alerts import GetAlertCountRequestStatus

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alert_count(
            status=GetAlertCountRequestStatus.OPEN,
        )
        """
        _response = self._raw_client.get_alert_count(status, request_options=request_options)
        return _response.data

    def submit_job_for_listing_alerts(
        self,
        *,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable in JSON format. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** body parameter allows you to request specific fields from the alert payload. These
        fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

         The **filters** body parameter enables you to narrow your request for alerts. See
         [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
         for an API request to list all the valid filters.

          #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.submit_job_for_listing_alerts()
        """
        _response = self._raw_client.submit_job_for_listing_alerts(
            time_range=time_range,
            detailed=detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_alerts_job_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncJob:
        """
        Get the status of the alerts list job with the specified job ID

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alerts_job_status(
            id="id",
        )
        """
        _response = self._raw_client.get_alerts_job_status(id, request_options=request_options)
        return _response.data

    def download_alerts_list_json(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the generated alerts list in JSON format for the specified job ID.

        Parameters
        ----------
        id : str
            Job ID

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
        client.alerts.download_alerts_list_json(
            id="id",
        )
        """
        _response = self._raw_client.download_alerts_list_json(id, request_options=request_options)
        return _response.data

    def submit_an_alert_csv_download_job(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable as a CSV file. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** request body parameter is ignored!

        The **filters** body parameter enables you to narrow your request for alerts. See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.submit_an_alert_csv_download_job()
        """
        _response = self._raw_client.submit_an_alert_csv_download_job(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_alert_csv_job_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncJob:
        """
        Returns the status of an alert CSV generation job with the specified job ID.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alert_csv_job_status(
            id="id",
        )
        """
        _response = self._raw_client.get_alert_csv_job_status(id, request_options=request_options)
        return _response.data

    def download_alert_csv(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the alert list that Prisma Cloud generated for the specified job ID, in CSV format.

        Parameters
        ----------
        id : str
            Job ID

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
        client.alerts.download_alert_csv(
            id="id",
        )
        """
        _response = self._raw_client.download_alert_csv(id, request_options=request_options)
        return _response.data

    def submit_a_job_for_listing_alerts_grouped_by_policy(
        self,
        *,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate a list of alerts grouped by the policy they violated. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** body parameter allows you to request specific fields from the alert payload. These
        fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters*8 body parameter enables you to narrow your request for alerts.
        See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.submit_a_job_for_listing_alerts_grouped_by_policy()
        """
        _response = self._raw_client.submit_a_job_for_listing_alerts_grouped_by_policy(
            time_range=time_range,
            detailed=detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def get_async_policy_alert_job_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncJob:
        """
        Returns the status of a job submitted to list alerts by policy. Uses the specified job ID to identify the job.

        Parameters
        ----------
        id : str
            Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_async_policy_alert_job_status(
            id="id",
        )
        """
        _response = self._raw_client.get_async_policy_alert_job_status(id, request_options=request_options)
        return _response.data

    def download_policy_alerts_json(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the policy alerts results in JSON format for the specified job ID.

        Parameters
        ----------
        id : str
            Job ID

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
        client.alerts.download_policy_alerts_json(
            id="id",
        )
        """
        _response = self._raw_client.download_policy_alerts_json(id, request_options=request_options)
        return _response.data

    def get_alerts_remediation(
        self,
        *,
        filter: AlertsLookupKeyModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemediationCliModel:
        """
        Generates and returns a list of remediation commands for the specified alerts and policies. Data returned for a successful call include fully constructed commands for remediation.

        This request requires the following filter request body parameters:

        * filter.timeRange.type
        * filter.timeRange.value

        The rest of the filter parameters are ignored.

        Parameters
        ----------
        filter : AlertsLookupKeyModelFilter
            Filter to narrow or manage the search

        alerts : typing.Optional[typing.Sequence[str]]
            List of alert IDs. One or more alert IDs associated with a single policy are required if no policies are specified. If a policy is specified, then all the alerts specified must belong to that policy.

        policies : typing.Optional[typing.Sequence[str]]
            List of policy IDs. A single policy ID is required if no alerts are specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemediationCliModel
            successful operation

        Examples
        --------
        from fern.alerts import AlertsLookupKeyModelFilter

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.alerts.get_alerts_remediation(
            filter=AlertsLookupKeyModelFilter(),
        )
        """
        _response = self._raw_client.get_alerts_remediation(
            filter=filter, alerts=alerts, policies=policies, request_options=request_options
        )
        return _response.data

    def perform_remediation_for_alert(
        self,
        id: str,
        *,
        finding_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remediates the alert with the specified ID if that alert is associated with a remediable policy.

        Parameters
        ----------
        id : str
            Alert ID

        finding_id : typing.Optional[str]

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
        client.alerts.perform_remediation_for_alert(
            id="id",
        )
        """
        _response = self._raw_client.perform_remediation_for_alert(
            id, finding_id=finding_id, request_options=request_options
        )
        return _response.data


class AsyncAlertsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlertsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlertsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlertsClient
        """
        return self._raw_client

    async def get_alert_filter_and_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertFilterSuggestion:
        """
        Returns an object whose keys are the available policy filters. The corresponding values are default or recently set filter options

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertFilterSuggestion
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alert_filter_and_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert_filter_and_options(request_options=request_options)
        return _response.data

    async def get_alert_filter_options(
        self,
        *,
        filter_name: str,
        query: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ParsedTableFilter:
        """
        Returns available options for an alert filter key. Supports fuzzy autocomplete search. If you specify a **query** value in the request body parameters, the response includes only items that contain the **query** string.

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
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alert_filter_options(
                filter_name="filterName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert_filter_options(
            filter_name=filter_name, query=query, request_options=request_options
        )
        return _response.data

    async def get_alerts(
        self,
        *,
        time_type: GetAlertsRequestTimeType,
        time_amount: str,
        time_unit: GetAlertsRequestTimeUnit,
        detailed: bool,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsRequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsRequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsRequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsRequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns a list of alerts that match the constraints specified in the query parameters. Max 10k results. To get more, use **List Alerts V2 - GET**.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_type : GetAlertsRequestTimeType
            Time Type

        time_amount : str
            Number of **timeUnits**

        time_unit : GetAlertsRequestTimeUnit
            Time Unit

        detailed : bool
            true = Return detailed alert data.

        fields : typing.Optional[str]
            Comma-separated list of specific fields to retrieve. Allowed values: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity

        limit : typing.Optional[float]
            The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.

        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsRequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsRequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsRequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsRequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        import asyncio

        from fern.alerts import GetAlertsRequestTimeType, GetAlertsRequestTimeUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alerts(
                time_type=GetAlertsRequestTimeType.RELATIVE,
                time_amount="timeAmount",
                time_unit=GetAlertsRequestTimeUnit.MINUTE,
                detailed=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts(
            time_type=time_type,
            time_amount=time_amount,
            time_unit=time_unit,
            detailed=detailed,
            fields=fields,
            limit=limit,
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    async def post_alerts(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns a list of alerts that matches the constraints specified in the body parameters. Max 10k results. To get more, use **List Alerts V2 - POST**.

        The **fields** body parameter allows you to request specific fields from the alert payload. These fields
        are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters** body parameter enables you to narrow your request for alerts. See
        [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.post_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_alerts(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_alerts_v2(
        self,
        *,
        time_type: GetAlertsV2RequestTimeType,
        time_amount: str,
        time_unit: GetAlertsV2RequestTimeUnit,
        detailed: bool,
        fields: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        page_token: typing.Optional[str] = None,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsV2RequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsV2RequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsV2RequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsV2RequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultsAlertModel:
        """
        Returns a paginated list of alerts from the Prisma Cloud platform.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_type : GetAlertsV2RequestTimeType
            Time Type

        time_amount : str
            Number of **timeUnits**

        time_unit : GetAlertsV2RequestTimeUnit
            Time Unit

        detailed : bool
            true = Return detailed alert data.

        fields : typing.Optional[str]
            Array of specific fields to return. Allowed fields: alert.id, alert.status, alert.time, cloud.accountId, cloud.account, cloud.region, resource.id, resource.name, policy.name, policy.type, policy.severity

        sort_by : typing.Optional[str]
            Response object property by which to sort response list. The valid values are in the response object attribute **sortAllowedColumns**. The format is **property:asc** for ascending and **property:desc** for descending sort

        limit : typing.Optional[float]
            The maximum number of items that will be returned in one response. The maximum cannot exceed 10,000. The default is 10,000.

        page_token : typing.Optional[str]
            Token that identifies the required page of data. When there are multiple pages of data in the response, set **pageToken** to the **nextPageToken** value from the previous API response to retrieve the next page of data.

        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsV2RequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsV2RequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsV2RequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsV2RequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultsAlertModel
            successful operation

        Examples
        --------
        import asyncio

        from fern.alerts import GetAlertsV2RequestTimeType, GetAlertsV2RequestTimeUnit

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alerts_v2(
                time_type=GetAlertsV2RequestTimeType.RELATIVE,
                time_amount="timeAmount",
                time_unit=GetAlertsV2RequestTimeUnit.MINUTE,
                detailed=True,
                sort_by="sortBy=id:desc&sortBy=firstseen:asc,lastseen:desc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts_v2(
            time_type=time_type,
            time_amount=time_amount,
            time_unit=time_unit,
            detailed=detailed,
            fields=fields,
            sort_by=sort_by,
            limit=limit,
            page_token=page_token,
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    async def post_alerts_v2(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultsAlertModel:
        """
        Returns a paginated list of alerts that matches the constraints specified in the body parameters.

        The **fields** request body parameter allows you to request specific fields from the alert payload.
        These fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters** request body parameter enables you to narrow your request for alerts. See
        [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        You can find the valid values for the **sortBy** request body parameter in the response
        object attribute **sortAllowedColumns**.

        Data in the response object does not include alert rules.

        Also, in the response object:

        * Property **riskDetail** is deprecated.
        * Property **items[].resource.cloudServiceName** is populated only for alerts whose resources belong to a cloud service.

        When `detailed` flag is set to **true**, following fields will be returned within the policy response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultsAlertModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.post_alerts_v2()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_alerts_v2(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_alerts_grouped(
        self,
        *,
        alert_id: typing.Optional[str] = None,
        alert_status: typing.Optional[GetAlertsGroupedRequestAlertStatus] = None,
        cloud_account: typing.Optional[str] = None,
        cloud_account_id: typing.Optional[str] = None,
        account_group: typing.Optional[str] = None,
        cloud_type: typing.Optional[str] = None,
        cloud_region: typing.Optional[str] = None,
        cloud_service: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        policy_name: typing.Optional[str] = None,
        policy_severity: typing.Optional[GetAlertsGroupedRequestPolicySeverity] = None,
        policy_label: typing.Optional[str] = None,
        policy_type: typing.Optional[GetAlertsGroupedRequestPolicyType] = None,
        policy_compliance_standard: typing.Optional[str] = None,
        policy_compliance_requirement: typing.Optional[str] = None,
        policy_compliance_section: typing.Optional[str] = None,
        policy_remediable: typing.Optional[GetAlertsGroupedRequestPolicyRemediable] = None,
        alert_rule_name: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        resource_name: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns alert counts grouped by policy. You can use query parameters to narrow the response.

        In the response object:

        * Property **alertRules** is not populated.
        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is not populated.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        alert_id : typing.Optional[str]
            Alert ID

        alert_status : typing.Optional[GetAlertsGroupedRequestAlertStatus]
            Alert status

        cloud_account : typing.Optional[str]
            Cloud account

        cloud_account_id : typing.Optional[str]
            Cloud account Id

        account_group : typing.Optional[str]
            Account group

        cloud_type : typing.Optional[str]
            Cloud type

        cloud_region : typing.Optional[str]
            Cloud region

        cloud_service : typing.Optional[str]
            Cloud service

        policy_id : typing.Optional[str]
            Policy ID

        policy_name : typing.Optional[str]
            Policy name

        policy_severity : typing.Optional[GetAlertsGroupedRequestPolicySeverity]
            Policy severity

        policy_label : typing.Optional[str]
            Policy label

        policy_type : typing.Optional[GetAlertsGroupedRequestPolicyType]
            Policy type

        policy_compliance_standard : typing.Optional[str]
            Policy compliance standard name

        policy_compliance_requirement : typing.Optional[str]
            Policy compliance requirement name

        policy_compliance_section : typing.Optional[str]
            Policy compliance section ID

        policy_remediable : typing.Optional[GetAlertsGroupedRequestPolicyRemediable]
            Policy is remediable

        alert_rule_name : typing.Optional[str]
            Alert rule name

        resource_id : typing.Optional[str]
            Resource ID

        resource_name : typing.Optional[str]
            Resource name

        resource_type : typing.Optional[str]
            Resource TYPE

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alerts_grouped()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts_grouped(
            alert_id=alert_id,
            alert_status=alert_status,
            cloud_account=cloud_account,
            cloud_account_id=cloud_account_id,
            account_group=account_group,
            cloud_type=cloud_type,
            cloud_region=cloud_region,
            cloud_service=cloud_service,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_severity=policy_severity,
            policy_label=policy_label,
            policy_type=policy_type,
            policy_compliance_standard=policy_compliance_standard,
            policy_compliance_requirement=policy_compliance_requirement,
            policy_compliance_section=policy_compliance_section,
            policy_remediable=policy_remediable,
            alert_rule_name=alert_rule_name,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            request_options=request_options,
        )
        return _response.data

    async def post_alerts_grouped(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AlertModel]:
        """
        Returns alert counts grouped by policy. You can use body parameters to narrow the response.

        In the response object:

        * Property **alertRules** is not populated.
        * Property **riskDetail** is deprecated.
        * Property **resource.cloudServiceName** is not populated.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertModel]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.post_alerts_grouped()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_alerts_grouped(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_alert(
        self,
        id: str,
        *,
        detailed: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertModel:
        """
        Returns information about an alert for the specified ID.

        In the response object, field **riskDetail** is deprecated.

        When `detailed` flag is set to **true**, following fields will be returned within the policy and response object:

        - `complianceMetadata`
        - `name`
        - `description`
        - `labels`
        - `deleted`
        - `recommendation`
        - `lastModifiedBy`
        - `lastModifiedOn`
        - `severity`

        The `resource` response object will include `cloudAccountGroups` field when `detailed` is set to **true**

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 5/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        id : str
            Alert ID

        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alert(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert(id, detailed=detailed, request_options=request_options)
        return _response.data

    async def dismiss_alerts(
        self,
        *,
        filter: AlertStatusChangeRequestModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        dismissal_note: typing.Optional[str] = OMIT,
        dismissal_time_range: typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Dismisses one or more alerts on the Prisma Cloud platform. If the caller specifies a dismissal time range, then alerts will snooze for that time period rather than be dismissed.

        Parameters
        ----------
        filter : AlertStatusChangeRequestModelFilter
            Filter

        alerts : typing.Optional[typing.Sequence[str]]
            Alert IDs

        dismissal_note : typing.Optional[str]
            Reason for dismissal (this only applies to the dismiss alerts endpoint)

        dismissal_time_range : typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange]
            Dismissal Time Range

        policies : typing.Optional[typing.Sequence[str]]
            Policy IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AlertStatusChangeRequestModelFilter, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.dismiss_alerts(
                filter=AlertStatusChangeRequestModelFilter(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dismiss_alerts(
            filter=filter,
            alerts=alerts,
            dismissal_note=dismissal_note,
            dismissal_time_range=dismissal_time_range,
            policies=policies,
            request_options=request_options,
        )
        return _response.data

    async def is_dismissal_note_required(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RequireDismissalNoteConfigModel:
        """
        Indicates whether or not the user is required to specify a reason (dismissal note) when dismissing an alert.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequireDismissalNoteConfigModel
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.is_dismissal_note_required()


        asyncio.run(main())
        """
        _response = await self._raw_client.is_dismissal_note_required(request_options=request_options)
        return _response.data

    async def set_dismissal_note_required(
        self,
        *,
        require_dismissal_note: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Manages whether or not a user must provide a reason (dismissal note) when dismissing an alert on the Prisma Cloud platform.

        Parameters
        ----------
        require_dismissal_note : typing.Optional[bool]
            Require Dismissal Note

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
            await client.alerts.set_dismissal_note_required()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_dismissal_note_required(
            require_dismissal_note=require_dismissal_note, request_options=request_options
        )
        return _response.data

    async def reopen_alerts(
        self,
        *,
        filter: AlertStatusChangeRequestModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        dismissal_note: typing.Optional[str] = OMIT,
        dismissal_time_range: typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sets the status of one or more dismissed or snoozed alerts on the Prisma Cloud platform to **open**.

        Parameters
        ----------
        filter : AlertStatusChangeRequestModelFilter
            Filter

        alerts : typing.Optional[typing.Sequence[str]]
            Alert IDs

        dismissal_note : typing.Optional[str]
            Reason for dismissal (this only applies to the dismiss alerts endpoint)

        dismissal_time_range : typing.Optional[AlertStatusChangeRequestModelDismissalTimeRange]
            Dismissal Time Range

        policies : typing.Optional[typing.Sequence[str]]
            Policy IDs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AlertStatusChangeRequestModelFilter, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.reopen_alerts(
                filter=AlertStatusChangeRequestModelFilter(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reopen_alerts(
            filter=filter,
            alerts=alerts,
            dismissal_note=dismissal_note,
            dismissal_time_range=dismissal_time_range,
            policies=policies,
            request_options=request_options,
        )
        return _response.data

    async def get_alert_count(
        self, status: GetAlertCountRequestStatus, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CountModel:
        """
        Returns an alert count for the specified status.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        status : GetAlertCountRequestStatus
            Alert Status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CountModel
            successful operation

        Examples
        --------
        import asyncio

        from fern.alerts import GetAlertCountRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alert_count(
                status=GetAlertCountRequestStatus.OPEN,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert_count(status, request_options=request_options)
        return _response.data

    async def submit_job_for_listing_alerts(
        self,
        *,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable in JSON format. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** body parameter allows you to request specific fields from the alert payload. These
        fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

         The **filters** body parameter enables you to narrow your request for alerts. See
         [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
         for an API request to list all the valid filters.

          #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 2/sec
        * Burst limit: 10/sec

        Parameters
        ----------
        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.submit_job_for_listing_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_job_for_listing_alerts(
            time_range=time_range,
            detailed=detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_alerts_job_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncJob:
        """
        Get the status of the alerts list job with the specified job ID

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alerts_job_status(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts_job_status(id, request_options=request_options)
        return _response.data

    async def download_alerts_list_json(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Downloads the generated alerts list in JSON format for the specified job ID.

        Parameters
        ----------
        id : str
            Job ID

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
            await client.alerts.download_alerts_list_json(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_alerts_list_json(id, request_options=request_options)
        return _response.data

    async def submit_an_alert_csv_download_job(
        self,
        *,
        detailed: typing.Optional[bool] = None,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        filter_model_detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate an alerts list that matches the constraints in the body parameters and is downloadable as a CSV file. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** request body parameter is ignored!

        The **filters** body parameter enables you to narrow your request for alerts. See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        Parameters
        ----------
        detailed : typing.Optional[bool]
            true = Return detailed alert data. Default is false. Overrides **detailed** in body param.

        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        filter_model_detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.submit_an_alert_csv_download_job()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_an_alert_csv_download_job(
            detailed=detailed,
            time_range=time_range,
            filter_model_detailed=filter_model_detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_alert_csv_job_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncJob:
        """
        Returns the status of an alert CSV generation job with the specified job ID.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alert_csv_job_status(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alert_csv_job_status(id, request_options=request_options)
        return _response.data

    async def download_alert_csv(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Downloads the alert list that Prisma Cloud generated for the specified job ID, in CSV format.

        Parameters
        ----------
        id : str
            Job ID

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
            await client.alerts.download_alert_csv(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_alert_csv(id, request_options=request_options)
        return _response.data

    async def submit_a_job_for_listing_alerts_grouped_by_policy(
        self,
        *,
        time_range: typing.Optional[FilterModelTimeRange] = OMIT,
        detailed: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        filters: typing.Optional[typing.Sequence[UiFilterModel]] = OMIT,
        group_by: typing.Optional[typing.Sequence[str]] = OMIT,
        limit: typing.Optional[float] = OMIT,
        offset: typing.Optional[float] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        sort_by: typing.Optional[typing.Sequence[str]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncJob:
        """
        Submits a job to generate a list of alerts grouped by the policy they violated. Returns the job ID and job submission status.

        Filter model fields specific to pagination (**sortBy**, **limit**, and **pageToken**) do not apply to this request,
        even though the body parameters include them.

        The **fields** body parameter allows you to request specific fields from the alert payload. These
        fields are separate from the filters you specify. The following are valid **fields** items.

        * alert.id
        * alert.status
        * alert.time
        * cloud.account
        * cloud.accountId
        * cloud.region
        * resource.id
        * resource.name
        * policy.name
        * policy.type
        * policy.severity

        The **filters*8 body parameter enables you to narrow your request for alerts.
        See [List Alert Filters](/prisma-cloud/api/cspm/get-alert-filter-and-options)
        for an API request to list all the valid filters.

        #### Rate Limits ####

        The following rate limits apply:
        * Request rate limit: 1/sec
        * Burst limit: 5/sec

        Parameters
        ----------
        time_range : typing.Optional[FilterModelTimeRange]
            Time range

        detailed : typing.Optional[bool]
            Detailed

        fields : typing.Optional[typing.Sequence[str]]
            Array of specific fields to return

        filters : typing.Optional[typing.Sequence[UiFilterModel]]
            Filtering parameters.

            For filter names, refer to List Filters API.

            For filter values, refer to List filter suggestions.

            The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"

        group_by : typing.Optional[typing.Sequence[str]]
            For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**

        limit : typing.Optional[float]
            Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.

        offset : typing.Optional[float]
            The number of items to skip before selecting items to return. Default is zero

        page_token : typing.Optional[str]
            Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data

        sort_by : typing.Optional[typing.Sequence[str]]
            Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.submit_a_job_for_listing_alerts_grouped_by_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_job_for_listing_alerts_grouped_by_policy(
            time_range=time_range,
            detailed=detailed,
            fields=fields,
            filters=filters,
            group_by=group_by,
            limit=limit,
            offset=offset,
            page_token=page_token,
            sort_by=sort_by,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def get_async_policy_alert_job_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncJob:
        """
        Returns the status of a job submitted to list alerts by policy. Uses the specified job ID to identify the job.

        Parameters
        ----------
        id : str
            Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncJob
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_async_policy_alert_job_status(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_async_policy_alert_job_status(id, request_options=request_options)
        return _response.data

    async def download_policy_alerts_json(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Downloads the policy alerts results in JSON format for the specified job ID.

        Parameters
        ----------
        id : str
            Job ID

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
            await client.alerts.download_policy_alerts_json(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_policy_alerts_json(id, request_options=request_options)
        return _response.data

    async def get_alerts_remediation(
        self,
        *,
        filter: AlertsLookupKeyModelFilter,
        alerts: typing.Optional[typing.Sequence[str]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemediationCliModel:
        """
        Generates and returns a list of remediation commands for the specified alerts and policies. Data returned for a successful call include fully constructed commands for remediation.

        This request requires the following filter request body parameters:

        * filter.timeRange.type
        * filter.timeRange.value

        The rest of the filter parameters are ignored.

        Parameters
        ----------
        filter : AlertsLookupKeyModelFilter
            Filter to narrow or manage the search

        alerts : typing.Optional[typing.Sequence[str]]
            List of alert IDs. One or more alert IDs associated with a single policy are required if no policies are specified. If a policy is specified, then all the alerts specified must belong to that policy.

        policies : typing.Optional[typing.Sequence[str]]
            List of policy IDs. A single policy ID is required if no alerts are specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemediationCliModel
            successful operation

        Examples
        --------
        import asyncio

        from fern.alerts import AlertsLookupKeyModelFilter

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.alerts.get_alerts_remediation(
                filter=AlertsLookupKeyModelFilter(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts_remediation(
            filter=filter, alerts=alerts, policies=policies, request_options=request_options
        )
        return _response.data

    async def perform_remediation_for_alert(
        self,
        id: str,
        *,
        finding_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Remediates the alert with the specified ID if that alert is associated with a remediable policy.

        Parameters
        ----------
        id : str
            Alert ID

        finding_id : typing.Optional[str]

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
            await client.alerts.perform_remediation_for_alert(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_remediation_for_alert(
            id, finding_id=finding_id, request_options=request_options
        )
        return _response.data
