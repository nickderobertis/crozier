

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectAdvisorsResponseOutputLintsItemName(enum.StrEnum):
    UNINDEXED_FOREIGN_KEYS = "unindexed_foreign_keys"
    AUTH_USERS_EXPOSED = "auth_users_exposed"
    AUTH_RLS_INITPLAN = "auth_rls_initplan"
    NO_PRIMARY_KEY = "no_primary_key"
    UNUSED_INDEX = "unused_index"
    MULTIPLE_PERMISSIVE_POLICIES = "multiple_permissive_policies"
    POLICY_EXISTS_RLS_DISABLED = "policy_exists_rls_disabled"
    RLS_ENABLED_NO_POLICY = "rls_enabled_no_policy"
    DUPLICATE_INDEX = "duplicate_index"
    SECURITY_DEFINER_VIEW = "security_definer_view"
    FUNCTION_SEARCH_PATH_MUTABLE = "function_search_path_mutable"
    RLS_DISABLED_IN_PUBLIC = "rls_disabled_in_public"
    EXTENSION_IN_PUBLIC = "extension_in_public"
    RLS_REFERENCES_USER_METADATA = "rls_references_user_metadata"
    MATERIALIZED_VIEW_IN_API = "materialized_view_in_api"
    FOREIGN_TABLE_IN_API = "foreign_table_in_api"
    UNSUPPORTED_REG_TYPES = "unsupported_reg_types"
    AUTH_OTP_LONG_EXPIRY = "auth_otp_long_expiry"
    AUTH_OTP_SHORT_LENGTH = "auth_otp_short_length"
    SSL_NOT_ENFORCED = "ssl_not_enforced"
    LOG_CONNECTIONS_NOT_ENABLED = "log_connections_not_enabled"
    NETWORK_RESTRICTIONS_NOT_SET = "network_restrictions_not_set"
    PASSWORD_REQUIREMENTS_MIN_LENGTH = "password_requirements_min_length"
    PITR_NOT_ENABLED = "pitr_not_enabled"
    AUTH_LEAKED_PASSWORD_PROTECTION = "auth_leaked_password_protection"
    AUTH_INSUFFICIENT_MFA_OPTIONS = "auth_insufficient_mfa_options"
    AUTH_PASSWORD_POLICY_MISSING = "auth_password_policy_missing"
    LEAKED_SERVICE_KEY = "leaked_service_key"
    NO_BACKUP_ADMIN = "no_backup_admin"
    VULNERABLE_POSTGRES_VERSION = "vulnerable_postgres_version"
    DB_NOT_REACHABLE = "db_not_reachable"
    DB_CONNECTION_FAILING = "db_connection_failing"
    DB_CONNECTION_LIMIT_REACHED = "db_connection_limit_reached"
    INSTANCE_TELEMETRY_LOST = "instance_telemetry_lost"
    INSTANCE_DB_DOWN = "instance_db_down"
    INSTANCE_ALERT_FIRING = "instance_alert_firing"
    LOG_DATA_API_ERROR_RATE_HIGH = "log_data_api_error_rate_high"
    LOG_AUTH_ERROR_RATE_HIGH = "log_auth_error_rate_high"
    LOG_STORAGE_ERROR_RATE_HIGH = "log_storage_error_rate_high"
    LOG_EDGE_FUNCTION_ERROR_RATE_HIGH = "log_edge_function_error_rate_high"
    PROJECT_NOT_ACTIVE = "project_not_active"
    ADVISOR_CHECK_UNAVAILABLE = "advisor_check_unavailable"

    def visit(
        self,
        unindexed_foreign_keys: typing.Callable[[], T_Result],
        auth_users_exposed: typing.Callable[[], T_Result],
        auth_rls_initplan: typing.Callable[[], T_Result],
        no_primary_key: typing.Callable[[], T_Result],
        unused_index: typing.Callable[[], T_Result],
        multiple_permissive_policies: typing.Callable[[], T_Result],
        policy_exists_rls_disabled: typing.Callable[[], T_Result],
        rls_enabled_no_policy: typing.Callable[[], T_Result],
        duplicate_index: typing.Callable[[], T_Result],
        security_definer_view: typing.Callable[[], T_Result],
        function_search_path_mutable: typing.Callable[[], T_Result],
        rls_disabled_in_public: typing.Callable[[], T_Result],
        extension_in_public: typing.Callable[[], T_Result],
        rls_references_user_metadata: typing.Callable[[], T_Result],
        materialized_view_in_api: typing.Callable[[], T_Result],
        foreign_table_in_api: typing.Callable[[], T_Result],
        unsupported_reg_types: typing.Callable[[], T_Result],
        auth_otp_long_expiry: typing.Callable[[], T_Result],
        auth_otp_short_length: typing.Callable[[], T_Result],
        ssl_not_enforced: typing.Callable[[], T_Result],
        log_connections_not_enabled: typing.Callable[[], T_Result],
        network_restrictions_not_set: typing.Callable[[], T_Result],
        password_requirements_min_length: typing.Callable[[], T_Result],
        pitr_not_enabled: typing.Callable[[], T_Result],
        auth_leaked_password_protection: typing.Callable[[], T_Result],
        auth_insufficient_mfa_options: typing.Callable[[], T_Result],
        auth_password_policy_missing: typing.Callable[[], T_Result],
        leaked_service_key: typing.Callable[[], T_Result],
        no_backup_admin: typing.Callable[[], T_Result],
        vulnerable_postgres_version: typing.Callable[[], T_Result],
        db_not_reachable: typing.Callable[[], T_Result],
        db_connection_failing: typing.Callable[[], T_Result],
        db_connection_limit_reached: typing.Callable[[], T_Result],
        instance_telemetry_lost: typing.Callable[[], T_Result],
        instance_db_down: typing.Callable[[], T_Result],
        instance_alert_firing: typing.Callable[[], T_Result],
        log_data_api_error_rate_high: typing.Callable[[], T_Result],
        log_auth_error_rate_high: typing.Callable[[], T_Result],
        log_storage_error_rate_high: typing.Callable[[], T_Result],
        log_edge_function_error_rate_high: typing.Callable[[], T_Result],
        project_not_active: typing.Callable[[], T_Result],
        advisor_check_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.UNINDEXED_FOREIGN_KEYS:
            return unindexed_foreign_keys()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_USERS_EXPOSED:
            return auth_users_exposed()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_RLS_INITPLAN:
            return auth_rls_initplan()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.NO_PRIMARY_KEY:
            return no_primary_key()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.UNUSED_INDEX:
            return unused_index()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.MULTIPLE_PERMISSIVE_POLICIES:
            return multiple_permissive_policies()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.POLICY_EXISTS_RLS_DISABLED:
            return policy_exists_rls_disabled()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.RLS_ENABLED_NO_POLICY:
            return rls_enabled_no_policy()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.DUPLICATE_INDEX:
            return duplicate_index()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.SECURITY_DEFINER_VIEW:
            return security_definer_view()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.FUNCTION_SEARCH_PATH_MUTABLE:
            return function_search_path_mutable()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.RLS_DISABLED_IN_PUBLIC:
            return rls_disabled_in_public()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.EXTENSION_IN_PUBLIC:
            return extension_in_public()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.RLS_REFERENCES_USER_METADATA:
            return rls_references_user_metadata()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.MATERIALIZED_VIEW_IN_API:
            return materialized_view_in_api()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.FOREIGN_TABLE_IN_API:
            return foreign_table_in_api()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.UNSUPPORTED_REG_TYPES:
            return unsupported_reg_types()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_OTP_LONG_EXPIRY:
            return auth_otp_long_expiry()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_OTP_SHORT_LENGTH:
            return auth_otp_short_length()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.SSL_NOT_ENFORCED:
            return ssl_not_enforced()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LOG_CONNECTIONS_NOT_ENABLED:
            return log_connections_not_enabled()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.NETWORK_RESTRICTIONS_NOT_SET:
            return network_restrictions_not_set()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.PASSWORD_REQUIREMENTS_MIN_LENGTH:
            return password_requirements_min_length()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.PITR_NOT_ENABLED:
            return pitr_not_enabled()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_LEAKED_PASSWORD_PROTECTION:
            return auth_leaked_password_protection()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_INSUFFICIENT_MFA_OPTIONS:
            return auth_insufficient_mfa_options()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.AUTH_PASSWORD_POLICY_MISSING:
            return auth_password_policy_missing()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LEAKED_SERVICE_KEY:
            return leaked_service_key()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.NO_BACKUP_ADMIN:
            return no_backup_admin()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.VULNERABLE_POSTGRES_VERSION:
            return vulnerable_postgres_version()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.DB_NOT_REACHABLE:
            return db_not_reachable()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.DB_CONNECTION_FAILING:
            return db_connection_failing()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.DB_CONNECTION_LIMIT_REACHED:
            return db_connection_limit_reached()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.INSTANCE_TELEMETRY_LOST:
            return instance_telemetry_lost()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.INSTANCE_DB_DOWN:
            return instance_db_down()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.INSTANCE_ALERT_FIRING:
            return instance_alert_firing()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LOG_DATA_API_ERROR_RATE_HIGH:
            return log_data_api_error_rate_high()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LOG_AUTH_ERROR_RATE_HIGH:
            return log_auth_error_rate_high()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LOG_STORAGE_ERROR_RATE_HIGH:
            return log_storage_error_rate_high()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.LOG_EDGE_FUNCTION_ERROR_RATE_HIGH:
            return log_edge_function_error_rate_high()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.PROJECT_NOT_ACTIVE:
            return project_not_active()
        if self is V1ProjectAdvisorsResponseOutputLintsItemName.ADVISOR_CHECK_UNAVAILABLE:
            return advisor_check_unavailable()
