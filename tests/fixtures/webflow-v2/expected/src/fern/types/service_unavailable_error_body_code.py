

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceUnavailableErrorBodyCode(enum.StrEnum):
    """
    Error code
    """

    ANALYZE_FILTER_CONFLICT = "analyze_filter_conflict"
    ANALYZE_INPUT_VALIDATION = "analyze_input_validation"
    ANALYZE_UNSUPPORTED_FILTER = "analyze_unsupported_filter"
    BAD_REQUEST = "bad_request"
    BEFORE_HISTORICAL_FLOOR = "before_historical_floor"
    COLLECTION_NOT_FOUND = "collection_not_found"
    CONFLICT = "conflict"
    DUPLICATE_COLLECTION = "duplicate_collection"
    DUPLICATE_USER_EMAIL = "duplicate_user_email"
    ECOMMERCE_NOT_ENABLED = "ecommerce_not_enabled"
    FORBIDDEN = "forbidden"
    FORMS_REQUIRE_REPUBLISH = "forms_require_republish"
    INCOMPATIBLE_WEBHOOK_FILTER = "incompatible_webhook_filter"
    INTERNAL_ERROR = "internal_error"
    INVALID_AUTH_VERSION = "invalid_auth_version"
    INVALID_CREDENTIALS = "invalid_credentials"
    INVALID_DOMAIN = "invalid_domain"
    INVALID_TIME_RANGE = "invalid_time_range"
    INVALID_USER_EMAIL = "invalid_user_email"
    ITEM_NOT_FOUND = "item_not_found"
    MISSING_SCOPES = "missing_scopes"
    NO_DOMAINS = "no_domains"
    NOT_AUTHORIZED = "not_authorized"
    NOT_ENTERPRISE_PLAN_SITE = "not_enterprise_plan_site"
    NOT_ENTERPRISE_PLAN_WORKSPACE = "not_enterprise_plan_workspace"
    ORDER_NOT_FOUND = "order_not_found"
    RESOURCE_NOT_FOUND = "resource_not_found"
    SERVICE_UNAVAILABLE = "service_unavailable"
    TIME_RANGE_TOO_WIDE = "time_range_too_wide"
    TOO_MANY_REQUESTS = "too_many_requests"
    UNSUPPORTED_VERSION = "unsupported_version"
    UNSUPPORTED_WEBHOOK_TRIGGER_TYPE = "unsupported_webhook_trigger_type"
    USER_LIMIT_REACHED = "user_limit_reached"
    USER_NOT_FOUND = "user_not_found"
    USERS_NOT_ENABLED = "users_not_enabled"
    VALIDATION_ERROR = "validation_error"

    def visit(
        self,
        analyze_filter_conflict: typing.Callable[[], T_Result],
        analyze_input_validation: typing.Callable[[], T_Result],
        analyze_unsupported_filter: typing.Callable[[], T_Result],
        bad_request: typing.Callable[[], T_Result],
        before_historical_floor: typing.Callable[[], T_Result],
        collection_not_found: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        duplicate_collection: typing.Callable[[], T_Result],
        duplicate_user_email: typing.Callable[[], T_Result],
        ecommerce_not_enabled: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        forms_require_republish: typing.Callable[[], T_Result],
        incompatible_webhook_filter: typing.Callable[[], T_Result],
        internal_error: typing.Callable[[], T_Result],
        invalid_auth_version: typing.Callable[[], T_Result],
        invalid_credentials: typing.Callable[[], T_Result],
        invalid_domain: typing.Callable[[], T_Result],
        invalid_time_range: typing.Callable[[], T_Result],
        invalid_user_email: typing.Callable[[], T_Result],
        item_not_found: typing.Callable[[], T_Result],
        missing_scopes: typing.Callable[[], T_Result],
        no_domains: typing.Callable[[], T_Result],
        not_authorized: typing.Callable[[], T_Result],
        not_enterprise_plan_site: typing.Callable[[], T_Result],
        not_enterprise_plan_workspace: typing.Callable[[], T_Result],
        order_not_found: typing.Callable[[], T_Result],
        resource_not_found: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
        time_range_too_wide: typing.Callable[[], T_Result],
        too_many_requests: typing.Callable[[], T_Result],
        unsupported_version: typing.Callable[[], T_Result],
        unsupported_webhook_trigger_type: typing.Callable[[], T_Result],
        user_limit_reached: typing.Callable[[], T_Result],
        user_not_found: typing.Callable[[], T_Result],
        users_not_enabled: typing.Callable[[], T_Result],
        validation_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceUnavailableErrorBodyCode.ANALYZE_FILTER_CONFLICT:
            return analyze_filter_conflict()
        if self is ServiceUnavailableErrorBodyCode.ANALYZE_INPUT_VALIDATION:
            return analyze_input_validation()
        if self is ServiceUnavailableErrorBodyCode.ANALYZE_UNSUPPORTED_FILTER:
            return analyze_unsupported_filter()
        if self is ServiceUnavailableErrorBodyCode.BAD_REQUEST:
            return bad_request()
        if self is ServiceUnavailableErrorBodyCode.BEFORE_HISTORICAL_FLOOR:
            return before_historical_floor()
        if self is ServiceUnavailableErrorBodyCode.COLLECTION_NOT_FOUND:
            return collection_not_found()
        if self is ServiceUnavailableErrorBodyCode.CONFLICT:
            return conflict()
        if self is ServiceUnavailableErrorBodyCode.DUPLICATE_COLLECTION:
            return duplicate_collection()
        if self is ServiceUnavailableErrorBodyCode.DUPLICATE_USER_EMAIL:
            return duplicate_user_email()
        if self is ServiceUnavailableErrorBodyCode.ECOMMERCE_NOT_ENABLED:
            return ecommerce_not_enabled()
        if self is ServiceUnavailableErrorBodyCode.FORBIDDEN:
            return forbidden()
        if self is ServiceUnavailableErrorBodyCode.FORMS_REQUIRE_REPUBLISH:
            return forms_require_republish()
        if self is ServiceUnavailableErrorBodyCode.INCOMPATIBLE_WEBHOOK_FILTER:
            return incompatible_webhook_filter()
        if self is ServiceUnavailableErrorBodyCode.INTERNAL_ERROR:
            return internal_error()
        if self is ServiceUnavailableErrorBodyCode.INVALID_AUTH_VERSION:
            return invalid_auth_version()
        if self is ServiceUnavailableErrorBodyCode.INVALID_CREDENTIALS:
            return invalid_credentials()
        if self is ServiceUnavailableErrorBodyCode.INVALID_DOMAIN:
            return invalid_domain()
        if self is ServiceUnavailableErrorBodyCode.INVALID_TIME_RANGE:
            return invalid_time_range()
        if self is ServiceUnavailableErrorBodyCode.INVALID_USER_EMAIL:
            return invalid_user_email()
        if self is ServiceUnavailableErrorBodyCode.ITEM_NOT_FOUND:
            return item_not_found()
        if self is ServiceUnavailableErrorBodyCode.MISSING_SCOPES:
            return missing_scopes()
        if self is ServiceUnavailableErrorBodyCode.NO_DOMAINS:
            return no_domains()
        if self is ServiceUnavailableErrorBodyCode.NOT_AUTHORIZED:
            return not_authorized()
        if self is ServiceUnavailableErrorBodyCode.NOT_ENTERPRISE_PLAN_SITE:
            return not_enterprise_plan_site()
        if self is ServiceUnavailableErrorBodyCode.NOT_ENTERPRISE_PLAN_WORKSPACE:
            return not_enterprise_plan_workspace()
        if self is ServiceUnavailableErrorBodyCode.ORDER_NOT_FOUND:
            return order_not_found()
        if self is ServiceUnavailableErrorBodyCode.RESOURCE_NOT_FOUND:
            return resource_not_found()
        if self is ServiceUnavailableErrorBodyCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
        if self is ServiceUnavailableErrorBodyCode.TIME_RANGE_TOO_WIDE:
            return time_range_too_wide()
        if self is ServiceUnavailableErrorBodyCode.TOO_MANY_REQUESTS:
            return too_many_requests()
        if self is ServiceUnavailableErrorBodyCode.UNSUPPORTED_VERSION:
            return unsupported_version()
        if self is ServiceUnavailableErrorBodyCode.UNSUPPORTED_WEBHOOK_TRIGGER_TYPE:
            return unsupported_webhook_trigger_type()
        if self is ServiceUnavailableErrorBodyCode.USER_LIMIT_REACHED:
            return user_limit_reached()
        if self is ServiceUnavailableErrorBodyCode.USER_NOT_FOUND:
            return user_not_found()
        if self is ServiceUnavailableErrorBodyCode.USERS_NOT_ENABLED:
            return users_not_enabled()
        if self is ServiceUnavailableErrorBodyCode.VALIDATION_ERROR:
            return validation_error()
