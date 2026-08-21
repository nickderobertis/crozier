



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_denied import AccessDenied
    from .active_trusted_signers import ActiveTrustedSigners
    from .active_trusted_signers_items_item import ActiveTrustedSignersItemsItem
    from .active_trusted_signers_items_item_key_pair_ids import ActiveTrustedSignersItemsItemKeyPairIds
    from .alias_list import AliasList
    from .aliases import Aliases
    from .allowed_methods import AllowedMethods
    from .allowed_methods_items_item import AllowedMethodsItemsItem
    from .aws_account_number_list import AwsAccountNumberList
    from .batch_too_large import BatchTooLarge
    from .boolean import Boolean
    from .cache_behavior import CacheBehavior
    from .cache_behavior_forwarded_values import CacheBehaviorForwardedValues
    from .cache_behavior_forwarded_values_cookies import CacheBehaviorForwardedValuesCookies
    from .cache_behavior_forwarded_values_cookies_forward import CacheBehaviorForwardedValuesCookiesForward
    from .cache_behavior_forwarded_values_cookies_whitelisted_names import (
        CacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .cache_behavior_forwarded_values_headers import CacheBehaviorForwardedValuesHeaders
    from .cache_behavior_forwarded_values_query_string_cache_keys import (
        CacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .cache_behavior_lambda_function_associations import CacheBehaviorLambdaFunctionAssociations
    from .cache_behavior_lambda_function_associations_items_item import CacheBehaviorLambdaFunctionAssociationsItemsItem
    from .cache_behavior_lambda_function_associations_items_item_event_type import (
        CacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .cache_behavior_list import CacheBehaviorList
    from .cache_behavior_list_item import CacheBehaviorListItem
    from .cache_behavior_list_item_forwarded_values import CacheBehaviorListItemForwardedValues
    from .cache_behavior_list_item_forwarded_values_cookies import CacheBehaviorListItemForwardedValuesCookies
    from .cache_behavior_list_item_forwarded_values_cookies_forward import (
        CacheBehaviorListItemForwardedValuesCookiesForward,
    )
    from .cache_behavior_list_item_forwarded_values_cookies_whitelisted_names import (
        CacheBehaviorListItemForwardedValuesCookiesWhitelistedNames,
    )
    from .cache_behavior_list_item_forwarded_values_headers import CacheBehaviorListItemForwardedValuesHeaders
    from .cache_behavior_list_item_forwarded_values_query_string_cache_keys import (
        CacheBehaviorListItemForwardedValuesQueryStringCacheKeys,
    )
    from .cache_behavior_list_item_lambda_function_associations import CacheBehaviorListItemLambdaFunctionAssociations
    from .cache_behavior_list_item_lambda_function_associations_items_item import (
        CacheBehaviorListItemLambdaFunctionAssociationsItemsItem,
    )
    from .cache_behavior_list_item_lambda_function_associations_items_item_event_type import (
        CacheBehaviorListItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .cache_behavior_list_item_trusted_signers import CacheBehaviorListItemTrustedSigners
    from .cache_behavior_list_item_viewer_protocol_policy import CacheBehaviorListItemViewerProtocolPolicy
    from .cache_behavior_trusted_signers import CacheBehaviorTrustedSigners
    from .cache_behavior_viewer_protocol_policy import CacheBehaviorViewerProtocolPolicy
    from .cache_behaviors import CacheBehaviors
    from .cache_behaviors_items_item import CacheBehaviorsItemsItem
    from .cache_behaviors_items_item_forwarded_values import CacheBehaviorsItemsItemForwardedValues
    from .cache_behaviors_items_item_forwarded_values_cookies import CacheBehaviorsItemsItemForwardedValuesCookies
    from .cache_behaviors_items_item_forwarded_values_cookies_forward import (
        CacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        CacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .cache_behaviors_items_item_forwarded_values_headers import CacheBehaviorsItemsItemForwardedValuesHeaders
    from .cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        CacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .cache_behaviors_items_item_lambda_function_associations import (
        CacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .cache_behaviors_items_item_lambda_function_associations_items_item import (
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .cache_behaviors_items_item_trusted_signers import CacheBehaviorsItemsItemTrustedSigners
    from .cache_behaviors_items_item_viewer_protocol_policy import CacheBehaviorsItemsItemViewerProtocolPolicy
    from .cached_methods import CachedMethods
    from .cached_methods_items_item import CachedMethodsItemsItem
    from .certificate_source import CertificateSource
    from .cloud_front_origin_access_identity import CloudFrontOriginAccessIdentity
    from .cloud_front_origin_access_identity_already_exists import CloudFrontOriginAccessIdentityAlreadyExists
    from .cloud_front_origin_access_identity_cloud_front_origin_access_identity_config import (
        CloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig,
    )
    from .cloud_front_origin_access_identity_config import CloudFrontOriginAccessIdentityConfig
    from .cloud_front_origin_access_identity_in_use import CloudFrontOriginAccessIdentityInUse
    from .cloud_front_origin_access_identity_list import CloudFrontOriginAccessIdentityList
    from .cloud_front_origin_access_identity_list_items_item import CloudFrontOriginAccessIdentityListItemsItem
    from .cloud_front_origin_access_identity_summary import CloudFrontOriginAccessIdentitySummary
    from .cloud_front_origin_access_identity_summary_list import CloudFrontOriginAccessIdentitySummaryList
    from .cloud_front_origin_access_identity_summary_list_item import CloudFrontOriginAccessIdentitySummaryListItem
    from .cname_already_exists import CnameAlreadyExists
    from .cookie_name_list import CookieNameList
    from .cookie_names import CookieNames
    from .cookie_preference import CookiePreference
    from .cookie_preference_forward import CookiePreferenceForward
    from .cookie_preference_whitelisted_names import CookiePreferenceWhitelistedNames
    from .create_cloud_front_origin_access_identity_request import CreateCloudFrontOriginAccessIdentityRequest
    from .create_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config import (
        CreateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
    )
    from .create_cloud_front_origin_access_identity_result import CreateCloudFrontOriginAccessIdentityResult
    from .create_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity import (
        CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity,
    )
    from .create_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config import (
        CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig,
    )
    from .create_distribution_request import CreateDistributionRequest
    from .create_distribution_request_distribution_config import CreateDistributionRequestDistributionConfig
    from .create_distribution_request_distribution_config_aliases import (
        CreateDistributionRequestDistributionConfigAliases,
    )
    from .create_distribution_request_distribution_config_cache_behaviors import (
        CreateDistributionRequestDistributionConfigCacheBehaviors,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_trusted_signers import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .create_distribution_request_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .create_distribution_request_distribution_config_custom_error_responses import (
        CreateDistributionRequestDistributionConfigCustomErrorResponses,
    )
    from .create_distribution_request_distribution_config_custom_error_responses_items_item import (
        CreateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehavior,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_headers import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_trusted_signers import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .create_distribution_request_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        CreateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .create_distribution_request_distribution_config_http_version import (
        CreateDistributionRequestDistributionConfigHttpVersion,
    )
    from .create_distribution_request_distribution_config_logging import (
        CreateDistributionRequestDistributionConfigLogging,
    )
    from .create_distribution_request_distribution_config_origins import (
        CreateDistributionRequestDistributionConfigOrigins,
    )
    from .create_distribution_request_distribution_config_origins_items_item import (
        CreateDistributionRequestDistributionConfigOriginsItemsItem,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_headers import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_headers_items_item import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_origin_config import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .create_distribution_request_distribution_config_origins_items_item_s3origin_config import (
        CreateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .create_distribution_request_distribution_config_price_class import (
        CreateDistributionRequestDistributionConfigPriceClass,
    )
    from .create_distribution_result import CreateDistributionResult
    from .create_distribution_result_distribution import CreateDistributionResultDistribution
    from .create_distribution_result_distribution_active_trusted_signers import (
        CreateDistributionResultDistributionActiveTrustedSigners,
    )
    from .create_distribution_result_distribution_active_trusted_signers_items_item import (
        CreateDistributionResultDistributionActiveTrustedSignersItemsItem,
    )
    from .create_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids import (
        CreateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .create_distribution_result_distribution_distribution_config import (
        CreateDistributionResultDistributionDistributionConfig,
    )
    from .create_distribution_result_distribution_distribution_config_aliases import (
        CreateDistributionResultDistributionDistributionConfigAliases,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviors,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .create_distribution_result_distribution_distribution_config_custom_error_responses import (
        CreateDistributionResultDistributionDistributionConfigCustomErrorResponses,
    )
    from .create_distribution_result_distribution_distribution_config_custom_error_responses_items_item import (
        CreateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehavior,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .create_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .create_distribution_result_distribution_distribution_config_http_version import (
        CreateDistributionResultDistributionDistributionConfigHttpVersion,
    )
    from .create_distribution_result_distribution_distribution_config_logging import (
        CreateDistributionResultDistributionDistributionConfigLogging,
    )
    from .create_distribution_result_distribution_distribution_config_origins import (
        CreateDistributionResultDistributionDistributionConfigOrigins,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_headers import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .create_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config import (
        CreateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .create_distribution_result_distribution_distribution_config_price_class import (
        CreateDistributionResultDistributionDistributionConfigPriceClass,
    )
    from .create_distribution_with_tags_request import CreateDistributionWithTagsRequest
    from .create_distribution_with_tags_request_distribution_config_with_tags import (
        CreateDistributionWithTagsRequestDistributionConfigWithTags,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfig,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_aliases import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigAliases,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviors,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_trusted_signers import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_custom_error_responses import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponses,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_custom_error_responses_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehavior,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_headers import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_trusted_signers import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_http_version import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigHttpVersion,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_logging import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigLogging,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOrigins,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_headers import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_headers_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_s3origin_config import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_price_class import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigPriceClass,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_tags import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsTags,
    )
    from .create_distribution_with_tags_request_distribution_config_with_tags_tags_items_item import (
        CreateDistributionWithTagsRequestDistributionConfigWithTagsTagsItemsItem,
    )
    from .create_distribution_with_tags_result import CreateDistributionWithTagsResult
    from .create_distribution_with_tags_result_distribution import CreateDistributionWithTagsResultDistribution
    from .create_distribution_with_tags_result_distribution_active_trusted_signers import (
        CreateDistributionWithTagsResultDistributionActiveTrustedSigners,
    )
    from .create_distribution_with_tags_result_distribution_active_trusted_signers_items_item import (
        CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_active_trusted_signers_items_item_key_pair_ids import (
        CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config import (
        CreateDistributionWithTagsResultDistributionDistributionConfig,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_aliases import (
        CreateDistributionWithTagsResultDistributionDistributionConfigAliases,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviors,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_custom_error_responses import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponses,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_custom_error_responses_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehavior,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_trusted_signers import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_http_version import (
        CreateDistributionWithTagsResultDistributionDistributionConfigHttpVersion,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_logging import (
        CreateDistributionWithTagsResultDistributionDistributionConfigLogging,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOrigins,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_headers import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_headers_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_s3origin_config import (
        CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .create_distribution_with_tags_result_distribution_distribution_config_price_class import (
        CreateDistributionWithTagsResultDistributionDistributionConfigPriceClass,
    )
    from .create_invalidation_request import CreateInvalidationRequest
    from .create_invalidation_request_invalidation_batch import CreateInvalidationRequestInvalidationBatch
    from .create_invalidation_request_invalidation_batch_paths import CreateInvalidationRequestInvalidationBatchPaths
    from .create_invalidation_result import CreateInvalidationResult
    from .create_invalidation_result_invalidation import CreateInvalidationResultInvalidation
    from .create_invalidation_result_invalidation_invalidation_batch import (
        CreateInvalidationResultInvalidationInvalidationBatch,
    )
    from .create_invalidation_result_invalidation_invalidation_batch_paths import (
        CreateInvalidationResultInvalidationInvalidationBatchPaths,
    )
    from .create_streaming_distribution_request import CreateStreamingDistributionRequest
    from .create_streaming_distribution_request_streaming_distribution_config import (
        CreateStreamingDistributionRequestStreamingDistributionConfig,
    )
    from .create_streaming_distribution_request_streaming_distribution_config_aliases import (
        CreateStreamingDistributionRequestStreamingDistributionConfigAliases,
    )
    from .create_streaming_distribution_request_streaming_distribution_config_logging import (
        CreateStreamingDistributionRequestStreamingDistributionConfigLogging,
    )
    from .create_streaming_distribution_request_streaming_distribution_config_price_class import (
        CreateStreamingDistributionRequestStreamingDistributionConfigPriceClass,
    )
    from .create_streaming_distribution_request_streaming_distribution_config_s3origin import (
        CreateStreamingDistributionRequestStreamingDistributionConfigS3Origin,
    )
    from .create_streaming_distribution_request_streaming_distribution_config_trusted_signers import (
        CreateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners,
    )
    from .create_streaming_distribution_result import CreateStreamingDistributionResult
    from .create_streaming_distribution_result_streaming_distribution import (
        CreateStreamingDistributionResultStreamingDistribution,
    )
    from .create_streaming_distribution_result_streaming_distribution_active_trusted_signers import (
        CreateStreamingDistributionResultStreamingDistributionActiveTrustedSigners,
    )
    from .create_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item import (
        CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem,
    )
    from .create_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
        CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin,
    )
    from .create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers import (
        CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners,
    )
    from .create_streaming_distribution_with_tags_request import CreateStreamingDistributionWithTagsRequest
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfig,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_aliases import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigAliases,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_logging import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigLogging,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_price_class import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_s3origin import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_trusted_signers import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_tags import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTags,
    )
    from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_tags_items_item import (
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTagsItemsItem,
    )
    from .create_streaming_distribution_with_tags_result import CreateStreamingDistributionWithTagsResult
    from .create_streaming_distribution_with_tags_result_streaming_distribution import (
        CreateStreamingDistributionWithTagsResultStreamingDistribution,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSigners,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers_items_item import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfig,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_aliases import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigAliases,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_logging import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigLogging,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_price_class import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigPriceClass,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_s3origin import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigS3Origin,
    )
    from .create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_trusted_signers import (
        CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigTrustedSigners,
    )
    from .custom_error_response import CustomErrorResponse
    from .custom_error_response_list import CustomErrorResponseList
    from .custom_error_response_list_item import CustomErrorResponseListItem
    from .custom_error_responses import CustomErrorResponses
    from .custom_error_responses_items_item import CustomErrorResponsesItemsItem
    from .custom_headers import CustomHeaders
    from .custom_headers_items_item import CustomHeadersItemsItem
    from .custom_origin_config import CustomOriginConfig
    from .custom_origin_config_origin_protocol_policy import CustomOriginConfigOriginProtocolPolicy
    from .custom_origin_config_origin_ssl_protocols import CustomOriginConfigOriginSslProtocols
    from .custom_origin_config_origin_ssl_protocols_items_item import CustomOriginConfigOriginSslProtocolsItemsItem
    from .default_cache_behavior import DefaultCacheBehavior
    from .default_cache_behavior_forwarded_values import DefaultCacheBehaviorForwardedValues
    from .default_cache_behavior_forwarded_values_cookies import DefaultCacheBehaviorForwardedValuesCookies
    from .default_cache_behavior_forwarded_values_cookies_forward import (
        DefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .default_cache_behavior_forwarded_values_headers import DefaultCacheBehaviorForwardedValuesHeaders
    from .default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .default_cache_behavior_lambda_function_associations import DefaultCacheBehaviorLambdaFunctionAssociations
    from .default_cache_behavior_lambda_function_associations_items_item import (
        DefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .default_cache_behavior_trusted_signers import DefaultCacheBehaviorTrustedSigners
    from .default_cache_behavior_viewer_protocol_policy import DefaultCacheBehaviorViewerProtocolPolicy
    from .delete_cloud_front_origin_access_identity_request import DeleteCloudFrontOriginAccessIdentityRequest
    from .delete_distribution_request import DeleteDistributionRequest
    from .delete_streaming_distribution_request import DeleteStreamingDistributionRequest
    from .distribution import Distribution
    from .distribution_active_trusted_signers import DistributionActiveTrustedSigners
    from .distribution_active_trusted_signers_items_item import DistributionActiveTrustedSignersItemsItem
    from .distribution_active_trusted_signers_items_item_key_pair_ids import (
        DistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .distribution_already_exists import DistributionAlreadyExists
    from .distribution_config import DistributionConfig
    from .distribution_config_aliases import DistributionConfigAliases
    from .distribution_config_cache_behaviors import DistributionConfigCacheBehaviors
    from .distribution_config_cache_behaviors_items_item import DistributionConfigCacheBehaviorsItemsItem
    from .distribution_config_cache_behaviors_items_item_forwarded_values import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_config_cache_behaviors_items_item_trusted_signers import (
        DistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_config_custom_error_responses import DistributionConfigCustomErrorResponses
    from .distribution_config_custom_error_responses_items_item import DistributionConfigCustomErrorResponsesItemsItem
    from .distribution_config_default_cache_behavior import DistributionConfigDefaultCacheBehavior
    from .distribution_config_default_cache_behavior_forwarded_values import (
        DistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_config_default_cache_behavior_forwarded_values_cookies import (
        DistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_config_default_cache_behavior_forwarded_values_headers import (
        DistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_config_default_cache_behavior_lambda_function_associations import (
        DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_config_default_cache_behavior_trusted_signers import (
        DistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_config_default_cache_behavior_viewer_protocol_policy import (
        DistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_config_http_version import DistributionConfigHttpVersion
    from .distribution_config_logging import DistributionConfigLogging
    from .distribution_config_origins import DistributionConfigOrigins
    from .distribution_config_origins_items_item import DistributionConfigOriginsItemsItem
    from .distribution_config_origins_items_item_custom_headers import DistributionConfigOriginsItemsItemCustomHeaders
    from .distribution_config_origins_items_item_custom_headers_items_item import (
        DistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_config_origins_items_item_custom_origin_config import (
        DistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_config_origins_items_item_s3origin_config import DistributionConfigOriginsItemsItemS3OriginConfig
    from .distribution_config_price_class import DistributionConfigPriceClass
    from .distribution_config_with_tags import DistributionConfigWithTags
    from .distribution_config_with_tags_distribution_config import DistributionConfigWithTagsDistributionConfig
    from .distribution_config_with_tags_distribution_config_aliases import (
        DistributionConfigWithTagsDistributionConfigAliases,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviors,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_trusted_signers import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_config_with_tags_distribution_config_custom_error_responses import (
        DistributionConfigWithTagsDistributionConfigCustomErrorResponses,
    )
    from .distribution_config_with_tags_distribution_config_custom_error_responses_items_item import (
        DistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehavior,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_headers import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_trusted_signers import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_config_with_tags_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_config_with_tags_distribution_config_http_version import (
        DistributionConfigWithTagsDistributionConfigHttpVersion,
    )
    from .distribution_config_with_tags_distribution_config_logging import (
        DistributionConfigWithTagsDistributionConfigLogging,
    )
    from .distribution_config_with_tags_distribution_config_origins import (
        DistributionConfigWithTagsDistributionConfigOrigins,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_headers import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_headers_items_item import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_config_with_tags_distribution_config_origins_items_item_s3origin_config import (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .distribution_config_with_tags_distribution_config_price_class import (
        DistributionConfigWithTagsDistributionConfigPriceClass,
    )
    from .distribution_config_with_tags_tags import DistributionConfigWithTagsTags
    from .distribution_config_with_tags_tags_items_item import DistributionConfigWithTagsTagsItemsItem
    from .distribution_distribution_config import DistributionDistributionConfig
    from .distribution_distribution_config_aliases import DistributionDistributionConfigAliases
    from .distribution_distribution_config_cache_behaviors import DistributionDistributionConfigCacheBehaviors
    from .distribution_distribution_config_cache_behaviors_items_item import (
        DistributionDistributionConfigCacheBehaviorsItemsItem,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_trusted_signers import (
        DistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_distribution_config_custom_error_responses import (
        DistributionDistributionConfigCustomErrorResponses,
    )
    from .distribution_distribution_config_custom_error_responses_items_item import (
        DistributionDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .distribution_distribution_config_default_cache_behavior import (
        DistributionDistributionConfigDefaultCacheBehavior,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_distribution_config_default_cache_behavior_lambda_function_associations import (
        DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_distribution_config_default_cache_behavior_trusted_signers import (
        DistributionDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        DistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_distribution_config_http_version import DistributionDistributionConfigHttpVersion
    from .distribution_distribution_config_logging import DistributionDistributionConfigLogging
    from .distribution_distribution_config_origins import DistributionDistributionConfigOrigins
    from .distribution_distribution_config_origins_items_item import DistributionDistributionConfigOriginsItemsItem
    from .distribution_distribution_config_origins_items_item_custom_headers import (
        DistributionDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .distribution_distribution_config_origins_items_item_custom_headers_items_item import (
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_distribution_config_origins_items_item_custom_origin_config import (
        DistributionDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_distribution_config_origins_items_item_s3origin_config import (
        DistributionDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .distribution_distribution_config_price_class import DistributionDistributionConfigPriceClass
    from .distribution_list import DistributionList
    from .distribution_list_items_item import DistributionListItemsItem
    from .distribution_list_items_item_aliases import DistributionListItemsItemAliases
    from .distribution_list_items_item_cache_behaviors import DistributionListItemsItemCacheBehaviors
    from .distribution_list_items_item_cache_behaviors_items_item import (
        DistributionListItemsItemCacheBehaviorsItemsItem,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations import (
        DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_trusted_signers import (
        DistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_list_items_item_custom_error_responses import DistributionListItemsItemCustomErrorResponses
    from .distribution_list_items_item_custom_error_responses_items_item import (
        DistributionListItemsItemCustomErrorResponsesItemsItem,
    )
    from .distribution_list_items_item_default_cache_behavior import DistributionListItemsItemDefaultCacheBehavior
    from .distribution_list_items_item_default_cache_behavior_forwarded_values import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_list_items_item_default_cache_behavior_forwarded_values_cookies import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_list_items_item_default_cache_behavior_forwarded_values_headers import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_list_items_item_default_cache_behavior_lambda_function_associations import (
        DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_list_items_item_default_cache_behavior_trusted_signers import (
        DistributionListItemsItemDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_list_items_item_default_cache_behavior_viewer_protocol_policy import (
        DistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_list_items_item_http_version import DistributionListItemsItemHttpVersion
    from .distribution_list_items_item_origins import DistributionListItemsItemOrigins
    from .distribution_list_items_item_origins_items_item import DistributionListItemsItemOriginsItemsItem
    from .distribution_list_items_item_origins_items_item_custom_headers import (
        DistributionListItemsItemOriginsItemsItemCustomHeaders,
    )
    from .distribution_list_items_item_origins_items_item_custom_headers_items_item import (
        DistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_list_items_item_origins_items_item_custom_origin_config import (
        DistributionListItemsItemOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_list_items_item_origins_items_item_s3origin_config import (
        DistributionListItemsItemOriginsItemsItemS3OriginConfig,
    )
    from .distribution_not_disabled import DistributionNotDisabled
    from .distribution_summary import DistributionSummary
    from .distribution_summary_aliases import DistributionSummaryAliases
    from .distribution_summary_cache_behaviors import DistributionSummaryCacheBehaviors
    from .distribution_summary_cache_behaviors_items_item import DistributionSummaryCacheBehaviorsItemsItem
    from .distribution_summary_cache_behaviors_items_item_forwarded_values import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_summary_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_summary_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_summary_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_summary_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_summary_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionSummaryCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_summary_cache_behaviors_items_item_lambda_function_associations import (
        DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_summary_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_summary_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_summary_cache_behaviors_items_item_trusted_signers import (
        DistributionSummaryCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_summary_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionSummaryCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_summary_custom_error_responses import DistributionSummaryCustomErrorResponses
    from .distribution_summary_custom_error_responses_items_item import DistributionSummaryCustomErrorResponsesItemsItem
    from .distribution_summary_default_cache_behavior import DistributionSummaryDefaultCacheBehavior
    from .distribution_summary_default_cache_behavior_forwarded_values import (
        DistributionSummaryDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_summary_default_cache_behavior_forwarded_values_cookies import (
        DistributionSummaryDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_summary_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_summary_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_summary_default_cache_behavior_forwarded_values_headers import (
        DistributionSummaryDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_summary_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionSummaryDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_summary_default_cache_behavior_lambda_function_associations import (
        DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_summary_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_summary_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_summary_default_cache_behavior_trusted_signers import (
        DistributionSummaryDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_summary_default_cache_behavior_viewer_protocol_policy import (
        DistributionSummaryDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_summary_http_version import DistributionSummaryHttpVersion
    from .distribution_summary_list import DistributionSummaryList
    from .distribution_summary_list_item import DistributionSummaryListItem
    from .distribution_summary_list_item_aliases import DistributionSummaryListItemAliases
    from .distribution_summary_list_item_cache_behaviors import DistributionSummaryListItemCacheBehaviors
    from .distribution_summary_list_item_cache_behaviors_items_item import (
        DistributionSummaryListItemCacheBehaviorsItemsItem,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValues,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_headers import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations import (
        DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations_items_item import (
        DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_trusted_signers import (
        DistributionSummaryListItemCacheBehaviorsItemsItemTrustedSigners,
    )
    from .distribution_summary_list_item_cache_behaviors_items_item_viewer_protocol_policy import (
        DistributionSummaryListItemCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .distribution_summary_list_item_custom_error_responses import DistributionSummaryListItemCustomErrorResponses
    from .distribution_summary_list_item_custom_error_responses_items_item import (
        DistributionSummaryListItemCustomErrorResponsesItemsItem,
    )
    from .distribution_summary_list_item_default_cache_behavior import DistributionSummaryListItemDefaultCacheBehavior
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValues,
    )
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies_forward import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values_headers import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .distribution_summary_list_item_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .distribution_summary_list_item_default_cache_behavior_lambda_function_associations import (
        DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .distribution_summary_list_item_default_cache_behavior_lambda_function_associations_items_item import (
        DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .distribution_summary_list_item_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .distribution_summary_list_item_default_cache_behavior_trusted_signers import (
        DistributionSummaryListItemDefaultCacheBehaviorTrustedSigners,
    )
    from .distribution_summary_list_item_default_cache_behavior_viewer_protocol_policy import (
        DistributionSummaryListItemDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .distribution_summary_list_item_http_version import DistributionSummaryListItemHttpVersion
    from .distribution_summary_list_item_origins import DistributionSummaryListItemOrigins
    from .distribution_summary_list_item_origins_items_item import DistributionSummaryListItemOriginsItemsItem
    from .distribution_summary_list_item_origins_items_item_custom_headers import (
        DistributionSummaryListItemOriginsItemsItemCustomHeaders,
    )
    from .distribution_summary_list_item_origins_items_item_custom_headers_items_item import (
        DistributionSummaryListItemOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_summary_list_item_origins_items_item_custom_origin_config import (
        DistributionSummaryListItemOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_summary_list_item_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_summary_list_item_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_summary_list_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_summary_list_item_origins_items_item_s3origin_config import (
        DistributionSummaryListItemOriginsItemsItemS3OriginConfig,
    )
    from .distribution_summary_origins import DistributionSummaryOrigins
    from .distribution_summary_origins_items_item import DistributionSummaryOriginsItemsItem
    from .distribution_summary_origins_items_item_custom_headers import DistributionSummaryOriginsItemsItemCustomHeaders
    from .distribution_summary_origins_items_item_custom_headers_items_item import (
        DistributionSummaryOriginsItemsItemCustomHeadersItemsItem,
    )
    from .distribution_summary_origins_items_item_custom_origin_config import (
        DistributionSummaryOriginsItemsItemCustomOriginConfig,
    )
    from .distribution_summary_origins_items_item_custom_origin_config_origin_protocol_policy import (
        DistributionSummaryOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .distribution_summary_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .distribution_summary_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .distribution_summary_origins_items_item_s3origin_config import (
        DistributionSummaryOriginsItemsItemS3OriginConfig,
    )
    from .event_type import EventType
    from .forwarded_values import ForwardedValues
    from .forwarded_values_cookies import ForwardedValuesCookies
    from .forwarded_values_cookies_forward import ForwardedValuesCookiesForward
    from .forwarded_values_cookies_whitelisted_names import ForwardedValuesCookiesWhitelistedNames
    from .forwarded_values_headers import ForwardedValuesHeaders
    from .forwarded_values_query_string_cache_keys import ForwardedValuesQueryStringCacheKeys
    from .geo_restriction import GeoRestriction
    from .geo_restriction_restriction_type import GeoRestrictionRestrictionType
    from .geo_restriction_type import GeoRestrictionType
    from .get_cloud_front_origin_access_identity_config_request import GetCloudFrontOriginAccessIdentityConfigRequest
    from .get_cloud_front_origin_access_identity_config_result import GetCloudFrontOriginAccessIdentityConfigResult
    from .get_cloud_front_origin_access_identity_config_result_cloud_front_origin_access_identity_config import (
        GetCloudFrontOriginAccessIdentityConfigResultCloudFrontOriginAccessIdentityConfig,
    )
    from .get_cloud_front_origin_access_identity_request import GetCloudFrontOriginAccessIdentityRequest
    from .get_cloud_front_origin_access_identity_result import GetCloudFrontOriginAccessIdentityResult
    from .get_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity import (
        GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity,
    )
    from .get_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config import (
        GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig,
    )
    from .get_distribution_config_request import GetDistributionConfigRequest
    from .get_distribution_config_result import GetDistributionConfigResult
    from .get_distribution_config_result_distribution_config import GetDistributionConfigResultDistributionConfig
    from .get_distribution_config_result_distribution_config_aliases import (
        GetDistributionConfigResultDistributionConfigAliases,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors import (
        GetDistributionConfigResultDistributionConfigCacheBehaviors,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItem,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_trusted_signers import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .get_distribution_config_result_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .get_distribution_config_result_distribution_config_custom_error_responses import (
        GetDistributionConfigResultDistributionConfigCustomErrorResponses,
    )
    from .get_distribution_config_result_distribution_config_custom_error_responses_items_item import (
        GetDistributionConfigResultDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehavior,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_headers import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_trusted_signers import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .get_distribution_config_result_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .get_distribution_config_result_distribution_config_http_version import (
        GetDistributionConfigResultDistributionConfigHttpVersion,
    )
    from .get_distribution_config_result_distribution_config_logging import (
        GetDistributionConfigResultDistributionConfigLogging,
    )
    from .get_distribution_config_result_distribution_config_origins import (
        GetDistributionConfigResultDistributionConfigOrigins,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItem,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_headers import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_headers_items_item import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .get_distribution_config_result_distribution_config_origins_items_item_s3origin_config import (
        GetDistributionConfigResultDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .get_distribution_config_result_distribution_config_price_class import (
        GetDistributionConfigResultDistributionConfigPriceClass,
    )
    from .get_distribution_request import GetDistributionRequest
    from .get_distribution_result import GetDistributionResult
    from .get_distribution_result_distribution import GetDistributionResultDistribution
    from .get_distribution_result_distribution_active_trusted_signers import (
        GetDistributionResultDistributionActiveTrustedSigners,
    )
    from .get_distribution_result_distribution_active_trusted_signers_items_item import (
        GetDistributionResultDistributionActiveTrustedSignersItemsItem,
    )
    from .get_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids import (
        GetDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .get_distribution_result_distribution_distribution_config import (
        GetDistributionResultDistributionDistributionConfig,
    )
    from .get_distribution_result_distribution_distribution_config_aliases import (
        GetDistributionResultDistributionDistributionConfigAliases,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviors,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .get_distribution_result_distribution_distribution_config_custom_error_responses import (
        GetDistributionResultDistributionDistributionConfigCustomErrorResponses,
    )
    from .get_distribution_result_distribution_distribution_config_custom_error_responses_items_item import (
        GetDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehavior,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .get_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .get_distribution_result_distribution_distribution_config_http_version import (
        GetDistributionResultDistributionDistributionConfigHttpVersion,
    )
    from .get_distribution_result_distribution_distribution_config_logging import (
        GetDistributionResultDistributionDistributionConfigLogging,
    )
    from .get_distribution_result_distribution_distribution_config_origins import (
        GetDistributionResultDistributionDistributionConfigOrigins,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_headers import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .get_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config import (
        GetDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .get_distribution_result_distribution_distribution_config_price_class import (
        GetDistributionResultDistributionDistributionConfigPriceClass,
    )
    from .get_invalidation_request import GetInvalidationRequest
    from .get_invalidation_result import GetInvalidationResult
    from .get_invalidation_result_invalidation import GetInvalidationResultInvalidation
    from .get_invalidation_result_invalidation_invalidation_batch import (
        GetInvalidationResultInvalidationInvalidationBatch,
    )
    from .get_invalidation_result_invalidation_invalidation_batch_paths import (
        GetInvalidationResultInvalidationInvalidationBatchPaths,
    )
    from .get_streaming_distribution_config_request import GetStreamingDistributionConfigRequest
    from .get_streaming_distribution_config_result import GetStreamingDistributionConfigResult
    from .get_streaming_distribution_config_result_streaming_distribution_config import (
        GetStreamingDistributionConfigResultStreamingDistributionConfig,
    )
    from .get_streaming_distribution_config_result_streaming_distribution_config_aliases import (
        GetStreamingDistributionConfigResultStreamingDistributionConfigAliases,
    )
    from .get_streaming_distribution_config_result_streaming_distribution_config_logging import (
        GetStreamingDistributionConfigResultStreamingDistributionConfigLogging,
    )
    from .get_streaming_distribution_config_result_streaming_distribution_config_price_class import (
        GetStreamingDistributionConfigResultStreamingDistributionConfigPriceClass,
    )
    from .get_streaming_distribution_config_result_streaming_distribution_config_s3origin import (
        GetStreamingDistributionConfigResultStreamingDistributionConfigS3Origin,
    )
    from .get_streaming_distribution_config_result_streaming_distribution_config_trusted_signers import (
        GetStreamingDistributionConfigResultStreamingDistributionConfigTrustedSigners,
    )
    from .get_streaming_distribution_request import GetStreamingDistributionRequest
    from .get_streaming_distribution_result import GetStreamingDistributionResult
    from .get_streaming_distribution_result_streaming_distribution import (
        GetStreamingDistributionResultStreamingDistribution,
    )
    from .get_streaming_distribution_result_streaming_distribution_active_trusted_signers import (
        GetStreamingDistributionResultStreamingDistributionActiveTrustedSigners,
    )
    from .get_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item import (
        GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem,
    )
    from .get_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
        GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfig,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin,
    )
    from .get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers import (
        GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners,
    )
    from .header_list import HeaderList
    from .headers import Headers
    from .http_version import HttpVersion
    from .illegal_update import IllegalUpdate
    from .inconsistent_quantities import InconsistentQuantities
    from .integer import Integer
    from .invalid_argument import InvalidArgument
    from .invalid_default_root_object import InvalidDefaultRootObject
    from .invalid_error_code import InvalidErrorCode
    from .invalid_forward_cookies import InvalidForwardCookies
    from .invalid_geo_restriction_parameter import InvalidGeoRestrictionParameter
    from .invalid_headers_for_s3origin import InvalidHeadersForS3Origin
    from .invalid_if_match_version import InvalidIfMatchVersion
    from .invalid_lambda_function_association import InvalidLambdaFunctionAssociation
    from .invalid_location_code import InvalidLocationCode
    from .invalid_minimum_protocol_version import InvalidMinimumProtocolVersion
    from .invalid_origin import InvalidOrigin
    from .invalid_origin_access_identity import InvalidOriginAccessIdentity
    from .invalid_protocol_settings import InvalidProtocolSettings
    from .invalid_query_string_parameters import InvalidQueryStringParameters
    from .invalid_relative_path import InvalidRelativePath
    from .invalid_required_protocol import InvalidRequiredProtocol
    from .invalid_response_code import InvalidResponseCode
    from .invalid_tagging import InvalidTagging
    from .invalid_ttl_order import InvalidTtlOrder
    from .invalid_viewer_certificate import InvalidViewerCertificate
    from .invalid_web_acl_id import InvalidWebAclId
    from .invalidation import Invalidation
    from .invalidation_batch import InvalidationBatch
    from .invalidation_batch_paths import InvalidationBatchPaths
    from .invalidation_invalidation_batch import InvalidationInvalidationBatch
    from .invalidation_invalidation_batch_paths import InvalidationInvalidationBatchPaths
    from .invalidation_list import InvalidationList
    from .invalidation_list_items_item import InvalidationListItemsItem
    from .invalidation_summary import InvalidationSummary
    from .invalidation_summary_list import InvalidationSummaryList
    from .invalidation_summary_list_item import InvalidationSummaryListItem
    from .item_selection import ItemSelection
    from .key_pair_id_list import KeyPairIdList
    from .key_pair_ids import KeyPairIds
    from .lambda_function_association import LambdaFunctionAssociation
    from .lambda_function_association_event_type import LambdaFunctionAssociationEventType
    from .lambda_function_association_list import LambdaFunctionAssociationList
    from .lambda_function_association_list_item import LambdaFunctionAssociationListItem
    from .lambda_function_association_list_item_event_type import LambdaFunctionAssociationListItemEventType
    from .lambda_function_associations import LambdaFunctionAssociations
    from .lambda_function_associations_items_item import LambdaFunctionAssociationsItemsItem
    from .lambda_function_associations_items_item_event_type import LambdaFunctionAssociationsItemsItemEventType
    from .list_cloud_front_origin_access_identities_request import ListCloudFrontOriginAccessIdentitiesRequest
    from .list_cloud_front_origin_access_identities_result import ListCloudFrontOriginAccessIdentitiesResult
    from .list_cloud_front_origin_access_identities_result_cloud_front_origin_access_identity_list import (
        ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityList,
    )
    from .list_cloud_front_origin_access_identities_result_cloud_front_origin_access_identity_list_items_item import (
        ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityListItemsItem,
    )
    from .list_distributions_by_web_acl_id_request import ListDistributionsByWebAclIdRequest
    from .list_distributions_by_web_acl_id_result import ListDistributionsByWebAclIdResult
    from .list_distributions_by_web_acl_id_result_distribution_list import (
        ListDistributionsByWebAclIdResultDistributionList,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_aliases import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemAliases,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviors,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_trusted_signers import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_custom_error_responses import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponses,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_custom_error_responses_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponsesItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehavior,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_headers import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_trusted_signers import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_viewer_protocol_policy import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_http_version import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemHttpVersion,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOrigins,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_headers import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeaders,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_headers_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_s3origin_config import (
        ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemS3OriginConfig,
    )
    from .list_distributions_request import ListDistributionsRequest
    from .list_distributions_result import ListDistributionsResult
    from .list_distributions_result_distribution_list import ListDistributionsResultDistributionList
    from .list_distributions_result_distribution_list_items_item import ListDistributionsResultDistributionListItemsItem
    from .list_distributions_result_distribution_list_items_item_aliases import (
        ListDistributionsResultDistributionListItemsItemAliases,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviors,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_trusted_signers import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners,
    )
    from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy import (
        ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .list_distributions_result_distribution_list_items_item_custom_error_responses import (
        ListDistributionsResultDistributionListItemsItemCustomErrorResponses,
    )
    from .list_distributions_result_distribution_list_items_item_custom_error_responses_items_item import (
        ListDistributionsResultDistributionListItemsItemCustomErrorResponsesItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehavior,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_headers import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_trusted_signers import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners,
    )
    from .list_distributions_result_distribution_list_items_item_default_cache_behavior_viewer_protocol_policy import (
        ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .list_distributions_result_distribution_list_items_item_http_version import (
        ListDistributionsResultDistributionListItemsItemHttpVersion,
    )
    from .list_distributions_result_distribution_list_items_item_origins import (
        ListDistributionsResultDistributionListItemsItemOrigins,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_headers import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeaders,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_headers_items_item import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .list_distributions_result_distribution_list_items_item_origins_items_item_s3origin_config import (
        ListDistributionsResultDistributionListItemsItemOriginsItemsItemS3OriginConfig,
    )
    from .list_invalidations_request import ListInvalidationsRequest
    from .list_invalidations_result import ListInvalidationsResult
    from .list_invalidations_result_invalidation_list import ListInvalidationsResultInvalidationList
    from .list_invalidations_result_invalidation_list_items_item import ListInvalidationsResultInvalidationListItemsItem
    from .list_streaming_distributions_request import ListStreamingDistributionsRequest
    from .list_streaming_distributions_result import ListStreamingDistributionsResult
    from .list_streaming_distributions_result_streaming_distribution_list import (
        ListStreamingDistributionsResultStreamingDistributionList,
    )
    from .list_streaming_distributions_result_streaming_distribution_list_items_item import (
        ListStreamingDistributionsResultStreamingDistributionListItemsItem,
    )
    from .list_streaming_distributions_result_streaming_distribution_list_items_item_aliases import (
        ListStreamingDistributionsResultStreamingDistributionListItemsItemAliases,
    )
    from .list_streaming_distributions_result_streaming_distribution_list_items_item_s3origin import (
        ListStreamingDistributionsResultStreamingDistributionListItemsItemS3Origin,
    )
    from .list_streaming_distributions_result_streaming_distribution_list_items_item_trusted_signers import (
        ListStreamingDistributionsResultStreamingDistributionListItemsItemTrustedSigners,
    )
    from .list_tags_for_resource_request import ListTagsForResourceRequest
    from .list_tags_for_resource_result import ListTagsForResourceResult
    from .list_tags_for_resource_result_tags import ListTagsForResourceResultTags
    from .list_tags_for_resource_result_tags_items_item import ListTagsForResourceResultTagsItemsItem
    from .location_list import LocationList
    from .logging_config import LoggingConfig
    from .long_ import Long
    from .method import Method
    from .methods_list import MethodsList
    from .methods_list_item import MethodsListItem
    from .minimum_protocol_version import MinimumProtocolVersion
    from .missing_body import MissingBody
    from .no_such_cloud_front_origin_access_identity import NoSuchCloudFrontOriginAccessIdentity
    from .no_such_distribution import NoSuchDistribution
    from .no_such_invalidation import NoSuchInvalidation
    from .no_such_origin import NoSuchOrigin
    from .no_such_resource import NoSuchResource
    from .no_such_streaming_distribution import NoSuchStreamingDistribution
    from .origin import Origin
    from .origin_custom_header import OriginCustomHeader
    from .origin_custom_headers import OriginCustomHeaders
    from .origin_custom_headers_items_item import OriginCustomHeadersItemsItem
    from .origin_custom_headers_list import OriginCustomHeadersList
    from .origin_custom_headers_list_item import OriginCustomHeadersListItem
    from .origin_custom_origin_config import OriginCustomOriginConfig
    from .origin_custom_origin_config_origin_protocol_policy import OriginCustomOriginConfigOriginProtocolPolicy
    from .origin_custom_origin_config_origin_ssl_protocols import OriginCustomOriginConfigOriginSslProtocols
    from .origin_custom_origin_config_origin_ssl_protocols_items_item import (
        OriginCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .origin_list import OriginList
    from .origin_list_item import OriginListItem
    from .origin_list_item_custom_headers import OriginListItemCustomHeaders
    from .origin_list_item_custom_headers_items_item import OriginListItemCustomHeadersItemsItem
    from .origin_list_item_custom_origin_config import OriginListItemCustomOriginConfig
    from .origin_list_item_custom_origin_config_origin_protocol_policy import (
        OriginListItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .origin_list_item_custom_origin_config_origin_ssl_protocols import (
        OriginListItemCustomOriginConfigOriginSslProtocols,
    )
    from .origin_list_item_custom_origin_config_origin_ssl_protocols_items_item import (
        OriginListItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .origin_list_item_s3origin_config import OriginListItemS3OriginConfig
    from .origin_protocol_policy import OriginProtocolPolicy
    from .origin_s3origin_config import OriginS3OriginConfig
    from .origin_ssl_protocols import OriginSslProtocols
    from .origin_ssl_protocols_items_item import OriginSslProtocolsItemsItem
    from .origins import Origins
    from .origins_items_item import OriginsItemsItem
    from .origins_items_item_custom_headers import OriginsItemsItemCustomHeaders
    from .origins_items_item_custom_headers_items_item import OriginsItemsItemCustomHeadersItemsItem
    from .origins_items_item_custom_origin_config import OriginsItemsItemCustomOriginConfig
    from .origins_items_item_custom_origin_config_origin_protocol_policy import (
        OriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .origins_items_item_custom_origin_config_origin_ssl_protocols import (
        OriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        OriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .origins_items_item_s3origin_config import OriginsItemsItemS3OriginConfig
    from .path_list import PathList
    from .paths import Paths
    from .precondition_failed import PreconditionFailed
    from .price_class import PriceClass
    from .query_string_cache_keys import QueryStringCacheKeys
    from .query_string_cache_keys_list import QueryStringCacheKeysList
    from .resource_arn import ResourceArn
    from .restrictions import Restrictions
    from .s3origin import S3Origin
    from .s3origin_config import S3OriginConfig
    from .signer import Signer
    from .signer_key_pair_ids import SignerKeyPairIds
    from .signer_list import SignerList
    from .signer_list_item import SignerListItem
    from .signer_list_item_key_pair_ids import SignerListItemKeyPairIds
    from .ssl_protocol import SslProtocol
    from .ssl_protocols_list import SslProtocolsList
    from .ssl_protocols_list_item import SslProtocolsListItem
    from .ssl_support_method import SslSupportMethod
    from .streaming_distribution import StreamingDistribution
    from .streaming_distribution_active_trusted_signers import StreamingDistributionActiveTrustedSigners
    from .streaming_distribution_active_trusted_signers_items_item import (
        StreamingDistributionActiveTrustedSignersItemsItem,
    )
    from .streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
        StreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .streaming_distribution_already_exists import StreamingDistributionAlreadyExists
    from .streaming_distribution_config import StreamingDistributionConfig
    from .streaming_distribution_config_aliases import StreamingDistributionConfigAliases
    from .streaming_distribution_config_logging import StreamingDistributionConfigLogging
    from .streaming_distribution_config_price_class import StreamingDistributionConfigPriceClass
    from .streaming_distribution_config_s3origin import StreamingDistributionConfigS3Origin
    from .streaming_distribution_config_trusted_signers import StreamingDistributionConfigTrustedSigners
    from .streaming_distribution_config_with_tags import StreamingDistributionConfigWithTags
    from .streaming_distribution_config_with_tags_streaming_distribution_config import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfig,
    )
    from .streaming_distribution_config_with_tags_streaming_distribution_config_aliases import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfigAliases,
    )
    from .streaming_distribution_config_with_tags_streaming_distribution_config_logging import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfigLogging,
    )
    from .streaming_distribution_config_with_tags_streaming_distribution_config_price_class import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass,
    )
    from .streaming_distribution_config_with_tags_streaming_distribution_config_s3origin import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin,
    )
    from .streaming_distribution_config_with_tags_streaming_distribution_config_trusted_signers import (
        StreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners,
    )
    from .streaming_distribution_config_with_tags_tags import StreamingDistributionConfigWithTagsTags
    from .streaming_distribution_config_with_tags_tags_items_item import (
        StreamingDistributionConfigWithTagsTagsItemsItem,
    )
    from .streaming_distribution_list import StreamingDistributionList
    from .streaming_distribution_list_items_item import StreamingDistributionListItemsItem
    from .streaming_distribution_list_items_item_aliases import StreamingDistributionListItemsItemAliases
    from .streaming_distribution_list_items_item_s3origin import StreamingDistributionListItemsItemS3Origin
    from .streaming_distribution_list_items_item_trusted_signers import StreamingDistributionListItemsItemTrustedSigners
    from .streaming_distribution_not_disabled import StreamingDistributionNotDisabled
    from .streaming_distribution_streaming_distribution_config import StreamingDistributionStreamingDistributionConfig
    from .streaming_distribution_streaming_distribution_config_aliases import (
        StreamingDistributionStreamingDistributionConfigAliases,
    )
    from .streaming_distribution_streaming_distribution_config_logging import (
        StreamingDistributionStreamingDistributionConfigLogging,
    )
    from .streaming_distribution_streaming_distribution_config_price_class import (
        StreamingDistributionStreamingDistributionConfigPriceClass,
    )
    from .streaming_distribution_streaming_distribution_config_s3origin import (
        StreamingDistributionStreamingDistributionConfigS3Origin,
    )
    from .streaming_distribution_streaming_distribution_config_trusted_signers import (
        StreamingDistributionStreamingDistributionConfigTrustedSigners,
    )
    from .streaming_distribution_summary import StreamingDistributionSummary
    from .streaming_distribution_summary_aliases import StreamingDistributionSummaryAliases
    from .streaming_distribution_summary_list import StreamingDistributionSummaryList
    from .streaming_distribution_summary_list_item import StreamingDistributionSummaryListItem
    from .streaming_distribution_summary_list_item_aliases import StreamingDistributionSummaryListItemAliases
    from .streaming_distribution_summary_list_item_s3origin import StreamingDistributionSummaryListItemS3Origin
    from .streaming_distribution_summary_list_item_trusted_signers import (
        StreamingDistributionSummaryListItemTrustedSigners,
    )
    from .streaming_distribution_summary_s3origin import StreamingDistributionSummaryS3Origin
    from .streaming_distribution_summary_trusted_signers import StreamingDistributionSummaryTrustedSigners
    from .streaming_logging_config import StreamingLoggingConfig
    from .string import String
    from .tag import Tag
    from .tag_key import TagKey
    from .tag_key_list import TagKeyList
    from .tag_keys import TagKeys
    from .tag_list import TagList
    from .tag_list_item import TagListItem
    from .tag_resource20161125request_operation import TagResource20161125RequestOperation
    from .tag_resource_request import TagResourceRequest
    from .tag_resource_request_tags import TagResourceRequestTags
    from .tag_resource_request_tags_items_item import TagResourceRequestTagsItemsItem
    from .tag_value import TagValue
    from .tags import Tags
    from .tags_items_item import TagsItemsItem
    from .timestamp import Timestamp
    from .too_many_cache_behaviors import TooManyCacheBehaviors
    from .too_many_certificates import TooManyCertificates
    from .too_many_cloud_front_origin_access_identities import TooManyCloudFrontOriginAccessIdentities
    from .too_many_cookie_names_in_white_list import TooManyCookieNamesInWhiteList
    from .too_many_distribution_cnam_es import TooManyDistributionCnamEs
    from .too_many_distributions import TooManyDistributions
    from .too_many_distributions_with_lambda_associations import TooManyDistributionsWithLambdaAssociations
    from .too_many_headers_in_forwarded_values import TooManyHeadersInForwardedValues
    from .too_many_invalidations_in_progress import TooManyInvalidationsInProgress
    from .too_many_lambda_function_associations import TooManyLambdaFunctionAssociations
    from .too_many_origin_custom_headers import TooManyOriginCustomHeaders
    from .too_many_origins import TooManyOrigins
    from .too_many_query_string_parameters import TooManyQueryStringParameters
    from .too_many_streaming_distribution_cnam_es import TooManyStreamingDistributionCnamEs
    from .too_many_streaming_distributions import TooManyStreamingDistributions
    from .too_many_trusted_signers import TooManyTrustedSigners
    from .trusted_signer_does_not_exist import TrustedSignerDoesNotExist
    from .trusted_signers import TrustedSigners
    from .untag_resource20161125request_operation import UntagResource20161125RequestOperation
    from .untag_resource_request import UntagResourceRequest
    from .untag_resource_request_tag_keys import UntagResourceRequestTagKeys
    from .update_cloud_front_origin_access_identity_request import UpdateCloudFrontOriginAccessIdentityRequest
    from .update_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config import (
        UpdateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
    )
    from .update_cloud_front_origin_access_identity_result import UpdateCloudFrontOriginAccessIdentityResult
    from .update_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity import (
        UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity,
    )
    from .update_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config import (
        UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig,
    )
    from .update_distribution_request import UpdateDistributionRequest
    from .update_distribution_request_distribution_config import UpdateDistributionRequestDistributionConfig
    from .update_distribution_request_distribution_config_aliases import (
        UpdateDistributionRequestDistributionConfigAliases,
    )
    from .update_distribution_request_distribution_config_cache_behaviors import (
        UpdateDistributionRequestDistributionConfigCacheBehaviors,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItem,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_trusted_signers import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .update_distribution_request_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .update_distribution_request_distribution_config_custom_error_responses import (
        UpdateDistributionRequestDistributionConfigCustomErrorResponses,
    )
    from .update_distribution_request_distribution_config_custom_error_responses_items_item import (
        UpdateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehavior,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_headers import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_trusted_signers import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .update_distribution_request_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .update_distribution_request_distribution_config_http_version import (
        UpdateDistributionRequestDistributionConfigHttpVersion,
    )
    from .update_distribution_request_distribution_config_logging import (
        UpdateDistributionRequestDistributionConfigLogging,
    )
    from .update_distribution_request_distribution_config_origins import (
        UpdateDistributionRequestDistributionConfigOrigins,
    )
    from .update_distribution_request_distribution_config_origins_items_item import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItem,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_headers import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_headers_items_item import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_origin_config import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .update_distribution_request_distribution_config_origins_items_item_s3origin_config import (
        UpdateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .update_distribution_request_distribution_config_price_class import (
        UpdateDistributionRequestDistributionConfigPriceClass,
    )
    from .update_distribution_result import UpdateDistributionResult
    from .update_distribution_result_distribution import UpdateDistributionResultDistribution
    from .update_distribution_result_distribution_active_trusted_signers import (
        UpdateDistributionResultDistributionActiveTrustedSigners,
    )
    from .update_distribution_result_distribution_active_trusted_signers_items_item import (
        UpdateDistributionResultDistributionActiveTrustedSignersItemsItem,
    )
    from .update_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids import (
        UpdateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .update_distribution_result_distribution_distribution_config import (
        UpdateDistributionResultDistributionDistributionConfig,
    )
    from .update_distribution_result_distribution_distribution_config_aliases import (
        UpdateDistributionResultDistributionDistributionConfigAliases,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviors,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
    )
    from .update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
        UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
    )
    from .update_distribution_result_distribution_distribution_config_custom_error_responses import (
        UpdateDistributionResultDistributionDistributionConfigCustomErrorResponses,
    )
    from .update_distribution_result_distribution_distribution_config_custom_error_responses_items_item import (
        UpdateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehavior,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners,
    )
    from .update_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy import (
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy,
    )
    from .update_distribution_result_distribution_distribution_config_http_version import (
        UpdateDistributionResultDistributionDistributionConfigHttpVersion,
    )
    from .update_distribution_result_distribution_distribution_config_logging import (
        UpdateDistributionResultDistributionDistributionConfigLogging,
    )
    from .update_distribution_result_distribution_distribution_config_origins import (
        UpdateDistributionResultDistributionDistributionConfigOrigins,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_headers import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem,
    )
    from .update_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config import (
        UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig,
    )
    from .update_distribution_result_distribution_distribution_config_price_class import (
        UpdateDistributionResultDistributionDistributionConfigPriceClass,
    )
    from .update_streaming_distribution_request import UpdateStreamingDistributionRequest
    from .update_streaming_distribution_request_streaming_distribution_config import (
        UpdateStreamingDistributionRequestStreamingDistributionConfig,
    )
    from .update_streaming_distribution_request_streaming_distribution_config_aliases import (
        UpdateStreamingDistributionRequestStreamingDistributionConfigAliases,
    )
    from .update_streaming_distribution_request_streaming_distribution_config_logging import (
        UpdateStreamingDistributionRequestStreamingDistributionConfigLogging,
    )
    from .update_streaming_distribution_request_streaming_distribution_config_price_class import (
        UpdateStreamingDistributionRequestStreamingDistributionConfigPriceClass,
    )
    from .update_streaming_distribution_request_streaming_distribution_config_s3origin import (
        UpdateStreamingDistributionRequestStreamingDistributionConfigS3Origin,
    )
    from .update_streaming_distribution_request_streaming_distribution_config_trusted_signers import (
        UpdateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners,
    )
    from .update_streaming_distribution_result import UpdateStreamingDistributionResult
    from .update_streaming_distribution_result_streaming_distribution import (
        UpdateStreamingDistributionResultStreamingDistribution,
    )
    from .update_streaming_distribution_result_streaming_distribution_active_trusted_signers import (
        UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSigners,
    )
    from .update_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item import (
        UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem,
    )
    from .update_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
        UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin,
    )
    from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers import (
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners,
    )
    from .viewer_certificate import ViewerCertificate
    from .viewer_certificate_certificate_source import ViewerCertificateCertificateSource
    from .viewer_certificate_minimum_protocol_version import ViewerCertificateMinimumProtocolVersion
    from .viewer_certificate_ssl_support_method import ViewerCertificateSslSupportMethod
    from .viewer_protocol_policy import ViewerProtocolPolicy
_dynamic_imports: typing.Dict[str, str] = {
    "AccessDenied": ".access_denied",
    "ActiveTrustedSigners": ".active_trusted_signers",
    "ActiveTrustedSignersItemsItem": ".active_trusted_signers_items_item",
    "ActiveTrustedSignersItemsItemKeyPairIds": ".active_trusted_signers_items_item_key_pair_ids",
    "AliasList": ".alias_list",
    "Aliases": ".aliases",
    "AllowedMethods": ".allowed_methods",
    "AllowedMethodsItemsItem": ".allowed_methods_items_item",
    "AwsAccountNumberList": ".aws_account_number_list",
    "BatchTooLarge": ".batch_too_large",
    "Boolean": ".boolean",
    "CacheBehavior": ".cache_behavior",
    "CacheBehaviorForwardedValues": ".cache_behavior_forwarded_values",
    "CacheBehaviorForwardedValuesCookies": ".cache_behavior_forwarded_values_cookies",
    "CacheBehaviorForwardedValuesCookiesForward": ".cache_behavior_forwarded_values_cookies_forward",
    "CacheBehaviorForwardedValuesCookiesWhitelistedNames": ".cache_behavior_forwarded_values_cookies_whitelisted_names",
    "CacheBehaviorForwardedValuesHeaders": ".cache_behavior_forwarded_values_headers",
    "CacheBehaviorForwardedValuesQueryStringCacheKeys": ".cache_behavior_forwarded_values_query_string_cache_keys",
    "CacheBehaviorLambdaFunctionAssociations": ".cache_behavior_lambda_function_associations",
    "CacheBehaviorLambdaFunctionAssociationsItemsItem": ".cache_behavior_lambda_function_associations_items_item",
    "CacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".cache_behavior_lambda_function_associations_items_item_event_type",
    "CacheBehaviorList": ".cache_behavior_list",
    "CacheBehaviorListItem": ".cache_behavior_list_item",
    "CacheBehaviorListItemForwardedValues": ".cache_behavior_list_item_forwarded_values",
    "CacheBehaviorListItemForwardedValuesCookies": ".cache_behavior_list_item_forwarded_values_cookies",
    "CacheBehaviorListItemForwardedValuesCookiesForward": ".cache_behavior_list_item_forwarded_values_cookies_forward",
    "CacheBehaviorListItemForwardedValuesCookiesWhitelistedNames": ".cache_behavior_list_item_forwarded_values_cookies_whitelisted_names",
    "CacheBehaviorListItemForwardedValuesHeaders": ".cache_behavior_list_item_forwarded_values_headers",
    "CacheBehaviorListItemForwardedValuesQueryStringCacheKeys": ".cache_behavior_list_item_forwarded_values_query_string_cache_keys",
    "CacheBehaviorListItemLambdaFunctionAssociations": ".cache_behavior_list_item_lambda_function_associations",
    "CacheBehaviorListItemLambdaFunctionAssociationsItemsItem": ".cache_behavior_list_item_lambda_function_associations_items_item",
    "CacheBehaviorListItemLambdaFunctionAssociationsItemsItemEventType": ".cache_behavior_list_item_lambda_function_associations_items_item_event_type",
    "CacheBehaviorListItemTrustedSigners": ".cache_behavior_list_item_trusted_signers",
    "CacheBehaviorListItemViewerProtocolPolicy": ".cache_behavior_list_item_viewer_protocol_policy",
    "CacheBehaviorTrustedSigners": ".cache_behavior_trusted_signers",
    "CacheBehaviorViewerProtocolPolicy": ".cache_behavior_viewer_protocol_policy",
    "CacheBehaviors": ".cache_behaviors",
    "CacheBehaviorsItemsItem": ".cache_behaviors_items_item",
    "CacheBehaviorsItemsItemForwardedValues": ".cache_behaviors_items_item_forwarded_values",
    "CacheBehaviorsItemsItemForwardedValuesCookies": ".cache_behaviors_items_item_forwarded_values_cookies",
    "CacheBehaviorsItemsItemForwardedValuesCookiesForward": ".cache_behaviors_items_item_forwarded_values_cookies_forward",
    "CacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "CacheBehaviorsItemsItemForwardedValuesHeaders": ".cache_behaviors_items_item_forwarded_values_headers",
    "CacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "CacheBehaviorsItemsItemLambdaFunctionAssociations": ".cache_behaviors_items_item_lambda_function_associations",
    "CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".cache_behaviors_items_item_lambda_function_associations_items_item",
    "CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "CacheBehaviorsItemsItemTrustedSigners": ".cache_behaviors_items_item_trusted_signers",
    "CacheBehaviorsItemsItemViewerProtocolPolicy": ".cache_behaviors_items_item_viewer_protocol_policy",
    "CachedMethods": ".cached_methods",
    "CachedMethodsItemsItem": ".cached_methods_items_item",
    "CertificateSource": ".certificate_source",
    "CloudFrontOriginAccessIdentity": ".cloud_front_origin_access_identity",
    "CloudFrontOriginAccessIdentityAlreadyExists": ".cloud_front_origin_access_identity_already_exists",
    "CloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig": ".cloud_front_origin_access_identity_cloud_front_origin_access_identity_config",
    "CloudFrontOriginAccessIdentityConfig": ".cloud_front_origin_access_identity_config",
    "CloudFrontOriginAccessIdentityInUse": ".cloud_front_origin_access_identity_in_use",
    "CloudFrontOriginAccessIdentityList": ".cloud_front_origin_access_identity_list",
    "CloudFrontOriginAccessIdentityListItemsItem": ".cloud_front_origin_access_identity_list_items_item",
    "CloudFrontOriginAccessIdentitySummary": ".cloud_front_origin_access_identity_summary",
    "CloudFrontOriginAccessIdentitySummaryList": ".cloud_front_origin_access_identity_summary_list",
    "CloudFrontOriginAccessIdentitySummaryListItem": ".cloud_front_origin_access_identity_summary_list_item",
    "CnameAlreadyExists": ".cname_already_exists",
    "CookieNameList": ".cookie_name_list",
    "CookieNames": ".cookie_names",
    "CookiePreference": ".cookie_preference",
    "CookiePreferenceForward": ".cookie_preference_forward",
    "CookiePreferenceWhitelistedNames": ".cookie_preference_whitelisted_names",
    "CreateCloudFrontOriginAccessIdentityRequest": ".create_cloud_front_origin_access_identity_request",
    "CreateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig": ".create_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config",
    "CreateCloudFrontOriginAccessIdentityResult": ".create_cloud_front_origin_access_identity_result",
    "CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity": ".create_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity",
    "CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig": ".create_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config",
    "CreateDistributionRequest": ".create_distribution_request",
    "CreateDistributionRequestDistributionConfig": ".create_distribution_request_distribution_config",
    "CreateDistributionRequestDistributionConfigAliases": ".create_distribution_request_distribution_config_aliases",
    "CreateDistributionRequestDistributionConfigCacheBehaviors": ".create_distribution_request_distribution_config_cache_behaviors",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem": ".create_distribution_request_distribution_config_cache_behaviors_items_item",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".create_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".create_distribution_request_distribution_config_cache_behaviors_items_item_trusted_signers",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".create_distribution_request_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "CreateDistributionRequestDistributionConfigCustomErrorResponses": ".create_distribution_request_distribution_config_custom_error_responses",
    "CreateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem": ".create_distribution_request_distribution_config_custom_error_responses_items_item",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehavior": ".create_distribution_request_distribution_config_default_cache_behavior",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_headers",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".create_distribution_request_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners": ".create_distribution_request_distribution_config_default_cache_behavior_trusted_signers",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".create_distribution_request_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "CreateDistributionRequestDistributionConfigHttpVersion": ".create_distribution_request_distribution_config_http_version",
    "CreateDistributionRequestDistributionConfigLogging": ".create_distribution_request_distribution_config_logging",
    "CreateDistributionRequestDistributionConfigOrigins": ".create_distribution_request_distribution_config_origins",
    "CreateDistributionRequestDistributionConfigOriginsItemsItem": ".create_distribution_request_distribution_config_origins_items_item",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders": ".create_distribution_request_distribution_config_origins_items_item_custom_headers",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".create_distribution_request_distribution_config_origins_items_item_custom_headers_items_item",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig": ".create_distribution_request_distribution_config_origins_items_item_custom_origin_config",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".create_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig": ".create_distribution_request_distribution_config_origins_items_item_s3origin_config",
    "CreateDistributionRequestDistributionConfigPriceClass": ".create_distribution_request_distribution_config_price_class",
    "CreateDistributionResult": ".create_distribution_result",
    "CreateDistributionResultDistribution": ".create_distribution_result_distribution",
    "CreateDistributionResultDistributionActiveTrustedSigners": ".create_distribution_result_distribution_active_trusted_signers",
    "CreateDistributionResultDistributionActiveTrustedSignersItemsItem": ".create_distribution_result_distribution_active_trusted_signers_items_item",
    "CreateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds": ".create_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids",
    "CreateDistributionResultDistributionDistributionConfig": ".create_distribution_result_distribution_distribution_config",
    "CreateDistributionResultDistributionDistributionConfigAliases": ".create_distribution_result_distribution_distribution_config_aliases",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviors": ".create_distribution_result_distribution_distribution_config_cache_behaviors",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".create_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "CreateDistributionResultDistributionDistributionConfigCustomErrorResponses": ".create_distribution_result_distribution_distribution_config_custom_error_responses",
    "CreateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem": ".create_distribution_result_distribution_distribution_config_custom_error_responses_items_item",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehavior": ".create_distribution_result_distribution_distribution_config_default_cache_behavior",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".create_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "CreateDistributionResultDistributionDistributionConfigHttpVersion": ".create_distribution_result_distribution_distribution_config_http_version",
    "CreateDistributionResultDistributionDistributionConfigLogging": ".create_distribution_result_distribution_distribution_config_logging",
    "CreateDistributionResultDistributionDistributionConfigOrigins": ".create_distribution_result_distribution_distribution_config_origins",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItem": ".create_distribution_result_distribution_distribution_config_origins_items_item",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_headers",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".create_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig": ".create_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config",
    "CreateDistributionResultDistributionDistributionConfigPriceClass": ".create_distribution_result_distribution_distribution_config_price_class",
    "CreateDistributionWithTagsRequest": ".create_distribution_with_tags_request",
    "CreateDistributionWithTagsRequestDistributionConfigWithTags": ".create_distribution_with_tags_request_distribution_config_with_tags",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfig": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigAliases": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_aliases",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviors": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_trusted_signers",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponses": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_custom_error_responses",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_custom_error_responses_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehavior": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_headers",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_trusted_signers",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigHttpVersion": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_http_version",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigLogging": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_logging",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOrigins": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_headers",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_headers_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_origins_items_item_s3origin_config",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigPriceClass": ".create_distribution_with_tags_request_distribution_config_with_tags_distribution_config_price_class",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsTags": ".create_distribution_with_tags_request_distribution_config_with_tags_tags",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsTagsItemsItem": ".create_distribution_with_tags_request_distribution_config_with_tags_tags_items_item",
    "CreateDistributionWithTagsResult": ".create_distribution_with_tags_result",
    "CreateDistributionWithTagsResultDistribution": ".create_distribution_with_tags_result_distribution",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSigners": ".create_distribution_with_tags_result_distribution_active_trusted_signers",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItem": ".create_distribution_with_tags_result_distribution_active_trusted_signers_items_item",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItemKeyPairIds": ".create_distribution_with_tags_result_distribution_active_trusted_signers_items_item_key_pair_ids",
    "CreateDistributionWithTagsResultDistributionDistributionConfig": ".create_distribution_with_tags_result_distribution_distribution_config",
    "CreateDistributionWithTagsResultDistributionDistributionConfigAliases": ".create_distribution_with_tags_result_distribution_distribution_config_aliases",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviors": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".create_distribution_with_tags_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponses": ".create_distribution_with_tags_result_distribution_distribution_config_custom_error_responses",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponsesItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_custom_error_responses_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehavior": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_trusted_signers",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".create_distribution_with_tags_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigHttpVersion": ".create_distribution_with_tags_result_distribution_distribution_config_http_version",
    "CreateDistributionWithTagsResultDistributionDistributionConfigLogging": ".create_distribution_with_tags_result_distribution_distribution_config_logging",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOrigins": ".create_distribution_with_tags_result_distribution_distribution_config_origins",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeaders": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_headers",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_headers_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig": ".create_distribution_with_tags_result_distribution_distribution_config_origins_items_item_s3origin_config",
    "CreateDistributionWithTagsResultDistributionDistributionConfigPriceClass": ".create_distribution_with_tags_result_distribution_distribution_config_price_class",
    "CreateInvalidationRequest": ".create_invalidation_request",
    "CreateInvalidationRequestInvalidationBatch": ".create_invalidation_request_invalidation_batch",
    "CreateInvalidationRequestInvalidationBatchPaths": ".create_invalidation_request_invalidation_batch_paths",
    "CreateInvalidationResult": ".create_invalidation_result",
    "CreateInvalidationResultInvalidation": ".create_invalidation_result_invalidation",
    "CreateInvalidationResultInvalidationInvalidationBatch": ".create_invalidation_result_invalidation_invalidation_batch",
    "CreateInvalidationResultInvalidationInvalidationBatchPaths": ".create_invalidation_result_invalidation_invalidation_batch_paths",
    "CreateStreamingDistributionRequest": ".create_streaming_distribution_request",
    "CreateStreamingDistributionRequestStreamingDistributionConfig": ".create_streaming_distribution_request_streaming_distribution_config",
    "CreateStreamingDistributionRequestStreamingDistributionConfigAliases": ".create_streaming_distribution_request_streaming_distribution_config_aliases",
    "CreateStreamingDistributionRequestStreamingDistributionConfigLogging": ".create_streaming_distribution_request_streaming_distribution_config_logging",
    "CreateStreamingDistributionRequestStreamingDistributionConfigPriceClass": ".create_streaming_distribution_request_streaming_distribution_config_price_class",
    "CreateStreamingDistributionRequestStreamingDistributionConfigS3Origin": ".create_streaming_distribution_request_streaming_distribution_config_s3origin",
    "CreateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners": ".create_streaming_distribution_request_streaming_distribution_config_trusted_signers",
    "CreateStreamingDistributionResult": ".create_streaming_distribution_result",
    "CreateStreamingDistributionResultStreamingDistribution": ".create_streaming_distribution_result_streaming_distribution",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSigners": ".create_streaming_distribution_result_streaming_distribution_active_trusted_signers",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem": ".create_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds": ".create_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners": ".create_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers",
    "CreateStreamingDistributionWithTagsRequest": ".create_streaming_distribution_with_tags_request",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfig": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigAliases": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_aliases",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigLogging": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_logging",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_price_class",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_s3origin",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config_trusted_signers",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTags": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_tags",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTagsItemsItem": ".create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_tags_items_item",
    "CreateStreamingDistributionWithTagsResult": ".create_streaming_distribution_with_tags_result",
    "CreateStreamingDistributionWithTagsResultStreamingDistribution": ".create_streaming_distribution_with_tags_result_streaming_distribution",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSigners": ".create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem": ".create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers_items_item",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds": ".create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfig": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigAliases": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_aliases",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigLogging": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_logging",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigPriceClass": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_price_class",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigS3Origin": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_s3origin",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigTrustedSigners": ".create_streaming_distribution_with_tags_result_streaming_distribution_streaming_distribution_config_trusted_signers",
    "CustomErrorResponse": ".custom_error_response",
    "CustomErrorResponseList": ".custom_error_response_list",
    "CustomErrorResponseListItem": ".custom_error_response_list_item",
    "CustomErrorResponses": ".custom_error_responses",
    "CustomErrorResponsesItemsItem": ".custom_error_responses_items_item",
    "CustomHeaders": ".custom_headers",
    "CustomHeadersItemsItem": ".custom_headers_items_item",
    "CustomOriginConfig": ".custom_origin_config",
    "CustomOriginConfigOriginProtocolPolicy": ".custom_origin_config_origin_protocol_policy",
    "CustomOriginConfigOriginSslProtocols": ".custom_origin_config_origin_ssl_protocols",
    "CustomOriginConfigOriginSslProtocolsItemsItem": ".custom_origin_config_origin_ssl_protocols_items_item",
    "DefaultCacheBehavior": ".default_cache_behavior",
    "DefaultCacheBehaviorForwardedValues": ".default_cache_behavior_forwarded_values",
    "DefaultCacheBehaviorForwardedValuesCookies": ".default_cache_behavior_forwarded_values_cookies",
    "DefaultCacheBehaviorForwardedValuesCookiesForward": ".default_cache_behavior_forwarded_values_cookies_forward",
    "DefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DefaultCacheBehaviorForwardedValuesHeaders": ".default_cache_behavior_forwarded_values_headers",
    "DefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DefaultCacheBehaviorLambdaFunctionAssociations": ".default_cache_behavior_lambda_function_associations",
    "DefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".default_cache_behavior_lambda_function_associations_items_item",
    "DefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DefaultCacheBehaviorTrustedSigners": ".default_cache_behavior_trusted_signers",
    "DefaultCacheBehaviorViewerProtocolPolicy": ".default_cache_behavior_viewer_protocol_policy",
    "DeleteCloudFrontOriginAccessIdentityRequest": ".delete_cloud_front_origin_access_identity_request",
    "DeleteDistributionRequest": ".delete_distribution_request",
    "DeleteStreamingDistributionRequest": ".delete_streaming_distribution_request",
    "Distribution": ".distribution",
    "DistributionActiveTrustedSigners": ".distribution_active_trusted_signers",
    "DistributionActiveTrustedSignersItemsItem": ".distribution_active_trusted_signers_items_item",
    "DistributionActiveTrustedSignersItemsItemKeyPairIds": ".distribution_active_trusted_signers_items_item_key_pair_ids",
    "DistributionAlreadyExists": ".distribution_already_exists",
    "DistributionConfig": ".distribution_config",
    "DistributionConfigAliases": ".distribution_config_aliases",
    "DistributionConfigCacheBehaviors": ".distribution_config_cache_behaviors",
    "DistributionConfigCacheBehaviorsItemsItem": ".distribution_config_cache_behaviors_items_item",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValues": ".distribution_config_cache_behaviors_items_item_forwarded_values",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".distribution_config_cache_behaviors_items_item_trusted_signers",
    "DistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionConfigCustomErrorResponses": ".distribution_config_custom_error_responses",
    "DistributionConfigCustomErrorResponsesItemsItem": ".distribution_config_custom_error_responses_items_item",
    "DistributionConfigDefaultCacheBehavior": ".distribution_config_default_cache_behavior",
    "DistributionConfigDefaultCacheBehaviorForwardedValues": ".distribution_config_default_cache_behavior_forwarded_values",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".distribution_config_default_cache_behavior_forwarded_values_cookies",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_config_default_cache_behavior_forwarded_values_headers",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_config_default_cache_behavior_lambda_function_associations",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionConfigDefaultCacheBehaviorTrustedSigners": ".distribution_config_default_cache_behavior_trusted_signers",
    "DistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_config_default_cache_behavior_viewer_protocol_policy",
    "DistributionConfigHttpVersion": ".distribution_config_http_version",
    "DistributionConfigLogging": ".distribution_config_logging",
    "DistributionConfigOrigins": ".distribution_config_origins",
    "DistributionConfigOriginsItemsItem": ".distribution_config_origins_items_item",
    "DistributionConfigOriginsItemsItemCustomHeaders": ".distribution_config_origins_items_item_custom_headers",
    "DistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".distribution_config_origins_items_item_custom_headers_items_item",
    "DistributionConfigOriginsItemsItemCustomOriginConfig": ".distribution_config_origins_items_item_custom_origin_config",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionConfigOriginsItemsItemS3OriginConfig": ".distribution_config_origins_items_item_s3origin_config",
    "DistributionConfigPriceClass": ".distribution_config_price_class",
    "DistributionConfigWithTags": ".distribution_config_with_tags",
    "DistributionConfigWithTagsDistributionConfig": ".distribution_config_with_tags_distribution_config",
    "DistributionConfigWithTagsDistributionConfigAliases": ".distribution_config_with_tags_distribution_config_aliases",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviors": ".distribution_config_with_tags_distribution_config_cache_behaviors",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_trusted_signers",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_config_with_tags_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionConfigWithTagsDistributionConfigCustomErrorResponses": ".distribution_config_with_tags_distribution_config_custom_error_responses",
    "DistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem": ".distribution_config_with_tags_distribution_config_custom_error_responses_items_item",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehavior": ".distribution_config_with_tags_distribution_config_default_cache_behavior",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_headers",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_config_with_tags_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_config_with_tags_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners": ".distribution_config_with_tags_distribution_config_default_cache_behavior_trusted_signers",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_config_with_tags_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "DistributionConfigWithTagsDistributionConfigHttpVersion": ".distribution_config_with_tags_distribution_config_http_version",
    "DistributionConfigWithTagsDistributionConfigLogging": ".distribution_config_with_tags_distribution_config_logging",
    "DistributionConfigWithTagsDistributionConfigOrigins": ".distribution_config_with_tags_distribution_config_origins",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItem": ".distribution_config_with_tags_distribution_config_origins_items_item",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_headers",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_headers_items_item",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_config_with_tags_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig": ".distribution_config_with_tags_distribution_config_origins_items_item_s3origin_config",
    "DistributionConfigWithTagsDistributionConfigPriceClass": ".distribution_config_with_tags_distribution_config_price_class",
    "DistributionConfigWithTagsTags": ".distribution_config_with_tags_tags",
    "DistributionConfigWithTagsTagsItemsItem": ".distribution_config_with_tags_tags_items_item",
    "DistributionDistributionConfig": ".distribution_distribution_config",
    "DistributionDistributionConfigAliases": ".distribution_distribution_config_aliases",
    "DistributionDistributionConfigCacheBehaviors": ".distribution_distribution_config_cache_behaviors",
    "DistributionDistributionConfigCacheBehaviorsItemsItem": ".distribution_distribution_config_cache_behaviors_items_item",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".distribution_distribution_config_cache_behaviors_items_item_trusted_signers",
    "DistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionDistributionConfigCustomErrorResponses": ".distribution_distribution_config_custom_error_responses",
    "DistributionDistributionConfigCustomErrorResponsesItemsItem": ".distribution_distribution_config_custom_error_responses_items_item",
    "DistributionDistributionConfigDefaultCacheBehavior": ".distribution_distribution_config_default_cache_behavior",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValues": ".distribution_distribution_config_default_cache_behavior_forwarded_values",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".distribution_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_distribution_config_default_cache_behavior_forwarded_values_headers",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_distribution_config_default_cache_behavior_lambda_function_associations",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionDistributionConfigDefaultCacheBehaviorTrustedSigners": ".distribution_distribution_config_default_cache_behavior_trusted_signers",
    "DistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "DistributionDistributionConfigHttpVersion": ".distribution_distribution_config_http_version",
    "DistributionDistributionConfigLogging": ".distribution_distribution_config_logging",
    "DistributionDistributionConfigOrigins": ".distribution_distribution_config_origins",
    "DistributionDistributionConfigOriginsItemsItem": ".distribution_distribution_config_origins_items_item",
    "DistributionDistributionConfigOriginsItemsItemCustomHeaders": ".distribution_distribution_config_origins_items_item_custom_headers",
    "DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".distribution_distribution_config_origins_items_item_custom_headers_items_item",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfig": ".distribution_distribution_config_origins_items_item_custom_origin_config",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionDistributionConfigOriginsItemsItemS3OriginConfig": ".distribution_distribution_config_origins_items_item_s3origin_config",
    "DistributionDistributionConfigPriceClass": ".distribution_distribution_config_price_class",
    "DistributionList": ".distribution_list",
    "DistributionListItemsItem": ".distribution_list_items_item",
    "DistributionListItemsItemAliases": ".distribution_list_items_item_aliases",
    "DistributionListItemsItemCacheBehaviors": ".distribution_list_items_item_cache_behaviors",
    "DistributionListItemsItemCacheBehaviorsItemsItem": ".distribution_list_items_item_cache_behaviors_items_item",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValues": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners": ".distribution_list_items_item_cache_behaviors_items_item_trusted_signers",
    "DistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionListItemsItemCustomErrorResponses": ".distribution_list_items_item_custom_error_responses",
    "DistributionListItemsItemCustomErrorResponsesItemsItem": ".distribution_list_items_item_custom_error_responses_items_item",
    "DistributionListItemsItemDefaultCacheBehavior": ".distribution_list_items_item_default_cache_behavior",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValues": ".distribution_list_items_item_default_cache_behavior_forwarded_values",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies": ".distribution_list_items_item_default_cache_behavior_forwarded_values_cookies",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_list_items_item_default_cache_behavior_forwarded_values_headers",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_list_items_item_default_cache_behavior_lambda_function_associations",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionListItemsItemDefaultCacheBehaviorTrustedSigners": ".distribution_list_items_item_default_cache_behavior_trusted_signers",
    "DistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_list_items_item_default_cache_behavior_viewer_protocol_policy",
    "DistributionListItemsItemHttpVersion": ".distribution_list_items_item_http_version",
    "DistributionListItemsItemOrigins": ".distribution_list_items_item_origins",
    "DistributionListItemsItemOriginsItemsItem": ".distribution_list_items_item_origins_items_item",
    "DistributionListItemsItemOriginsItemsItemCustomHeaders": ".distribution_list_items_item_origins_items_item_custom_headers",
    "DistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem": ".distribution_list_items_item_origins_items_item_custom_headers_items_item",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfig": ".distribution_list_items_item_origins_items_item_custom_origin_config",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionListItemsItemOriginsItemsItemS3OriginConfig": ".distribution_list_items_item_origins_items_item_s3origin_config",
    "DistributionNotDisabled": ".distribution_not_disabled",
    "DistributionSummary": ".distribution_summary",
    "DistributionSummaryAliases": ".distribution_summary_aliases",
    "DistributionSummaryCacheBehaviors": ".distribution_summary_cache_behaviors",
    "DistributionSummaryCacheBehaviorsItemsItem": ".distribution_summary_cache_behaviors_items_item",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValues": ".distribution_summary_cache_behaviors_items_item_forwarded_values",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_summary_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_summary_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_summary_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_summary_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_summary_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_summary_cache_behaviors_items_item_lambda_function_associations",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_summary_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_summary_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionSummaryCacheBehaviorsItemsItemTrustedSigners": ".distribution_summary_cache_behaviors_items_item_trusted_signers",
    "DistributionSummaryCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_summary_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionSummaryCustomErrorResponses": ".distribution_summary_custom_error_responses",
    "DistributionSummaryCustomErrorResponsesItemsItem": ".distribution_summary_custom_error_responses_items_item",
    "DistributionSummaryDefaultCacheBehavior": ".distribution_summary_default_cache_behavior",
    "DistributionSummaryDefaultCacheBehaviorForwardedValues": ".distribution_summary_default_cache_behavior_forwarded_values",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookies": ".distribution_summary_default_cache_behavior_forwarded_values_cookies",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_summary_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_summary_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_summary_default_cache_behavior_forwarded_values_headers",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_summary_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_summary_default_cache_behavior_lambda_function_associations",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_summary_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_summary_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionSummaryDefaultCacheBehaviorTrustedSigners": ".distribution_summary_default_cache_behavior_trusted_signers",
    "DistributionSummaryDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_summary_default_cache_behavior_viewer_protocol_policy",
    "DistributionSummaryHttpVersion": ".distribution_summary_http_version",
    "DistributionSummaryList": ".distribution_summary_list",
    "DistributionSummaryListItem": ".distribution_summary_list_item",
    "DistributionSummaryListItemAliases": ".distribution_summary_list_item_aliases",
    "DistributionSummaryListItemCacheBehaviors": ".distribution_summary_list_item_cache_behaviors",
    "DistributionSummaryListItemCacheBehaviorsItemsItem": ".distribution_summary_list_item_cache_behaviors_items_item",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValues": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookies": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesHeaders": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_headers",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".distribution_summary_list_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociations": ".distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations_items_item",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".distribution_summary_list_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "DistributionSummaryListItemCacheBehaviorsItemsItemTrustedSigners": ".distribution_summary_list_item_cache_behaviors_items_item_trusted_signers",
    "DistributionSummaryListItemCacheBehaviorsItemsItemViewerProtocolPolicy": ".distribution_summary_list_item_cache_behaviors_items_item_viewer_protocol_policy",
    "DistributionSummaryListItemCustomErrorResponses": ".distribution_summary_list_item_custom_error_responses",
    "DistributionSummaryListItemCustomErrorResponsesItemsItem": ".distribution_summary_list_item_custom_error_responses_items_item",
    "DistributionSummaryListItemDefaultCacheBehavior": ".distribution_summary_list_item_default_cache_behavior",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValues": ".distribution_summary_list_item_default_cache_behavior_forwarded_values",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookies": ".distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesForward": ".distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies_forward",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".distribution_summary_list_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesHeaders": ".distribution_summary_list_item_default_cache_behavior_forwarded_values_headers",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".distribution_summary_list_item_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociations": ".distribution_summary_list_item_default_cache_behavior_lambda_function_associations",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".distribution_summary_list_item_default_cache_behavior_lambda_function_associations_items_item",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".distribution_summary_list_item_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "DistributionSummaryListItemDefaultCacheBehaviorTrustedSigners": ".distribution_summary_list_item_default_cache_behavior_trusted_signers",
    "DistributionSummaryListItemDefaultCacheBehaviorViewerProtocolPolicy": ".distribution_summary_list_item_default_cache_behavior_viewer_protocol_policy",
    "DistributionSummaryListItemHttpVersion": ".distribution_summary_list_item_http_version",
    "DistributionSummaryListItemOrigins": ".distribution_summary_list_item_origins",
    "DistributionSummaryListItemOriginsItemsItem": ".distribution_summary_list_item_origins_items_item",
    "DistributionSummaryListItemOriginsItemsItemCustomHeaders": ".distribution_summary_list_item_origins_items_item_custom_headers",
    "DistributionSummaryListItemOriginsItemsItemCustomHeadersItemsItem": ".distribution_summary_list_item_origins_items_item_custom_headers_items_item",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfig": ".distribution_summary_list_item_origins_items_item_custom_origin_config",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_summary_list_item_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_summary_list_item_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_summary_list_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionSummaryListItemOriginsItemsItemS3OriginConfig": ".distribution_summary_list_item_origins_items_item_s3origin_config",
    "DistributionSummaryOrigins": ".distribution_summary_origins",
    "DistributionSummaryOriginsItemsItem": ".distribution_summary_origins_items_item",
    "DistributionSummaryOriginsItemsItemCustomHeaders": ".distribution_summary_origins_items_item_custom_headers",
    "DistributionSummaryOriginsItemsItemCustomHeadersItemsItem": ".distribution_summary_origins_items_item_custom_headers_items_item",
    "DistributionSummaryOriginsItemsItemCustomOriginConfig": ".distribution_summary_origins_items_item_custom_origin_config",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".distribution_summary_origins_items_item_custom_origin_config_origin_protocol_policy",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".distribution_summary_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".distribution_summary_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "DistributionSummaryOriginsItemsItemS3OriginConfig": ".distribution_summary_origins_items_item_s3origin_config",
    "EventType": ".event_type",
    "ForwardedValues": ".forwarded_values",
    "ForwardedValuesCookies": ".forwarded_values_cookies",
    "ForwardedValuesCookiesForward": ".forwarded_values_cookies_forward",
    "ForwardedValuesCookiesWhitelistedNames": ".forwarded_values_cookies_whitelisted_names",
    "ForwardedValuesHeaders": ".forwarded_values_headers",
    "ForwardedValuesQueryStringCacheKeys": ".forwarded_values_query_string_cache_keys",
    "GeoRestriction": ".geo_restriction",
    "GeoRestrictionRestrictionType": ".geo_restriction_restriction_type",
    "GeoRestrictionType": ".geo_restriction_type",
    "GetCloudFrontOriginAccessIdentityConfigRequest": ".get_cloud_front_origin_access_identity_config_request",
    "GetCloudFrontOriginAccessIdentityConfigResult": ".get_cloud_front_origin_access_identity_config_result",
    "GetCloudFrontOriginAccessIdentityConfigResultCloudFrontOriginAccessIdentityConfig": ".get_cloud_front_origin_access_identity_config_result_cloud_front_origin_access_identity_config",
    "GetCloudFrontOriginAccessIdentityRequest": ".get_cloud_front_origin_access_identity_request",
    "GetCloudFrontOriginAccessIdentityResult": ".get_cloud_front_origin_access_identity_result",
    "GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity": ".get_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity",
    "GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig": ".get_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config",
    "GetDistributionConfigRequest": ".get_distribution_config_request",
    "GetDistributionConfigResult": ".get_distribution_config_result",
    "GetDistributionConfigResultDistributionConfig": ".get_distribution_config_result_distribution_config",
    "GetDistributionConfigResultDistributionConfigAliases": ".get_distribution_config_result_distribution_config_aliases",
    "GetDistributionConfigResultDistributionConfigCacheBehaviors": ".get_distribution_config_result_distribution_config_cache_behaviors",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItem": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_trusted_signers",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".get_distribution_config_result_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "GetDistributionConfigResultDistributionConfigCustomErrorResponses": ".get_distribution_config_result_distribution_config_custom_error_responses",
    "GetDistributionConfigResultDistributionConfigCustomErrorResponsesItemsItem": ".get_distribution_config_result_distribution_config_custom_error_responses_items_item",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehavior": ".get_distribution_config_result_distribution_config_default_cache_behavior",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValues": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_headers",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".get_distribution_config_result_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".get_distribution_config_result_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorTrustedSigners": ".get_distribution_config_result_distribution_config_default_cache_behavior_trusted_signers",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".get_distribution_config_result_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "GetDistributionConfigResultDistributionConfigHttpVersion": ".get_distribution_config_result_distribution_config_http_version",
    "GetDistributionConfigResultDistributionConfigLogging": ".get_distribution_config_result_distribution_config_logging",
    "GetDistributionConfigResultDistributionConfigOrigins": ".get_distribution_config_result_distribution_config_origins",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItem": ".get_distribution_config_result_distribution_config_origins_items_item",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeaders": ".get_distribution_config_result_distribution_config_origins_items_item_custom_headers",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".get_distribution_config_result_distribution_config_origins_items_item_custom_headers_items_item",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfig": ".get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".get_distribution_config_result_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemS3OriginConfig": ".get_distribution_config_result_distribution_config_origins_items_item_s3origin_config",
    "GetDistributionConfigResultDistributionConfigPriceClass": ".get_distribution_config_result_distribution_config_price_class",
    "GetDistributionRequest": ".get_distribution_request",
    "GetDistributionResult": ".get_distribution_result",
    "GetDistributionResultDistribution": ".get_distribution_result_distribution",
    "GetDistributionResultDistributionActiveTrustedSigners": ".get_distribution_result_distribution_active_trusted_signers",
    "GetDistributionResultDistributionActiveTrustedSignersItemsItem": ".get_distribution_result_distribution_active_trusted_signers_items_item",
    "GetDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds": ".get_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids",
    "GetDistributionResultDistributionDistributionConfig": ".get_distribution_result_distribution_distribution_config",
    "GetDistributionResultDistributionDistributionConfigAliases": ".get_distribution_result_distribution_distribution_config_aliases",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviors": ".get_distribution_result_distribution_distribution_config_cache_behaviors",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".get_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "GetDistributionResultDistributionDistributionConfigCustomErrorResponses": ".get_distribution_result_distribution_distribution_config_custom_error_responses",
    "GetDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem": ".get_distribution_result_distribution_distribution_config_custom_error_responses_items_item",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehavior": ".get_distribution_result_distribution_distribution_config_default_cache_behavior",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".get_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "GetDistributionResultDistributionDistributionConfigHttpVersion": ".get_distribution_result_distribution_distribution_config_http_version",
    "GetDistributionResultDistributionDistributionConfigLogging": ".get_distribution_result_distribution_distribution_config_logging",
    "GetDistributionResultDistributionDistributionConfigOrigins": ".get_distribution_result_distribution_distribution_config_origins",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItem": ".get_distribution_result_distribution_distribution_config_origins_items_item",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_headers",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".get_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig": ".get_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config",
    "GetDistributionResultDistributionDistributionConfigPriceClass": ".get_distribution_result_distribution_distribution_config_price_class",
    "GetInvalidationRequest": ".get_invalidation_request",
    "GetInvalidationResult": ".get_invalidation_result",
    "GetInvalidationResultInvalidation": ".get_invalidation_result_invalidation",
    "GetInvalidationResultInvalidationInvalidationBatch": ".get_invalidation_result_invalidation_invalidation_batch",
    "GetInvalidationResultInvalidationInvalidationBatchPaths": ".get_invalidation_result_invalidation_invalidation_batch_paths",
    "GetStreamingDistributionConfigRequest": ".get_streaming_distribution_config_request",
    "GetStreamingDistributionConfigResult": ".get_streaming_distribution_config_result",
    "GetStreamingDistributionConfigResultStreamingDistributionConfig": ".get_streaming_distribution_config_result_streaming_distribution_config",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigAliases": ".get_streaming_distribution_config_result_streaming_distribution_config_aliases",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigLogging": ".get_streaming_distribution_config_result_streaming_distribution_config_logging",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigPriceClass": ".get_streaming_distribution_config_result_streaming_distribution_config_price_class",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigS3Origin": ".get_streaming_distribution_config_result_streaming_distribution_config_s3origin",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigTrustedSigners": ".get_streaming_distribution_config_result_streaming_distribution_config_trusted_signers",
    "GetStreamingDistributionRequest": ".get_streaming_distribution_request",
    "GetStreamingDistributionResult": ".get_streaming_distribution_result",
    "GetStreamingDistributionResultStreamingDistribution": ".get_streaming_distribution_result_streaming_distribution",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSigners": ".get_streaming_distribution_result_streaming_distribution_active_trusted_signers",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem": ".get_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds": ".get_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfig": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners": ".get_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers",
    "HeaderList": ".header_list",
    "Headers": ".headers",
    "HttpVersion": ".http_version",
    "IllegalUpdate": ".illegal_update",
    "InconsistentQuantities": ".inconsistent_quantities",
    "Integer": ".integer",
    "InvalidArgument": ".invalid_argument",
    "InvalidDefaultRootObject": ".invalid_default_root_object",
    "InvalidErrorCode": ".invalid_error_code",
    "InvalidForwardCookies": ".invalid_forward_cookies",
    "InvalidGeoRestrictionParameter": ".invalid_geo_restriction_parameter",
    "InvalidHeadersForS3Origin": ".invalid_headers_for_s3origin",
    "InvalidIfMatchVersion": ".invalid_if_match_version",
    "InvalidLambdaFunctionAssociation": ".invalid_lambda_function_association",
    "InvalidLocationCode": ".invalid_location_code",
    "InvalidMinimumProtocolVersion": ".invalid_minimum_protocol_version",
    "InvalidOrigin": ".invalid_origin",
    "InvalidOriginAccessIdentity": ".invalid_origin_access_identity",
    "InvalidProtocolSettings": ".invalid_protocol_settings",
    "InvalidQueryStringParameters": ".invalid_query_string_parameters",
    "InvalidRelativePath": ".invalid_relative_path",
    "InvalidRequiredProtocol": ".invalid_required_protocol",
    "InvalidResponseCode": ".invalid_response_code",
    "InvalidTagging": ".invalid_tagging",
    "InvalidTtlOrder": ".invalid_ttl_order",
    "InvalidViewerCertificate": ".invalid_viewer_certificate",
    "InvalidWebAclId": ".invalid_web_acl_id",
    "Invalidation": ".invalidation",
    "InvalidationBatch": ".invalidation_batch",
    "InvalidationBatchPaths": ".invalidation_batch_paths",
    "InvalidationInvalidationBatch": ".invalidation_invalidation_batch",
    "InvalidationInvalidationBatchPaths": ".invalidation_invalidation_batch_paths",
    "InvalidationList": ".invalidation_list",
    "InvalidationListItemsItem": ".invalidation_list_items_item",
    "InvalidationSummary": ".invalidation_summary",
    "InvalidationSummaryList": ".invalidation_summary_list",
    "InvalidationSummaryListItem": ".invalidation_summary_list_item",
    "ItemSelection": ".item_selection",
    "KeyPairIdList": ".key_pair_id_list",
    "KeyPairIds": ".key_pair_ids",
    "LambdaFunctionAssociation": ".lambda_function_association",
    "LambdaFunctionAssociationEventType": ".lambda_function_association_event_type",
    "LambdaFunctionAssociationList": ".lambda_function_association_list",
    "LambdaFunctionAssociationListItem": ".lambda_function_association_list_item",
    "LambdaFunctionAssociationListItemEventType": ".lambda_function_association_list_item_event_type",
    "LambdaFunctionAssociations": ".lambda_function_associations",
    "LambdaFunctionAssociationsItemsItem": ".lambda_function_associations_items_item",
    "LambdaFunctionAssociationsItemsItemEventType": ".lambda_function_associations_items_item_event_type",
    "ListCloudFrontOriginAccessIdentitiesRequest": ".list_cloud_front_origin_access_identities_request",
    "ListCloudFrontOriginAccessIdentitiesResult": ".list_cloud_front_origin_access_identities_result",
    "ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityList": ".list_cloud_front_origin_access_identities_result_cloud_front_origin_access_identity_list",
    "ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityListItemsItem": ".list_cloud_front_origin_access_identities_result_cloud_front_origin_access_identity_list_items_item",
    "ListDistributionsByWebAclIdRequest": ".list_distributions_by_web_acl_id_request",
    "ListDistributionsByWebAclIdResult": ".list_distributions_by_web_acl_id_result",
    "ListDistributionsByWebAclIdResultDistributionList": ".list_distributions_by_web_acl_id_result_distribution_list",
    "ListDistributionsByWebAclIdResultDistributionListItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemAliases": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_aliases",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviors": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_trusted_signers",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponses": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_custom_error_responses",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponsesItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_custom_error_responses_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehavior": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_headers",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_trusted_signers",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_viewer_protocol_policy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemHttpVersion": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_http_version",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOrigins": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeaders": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_headers",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_headers_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemS3OriginConfig": ".list_distributions_by_web_acl_id_result_distribution_list_items_item_origins_items_item_s3origin_config",
    "ListDistributionsRequest": ".list_distributions_request",
    "ListDistributionsResult": ".list_distributions_result",
    "ListDistributionsResultDistributionList": ".list_distributions_result_distribution_list",
    "ListDistributionsResultDistributionListItemsItem": ".list_distributions_result_distribution_list_items_item",
    "ListDistributionsResultDistributionListItemsItemAliases": ".list_distributions_result_distribution_list_items_item_aliases",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviors": ".list_distributions_result_distribution_list_items_item_cache_behaviors",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItem": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_headers",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_trusted_signers",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy": ".list_distributions_result_distribution_list_items_item_cache_behaviors_items_item_viewer_protocol_policy",
    "ListDistributionsResultDistributionListItemsItemCustomErrorResponses": ".list_distributions_result_distribution_list_items_item_custom_error_responses",
    "ListDistributionsResultDistributionListItemsItemCustomErrorResponsesItemsItem": ".list_distributions_result_distribution_list_items_item_custom_error_responses_items_item",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehavior": ".list_distributions_result_distribution_list_items_item_default_cache_behavior",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_forward",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_headers",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_trusted_signers",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy": ".list_distributions_result_distribution_list_items_item_default_cache_behavior_viewer_protocol_policy",
    "ListDistributionsResultDistributionListItemsItemHttpVersion": ".list_distributions_result_distribution_list_items_item_http_version",
    "ListDistributionsResultDistributionListItemsItemOrigins": ".list_distributions_result_distribution_list_items_item_origins",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItem": ".list_distributions_result_distribution_list_items_item_origins_items_item",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeaders": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_headers",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_headers_items_item",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_protocol_policy",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".list_distributions_result_distribution_list_items_item_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemS3OriginConfig": ".list_distributions_result_distribution_list_items_item_origins_items_item_s3origin_config",
    "ListInvalidationsRequest": ".list_invalidations_request",
    "ListInvalidationsResult": ".list_invalidations_result",
    "ListInvalidationsResultInvalidationList": ".list_invalidations_result_invalidation_list",
    "ListInvalidationsResultInvalidationListItemsItem": ".list_invalidations_result_invalidation_list_items_item",
    "ListStreamingDistributionsRequest": ".list_streaming_distributions_request",
    "ListStreamingDistributionsResult": ".list_streaming_distributions_result",
    "ListStreamingDistributionsResultStreamingDistributionList": ".list_streaming_distributions_result_streaming_distribution_list",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItem": ".list_streaming_distributions_result_streaming_distribution_list_items_item",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemAliases": ".list_streaming_distributions_result_streaming_distribution_list_items_item_aliases",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemS3Origin": ".list_streaming_distributions_result_streaming_distribution_list_items_item_s3origin",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemTrustedSigners": ".list_streaming_distributions_result_streaming_distribution_list_items_item_trusted_signers",
    "ListTagsForResourceRequest": ".list_tags_for_resource_request",
    "ListTagsForResourceResult": ".list_tags_for_resource_result",
    "ListTagsForResourceResultTags": ".list_tags_for_resource_result_tags",
    "ListTagsForResourceResultTagsItemsItem": ".list_tags_for_resource_result_tags_items_item",
    "LocationList": ".location_list",
    "LoggingConfig": ".logging_config",
    "Long": ".long_",
    "Method": ".method",
    "MethodsList": ".methods_list",
    "MethodsListItem": ".methods_list_item",
    "MinimumProtocolVersion": ".minimum_protocol_version",
    "MissingBody": ".missing_body",
    "NoSuchCloudFrontOriginAccessIdentity": ".no_such_cloud_front_origin_access_identity",
    "NoSuchDistribution": ".no_such_distribution",
    "NoSuchInvalidation": ".no_such_invalidation",
    "NoSuchOrigin": ".no_such_origin",
    "NoSuchResource": ".no_such_resource",
    "NoSuchStreamingDistribution": ".no_such_streaming_distribution",
    "Origin": ".origin",
    "OriginCustomHeader": ".origin_custom_header",
    "OriginCustomHeaders": ".origin_custom_headers",
    "OriginCustomHeadersItemsItem": ".origin_custom_headers_items_item",
    "OriginCustomHeadersList": ".origin_custom_headers_list",
    "OriginCustomHeadersListItem": ".origin_custom_headers_list_item",
    "OriginCustomOriginConfig": ".origin_custom_origin_config",
    "OriginCustomOriginConfigOriginProtocolPolicy": ".origin_custom_origin_config_origin_protocol_policy",
    "OriginCustomOriginConfigOriginSslProtocols": ".origin_custom_origin_config_origin_ssl_protocols",
    "OriginCustomOriginConfigOriginSslProtocolsItemsItem": ".origin_custom_origin_config_origin_ssl_protocols_items_item",
    "OriginList": ".origin_list",
    "OriginListItem": ".origin_list_item",
    "OriginListItemCustomHeaders": ".origin_list_item_custom_headers",
    "OriginListItemCustomHeadersItemsItem": ".origin_list_item_custom_headers_items_item",
    "OriginListItemCustomOriginConfig": ".origin_list_item_custom_origin_config",
    "OriginListItemCustomOriginConfigOriginProtocolPolicy": ".origin_list_item_custom_origin_config_origin_protocol_policy",
    "OriginListItemCustomOriginConfigOriginSslProtocols": ".origin_list_item_custom_origin_config_origin_ssl_protocols",
    "OriginListItemCustomOriginConfigOriginSslProtocolsItemsItem": ".origin_list_item_custom_origin_config_origin_ssl_protocols_items_item",
    "OriginListItemS3OriginConfig": ".origin_list_item_s3origin_config",
    "OriginProtocolPolicy": ".origin_protocol_policy",
    "OriginS3OriginConfig": ".origin_s3origin_config",
    "OriginSslProtocols": ".origin_ssl_protocols",
    "OriginSslProtocolsItemsItem": ".origin_ssl_protocols_items_item",
    "Origins": ".origins",
    "OriginsItemsItem": ".origins_items_item",
    "OriginsItemsItemCustomHeaders": ".origins_items_item_custom_headers",
    "OriginsItemsItemCustomHeadersItemsItem": ".origins_items_item_custom_headers_items_item",
    "OriginsItemsItemCustomOriginConfig": ".origins_items_item_custom_origin_config",
    "OriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".origins_items_item_custom_origin_config_origin_protocol_policy",
    "OriginsItemsItemCustomOriginConfigOriginSslProtocols": ".origins_items_item_custom_origin_config_origin_ssl_protocols",
    "OriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "OriginsItemsItemS3OriginConfig": ".origins_items_item_s3origin_config",
    "PathList": ".path_list",
    "Paths": ".paths",
    "PreconditionFailed": ".precondition_failed",
    "PriceClass": ".price_class",
    "QueryStringCacheKeys": ".query_string_cache_keys",
    "QueryStringCacheKeysList": ".query_string_cache_keys_list",
    "ResourceArn": ".resource_arn",
    "Restrictions": ".restrictions",
    "S3Origin": ".s3origin",
    "S3OriginConfig": ".s3origin_config",
    "Signer": ".signer",
    "SignerKeyPairIds": ".signer_key_pair_ids",
    "SignerList": ".signer_list",
    "SignerListItem": ".signer_list_item",
    "SignerListItemKeyPairIds": ".signer_list_item_key_pair_ids",
    "SslProtocol": ".ssl_protocol",
    "SslProtocolsList": ".ssl_protocols_list",
    "SslProtocolsListItem": ".ssl_protocols_list_item",
    "SslSupportMethod": ".ssl_support_method",
    "StreamingDistribution": ".streaming_distribution",
    "StreamingDistributionActiveTrustedSigners": ".streaming_distribution_active_trusted_signers",
    "StreamingDistributionActiveTrustedSignersItemsItem": ".streaming_distribution_active_trusted_signers_items_item",
    "StreamingDistributionActiveTrustedSignersItemsItemKeyPairIds": ".streaming_distribution_active_trusted_signers_items_item_key_pair_ids",
    "StreamingDistributionAlreadyExists": ".streaming_distribution_already_exists",
    "StreamingDistributionConfig": ".streaming_distribution_config",
    "StreamingDistributionConfigAliases": ".streaming_distribution_config_aliases",
    "StreamingDistributionConfigLogging": ".streaming_distribution_config_logging",
    "StreamingDistributionConfigPriceClass": ".streaming_distribution_config_price_class",
    "StreamingDistributionConfigS3Origin": ".streaming_distribution_config_s3origin",
    "StreamingDistributionConfigTrustedSigners": ".streaming_distribution_config_trusted_signers",
    "StreamingDistributionConfigWithTags": ".streaming_distribution_config_with_tags",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfig": ".streaming_distribution_config_with_tags_streaming_distribution_config",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigAliases": ".streaming_distribution_config_with_tags_streaming_distribution_config_aliases",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigLogging": ".streaming_distribution_config_with_tags_streaming_distribution_config_logging",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass": ".streaming_distribution_config_with_tags_streaming_distribution_config_price_class",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin": ".streaming_distribution_config_with_tags_streaming_distribution_config_s3origin",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners": ".streaming_distribution_config_with_tags_streaming_distribution_config_trusted_signers",
    "StreamingDistributionConfigWithTagsTags": ".streaming_distribution_config_with_tags_tags",
    "StreamingDistributionConfigWithTagsTagsItemsItem": ".streaming_distribution_config_with_tags_tags_items_item",
    "StreamingDistributionList": ".streaming_distribution_list",
    "StreamingDistributionListItemsItem": ".streaming_distribution_list_items_item",
    "StreamingDistributionListItemsItemAliases": ".streaming_distribution_list_items_item_aliases",
    "StreamingDistributionListItemsItemS3Origin": ".streaming_distribution_list_items_item_s3origin",
    "StreamingDistributionListItemsItemTrustedSigners": ".streaming_distribution_list_items_item_trusted_signers",
    "StreamingDistributionNotDisabled": ".streaming_distribution_not_disabled",
    "StreamingDistributionStreamingDistributionConfig": ".streaming_distribution_streaming_distribution_config",
    "StreamingDistributionStreamingDistributionConfigAliases": ".streaming_distribution_streaming_distribution_config_aliases",
    "StreamingDistributionStreamingDistributionConfigLogging": ".streaming_distribution_streaming_distribution_config_logging",
    "StreamingDistributionStreamingDistributionConfigPriceClass": ".streaming_distribution_streaming_distribution_config_price_class",
    "StreamingDistributionStreamingDistributionConfigS3Origin": ".streaming_distribution_streaming_distribution_config_s3origin",
    "StreamingDistributionStreamingDistributionConfigTrustedSigners": ".streaming_distribution_streaming_distribution_config_trusted_signers",
    "StreamingDistributionSummary": ".streaming_distribution_summary",
    "StreamingDistributionSummaryAliases": ".streaming_distribution_summary_aliases",
    "StreamingDistributionSummaryList": ".streaming_distribution_summary_list",
    "StreamingDistributionSummaryListItem": ".streaming_distribution_summary_list_item",
    "StreamingDistributionSummaryListItemAliases": ".streaming_distribution_summary_list_item_aliases",
    "StreamingDistributionSummaryListItemS3Origin": ".streaming_distribution_summary_list_item_s3origin",
    "StreamingDistributionSummaryListItemTrustedSigners": ".streaming_distribution_summary_list_item_trusted_signers",
    "StreamingDistributionSummaryS3Origin": ".streaming_distribution_summary_s3origin",
    "StreamingDistributionSummaryTrustedSigners": ".streaming_distribution_summary_trusted_signers",
    "StreamingLoggingConfig": ".streaming_logging_config",
    "String": ".string",
    "Tag": ".tag",
    "TagKey": ".tag_key",
    "TagKeyList": ".tag_key_list",
    "TagKeys": ".tag_keys",
    "TagList": ".tag_list",
    "TagListItem": ".tag_list_item",
    "TagResource20161125RequestOperation": ".tag_resource20161125request_operation",
    "TagResourceRequest": ".tag_resource_request",
    "TagResourceRequestTags": ".tag_resource_request_tags",
    "TagResourceRequestTagsItemsItem": ".tag_resource_request_tags_items_item",
    "TagValue": ".tag_value",
    "Tags": ".tags",
    "TagsItemsItem": ".tags_items_item",
    "Timestamp": ".timestamp",
    "TooManyCacheBehaviors": ".too_many_cache_behaviors",
    "TooManyCertificates": ".too_many_certificates",
    "TooManyCloudFrontOriginAccessIdentities": ".too_many_cloud_front_origin_access_identities",
    "TooManyCookieNamesInWhiteList": ".too_many_cookie_names_in_white_list",
    "TooManyDistributionCnamEs": ".too_many_distribution_cnam_es",
    "TooManyDistributions": ".too_many_distributions",
    "TooManyDistributionsWithLambdaAssociations": ".too_many_distributions_with_lambda_associations",
    "TooManyHeadersInForwardedValues": ".too_many_headers_in_forwarded_values",
    "TooManyInvalidationsInProgress": ".too_many_invalidations_in_progress",
    "TooManyLambdaFunctionAssociations": ".too_many_lambda_function_associations",
    "TooManyOriginCustomHeaders": ".too_many_origin_custom_headers",
    "TooManyOrigins": ".too_many_origins",
    "TooManyQueryStringParameters": ".too_many_query_string_parameters",
    "TooManyStreamingDistributionCnamEs": ".too_many_streaming_distribution_cnam_es",
    "TooManyStreamingDistributions": ".too_many_streaming_distributions",
    "TooManyTrustedSigners": ".too_many_trusted_signers",
    "TrustedSignerDoesNotExist": ".trusted_signer_does_not_exist",
    "TrustedSigners": ".trusted_signers",
    "UntagResource20161125RequestOperation": ".untag_resource20161125request_operation",
    "UntagResourceRequest": ".untag_resource_request",
    "UntagResourceRequestTagKeys": ".untag_resource_request_tag_keys",
    "UpdateCloudFrontOriginAccessIdentityRequest": ".update_cloud_front_origin_access_identity_request",
    "UpdateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig": ".update_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config",
    "UpdateCloudFrontOriginAccessIdentityResult": ".update_cloud_front_origin_access_identity_result",
    "UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity": ".update_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity",
    "UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig": ".update_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config",
    "UpdateDistributionRequest": ".update_distribution_request",
    "UpdateDistributionRequestDistributionConfig": ".update_distribution_request_distribution_config",
    "UpdateDistributionRequestDistributionConfigAliases": ".update_distribution_request_distribution_config_aliases",
    "UpdateDistributionRequestDistributionConfigCacheBehaviors": ".update_distribution_request_distribution_config_cache_behaviors",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItem": ".update_distribution_request_distribution_config_cache_behaviors_items_item",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".update_distribution_request_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".update_distribution_request_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".update_distribution_request_distribution_config_cache_behaviors_items_item_trusted_signers",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".update_distribution_request_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "UpdateDistributionRequestDistributionConfigCustomErrorResponses": ".update_distribution_request_distribution_config_custom_error_responses",
    "UpdateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem": ".update_distribution_request_distribution_config_custom_error_responses_items_item",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehavior": ".update_distribution_request_distribution_config_default_cache_behavior",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_headers",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".update_distribution_request_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".update_distribution_request_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners": ".update_distribution_request_distribution_config_default_cache_behavior_trusted_signers",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".update_distribution_request_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "UpdateDistributionRequestDistributionConfigHttpVersion": ".update_distribution_request_distribution_config_http_version",
    "UpdateDistributionRequestDistributionConfigLogging": ".update_distribution_request_distribution_config_logging",
    "UpdateDistributionRequestDistributionConfigOrigins": ".update_distribution_request_distribution_config_origins",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItem": ".update_distribution_request_distribution_config_origins_items_item",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders": ".update_distribution_request_distribution_config_origins_items_item_custom_headers",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".update_distribution_request_distribution_config_origins_items_item_custom_headers_items_item",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig": ".update_distribution_request_distribution_config_origins_items_item_custom_origin_config",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".update_distribution_request_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig": ".update_distribution_request_distribution_config_origins_items_item_s3origin_config",
    "UpdateDistributionRequestDistributionConfigPriceClass": ".update_distribution_request_distribution_config_price_class",
    "UpdateDistributionResult": ".update_distribution_result",
    "UpdateDistributionResultDistribution": ".update_distribution_result_distribution",
    "UpdateDistributionResultDistributionActiveTrustedSigners": ".update_distribution_result_distribution_active_trusted_signers",
    "UpdateDistributionResultDistributionActiveTrustedSignersItemsItem": ".update_distribution_result_distribution_active_trusted_signers_items_item",
    "UpdateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds": ".update_distribution_result_distribution_active_trusted_signers_items_item_key_pair_ids",
    "UpdateDistributionResultDistributionDistributionConfig": ".update_distribution_result_distribution_distribution_config",
    "UpdateDistributionResultDistributionDistributionConfigAliases": ".update_distribution_result_distribution_distribution_config_aliases",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviors": ".update_distribution_result_distribution_distribution_config_cache_behaviors",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_forward",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_cookies_whitelisted_names",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_headers",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_forwarded_values_query_string_cache_keys",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_lambda_function_associations_items_item_event_type",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_trusted_signers",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy": ".update_distribution_result_distribution_distribution_config_cache_behaviors_items_item_viewer_protocol_policy",
    "UpdateDistributionResultDistributionDistributionConfigCustomErrorResponses": ".update_distribution_result_distribution_distribution_config_custom_error_responses",
    "UpdateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem": ".update_distribution_result_distribution_distribution_config_custom_error_responses_items_item",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehavior": ".update_distribution_result_distribution_distribution_config_default_cache_behavior",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_forward",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies_whitelisted_names",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_lambda_function_associations_items_item_event_type",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_trusted_signers",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy": ".update_distribution_result_distribution_distribution_config_default_cache_behavior_viewer_protocol_policy",
    "UpdateDistributionResultDistributionDistributionConfigHttpVersion": ".update_distribution_result_distribution_distribution_config_http_version",
    "UpdateDistributionResultDistributionDistributionConfigLogging": ".update_distribution_result_distribution_distribution_config_logging",
    "UpdateDistributionResultDistributionDistributionConfigOrigins": ".update_distribution_result_distribution_distribution_config_origins",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItem": ".update_distribution_result_distribution_distribution_config_origins_items_item",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_headers",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_headers_items_item",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_protocol_policy",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem": ".update_distribution_result_distribution_distribution_config_origins_items_item_custom_origin_config_origin_ssl_protocols_items_item",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig": ".update_distribution_result_distribution_distribution_config_origins_items_item_s3origin_config",
    "UpdateDistributionResultDistributionDistributionConfigPriceClass": ".update_distribution_result_distribution_distribution_config_price_class",
    "UpdateStreamingDistributionRequest": ".update_streaming_distribution_request",
    "UpdateStreamingDistributionRequestStreamingDistributionConfig": ".update_streaming_distribution_request_streaming_distribution_config",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigAliases": ".update_streaming_distribution_request_streaming_distribution_config_aliases",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigLogging": ".update_streaming_distribution_request_streaming_distribution_config_logging",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigPriceClass": ".update_streaming_distribution_request_streaming_distribution_config_price_class",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigS3Origin": ".update_streaming_distribution_request_streaming_distribution_config_s3origin",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners": ".update_streaming_distribution_request_streaming_distribution_config_trusted_signers",
    "UpdateStreamingDistributionResult": ".update_streaming_distribution_result",
    "UpdateStreamingDistributionResultStreamingDistribution": ".update_streaming_distribution_result_streaming_distribution",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSigners": ".update_streaming_distribution_result_streaming_distribution_active_trusted_signers",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem": ".update_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds": ".update_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_aliases",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_logging",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_price_class",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_s3origin",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners": ".update_streaming_distribution_result_streaming_distribution_streaming_distribution_config_trusted_signers",
    "ViewerCertificate": ".viewer_certificate",
    "ViewerCertificateCertificateSource": ".viewer_certificate_certificate_source",
    "ViewerCertificateMinimumProtocolVersion": ".viewer_certificate_minimum_protocol_version",
    "ViewerCertificateSslSupportMethod": ".viewer_certificate_ssl_support_method",
    "ViewerProtocolPolicy": ".viewer_protocol_policy",
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
    "AccessDenied",
    "ActiveTrustedSigners",
    "ActiveTrustedSignersItemsItem",
    "ActiveTrustedSignersItemsItemKeyPairIds",
    "AliasList",
    "Aliases",
    "AllowedMethods",
    "AllowedMethodsItemsItem",
    "AwsAccountNumberList",
    "BatchTooLarge",
    "Boolean",
    "CacheBehavior",
    "CacheBehaviorForwardedValues",
    "CacheBehaviorForwardedValuesCookies",
    "CacheBehaviorForwardedValuesCookiesForward",
    "CacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "CacheBehaviorForwardedValuesHeaders",
    "CacheBehaviorForwardedValuesQueryStringCacheKeys",
    "CacheBehaviorLambdaFunctionAssociations",
    "CacheBehaviorLambdaFunctionAssociationsItemsItem",
    "CacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "CacheBehaviorList",
    "CacheBehaviorListItem",
    "CacheBehaviorListItemForwardedValues",
    "CacheBehaviorListItemForwardedValuesCookies",
    "CacheBehaviorListItemForwardedValuesCookiesForward",
    "CacheBehaviorListItemForwardedValuesCookiesWhitelistedNames",
    "CacheBehaviorListItemForwardedValuesHeaders",
    "CacheBehaviorListItemForwardedValuesQueryStringCacheKeys",
    "CacheBehaviorListItemLambdaFunctionAssociations",
    "CacheBehaviorListItemLambdaFunctionAssociationsItemsItem",
    "CacheBehaviorListItemLambdaFunctionAssociationsItemsItemEventType",
    "CacheBehaviorListItemTrustedSigners",
    "CacheBehaviorListItemViewerProtocolPolicy",
    "CacheBehaviorTrustedSigners",
    "CacheBehaviorViewerProtocolPolicy",
    "CacheBehaviors",
    "CacheBehaviorsItemsItem",
    "CacheBehaviorsItemsItemForwardedValues",
    "CacheBehaviorsItemsItemForwardedValuesCookies",
    "CacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "CacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "CacheBehaviorsItemsItemForwardedValuesHeaders",
    "CacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "CacheBehaviorsItemsItemLambdaFunctionAssociations",
    "CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "CacheBehaviorsItemsItemTrustedSigners",
    "CacheBehaviorsItemsItemViewerProtocolPolicy",
    "CachedMethods",
    "CachedMethodsItemsItem",
    "CertificateSource",
    "CloudFrontOriginAccessIdentity",
    "CloudFrontOriginAccessIdentityAlreadyExists",
    "CloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig",
    "CloudFrontOriginAccessIdentityConfig",
    "CloudFrontOriginAccessIdentityInUse",
    "CloudFrontOriginAccessIdentityList",
    "CloudFrontOriginAccessIdentityListItemsItem",
    "CloudFrontOriginAccessIdentitySummary",
    "CloudFrontOriginAccessIdentitySummaryList",
    "CloudFrontOriginAccessIdentitySummaryListItem",
    "CnameAlreadyExists",
    "CookieNameList",
    "CookieNames",
    "CookiePreference",
    "CookiePreferenceForward",
    "CookiePreferenceWhitelistedNames",
    "CreateCloudFrontOriginAccessIdentityRequest",
    "CreateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig",
    "CreateCloudFrontOriginAccessIdentityResult",
    "CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity",
    "CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig",
    "CreateDistributionRequest",
    "CreateDistributionRequestDistributionConfig",
    "CreateDistributionRequestDistributionConfigAliases",
    "CreateDistributionRequestDistributionConfigCacheBehaviors",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "CreateDistributionRequestDistributionConfigCustomErrorResponses",
    "CreateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehavior",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "CreateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "CreateDistributionRequestDistributionConfigHttpVersion",
    "CreateDistributionRequestDistributionConfigLogging",
    "CreateDistributionRequestDistributionConfigOrigins",
    "CreateDistributionRequestDistributionConfigOriginsItemsItem",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "CreateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig",
    "CreateDistributionRequestDistributionConfigPriceClass",
    "CreateDistributionResult",
    "CreateDistributionResultDistribution",
    "CreateDistributionResultDistributionActiveTrustedSigners",
    "CreateDistributionResultDistributionActiveTrustedSignersItemsItem",
    "CreateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "CreateDistributionResultDistributionDistributionConfig",
    "CreateDistributionResultDistributionDistributionConfigAliases",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviors",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "CreateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "CreateDistributionResultDistributionDistributionConfigCustomErrorResponses",
    "CreateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehavior",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "CreateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "CreateDistributionResultDistributionDistributionConfigHttpVersion",
    "CreateDistributionResultDistributionDistributionConfigLogging",
    "CreateDistributionResultDistributionDistributionConfigOrigins",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItem",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "CreateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig",
    "CreateDistributionResultDistributionDistributionConfigPriceClass",
    "CreateDistributionWithTagsRequest",
    "CreateDistributionWithTagsRequestDistributionConfigWithTags",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfig",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigAliases",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviors",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponses",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehavior",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigHttpVersion",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigLogging",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOrigins",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfigPriceClass",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsTags",
    "CreateDistributionWithTagsRequestDistributionConfigWithTagsTagsItemsItem",
    "CreateDistributionWithTagsResult",
    "CreateDistributionWithTagsResultDistribution",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSigners",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItem",
    "CreateDistributionWithTagsResultDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "CreateDistributionWithTagsResultDistributionDistributionConfig",
    "CreateDistributionWithTagsResultDistributionDistributionConfigAliases",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviors",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponses",
    "CreateDistributionWithTagsResultDistributionDistributionConfigCustomErrorResponsesItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehavior",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "CreateDistributionWithTagsResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigHttpVersion",
    "CreateDistributionWithTagsResultDistributionDistributionConfigLogging",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOrigins",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeaders",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "CreateDistributionWithTagsResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig",
    "CreateDistributionWithTagsResultDistributionDistributionConfigPriceClass",
    "CreateInvalidationRequest",
    "CreateInvalidationRequestInvalidationBatch",
    "CreateInvalidationRequestInvalidationBatchPaths",
    "CreateInvalidationResult",
    "CreateInvalidationResultInvalidation",
    "CreateInvalidationResultInvalidationInvalidationBatch",
    "CreateInvalidationResultInvalidationInvalidationBatchPaths",
    "CreateStreamingDistributionRequest",
    "CreateStreamingDistributionRequestStreamingDistributionConfig",
    "CreateStreamingDistributionRequestStreamingDistributionConfigAliases",
    "CreateStreamingDistributionRequestStreamingDistributionConfigLogging",
    "CreateStreamingDistributionRequestStreamingDistributionConfigPriceClass",
    "CreateStreamingDistributionRequestStreamingDistributionConfigS3Origin",
    "CreateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners",
    "CreateStreamingDistributionResult",
    "CreateStreamingDistributionResultStreamingDistribution",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSigners",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem",
    "CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin",
    "CreateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners",
    "CreateStreamingDistributionWithTagsRequest",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfig",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigAliases",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigLogging",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTags",
    "CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTagsItemsItem",
    "CreateStreamingDistributionWithTagsResult",
    "CreateStreamingDistributionWithTagsResultStreamingDistribution",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSigners",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfig",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigAliases",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigLogging",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigPriceClass",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigS3Origin",
    "CreateStreamingDistributionWithTagsResultStreamingDistributionStreamingDistributionConfigTrustedSigners",
    "CustomErrorResponse",
    "CustomErrorResponseList",
    "CustomErrorResponseListItem",
    "CustomErrorResponses",
    "CustomErrorResponsesItemsItem",
    "CustomHeaders",
    "CustomHeadersItemsItem",
    "CustomOriginConfig",
    "CustomOriginConfigOriginProtocolPolicy",
    "CustomOriginConfigOriginSslProtocols",
    "CustomOriginConfigOriginSslProtocolsItemsItem",
    "DefaultCacheBehavior",
    "DefaultCacheBehaviorForwardedValues",
    "DefaultCacheBehaviorForwardedValuesCookies",
    "DefaultCacheBehaviorForwardedValuesCookiesForward",
    "DefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DefaultCacheBehaviorForwardedValuesHeaders",
    "DefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DefaultCacheBehaviorLambdaFunctionAssociations",
    "DefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DefaultCacheBehaviorTrustedSigners",
    "DefaultCacheBehaviorViewerProtocolPolicy",
    "DeleteCloudFrontOriginAccessIdentityRequest",
    "DeleteDistributionRequest",
    "DeleteStreamingDistributionRequest",
    "Distribution",
    "DistributionActiveTrustedSigners",
    "DistributionActiveTrustedSignersItemsItem",
    "DistributionActiveTrustedSignersItemsItemKeyPairIds",
    "DistributionAlreadyExists",
    "DistributionConfig",
    "DistributionConfigAliases",
    "DistributionConfigCacheBehaviors",
    "DistributionConfigCacheBehaviorsItemsItem",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "DistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionConfigCustomErrorResponses",
    "DistributionConfigCustomErrorResponsesItemsItem",
    "DistributionConfigDefaultCacheBehavior",
    "DistributionConfigDefaultCacheBehaviorForwardedValues",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionConfigDefaultCacheBehaviorTrustedSigners",
    "DistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionConfigHttpVersion",
    "DistributionConfigLogging",
    "DistributionConfigOrigins",
    "DistributionConfigOriginsItemsItem",
    "DistributionConfigOriginsItemsItemCustomHeaders",
    "DistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "DistributionConfigOriginsItemsItemCustomOriginConfig",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionConfigOriginsItemsItemS3OriginConfig",
    "DistributionConfigPriceClass",
    "DistributionConfigWithTags",
    "DistributionConfigWithTagsDistributionConfig",
    "DistributionConfigWithTagsDistributionConfigAliases",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviors",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionConfigWithTagsDistributionConfigCustomErrorResponses",
    "DistributionConfigWithTagsDistributionConfigCustomErrorResponsesItemsItem",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehavior",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "DistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionConfigWithTagsDistributionConfigHttpVersion",
    "DistributionConfigWithTagsDistributionConfigLogging",
    "DistributionConfigWithTagsDistributionConfigOrigins",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItem",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeaders",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfig",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionConfigWithTagsDistributionConfigOriginsItemsItemS3OriginConfig",
    "DistributionConfigWithTagsDistributionConfigPriceClass",
    "DistributionConfigWithTagsTags",
    "DistributionConfigWithTagsTagsItemsItem",
    "DistributionDistributionConfig",
    "DistributionDistributionConfigAliases",
    "DistributionDistributionConfigCacheBehaviors",
    "DistributionDistributionConfigCacheBehaviorsItemsItem",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "DistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionDistributionConfigCustomErrorResponses",
    "DistributionDistributionConfigCustomErrorResponsesItemsItem",
    "DistributionDistributionConfigDefaultCacheBehavior",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValues",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "DistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionDistributionConfigHttpVersion",
    "DistributionDistributionConfigLogging",
    "DistributionDistributionConfigOrigins",
    "DistributionDistributionConfigOriginsItemsItem",
    "DistributionDistributionConfigOriginsItemsItemCustomHeaders",
    "DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfig",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionDistributionConfigOriginsItemsItemS3OriginConfig",
    "DistributionDistributionConfigPriceClass",
    "DistributionList",
    "DistributionListItemsItem",
    "DistributionListItemsItemAliases",
    "DistributionListItemsItemCacheBehaviors",
    "DistributionListItemsItemCacheBehaviorsItemsItem",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValues",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners",
    "DistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionListItemsItemCustomErrorResponses",
    "DistributionListItemsItemCustomErrorResponsesItemsItem",
    "DistributionListItemsItemDefaultCacheBehavior",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValues",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionListItemsItemDefaultCacheBehaviorTrustedSigners",
    "DistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionListItemsItemHttpVersion",
    "DistributionListItemsItemOrigins",
    "DistributionListItemsItemOriginsItemsItem",
    "DistributionListItemsItemOriginsItemsItemCustomHeaders",
    "DistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfig",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionListItemsItemOriginsItemsItemS3OriginConfig",
    "DistributionNotDisabled",
    "DistributionSummary",
    "DistributionSummaryAliases",
    "DistributionSummaryCacheBehaviors",
    "DistributionSummaryCacheBehaviorsItemsItem",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValues",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionSummaryCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionSummaryCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionSummaryCacheBehaviorsItemsItemTrustedSigners",
    "DistributionSummaryCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionSummaryCustomErrorResponses",
    "DistributionSummaryCustomErrorResponsesItemsItem",
    "DistributionSummaryDefaultCacheBehavior",
    "DistributionSummaryDefaultCacheBehaviorForwardedValues",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionSummaryDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionSummaryDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionSummaryDefaultCacheBehaviorTrustedSigners",
    "DistributionSummaryDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionSummaryHttpVersion",
    "DistributionSummaryList",
    "DistributionSummaryListItem",
    "DistributionSummaryListItemAliases",
    "DistributionSummaryListItemCacheBehaviors",
    "DistributionSummaryListItemCacheBehaviorsItemsItem",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValues",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookies",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesHeaders",
    "DistributionSummaryListItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "DistributionSummaryListItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "DistributionSummaryListItemCacheBehaviorsItemsItemTrustedSigners",
    "DistributionSummaryListItemCacheBehaviorsItemsItemViewerProtocolPolicy",
    "DistributionSummaryListItemCustomErrorResponses",
    "DistributionSummaryListItemCustomErrorResponsesItemsItem",
    "DistributionSummaryListItemDefaultCacheBehavior",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValues",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookies",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesForward",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesHeaders",
    "DistributionSummaryListItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociations",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "DistributionSummaryListItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "DistributionSummaryListItemDefaultCacheBehaviorTrustedSigners",
    "DistributionSummaryListItemDefaultCacheBehaviorViewerProtocolPolicy",
    "DistributionSummaryListItemHttpVersion",
    "DistributionSummaryListItemOrigins",
    "DistributionSummaryListItemOriginsItemsItem",
    "DistributionSummaryListItemOriginsItemsItemCustomHeaders",
    "DistributionSummaryListItemOriginsItemsItemCustomHeadersItemsItem",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfig",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionSummaryListItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionSummaryListItemOriginsItemsItemS3OriginConfig",
    "DistributionSummaryOrigins",
    "DistributionSummaryOriginsItemsItem",
    "DistributionSummaryOriginsItemsItemCustomHeaders",
    "DistributionSummaryOriginsItemsItemCustomHeadersItemsItem",
    "DistributionSummaryOriginsItemsItemCustomOriginConfig",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "DistributionSummaryOriginsItemsItemS3OriginConfig",
    "EventType",
    "ForwardedValues",
    "ForwardedValuesCookies",
    "ForwardedValuesCookiesForward",
    "ForwardedValuesCookiesWhitelistedNames",
    "ForwardedValuesHeaders",
    "ForwardedValuesQueryStringCacheKeys",
    "GeoRestriction",
    "GeoRestrictionRestrictionType",
    "GeoRestrictionType",
    "GetCloudFrontOriginAccessIdentityConfigRequest",
    "GetCloudFrontOriginAccessIdentityConfigResult",
    "GetCloudFrontOriginAccessIdentityConfigResultCloudFrontOriginAccessIdentityConfig",
    "GetCloudFrontOriginAccessIdentityRequest",
    "GetCloudFrontOriginAccessIdentityResult",
    "GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity",
    "GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig",
    "GetDistributionConfigRequest",
    "GetDistributionConfigResult",
    "GetDistributionConfigResultDistributionConfig",
    "GetDistributionConfigResultDistributionConfigAliases",
    "GetDistributionConfigResultDistributionConfigCacheBehaviors",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItem",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "GetDistributionConfigResultDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "GetDistributionConfigResultDistributionConfigCustomErrorResponses",
    "GetDistributionConfigResultDistributionConfigCustomErrorResponsesItemsItem",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehavior",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValues",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "GetDistributionConfigResultDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "GetDistributionConfigResultDistributionConfigHttpVersion",
    "GetDistributionConfigResultDistributionConfigLogging",
    "GetDistributionConfigResultDistributionConfigOrigins",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItem",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeaders",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfig",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "GetDistributionConfigResultDistributionConfigOriginsItemsItemS3OriginConfig",
    "GetDistributionConfigResultDistributionConfigPriceClass",
    "GetDistributionRequest",
    "GetDistributionResult",
    "GetDistributionResultDistribution",
    "GetDistributionResultDistributionActiveTrustedSigners",
    "GetDistributionResultDistributionActiveTrustedSignersItemsItem",
    "GetDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "GetDistributionResultDistributionDistributionConfig",
    "GetDistributionResultDistributionDistributionConfigAliases",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviors",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "GetDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "GetDistributionResultDistributionDistributionConfigCustomErrorResponses",
    "GetDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehavior",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "GetDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "GetDistributionResultDistributionDistributionConfigHttpVersion",
    "GetDistributionResultDistributionDistributionConfigLogging",
    "GetDistributionResultDistributionDistributionConfigOrigins",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItem",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "GetDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig",
    "GetDistributionResultDistributionDistributionConfigPriceClass",
    "GetInvalidationRequest",
    "GetInvalidationResult",
    "GetInvalidationResultInvalidation",
    "GetInvalidationResultInvalidationInvalidationBatch",
    "GetInvalidationResultInvalidationInvalidationBatchPaths",
    "GetStreamingDistributionConfigRequest",
    "GetStreamingDistributionConfigResult",
    "GetStreamingDistributionConfigResultStreamingDistributionConfig",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigAliases",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigLogging",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigPriceClass",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigS3Origin",
    "GetStreamingDistributionConfigResultStreamingDistributionConfigTrustedSigners",
    "GetStreamingDistributionRequest",
    "GetStreamingDistributionResult",
    "GetStreamingDistributionResultStreamingDistribution",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSigners",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem",
    "GetStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfig",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin",
    "GetStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners",
    "HeaderList",
    "Headers",
    "HttpVersion",
    "IllegalUpdate",
    "InconsistentQuantities",
    "Integer",
    "InvalidArgument",
    "InvalidDefaultRootObject",
    "InvalidErrorCode",
    "InvalidForwardCookies",
    "InvalidGeoRestrictionParameter",
    "InvalidHeadersForS3Origin",
    "InvalidIfMatchVersion",
    "InvalidLambdaFunctionAssociation",
    "InvalidLocationCode",
    "InvalidMinimumProtocolVersion",
    "InvalidOrigin",
    "InvalidOriginAccessIdentity",
    "InvalidProtocolSettings",
    "InvalidQueryStringParameters",
    "InvalidRelativePath",
    "InvalidRequiredProtocol",
    "InvalidResponseCode",
    "InvalidTagging",
    "InvalidTtlOrder",
    "InvalidViewerCertificate",
    "InvalidWebAclId",
    "Invalidation",
    "InvalidationBatch",
    "InvalidationBatchPaths",
    "InvalidationInvalidationBatch",
    "InvalidationInvalidationBatchPaths",
    "InvalidationList",
    "InvalidationListItemsItem",
    "InvalidationSummary",
    "InvalidationSummaryList",
    "InvalidationSummaryListItem",
    "ItemSelection",
    "KeyPairIdList",
    "KeyPairIds",
    "LambdaFunctionAssociation",
    "LambdaFunctionAssociationEventType",
    "LambdaFunctionAssociationList",
    "LambdaFunctionAssociationListItem",
    "LambdaFunctionAssociationListItemEventType",
    "LambdaFunctionAssociations",
    "LambdaFunctionAssociationsItemsItem",
    "LambdaFunctionAssociationsItemsItemEventType",
    "ListCloudFrontOriginAccessIdentitiesRequest",
    "ListCloudFrontOriginAccessIdentitiesResult",
    "ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityList",
    "ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityListItemsItem",
    "ListDistributionsByWebAclIdRequest",
    "ListDistributionsByWebAclIdResult",
    "ListDistributionsByWebAclIdResultDistributionList",
    "ListDistributionsByWebAclIdResultDistributionListItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemAliases",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviors",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponses",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponsesItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehavior",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemHttpVersion",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOrigins",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeaders",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemS3OriginConfig",
    "ListDistributionsRequest",
    "ListDistributionsResult",
    "ListDistributionsResultDistributionList",
    "ListDistributionsResultDistributionListItemsItem",
    "ListDistributionsResultDistributionListItemsItemAliases",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviors",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItem",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValues",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookies",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesHeaders",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemTrustedSigners",
    "ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItemViewerProtocolPolicy",
    "ListDistributionsResultDistributionListItemsItemCustomErrorResponses",
    "ListDistributionsResultDistributionListItemsItemCustomErrorResponsesItemsItem",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehavior",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookies",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesForward",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesHeaders",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners",
    "ListDistributionsResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy",
    "ListDistributionsResultDistributionListItemsItemHttpVersion",
    "ListDistributionsResultDistributionListItemsItemOrigins",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItem",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeaders",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfig",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "ListDistributionsResultDistributionListItemsItemOriginsItemsItemS3OriginConfig",
    "ListInvalidationsRequest",
    "ListInvalidationsResult",
    "ListInvalidationsResultInvalidationList",
    "ListInvalidationsResultInvalidationListItemsItem",
    "ListStreamingDistributionsRequest",
    "ListStreamingDistributionsResult",
    "ListStreamingDistributionsResultStreamingDistributionList",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItem",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemAliases",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemS3Origin",
    "ListStreamingDistributionsResultStreamingDistributionListItemsItemTrustedSigners",
    "ListTagsForResourceRequest",
    "ListTagsForResourceResult",
    "ListTagsForResourceResultTags",
    "ListTagsForResourceResultTagsItemsItem",
    "LocationList",
    "LoggingConfig",
    "Long",
    "Method",
    "MethodsList",
    "MethodsListItem",
    "MinimumProtocolVersion",
    "MissingBody",
    "NoSuchCloudFrontOriginAccessIdentity",
    "NoSuchDistribution",
    "NoSuchInvalidation",
    "NoSuchOrigin",
    "NoSuchResource",
    "NoSuchStreamingDistribution",
    "Origin",
    "OriginCustomHeader",
    "OriginCustomHeaders",
    "OriginCustomHeadersItemsItem",
    "OriginCustomHeadersList",
    "OriginCustomHeadersListItem",
    "OriginCustomOriginConfig",
    "OriginCustomOriginConfigOriginProtocolPolicy",
    "OriginCustomOriginConfigOriginSslProtocols",
    "OriginCustomOriginConfigOriginSslProtocolsItemsItem",
    "OriginList",
    "OriginListItem",
    "OriginListItemCustomHeaders",
    "OriginListItemCustomHeadersItemsItem",
    "OriginListItemCustomOriginConfig",
    "OriginListItemCustomOriginConfigOriginProtocolPolicy",
    "OriginListItemCustomOriginConfigOriginSslProtocols",
    "OriginListItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "OriginListItemS3OriginConfig",
    "OriginProtocolPolicy",
    "OriginS3OriginConfig",
    "OriginSslProtocols",
    "OriginSslProtocolsItemsItem",
    "Origins",
    "OriginsItemsItem",
    "OriginsItemsItemCustomHeaders",
    "OriginsItemsItemCustomHeadersItemsItem",
    "OriginsItemsItemCustomOriginConfig",
    "OriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "OriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "OriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "OriginsItemsItemS3OriginConfig",
    "PathList",
    "Paths",
    "PreconditionFailed",
    "PriceClass",
    "QueryStringCacheKeys",
    "QueryStringCacheKeysList",
    "ResourceArn",
    "Restrictions",
    "S3Origin",
    "S3OriginConfig",
    "Signer",
    "SignerKeyPairIds",
    "SignerList",
    "SignerListItem",
    "SignerListItemKeyPairIds",
    "SslProtocol",
    "SslProtocolsList",
    "SslProtocolsListItem",
    "SslSupportMethod",
    "StreamingDistribution",
    "StreamingDistributionActiveTrustedSigners",
    "StreamingDistributionActiveTrustedSignersItemsItem",
    "StreamingDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "StreamingDistributionAlreadyExists",
    "StreamingDistributionConfig",
    "StreamingDistributionConfigAliases",
    "StreamingDistributionConfigLogging",
    "StreamingDistributionConfigPriceClass",
    "StreamingDistributionConfigS3Origin",
    "StreamingDistributionConfigTrustedSigners",
    "StreamingDistributionConfigWithTags",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfig",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigAliases",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigLogging",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigPriceClass",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin",
    "StreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSigners",
    "StreamingDistributionConfigWithTagsTags",
    "StreamingDistributionConfigWithTagsTagsItemsItem",
    "StreamingDistributionList",
    "StreamingDistributionListItemsItem",
    "StreamingDistributionListItemsItemAliases",
    "StreamingDistributionListItemsItemS3Origin",
    "StreamingDistributionListItemsItemTrustedSigners",
    "StreamingDistributionNotDisabled",
    "StreamingDistributionStreamingDistributionConfig",
    "StreamingDistributionStreamingDistributionConfigAliases",
    "StreamingDistributionStreamingDistributionConfigLogging",
    "StreamingDistributionStreamingDistributionConfigPriceClass",
    "StreamingDistributionStreamingDistributionConfigS3Origin",
    "StreamingDistributionStreamingDistributionConfigTrustedSigners",
    "StreamingDistributionSummary",
    "StreamingDistributionSummaryAliases",
    "StreamingDistributionSummaryList",
    "StreamingDistributionSummaryListItem",
    "StreamingDistributionSummaryListItemAliases",
    "StreamingDistributionSummaryListItemS3Origin",
    "StreamingDistributionSummaryListItemTrustedSigners",
    "StreamingDistributionSummaryS3Origin",
    "StreamingDistributionSummaryTrustedSigners",
    "StreamingLoggingConfig",
    "String",
    "Tag",
    "TagKey",
    "TagKeyList",
    "TagKeys",
    "TagList",
    "TagListItem",
    "TagResource20161125RequestOperation",
    "TagResourceRequest",
    "TagResourceRequestTags",
    "TagResourceRequestTagsItemsItem",
    "TagValue",
    "Tags",
    "TagsItemsItem",
    "Timestamp",
    "TooManyCacheBehaviors",
    "TooManyCertificates",
    "TooManyCloudFrontOriginAccessIdentities",
    "TooManyCookieNamesInWhiteList",
    "TooManyDistributionCnamEs",
    "TooManyDistributions",
    "TooManyDistributionsWithLambdaAssociations",
    "TooManyHeadersInForwardedValues",
    "TooManyInvalidationsInProgress",
    "TooManyLambdaFunctionAssociations",
    "TooManyOriginCustomHeaders",
    "TooManyOrigins",
    "TooManyQueryStringParameters",
    "TooManyStreamingDistributionCnamEs",
    "TooManyStreamingDistributions",
    "TooManyTrustedSigners",
    "TrustedSignerDoesNotExist",
    "TrustedSigners",
    "UntagResource20161125RequestOperation",
    "UntagResourceRequest",
    "UntagResourceRequestTagKeys",
    "UpdateCloudFrontOriginAccessIdentityRequest",
    "UpdateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig",
    "UpdateCloudFrontOriginAccessIdentityResult",
    "UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity",
    "UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig",
    "UpdateDistributionRequest",
    "UpdateDistributionRequestDistributionConfig",
    "UpdateDistributionRequestDistributionConfigAliases",
    "UpdateDistributionRequestDistributionConfigCacheBehaviors",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItem",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "UpdateDistributionRequestDistributionConfigCustomErrorResponses",
    "UpdateDistributionRequestDistributionConfigCustomErrorResponsesItemsItem",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehavior",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValues",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "UpdateDistributionRequestDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "UpdateDistributionRequestDistributionConfigHttpVersion",
    "UpdateDistributionRequestDistributionConfigLogging",
    "UpdateDistributionRequestDistributionConfigOrigins",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItem",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeaders",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfig",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "UpdateDistributionRequestDistributionConfigOriginsItemsItemS3OriginConfig",
    "UpdateDistributionRequestDistributionConfigPriceClass",
    "UpdateDistributionResult",
    "UpdateDistributionResultDistribution",
    "UpdateDistributionResultDistributionActiveTrustedSigners",
    "UpdateDistributionResultDistributionActiveTrustedSignersItemsItem",
    "UpdateDistributionResultDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "UpdateDistributionResultDistributionDistributionConfig",
    "UpdateDistributionResultDistributionDistributionConfigAliases",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviors",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValues",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookies",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesForward",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesCookiesWhitelistedNames",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesHeaders",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItemEventType",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemTrustedSigners",
    "UpdateDistributionResultDistributionDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy",
    "UpdateDistributionResultDistributionDistributionConfigCustomErrorResponses",
    "UpdateDistributionResultDistributionDistributionConfigCustomErrorResponsesItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehavior",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesForward",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNames",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociations",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorLambdaFunctionAssociationsItemsItemEventType",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorTrustedSigners",
    "UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorViewerProtocolPolicy",
    "UpdateDistributionResultDistributionDistributionConfigHttpVersion",
    "UpdateDistributionResultDistributionDistributionConfigLogging",
    "UpdateDistributionResultDistributionDistributionConfigOrigins",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeaders",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfig",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginProtocolPolicy",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocols",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemCustomOriginConfigOriginSslProtocolsItemsItem",
    "UpdateDistributionResultDistributionDistributionConfigOriginsItemsItemS3OriginConfig",
    "UpdateDistributionResultDistributionDistributionConfigPriceClass",
    "UpdateStreamingDistributionRequest",
    "UpdateStreamingDistributionRequestStreamingDistributionConfig",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigAliases",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigLogging",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigPriceClass",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigS3Origin",
    "UpdateStreamingDistributionRequestStreamingDistributionConfigTrustedSigners",
    "UpdateStreamingDistributionResult",
    "UpdateStreamingDistributionResultStreamingDistribution",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSigners",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem",
    "UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigAliases",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigLogging",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigPriceClass",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigS3Origin",
    "UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfigTrustedSigners",
    "ViewerCertificate",
    "ViewerCertificateCertificateSource",
    "ViewerCertificateMinimumProtocolVersion",
    "ViewerCertificateSslSupportMethod",
    "ViewerProtocolPolicy",
]
