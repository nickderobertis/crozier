



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account import Account
    from .account_members_response import AccountMembersResponse
    from .account_members_response_object import AccountMembersResponseObject
    from .account_object import AccountObject
    from .address import Address
    from .api_key import ApiKey
    from .api_key_object import ApiKeyObject
    from .api_key_scope import ApiKeyScope
    from .attachment import Attachment
    from .bounce import Bounce
    from .bounce_statistics import BounceStatistics
    from .bounce_statistics_response import BounceStatisticsResponse
    from .bounce_statistics_response_object import BounceStatisticsResponseObject
    from .create_api_key_request import CreateApiKeyRequest
    from .create_message_response import CreateMessageResponse
    from .create_message_response_object import CreateMessageResponseObject
    from .create_single_message_response import CreateSingleMessageResponse
    from .create_single_message_response_object import CreateSingleMessageResponseObject
    from .create_single_message_response_recipient import CreateSingleMessageResponseRecipient
    from .create_single_message_response_status import CreateSingleMessageResponseStatus
    from .create_suppression_response import CreateSuppressionResponse
    from .create_suppression_response_object import CreateSuppressionResponseObject
    from .created_route import CreatedRoute
    from .created_smtp_credential import CreatedSmtpCredential
    from .created_webhook import CreatedWebhook
    from .deliverability_statistics import DeliverabilityStatistics
    from .deliverability_statistics_response import DeliverabilityStatisticsResponse
    from .deliverability_statistics_response_object import DeliverabilityStatisticsResponseObject
    from .delivery_event import DeliveryEvent
    from .delivery_time import DeliveryTime
    from .delivery_time_statistics import DeliveryTimeStatistics
    from .delivery_time_statistics_response import DeliveryTimeStatisticsResponse
    from .delivery_time_statistics_response_object import DeliveryTimeStatisticsResponseObject
    from .dns_record import DnsRecord
    from .domain import Domain
    from .domain_object import DomainObject
    from .error_response import ErrorResponse
    from .message import Message
    from .message_attachment import MessageAttachment
    from .message_content_parsed import MessageContentParsed
    from .message_content_part import MessageContentPart
    from .message_schedule import MessageSchedule
    from .message_summary import MessageSummary
    from .message_summary_direction import MessageSummaryDirection
    from .message_summary_object import MessageSummaryObject
    from .paginated_api_keys_response import PaginatedApiKeysResponse
    from .paginated_api_keys_response_object import PaginatedApiKeysResponseObject
    from .paginated_domains_response import PaginatedDomainsResponse
    from .paginated_domains_response_object import PaginatedDomainsResponseObject
    from .paginated_messages_response import PaginatedMessagesResponse
    from .paginated_messages_response_object import PaginatedMessagesResponseObject
    from .paginated_routes_response import PaginatedRoutesResponse
    from .paginated_routes_response_object import PaginatedRoutesResponseObject
    from .paginated_smtp_credentials_response import PaginatedSmtpCredentialsResponse
    from .paginated_smtp_credentials_response_object import PaginatedSmtpCredentialsResponseObject
    from .paginated_sub_accounts_response import PaginatedSubAccountsResponse
    from .paginated_sub_accounts_response_object import PaginatedSubAccountsResponseObject
    from .paginated_suppressions_response import PaginatedSuppressionsResponse
    from .paginated_suppressions_response_object import PaginatedSuppressionsResponseObject
    from .paginated_webhooks_response import PaginatedWebhooksResponse
    from .paginated_webhooks_response_object import PaginatedWebhooksResponseObject
    from .pagination_info import PaginationInfo
    from .recipient import Recipient
    from .retention import Retention
    from .route import Route
    from .route_object import RouteObject
    from .smtp_credential import SmtpCredential
    from .smtp_credential_object import SmtpCredentialObject
    from .smtp_credential_scope import SmtpCredentialScope
    from .sub_account import SubAccount
    from .sub_account_object import SubAccountObject
    from .sub_account_status import SubAccountStatus
    from .sub_account_usage_breakdown import SubAccountUsageBreakdown
    from .sub_account_usage_response import SubAccountUsageResponse
    from .sub_account_usage_response_allocation_method import SubAccountUsageResponseAllocationMethod
    from .sub_account_usage_response_billing_period import SubAccountUsageResponseBillingPeriod
    from .sub_account_usage_response_parent import SubAccountUsageResponseParent
    from .sub_account_usage_response_sub_accounts_item import SubAccountUsageResponseSubAccountsItem
    from .success_response import SuccessResponse
    from .suppression import Suppression
    from .suppression_object import SuppressionObject
    from .tracking import Tracking
    from .update_api_key_request import UpdateApiKeyRequest
    from .update_api_key_request_ip_allow_list import UpdateApiKeyRequestIpAllowList
    from .update_api_key_request_label import UpdateApiKeyRequestLabel
    from .update_api_key_request_scopes import UpdateApiKeyRequestScopes
    from .update_sub_account_request import UpdateSubAccountRequest
    from .update_sub_account_request_monthly_credit import UpdateSubAccountRequestMonthlyCredit
    from .update_sub_account_request_name import UpdateSubAccountRequestName
    from .update_sub_account_request_website import UpdateSubAccountRequestWebsite
    from .user_account import UserAccount
    from .user_account_role import UserAccountRole
    from .webhook import Webhook
    from .webhook_object import WebhookObject
    from .webhook_scope import WebhookScope
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".account",
    "AccountMembersResponse": ".account_members_response",
    "AccountMembersResponseObject": ".account_members_response_object",
    "AccountObject": ".account_object",
    "Address": ".address",
    "ApiKey": ".api_key",
    "ApiKeyObject": ".api_key_object",
    "ApiKeyScope": ".api_key_scope",
    "Attachment": ".attachment",
    "Bounce": ".bounce",
    "BounceStatistics": ".bounce_statistics",
    "BounceStatisticsResponse": ".bounce_statistics_response",
    "BounceStatisticsResponseObject": ".bounce_statistics_response_object",
    "CreateApiKeyRequest": ".create_api_key_request",
    "CreateMessageResponse": ".create_message_response",
    "CreateMessageResponseObject": ".create_message_response_object",
    "CreateSingleMessageResponse": ".create_single_message_response",
    "CreateSingleMessageResponseObject": ".create_single_message_response_object",
    "CreateSingleMessageResponseRecipient": ".create_single_message_response_recipient",
    "CreateSingleMessageResponseStatus": ".create_single_message_response_status",
    "CreateSuppressionResponse": ".create_suppression_response",
    "CreateSuppressionResponseObject": ".create_suppression_response_object",
    "CreatedRoute": ".created_route",
    "CreatedSmtpCredential": ".created_smtp_credential",
    "CreatedWebhook": ".created_webhook",
    "DeliverabilityStatistics": ".deliverability_statistics",
    "DeliverabilityStatisticsResponse": ".deliverability_statistics_response",
    "DeliverabilityStatisticsResponseObject": ".deliverability_statistics_response_object",
    "DeliveryEvent": ".delivery_event",
    "DeliveryTime": ".delivery_time",
    "DeliveryTimeStatistics": ".delivery_time_statistics",
    "DeliveryTimeStatisticsResponse": ".delivery_time_statistics_response",
    "DeliveryTimeStatisticsResponseObject": ".delivery_time_statistics_response_object",
    "DnsRecord": ".dns_record",
    "Domain": ".domain",
    "DomainObject": ".domain_object",
    "ErrorResponse": ".error_response",
    "Message": ".message",
    "MessageAttachment": ".message_attachment",
    "MessageContentParsed": ".message_content_parsed",
    "MessageContentPart": ".message_content_part",
    "MessageSchedule": ".message_schedule",
    "MessageSummary": ".message_summary",
    "MessageSummaryDirection": ".message_summary_direction",
    "MessageSummaryObject": ".message_summary_object",
    "PaginatedApiKeysResponse": ".paginated_api_keys_response",
    "PaginatedApiKeysResponseObject": ".paginated_api_keys_response_object",
    "PaginatedDomainsResponse": ".paginated_domains_response",
    "PaginatedDomainsResponseObject": ".paginated_domains_response_object",
    "PaginatedMessagesResponse": ".paginated_messages_response",
    "PaginatedMessagesResponseObject": ".paginated_messages_response_object",
    "PaginatedRoutesResponse": ".paginated_routes_response",
    "PaginatedRoutesResponseObject": ".paginated_routes_response_object",
    "PaginatedSmtpCredentialsResponse": ".paginated_smtp_credentials_response",
    "PaginatedSmtpCredentialsResponseObject": ".paginated_smtp_credentials_response_object",
    "PaginatedSubAccountsResponse": ".paginated_sub_accounts_response",
    "PaginatedSubAccountsResponseObject": ".paginated_sub_accounts_response_object",
    "PaginatedSuppressionsResponse": ".paginated_suppressions_response",
    "PaginatedSuppressionsResponseObject": ".paginated_suppressions_response_object",
    "PaginatedWebhooksResponse": ".paginated_webhooks_response",
    "PaginatedWebhooksResponseObject": ".paginated_webhooks_response_object",
    "PaginationInfo": ".pagination_info",
    "Recipient": ".recipient",
    "Retention": ".retention",
    "Route": ".route",
    "RouteObject": ".route_object",
    "SmtpCredential": ".smtp_credential",
    "SmtpCredentialObject": ".smtp_credential_object",
    "SmtpCredentialScope": ".smtp_credential_scope",
    "SubAccount": ".sub_account",
    "SubAccountObject": ".sub_account_object",
    "SubAccountStatus": ".sub_account_status",
    "SubAccountUsageBreakdown": ".sub_account_usage_breakdown",
    "SubAccountUsageResponse": ".sub_account_usage_response",
    "SubAccountUsageResponseAllocationMethod": ".sub_account_usage_response_allocation_method",
    "SubAccountUsageResponseBillingPeriod": ".sub_account_usage_response_billing_period",
    "SubAccountUsageResponseParent": ".sub_account_usage_response_parent",
    "SubAccountUsageResponseSubAccountsItem": ".sub_account_usage_response_sub_accounts_item",
    "SuccessResponse": ".success_response",
    "Suppression": ".suppression",
    "SuppressionObject": ".suppression_object",
    "Tracking": ".tracking",
    "UpdateApiKeyRequest": ".update_api_key_request",
    "UpdateApiKeyRequestIpAllowList": ".update_api_key_request_ip_allow_list",
    "UpdateApiKeyRequestLabel": ".update_api_key_request_label",
    "UpdateApiKeyRequestScopes": ".update_api_key_request_scopes",
    "UpdateSubAccountRequest": ".update_sub_account_request",
    "UpdateSubAccountRequestMonthlyCredit": ".update_sub_account_request_monthly_credit",
    "UpdateSubAccountRequestName": ".update_sub_account_request_name",
    "UpdateSubAccountRequestWebsite": ".update_sub_account_request_website",
    "UserAccount": ".user_account",
    "UserAccountRole": ".user_account_role",
    "Webhook": ".webhook",
    "WebhookObject": ".webhook_object",
    "WebhookScope": ".webhook_scope",
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
    "Account",
    "AccountMembersResponse",
    "AccountMembersResponseObject",
    "AccountObject",
    "Address",
    "ApiKey",
    "ApiKeyObject",
    "ApiKeyScope",
    "Attachment",
    "Bounce",
    "BounceStatistics",
    "BounceStatisticsResponse",
    "BounceStatisticsResponseObject",
    "CreateApiKeyRequest",
    "CreateMessageResponse",
    "CreateMessageResponseObject",
    "CreateSingleMessageResponse",
    "CreateSingleMessageResponseObject",
    "CreateSingleMessageResponseRecipient",
    "CreateSingleMessageResponseStatus",
    "CreateSuppressionResponse",
    "CreateSuppressionResponseObject",
    "CreatedRoute",
    "CreatedSmtpCredential",
    "CreatedWebhook",
    "DeliverabilityStatistics",
    "DeliverabilityStatisticsResponse",
    "DeliverabilityStatisticsResponseObject",
    "DeliveryEvent",
    "DeliveryTime",
    "DeliveryTimeStatistics",
    "DeliveryTimeStatisticsResponse",
    "DeliveryTimeStatisticsResponseObject",
    "DnsRecord",
    "Domain",
    "DomainObject",
    "ErrorResponse",
    "Message",
    "MessageAttachment",
    "MessageContentParsed",
    "MessageContentPart",
    "MessageSchedule",
    "MessageSummary",
    "MessageSummaryDirection",
    "MessageSummaryObject",
    "PaginatedApiKeysResponse",
    "PaginatedApiKeysResponseObject",
    "PaginatedDomainsResponse",
    "PaginatedDomainsResponseObject",
    "PaginatedMessagesResponse",
    "PaginatedMessagesResponseObject",
    "PaginatedRoutesResponse",
    "PaginatedRoutesResponseObject",
    "PaginatedSmtpCredentialsResponse",
    "PaginatedSmtpCredentialsResponseObject",
    "PaginatedSubAccountsResponse",
    "PaginatedSubAccountsResponseObject",
    "PaginatedSuppressionsResponse",
    "PaginatedSuppressionsResponseObject",
    "PaginatedWebhooksResponse",
    "PaginatedWebhooksResponseObject",
    "PaginationInfo",
    "Recipient",
    "Retention",
    "Route",
    "RouteObject",
    "SmtpCredential",
    "SmtpCredentialObject",
    "SmtpCredentialScope",
    "SubAccount",
    "SubAccountObject",
    "SubAccountStatus",
    "SubAccountUsageBreakdown",
    "SubAccountUsageResponse",
    "SubAccountUsageResponseAllocationMethod",
    "SubAccountUsageResponseBillingPeriod",
    "SubAccountUsageResponseParent",
    "SubAccountUsageResponseSubAccountsItem",
    "SuccessResponse",
    "Suppression",
    "SuppressionObject",
    "Tracking",
    "UpdateApiKeyRequest",
    "UpdateApiKeyRequestIpAllowList",
    "UpdateApiKeyRequestLabel",
    "UpdateApiKeyRequestScopes",
    "UpdateSubAccountRequest",
    "UpdateSubAccountRequestMonthlyCredit",
    "UpdateSubAccountRequestName",
    "UpdateSubAccountRequestWebsite",
    "UserAccount",
    "UserAccountRole",
    "Webhook",
    "WebhookObject",
    "WebhookScope",
]
