

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey(enum.StrEnum):
    INSTANCES_COMPUTE_UPDATE_AVAILABLE_SIZES = "instances.compute_update_available_sizes"
    INSTANCES_READ_REPLICAS = "instances.read_replicas"
    INSTANCES_DISK_MODIFICATIONS = "instances.disk_modifications"
    INSTANCES_HIGH_AVAILABILITY = "instances.high_availability"
    INSTANCES_ORIOLEDB = "instances.orioledb"
    REPLICATION_ETL = "replication.etl"
    STORAGE_MAX_FILE_SIZE = "storage.max_file_size"
    STORAGE_MAX_FILE_SIZE_CONFIGURABLE = "storage.max_file_size.configurable"
    STORAGE_IMAGE_TRANSFORMATIONS = "storage.image_transformations"
    STORAGE_VECTOR_BUCKETS = "storage.vector_buckets"
    STORAGE_ICEBERG_CATALOG = "storage.iceberg_catalog"
    STORAGE_PURGE_CACHE = "storage.purge_cache"
    SECURITY_AUDIT_LOGS_DAYS = "security.audit_logs_days"
    SECURITY_QUESTIONNAIRE = "security.questionnaire"
    SECURITY_SOC2REPORT = "security.soc2_report"
    SECURITY_ISO27001CERTIFICATE = "security.iso27001_certificate"
    SECURITY_PRIVATE_LINK = "security.private_link"
    SECURITY_ENFORCE_MFA = "security.enforce_mfa"
    LOG_RETENTION_DAYS = "log.retention_days"
    CUSTOM_DOMAIN = "custom_domain"
    VANITY_SUBDOMAIN = "vanity_subdomain"
    IPV4 = "ipv4"
    PITR_AVAILABLE_VARIANTS = "pitr.available_variants"
    LOG_DRAINS = "log_drains"
    AUDIT_LOG_DRAINS = "audit_log_drains"
    BRANCHING_LIMIT = "branching_limit"
    BRANCHING_PERSISTENT = "branching_persistent"
    AUTH_MFA_PHONE = "auth.mfa_phone"
    AUTH_MFA_WEB_AUTHN = "auth.mfa_web_authn"
    AUTH_MFA_ENHANCED_SECURITY = "auth.mfa_enhanced_security"
    AUTH_HOOKS = "auth.hooks"
    AUTH_PLATFORM_SSO = "auth.platform.sso"
    AUTH_CUSTOM_JWT_TEMPLATE = "auth.custom_jwt_template"
    AUTH_SAML2 = "auth.saml_2"
    AUTH_USER_SESSIONS = "auth.user_sessions"
    AUTH_LEAKED_PASSWORD_PROTECTION = "auth.leaked_password_protection"
    AUTH_ADVANCED_AUTH_SETTINGS = "auth.advanced_auth_settings"
    AUTH_PERFORMANCE_SETTINGS = "auth.performance_settings"
    AUTH_PASSWORD_HIBP = "auth.password_hibp"
    AUTH_CUSTOM_OAUTH_MAX_PROVIDERS = "auth.custom_oauth.max_providers"
    BACKUP_RETENTION_DAYS = "backup.retention_days"
    BACKUP_RESTORE_TO_NEW_PROJECT = "backup.restore_to_new_project"
    BACKUP_SCHEDULE = "backup.schedule"
    FUNCTION_MAX_COUNT = "function.max_count"
    FUNCTION_SIZE_LIMIT_MB = "function.size_limit_mb"
    REALTIME_MAX_CONCURRENT_USERS = "realtime.max_concurrent_users"
    REALTIME_MAX_EVENTS_PER_SECOND = "realtime.max_events_per_second"
    REALTIME_MAX_JOINS_PER_SECOND = "realtime.max_joins_per_second"
    REALTIME_MAX_CHANNELS_PER_CLIENT = "realtime.max_channels_per_client"
    REALTIME_MAX_BYTES_PER_SECOND = "realtime.max_bytes_per_second"
    REALTIME_MAX_PRESENCE_EVENTS_PER_SECOND = "realtime.max_presence_events_per_second"
    REALTIME_MAX_PAYLOAD_SIZE_IN_KB = "realtime.max_payload_size_in_kb"
    PROJECT_SCOPED_ROLES = "project_scoped_roles"
    SECURITY_MEMBER_ROLES = "security.member_roles"
    PROJECT_PAUSING = "project_pausing"
    PROJECT_CLONING = "project_cloning"
    PROJECT_RESTORE_AFTER_EXPIRY = "project_restore_after_expiry"
    ASSISTANT_ADVANCE_MODEL = "assistant.advance_model"
    INTEGRATIONS_GITHUB_CONNECTIONS = "integrations.github_connections"
    INTEGRATIONS_GITHUB_PUSH_WEBHOOKS_LIMIT = "integrations.github_push_webhooks_limit"
    DEDICATED_POOLER = "dedicated_pooler"
    OBSERVABILITY_DASHBOARD_ADVANCED_METRICS = "observability.dashboard_advanced_metrics"
    API_MEMBERS_INVITATIONS = "api.members.invitations"
    API_MEMBERS_ROLES = "api.members.roles"

    def visit(
        self,
        instances_compute_update_available_sizes: typing.Callable[[], T_Result],
        instances_read_replicas: typing.Callable[[], T_Result],
        instances_disk_modifications: typing.Callable[[], T_Result],
        instances_high_availability: typing.Callable[[], T_Result],
        instances_orioledb: typing.Callable[[], T_Result],
        replication_etl: typing.Callable[[], T_Result],
        storage_max_file_size: typing.Callable[[], T_Result],
        storage_max_file_size_configurable: typing.Callable[[], T_Result],
        storage_image_transformations: typing.Callable[[], T_Result],
        storage_vector_buckets: typing.Callable[[], T_Result],
        storage_iceberg_catalog: typing.Callable[[], T_Result],
        storage_purge_cache: typing.Callable[[], T_Result],
        security_audit_logs_days: typing.Callable[[], T_Result],
        security_questionnaire: typing.Callable[[], T_Result],
        security_soc2report: typing.Callable[[], T_Result],
        security_iso27001certificate: typing.Callable[[], T_Result],
        security_private_link: typing.Callable[[], T_Result],
        security_enforce_mfa: typing.Callable[[], T_Result],
        log_retention_days: typing.Callable[[], T_Result],
        custom_domain: typing.Callable[[], T_Result],
        vanity_subdomain: typing.Callable[[], T_Result],
        ipv4: typing.Callable[[], T_Result],
        pitr_available_variants: typing.Callable[[], T_Result],
        log_drains: typing.Callable[[], T_Result],
        audit_log_drains: typing.Callable[[], T_Result],
        branching_limit: typing.Callable[[], T_Result],
        branching_persistent: typing.Callable[[], T_Result],
        auth_mfa_phone: typing.Callable[[], T_Result],
        auth_mfa_web_authn: typing.Callable[[], T_Result],
        auth_mfa_enhanced_security: typing.Callable[[], T_Result],
        auth_hooks: typing.Callable[[], T_Result],
        auth_platform_sso: typing.Callable[[], T_Result],
        auth_custom_jwt_template: typing.Callable[[], T_Result],
        auth_saml2: typing.Callable[[], T_Result],
        auth_user_sessions: typing.Callable[[], T_Result],
        auth_leaked_password_protection: typing.Callable[[], T_Result],
        auth_advanced_auth_settings: typing.Callable[[], T_Result],
        auth_performance_settings: typing.Callable[[], T_Result],
        auth_password_hibp: typing.Callable[[], T_Result],
        auth_custom_oauth_max_providers: typing.Callable[[], T_Result],
        backup_retention_days: typing.Callable[[], T_Result],
        backup_restore_to_new_project: typing.Callable[[], T_Result],
        backup_schedule: typing.Callable[[], T_Result],
        function_max_count: typing.Callable[[], T_Result],
        function_size_limit_mb: typing.Callable[[], T_Result],
        realtime_max_concurrent_users: typing.Callable[[], T_Result],
        realtime_max_events_per_second: typing.Callable[[], T_Result],
        realtime_max_joins_per_second: typing.Callable[[], T_Result],
        realtime_max_channels_per_client: typing.Callable[[], T_Result],
        realtime_max_bytes_per_second: typing.Callable[[], T_Result],
        realtime_max_presence_events_per_second: typing.Callable[[], T_Result],
        realtime_max_payload_size_in_kb: typing.Callable[[], T_Result],
        project_scoped_roles: typing.Callable[[], T_Result],
        security_member_roles: typing.Callable[[], T_Result],
        project_pausing: typing.Callable[[], T_Result],
        project_cloning: typing.Callable[[], T_Result],
        project_restore_after_expiry: typing.Callable[[], T_Result],
        assistant_advance_model: typing.Callable[[], T_Result],
        integrations_github_connections: typing.Callable[[], T_Result],
        integrations_github_push_webhooks_limit: typing.Callable[[], T_Result],
        dedicated_pooler: typing.Callable[[], T_Result],
        observability_dashboard_advanced_metrics: typing.Callable[[], T_Result],
        api_members_invitations: typing.Callable[[], T_Result],
        api_members_roles: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INSTANCES_COMPUTE_UPDATE_AVAILABLE_SIZES:
            return instances_compute_update_available_sizes()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INSTANCES_READ_REPLICAS:
            return instances_read_replicas()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INSTANCES_DISK_MODIFICATIONS:
            return instances_disk_modifications()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INSTANCES_HIGH_AVAILABILITY:
            return instances_high_availability()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INSTANCES_ORIOLEDB:
            return instances_orioledb()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REPLICATION_ETL:
            return replication_etl()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_MAX_FILE_SIZE:
            return storage_max_file_size()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_MAX_FILE_SIZE_CONFIGURABLE:
            return storage_max_file_size_configurable()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_IMAGE_TRANSFORMATIONS:
            return storage_image_transformations()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_VECTOR_BUCKETS:
            return storage_vector_buckets()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_ICEBERG_CATALOG:
            return storage_iceberg_catalog()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.STORAGE_PURGE_CACHE:
            return storage_purge_cache()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_AUDIT_LOGS_DAYS:
            return security_audit_logs_days()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_QUESTIONNAIRE:
            return security_questionnaire()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_SOC2REPORT:
            return security_soc2report()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_ISO27001CERTIFICATE:
            return security_iso27001certificate()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_PRIVATE_LINK:
            return security_private_link()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_ENFORCE_MFA:
            return security_enforce_mfa()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.LOG_RETENTION_DAYS:
            return log_retention_days()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.CUSTOM_DOMAIN:
            return custom_domain()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.VANITY_SUBDOMAIN:
            return vanity_subdomain()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.IPV4:
            return ipv4()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.PITR_AVAILABLE_VARIANTS:
            return pitr_available_variants()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.LOG_DRAINS:
            return log_drains()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUDIT_LOG_DRAINS:
            return audit_log_drains()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.BRANCHING_LIMIT:
            return branching_limit()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.BRANCHING_PERSISTENT:
            return branching_persistent()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_MFA_PHONE:
            return auth_mfa_phone()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_MFA_WEB_AUTHN:
            return auth_mfa_web_authn()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_MFA_ENHANCED_SECURITY:
            return auth_mfa_enhanced_security()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_HOOKS:
            return auth_hooks()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_PLATFORM_SSO:
            return auth_platform_sso()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_CUSTOM_JWT_TEMPLATE:
            return auth_custom_jwt_template()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_SAML2:
            return auth_saml2()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_USER_SESSIONS:
            return auth_user_sessions()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_LEAKED_PASSWORD_PROTECTION:
            return auth_leaked_password_protection()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_ADVANCED_AUTH_SETTINGS:
            return auth_advanced_auth_settings()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_PERFORMANCE_SETTINGS:
            return auth_performance_settings()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_PASSWORD_HIBP:
            return auth_password_hibp()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.AUTH_CUSTOM_OAUTH_MAX_PROVIDERS:
            return auth_custom_oauth_max_providers()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.BACKUP_RETENTION_DAYS:
            return backup_retention_days()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.BACKUP_RESTORE_TO_NEW_PROJECT:
            return backup_restore_to_new_project()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.BACKUP_SCHEDULE:
            return backup_schedule()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.FUNCTION_MAX_COUNT:
            return function_max_count()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.FUNCTION_SIZE_LIMIT_MB:
            return function_size_limit_mb()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_CONCURRENT_USERS:
            return realtime_max_concurrent_users()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_EVENTS_PER_SECOND:
            return realtime_max_events_per_second()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_JOINS_PER_SECOND:
            return realtime_max_joins_per_second()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_CHANNELS_PER_CLIENT:
            return realtime_max_channels_per_client()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_BYTES_PER_SECOND:
            return realtime_max_bytes_per_second()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_PRESENCE_EVENTS_PER_SECOND:
            return realtime_max_presence_events_per_second()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.REALTIME_MAX_PAYLOAD_SIZE_IN_KB:
            return realtime_max_payload_size_in_kb()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.PROJECT_SCOPED_ROLES:
            return project_scoped_roles()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.SECURITY_MEMBER_ROLES:
            return security_member_roles()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.PROJECT_PAUSING:
            return project_pausing()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.PROJECT_CLONING:
            return project_cloning()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.PROJECT_RESTORE_AFTER_EXPIRY:
            return project_restore_after_expiry()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.ASSISTANT_ADVANCE_MODEL:
            return assistant_advance_model()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INTEGRATIONS_GITHUB_CONNECTIONS:
            return integrations_github_connections()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.INTEGRATIONS_GITHUB_PUSH_WEBHOOKS_LIMIT:
            return integrations_github_push_webhooks_limit()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.DEDICATED_POOLER:
            return dedicated_pooler()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.OBSERVABILITY_DASHBOARD_ADVANCED_METRICS:
            return observability_dashboard_advanced_metrics()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.API_MEMBERS_INVITATIONS:
            return api_members_invitations()
        if self is V1ListEntitlementsResponseOutputEntitlementsItemFeatureKey.API_MEMBERS_ROLES:
            return api_members_roles()
