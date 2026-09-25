



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .oauth_scope import OauthScope
    from .v1bulk_hours_import import V1BulkHoursImport
    from .v1bulk_hours_import_create_item import V1BulkHoursImportCreateItem
    from .v1bulk_hours_import_create_item_external_links_item import V1BulkHoursImportCreateItemExternalLinksItem
    from .v1bulk_hours_import_create_item_timestamps_item import V1BulkHoursImportCreateItemTimestampsItem
    from .v1bulk_hours_import_update_item import V1BulkHoursImportUpdateItem
    from .v1bulk_import_response import V1BulkImportResponse
    from .v1bulk_import_response_errors import V1BulkImportResponseErrors
    from .v1company import V1Company
    from .v1company_external_references_item import V1CompanyExternalReferencesItem
    from .v1company_tic import V1CompanyTic
    from .v1day_property import V1DayProperty
    from .v1error import V1Error
    from .v1forbidden_error import V1ForbiddenError
    from .v1forbidden_error_errors import V1ForbiddenErrorErrors
    from .v1forecast import V1Forecast
    from .v1forecast_estimated_duration import V1ForecastEstimatedDuration
    from .v1forecast_logged_duration import V1ForecastLoggedDuration
    from .v1forecast_planned_duration import V1ForecastPlannedDuration
    from .v1forecast_project import V1ForecastProject
    from .v1forecast_project_client import V1ForecastProjectClient
    from .v1forecast_summary import V1ForecastSummary
    from .v1forecast_summary_estimated_total import V1ForecastSummaryEstimatedTotal
    from .v1forecast_summary_logged_total import V1ForecastSummaryLoggedTotal
    from .v1forecast_summary_planned_total import V1ForecastSummaryPlannedTotal
    from .v1forecast_user import V1ForecastUser
    from .v1forecast_user_avatar import V1ForecastUserAvatar
    from .v1forecast_user_estimated_duration import V1ForecastUserEstimatedDuration
    from .v1forecast_users_item import V1ForecastUsersItem
    from .v1forecast_users_item_avatar import V1ForecastUsersItemAvatar
    from .v1forecast_users_item_estimated_duration import V1ForecastUsersItemEstimatedDuration
    from .v1hour import V1Hour
    from .v1hour_cost import V1HourCost
    from .v1hour_duration import V1HourDuration
    from .v1hour_estimated_cost import V1HourEstimatedCost
    from .v1hour_estimated_duration import V1HourEstimatedDuration
    from .v1hour_estimated_internal_cost import V1HourEstimatedInternalCost
    from .v1hour_estimated_internal_cost_amount import V1HourEstimatedInternalCostAmount
    from .v1hour_estimated_internal_cost_one import V1HourEstimatedInternalCostOne
    from .v1hour_external_links_item import V1HourExternalLinksItem
    from .v1hour_internal_cost import V1HourInternalCost
    from .v1hour_internal_cost_amount import V1HourInternalCostAmount
    from .v1hour_internal_cost_one import V1HourInternalCostOne
    from .v1hour_project import V1HourProject
    from .v1hour_project_billed_cost import V1HourProjectBilledCost
    from .v1hour_project_billed_duration import V1HourProjectBilledDuration
    from .v1hour_project_client import V1HourProjectClient
    from .v1hour_project_cost import V1HourProjectCost
    from .v1hour_project_currency import V1HourProjectCurrency
    from .v1hour_project_duration import V1HourProjectDuration
    from .v1hour_project_estimated_cost import V1HourProjectEstimatedCost
    from .v1hour_project_estimated_duration import V1HourProjectEstimatedDuration
    from .v1hour_project_labels_item import V1HourProjectLabelsItem
    from .v1hour_project_labels_item_tic import V1HourProjectLabelsItemTic
    from .v1hour_project_unbilled_cost import V1HourProjectUnbilledCost
    from .v1hour_project_unbilled_duration import V1HourProjectUnbilledDuration
    from .v1hour_state import V1HourState
    from .v1hour_state_permissions_item import V1HourStatePermissionsItem
    from .v1hour_timestamps_item import V1HourTimestampsItem
    from .v1hour_user import V1HourUser
    from .v1hour_user_avatar import V1HourUserAvatar
    from .v1label import V1Label
    from .v1label_tic import V1LabelTic
    from .v1not_found_error import V1NotFoundError
    from .v1not_found_error_errors import V1NotFoundErrorErrors
    from .v1o_auth_authorized_application import V1OAuthAuthorizedApplication
    from .v1o_auth_introspect_response import V1OAuthIntrospectResponse
    from .v1o_auth_token_response import V1OAuthTokenResponse
    from .v1permission import V1Permission
    from .v1project import V1Project
    from .v1project_billable_duration import V1ProjectBillableDuration
    from .v1project_billed_cost import V1ProjectBilledCost
    from .v1project_billed_cost_amount import V1ProjectBilledCostAmount
    from .v1project_billed_cost_one import V1ProjectBilledCostOne
    from .v1project_billed_duration import V1ProjectBilledDuration
    from .v1project_budget_calculation import V1ProjectBudgetCalculation
    from .v1project_budget_scope import V1ProjectBudgetScope
    from .v1project_budget_type import V1ProjectBudgetType
    from .v1project_client import V1ProjectClient
    from .v1project_client_external_references_item import V1ProjectClientExternalReferencesItem
    from .v1project_client_tic import V1ProjectClientTic
    from .v1project_cost import V1ProjectCost
    from .v1project_cost_amount import V1ProjectCostAmount
    from .v1project_cost_one import V1ProjectCostOne
    from .v1project_currency import V1ProjectCurrency
    from .v1project_duration import V1ProjectDuration
    from .v1project_enable_labels import V1ProjectEnableLabels
    from .v1project_estimated_cost import V1ProjectEstimatedCost
    from .v1project_estimated_cost_amount import V1ProjectEstimatedCostAmount
    from .v1project_estimated_cost_one import V1ProjectEstimatedCostOne
    from .v1project_estimated_duration import V1ProjectEstimatedDuration
    from .v1project_internal_cost import V1ProjectInternalCost
    from .v1project_internal_cost_amount import V1ProjectInternalCostAmount
    from .v1project_internal_cost_one import V1ProjectInternalCostOne
    from .v1project_labels_item import V1ProjectLabelsItem
    from .v1project_non_billable_duration import V1ProjectNonBillableDuration
    from .v1project_profit import V1ProjectProfit
    from .v1project_profit_amount import V1ProjectProfitAmount
    from .v1project_profit_one import V1ProjectProfitOne
    from .v1project_rate_type import V1ProjectRateType
    from .v1project_tic import V1ProjectTic
    from .v1project_unbilled_cost import V1ProjectUnbilledCost
    from .v1project_unbilled_cost_amount import V1ProjectUnbilledCostAmount
    from .v1project_unbilled_cost_one import V1ProjectUnbilledCostOne
    from .v1project_unbilled_duration import V1ProjectUnbilledDuration
    from .v1project_users_item import V1ProjectUsersItem
    from .v1report_totals import V1ReportTotals
    from .v1report_totals_billable_duration import V1ReportTotalsBillableDuration
    from .v1report_totals_billed_cost import V1ReportTotalsBilledCost
    from .v1report_totals_billed_duration import V1ReportTotalsBilledDuration
    from .v1report_totals_cost import V1ReportTotalsCost
    from .v1report_totals_duration import V1ReportTotalsDuration
    from .v1report_totals_estimated_cost import V1ReportTotalsEstimatedCost
    from .v1report_totals_estimated_duration import V1ReportTotalsEstimatedDuration
    from .v1report_totals_internal_cost import V1ReportTotalsInternalCost
    from .v1report_totals_non_billable_duration import V1ReportTotalsNonBillableDuration
    from .v1report_totals_profit import V1ReportTotalsProfit
    from .v1report_totals_unbilled_cost import V1ReportTotalsUnbilledCost
    from .v1report_totals_unbilled_duration import V1ReportTotalsUnbilledDuration
    from .v1role import V1Role
    from .v1role_scopes_item import V1RoleScopesItem
    from .v1state import V1State
    from .v1state_permission import V1StatePermission
    from .v1state_permissions_item import V1StatePermissionsItem
    from .v1states_create import V1StatesCreate
    from .v1states_create_state import V1StatesCreateState
    from .v1states_update import V1StatesUpdate
    from .v1states_update_state import V1StatesUpdateState
    from .v1team import V1Team
    from .v1unauthorized_error import V1UnauthorizedError
    from .v1unprocessable_entity_error import V1UnprocessableEntityError
    from .v1unprocessable_entity_error_errors_value import V1UnprocessableEntityErrorErrorsValue
    from .v1user import V1User
    from .v1user_avatar import V1UserAvatar
    from .v1user_capacity import V1UserCapacity
    from .v1user_role import V1UserRole
    from .v1users_create import V1UsersCreate
    from .v1users_create_user import V1UsersCreateUser
    from .v1users_create_user_capacity import V1UsersCreateUserCapacity
    from .v1users_create_user_projects import V1UsersCreateUserProjects
    from .v1users_create_user_projects_create import V1UsersCreateUserProjectsCreate
    from .v1users_create_user_projects_create_create_item import V1UsersCreateUserProjectsCreateCreateItem
    from .v1users_create_user_projects_one_item import V1UsersCreateUserProjectsOneItem
    from .v1users_create_user_properties_attributes_item import V1UsersCreateUserPropertiesAttributesItem
    from .v1users_create_user_properties_attributes_item_account_user_property_id import (
        V1UsersCreateUserPropertiesAttributesItemAccountUserPropertyId,
    )
    from .v1users_create_user_properties_attributes_item_destroy import V1UsersCreateUserPropertiesAttributesItemDestroy
    from .v1users_create_user_properties_attributes_item_zero import V1UsersCreateUserPropertiesAttributesItemZero
    from .v1users_create_user_user_level import V1UsersCreateUserUserLevel
    from .v1validation_error import V1ValidationError
    from .v1webhook import V1Webhook
    from .v1webhook_subscriptions_item import V1WebhookSubscriptionsItem
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "OauthScope": ".oauth_scope",
    "V1BulkHoursImport": ".v1bulk_hours_import",
    "V1BulkHoursImportCreateItem": ".v1bulk_hours_import_create_item",
    "V1BulkHoursImportCreateItemExternalLinksItem": ".v1bulk_hours_import_create_item_external_links_item",
    "V1BulkHoursImportCreateItemTimestampsItem": ".v1bulk_hours_import_create_item_timestamps_item",
    "V1BulkHoursImportUpdateItem": ".v1bulk_hours_import_update_item",
    "V1BulkImportResponse": ".v1bulk_import_response",
    "V1BulkImportResponseErrors": ".v1bulk_import_response_errors",
    "V1Company": ".v1company",
    "V1CompanyExternalReferencesItem": ".v1company_external_references_item",
    "V1CompanyTic": ".v1company_tic",
    "V1DayProperty": ".v1day_property",
    "V1Error": ".v1error",
    "V1ForbiddenError": ".v1forbidden_error",
    "V1ForbiddenErrorErrors": ".v1forbidden_error_errors",
    "V1Forecast": ".v1forecast",
    "V1ForecastEstimatedDuration": ".v1forecast_estimated_duration",
    "V1ForecastLoggedDuration": ".v1forecast_logged_duration",
    "V1ForecastPlannedDuration": ".v1forecast_planned_duration",
    "V1ForecastProject": ".v1forecast_project",
    "V1ForecastProjectClient": ".v1forecast_project_client",
    "V1ForecastSummary": ".v1forecast_summary",
    "V1ForecastSummaryEstimatedTotal": ".v1forecast_summary_estimated_total",
    "V1ForecastSummaryLoggedTotal": ".v1forecast_summary_logged_total",
    "V1ForecastSummaryPlannedTotal": ".v1forecast_summary_planned_total",
    "V1ForecastUser": ".v1forecast_user",
    "V1ForecastUserAvatar": ".v1forecast_user_avatar",
    "V1ForecastUserEstimatedDuration": ".v1forecast_user_estimated_duration",
    "V1ForecastUsersItem": ".v1forecast_users_item",
    "V1ForecastUsersItemAvatar": ".v1forecast_users_item_avatar",
    "V1ForecastUsersItemEstimatedDuration": ".v1forecast_users_item_estimated_duration",
    "V1Hour": ".v1hour",
    "V1HourCost": ".v1hour_cost",
    "V1HourDuration": ".v1hour_duration",
    "V1HourEstimatedCost": ".v1hour_estimated_cost",
    "V1HourEstimatedDuration": ".v1hour_estimated_duration",
    "V1HourEstimatedInternalCost": ".v1hour_estimated_internal_cost",
    "V1HourEstimatedInternalCostAmount": ".v1hour_estimated_internal_cost_amount",
    "V1HourEstimatedInternalCostOne": ".v1hour_estimated_internal_cost_one",
    "V1HourExternalLinksItem": ".v1hour_external_links_item",
    "V1HourInternalCost": ".v1hour_internal_cost",
    "V1HourInternalCostAmount": ".v1hour_internal_cost_amount",
    "V1HourInternalCostOne": ".v1hour_internal_cost_one",
    "V1HourProject": ".v1hour_project",
    "V1HourProjectBilledCost": ".v1hour_project_billed_cost",
    "V1HourProjectBilledDuration": ".v1hour_project_billed_duration",
    "V1HourProjectClient": ".v1hour_project_client",
    "V1HourProjectCost": ".v1hour_project_cost",
    "V1HourProjectCurrency": ".v1hour_project_currency",
    "V1HourProjectDuration": ".v1hour_project_duration",
    "V1HourProjectEstimatedCost": ".v1hour_project_estimated_cost",
    "V1HourProjectEstimatedDuration": ".v1hour_project_estimated_duration",
    "V1HourProjectLabelsItem": ".v1hour_project_labels_item",
    "V1HourProjectLabelsItemTic": ".v1hour_project_labels_item_tic",
    "V1HourProjectUnbilledCost": ".v1hour_project_unbilled_cost",
    "V1HourProjectUnbilledDuration": ".v1hour_project_unbilled_duration",
    "V1HourState": ".v1hour_state",
    "V1HourStatePermissionsItem": ".v1hour_state_permissions_item",
    "V1HourTimestampsItem": ".v1hour_timestamps_item",
    "V1HourUser": ".v1hour_user",
    "V1HourUserAvatar": ".v1hour_user_avatar",
    "V1Label": ".v1label",
    "V1LabelTic": ".v1label_tic",
    "V1NotFoundError": ".v1not_found_error",
    "V1NotFoundErrorErrors": ".v1not_found_error_errors",
    "V1OAuthAuthorizedApplication": ".v1o_auth_authorized_application",
    "V1OAuthIntrospectResponse": ".v1o_auth_introspect_response",
    "V1OAuthTokenResponse": ".v1o_auth_token_response",
    "V1Permission": ".v1permission",
    "V1Project": ".v1project",
    "V1ProjectBillableDuration": ".v1project_billable_duration",
    "V1ProjectBilledCost": ".v1project_billed_cost",
    "V1ProjectBilledCostAmount": ".v1project_billed_cost_amount",
    "V1ProjectBilledCostOne": ".v1project_billed_cost_one",
    "V1ProjectBilledDuration": ".v1project_billed_duration",
    "V1ProjectBudgetCalculation": ".v1project_budget_calculation",
    "V1ProjectBudgetScope": ".v1project_budget_scope",
    "V1ProjectBudgetType": ".v1project_budget_type",
    "V1ProjectClient": ".v1project_client",
    "V1ProjectClientExternalReferencesItem": ".v1project_client_external_references_item",
    "V1ProjectClientTic": ".v1project_client_tic",
    "V1ProjectCost": ".v1project_cost",
    "V1ProjectCostAmount": ".v1project_cost_amount",
    "V1ProjectCostOne": ".v1project_cost_one",
    "V1ProjectCurrency": ".v1project_currency",
    "V1ProjectDuration": ".v1project_duration",
    "V1ProjectEnableLabels": ".v1project_enable_labels",
    "V1ProjectEstimatedCost": ".v1project_estimated_cost",
    "V1ProjectEstimatedCostAmount": ".v1project_estimated_cost_amount",
    "V1ProjectEstimatedCostOne": ".v1project_estimated_cost_one",
    "V1ProjectEstimatedDuration": ".v1project_estimated_duration",
    "V1ProjectInternalCost": ".v1project_internal_cost",
    "V1ProjectInternalCostAmount": ".v1project_internal_cost_amount",
    "V1ProjectInternalCostOne": ".v1project_internal_cost_one",
    "V1ProjectLabelsItem": ".v1project_labels_item",
    "V1ProjectNonBillableDuration": ".v1project_non_billable_duration",
    "V1ProjectProfit": ".v1project_profit",
    "V1ProjectProfitAmount": ".v1project_profit_amount",
    "V1ProjectProfitOne": ".v1project_profit_one",
    "V1ProjectRateType": ".v1project_rate_type",
    "V1ProjectTic": ".v1project_tic",
    "V1ProjectUnbilledCost": ".v1project_unbilled_cost",
    "V1ProjectUnbilledCostAmount": ".v1project_unbilled_cost_amount",
    "V1ProjectUnbilledCostOne": ".v1project_unbilled_cost_one",
    "V1ProjectUnbilledDuration": ".v1project_unbilled_duration",
    "V1ProjectUsersItem": ".v1project_users_item",
    "V1ReportTotals": ".v1report_totals",
    "V1ReportTotalsBillableDuration": ".v1report_totals_billable_duration",
    "V1ReportTotalsBilledCost": ".v1report_totals_billed_cost",
    "V1ReportTotalsBilledDuration": ".v1report_totals_billed_duration",
    "V1ReportTotalsCost": ".v1report_totals_cost",
    "V1ReportTotalsDuration": ".v1report_totals_duration",
    "V1ReportTotalsEstimatedCost": ".v1report_totals_estimated_cost",
    "V1ReportTotalsEstimatedDuration": ".v1report_totals_estimated_duration",
    "V1ReportTotalsInternalCost": ".v1report_totals_internal_cost",
    "V1ReportTotalsNonBillableDuration": ".v1report_totals_non_billable_duration",
    "V1ReportTotalsProfit": ".v1report_totals_profit",
    "V1ReportTotalsUnbilledCost": ".v1report_totals_unbilled_cost",
    "V1ReportTotalsUnbilledDuration": ".v1report_totals_unbilled_duration",
    "V1Role": ".v1role",
    "V1RoleScopesItem": ".v1role_scopes_item",
    "V1State": ".v1state",
    "V1StatePermission": ".v1state_permission",
    "V1StatePermissionsItem": ".v1state_permissions_item",
    "V1StatesCreate": ".v1states_create",
    "V1StatesCreateState": ".v1states_create_state",
    "V1StatesUpdate": ".v1states_update",
    "V1StatesUpdateState": ".v1states_update_state",
    "V1Team": ".v1team",
    "V1UnauthorizedError": ".v1unauthorized_error",
    "V1UnprocessableEntityError": ".v1unprocessable_entity_error",
    "V1UnprocessableEntityErrorErrorsValue": ".v1unprocessable_entity_error_errors_value",
    "V1User": ".v1user",
    "V1UserAvatar": ".v1user_avatar",
    "V1UserCapacity": ".v1user_capacity",
    "V1UserRole": ".v1user_role",
    "V1UsersCreate": ".v1users_create",
    "V1UsersCreateUser": ".v1users_create_user",
    "V1UsersCreateUserCapacity": ".v1users_create_user_capacity",
    "V1UsersCreateUserProjects": ".v1users_create_user_projects",
    "V1UsersCreateUserProjectsCreate": ".v1users_create_user_projects_create",
    "V1UsersCreateUserProjectsCreateCreateItem": ".v1users_create_user_projects_create_create_item",
    "V1UsersCreateUserProjectsOneItem": ".v1users_create_user_projects_one_item",
    "V1UsersCreateUserPropertiesAttributesItem": ".v1users_create_user_properties_attributes_item",
    "V1UsersCreateUserPropertiesAttributesItemAccountUserPropertyId": ".v1users_create_user_properties_attributes_item_account_user_property_id",
    "V1UsersCreateUserPropertiesAttributesItemDestroy": ".v1users_create_user_properties_attributes_item_destroy",
    "V1UsersCreateUserPropertiesAttributesItemZero": ".v1users_create_user_properties_attributes_item_zero",
    "V1UsersCreateUserUserLevel": ".v1users_create_user_user_level",
    "V1ValidationError": ".v1validation_error",
    "V1Webhook": ".v1webhook",
    "V1WebhookSubscriptionsItem": ".v1webhook_subscriptions_item",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "BadRequestErrorBody",
    "OauthScope",
    "V1BulkHoursImport",
    "V1BulkHoursImportCreateItem",
    "V1BulkHoursImportCreateItemExternalLinksItem",
    "V1BulkHoursImportCreateItemTimestampsItem",
    "V1BulkHoursImportUpdateItem",
    "V1BulkImportResponse",
    "V1BulkImportResponseErrors",
    "V1Company",
    "V1CompanyExternalReferencesItem",
    "V1CompanyTic",
    "V1DayProperty",
    "V1Error",
    "V1ForbiddenError",
    "V1ForbiddenErrorErrors",
    "V1Forecast",
    "V1ForecastEstimatedDuration",
    "V1ForecastLoggedDuration",
    "V1ForecastPlannedDuration",
    "V1ForecastProject",
    "V1ForecastProjectClient",
    "V1ForecastSummary",
    "V1ForecastSummaryEstimatedTotal",
    "V1ForecastSummaryLoggedTotal",
    "V1ForecastSummaryPlannedTotal",
    "V1ForecastUser",
    "V1ForecastUserAvatar",
    "V1ForecastUserEstimatedDuration",
    "V1ForecastUsersItem",
    "V1ForecastUsersItemAvatar",
    "V1ForecastUsersItemEstimatedDuration",
    "V1Hour",
    "V1HourCost",
    "V1HourDuration",
    "V1HourEstimatedCost",
    "V1HourEstimatedDuration",
    "V1HourEstimatedInternalCost",
    "V1HourEstimatedInternalCostAmount",
    "V1HourEstimatedInternalCostOne",
    "V1HourExternalLinksItem",
    "V1HourInternalCost",
    "V1HourInternalCostAmount",
    "V1HourInternalCostOne",
    "V1HourProject",
    "V1HourProjectBilledCost",
    "V1HourProjectBilledDuration",
    "V1HourProjectClient",
    "V1HourProjectCost",
    "V1HourProjectCurrency",
    "V1HourProjectDuration",
    "V1HourProjectEstimatedCost",
    "V1HourProjectEstimatedDuration",
    "V1HourProjectLabelsItem",
    "V1HourProjectLabelsItemTic",
    "V1HourProjectUnbilledCost",
    "V1HourProjectUnbilledDuration",
    "V1HourState",
    "V1HourStatePermissionsItem",
    "V1HourTimestampsItem",
    "V1HourUser",
    "V1HourUserAvatar",
    "V1Label",
    "V1LabelTic",
    "V1NotFoundError",
    "V1NotFoundErrorErrors",
    "V1OAuthAuthorizedApplication",
    "V1OAuthIntrospectResponse",
    "V1OAuthTokenResponse",
    "V1Permission",
    "V1Project",
    "V1ProjectBillableDuration",
    "V1ProjectBilledCost",
    "V1ProjectBilledCostAmount",
    "V1ProjectBilledCostOne",
    "V1ProjectBilledDuration",
    "V1ProjectBudgetCalculation",
    "V1ProjectBudgetScope",
    "V1ProjectBudgetType",
    "V1ProjectClient",
    "V1ProjectClientExternalReferencesItem",
    "V1ProjectClientTic",
    "V1ProjectCost",
    "V1ProjectCostAmount",
    "V1ProjectCostOne",
    "V1ProjectCurrency",
    "V1ProjectDuration",
    "V1ProjectEnableLabels",
    "V1ProjectEstimatedCost",
    "V1ProjectEstimatedCostAmount",
    "V1ProjectEstimatedCostOne",
    "V1ProjectEstimatedDuration",
    "V1ProjectInternalCost",
    "V1ProjectInternalCostAmount",
    "V1ProjectInternalCostOne",
    "V1ProjectLabelsItem",
    "V1ProjectNonBillableDuration",
    "V1ProjectProfit",
    "V1ProjectProfitAmount",
    "V1ProjectProfitOne",
    "V1ProjectRateType",
    "V1ProjectTic",
    "V1ProjectUnbilledCost",
    "V1ProjectUnbilledCostAmount",
    "V1ProjectUnbilledCostOne",
    "V1ProjectUnbilledDuration",
    "V1ProjectUsersItem",
    "V1ReportTotals",
    "V1ReportTotalsBillableDuration",
    "V1ReportTotalsBilledCost",
    "V1ReportTotalsBilledDuration",
    "V1ReportTotalsCost",
    "V1ReportTotalsDuration",
    "V1ReportTotalsEstimatedCost",
    "V1ReportTotalsEstimatedDuration",
    "V1ReportTotalsInternalCost",
    "V1ReportTotalsNonBillableDuration",
    "V1ReportTotalsProfit",
    "V1ReportTotalsUnbilledCost",
    "V1ReportTotalsUnbilledDuration",
    "V1Role",
    "V1RoleScopesItem",
    "V1State",
    "V1StatePermission",
    "V1StatePermissionsItem",
    "V1StatesCreate",
    "V1StatesCreateState",
    "V1StatesUpdate",
    "V1StatesUpdateState",
    "V1Team",
    "V1UnauthorizedError",
    "V1UnprocessableEntityError",
    "V1UnprocessableEntityErrorErrorsValue",
    "V1User",
    "V1UserAvatar",
    "V1UserCapacity",
    "V1UserRole",
    "V1UsersCreate",
    "V1UsersCreateUser",
    "V1UsersCreateUserCapacity",
    "V1UsersCreateUserProjects",
    "V1UsersCreateUserProjectsCreate",
    "V1UsersCreateUserProjectsCreateCreateItem",
    "V1UsersCreateUserProjectsOneItem",
    "V1UsersCreateUserPropertiesAttributesItem",
    "V1UsersCreateUserPropertiesAttributesItemAccountUserPropertyId",
    "V1UsersCreateUserPropertiesAttributesItemDestroy",
    "V1UsersCreateUserPropertiesAttributesItemZero",
    "V1UsersCreateUserUserLevel",
    "V1ValidationError",
    "V1Webhook",
    "V1WebhookSubscriptionsItem",
]
