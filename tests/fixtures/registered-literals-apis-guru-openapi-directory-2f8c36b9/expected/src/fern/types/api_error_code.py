

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiErrorCode(enum.StrEnum):
    ERR_REGISTRATION_VERIFICATION_NO_TOKEN = "ERR_REGISTRATION_VERIFICATION_NO_TOKEN"
    ERR_REGISTRATION_VERIFICATION_INVALID_TOKEN = "ERR_REGISTRATION_VERIFICATION_INVALID_TOKEN"
    ERR_REGISTRATION_VERIFICATION_EXPIRED_TOKEN = "ERR_REGISTRATION_VERIFICATION_EXPIRED_TOKEN"
    ERR_AUTHENTICATION_NO_TOKEN = "ERR_AUTHENTICATION_NO_TOKEN"
    ERR_AUTHENTICATION_INVALID_TOKEN = "ERR_AUTHENTICATION_INVALID_TOKEN"
    ERR_AUTHENTICATION_EXPIRED_TOKEN = "ERR_AUTHENTICATION_EXPIRED_TOKEN"
    ERR_AUTHENTICATION_FAILED = "ERR_AUTHENTICATION_FAILED"
    ERR_AUTHORIZATION_MISSING_PRIVILEGES = "ERR_AUTHORIZATION_MISSING_PRIVILEGES"
    ERR_AUTHORIZATION_FORBIDDEN = "ERR_AUTHORIZATION_FORBIDDEN"
    ERR_AUTHORIZATION_REQUIRE_USER = "ERR_AUTHORIZATION_REQUIRE_USER"
    ERR_INPUT_VALIDATION_FAILED = "ERR_INPUT_VALIDATION_FAILED"
    ERR_FIELD_INPUT_VALIDATION_FAILED = "ERR_FIELD_INPUT_VALIDATION_FAILED"
    ERR_VALIDATION_CONSTRAINT_FAILED = "ERR_VALIDATION_CONSTRAINT_FAILED"
    ERR_INPUT_NOT_READABLE = "ERR_INPUT_NOT_READABLE"
    ERR_INVALID_INPUT_PARAMETER = "ERR_INVALID_INPUT_PARAMETER"
    ERR_GUID_CREATION = "ERR_GUID_CREATION"
    ERR_INVALID_ID4N_OBJECT_TYPE = "ERR_INVALID_ID4N_OBJECT_TYPE"
    ERR_MISSING_BILLING_INFORMATION = "ERR_MISSING_BILLING_INFORMATION"
    ERR_COLLECTION_UPDATE_DENIED = "ERR_COLLECTION_UPDATE_DENIED"
    ERR_ENTITY_NOT_FOUND = "ERR_ENTITY_NOT_FOUND"
    ERR_ENTITY_TOO_BIG = "ERR_ENTITY_TOO_BIG"
    ERR_DUPLICATE = "ERR_DUPLICATE"
    ERR_INTERNAL = "ERR_INTERNAL"
    ERR_UNKNOWN = "ERR_UNKNOWN"
    ERR_INVALID_ORGANIZATION_USERROLE = "ERR_INVALID_ORGANIZATION_USERROLE"
    ERR_ORGANIZATION_ROLE_INCONSISTENCY = "ERR_ORGANIZATION_ROLE_INCONSISTENCY"
    ERR_ORGANIZATION_NOT_DELETABLE = "ERR_ORGANIZATION_NOT_DELETABLE"
    ERR_USER_ALREADY_IN_ORGANIZATION = "ERR_USER_ALREADY_IN_ORGANIZATION"
    ERR_USER_INVITATION_NEEDS_MINIMUM_ONE_ROLE = "ERR_USER_INVITATION_NEEDS_MINIMUM_ONE_ROLE"
    ERR_USER_INVITATION_SPECIFY_EMAIL_OR_USERNAME = "ERR_USER_INVITATION_SPECIFY_EMAIL_OR_USERNAME"
    ERR_USER_DEACTIVATED = "ERR_USER_DEACTIVATED"
    ERR_LANGUAGE_NOT_SUPPORTED = "ERR_LANGUAGE_NOT_SUPPORTED"
    ERR_EMAIL_MISSING_TEMPLATE_PARAM = "ERR_EMAIL_MISSING_TEMPLATE_PARAM"
    ERR_EMAIL_TEMPLATE_NOT_AVAILABLE = "ERR_EMAIL_TEMPLATE_NOT_AVAILABLE"
    ERR_EMAIL_PREPARATION_FAILED = "ERR_EMAIL_PREPARATION_FAILED"
    ERR_IMAGE_CONVERSION = "ERR_IMAGE_CONVERSION"
    ERR_UPLOAD_TOO_LARGE = "ERR_UPLOAD_TOO_LARGE"
    ERR_INVALID_ALIAS_TYPE = "ERR_INVALID_ALIAS_TYPE"
    ERR_INVALID_URI_TEMPLATE = "ERR_INVALID_URI_TEMPLATE"
    ERR_INVALID_URI_TEMPLATE_VARIABLE = "ERR_INVALID_URI_TEMPLATE_VARIABLE"
    ERR_INVALID_NAMESPACE = "ERR_INVALID_NAMESPACE"
    ERR_INVALID_PROPERTY_KEY = "ERR_INVALID_PROPERTY_KEY"
    ERR_INVALID_FILTER = "ERR_INVALID_FILTER"
    ERR_NAMESPACE_ALREADY_EXISTS = "ERR_NAMESPACE_ALREADY_EXISTS"
    ERR_INSECURE_PASSWORD = "ERR_INSECURE_PASSWORD"
    ERR_TRANSFER_DENIED = "ERR_TRANSFER_DENIED"
    ERR_INVALID_PHYSICAL_STATE = "ERR_INVALID_PHYSICAL_STATE"
    ERR_INVALID_HISTORY_PROPERTY_NAMESPACE = "ERR_INVALID_HISTORY_PROPERTY_NAMESPACE"
    ERR_INVALID_HISTORY_PROPERTY_VALUE = "ERR_INVALID_HISTORY_PROPERTY_VALUE"
    ERR_ORGA_CANNOT_BE_OWN_PARTNER = "ERR_ORGA_CANNOT_BE_OWN_PARTNER"
    ERR_INVALID_GS1CODE = "ERR_INVALID_GS1_CODE"
    ERR_INVALID_GS1CHAR_IN_CODE = "ERR_INVALID_GS1_CHAR_IN_CODE"
    ERR_INVALID_GS1CODE_NOT_UNIQUE = "ERR_INVALID_GS1_CODE_NOT_UNIQUE"
    ERR_INVALID_GS1GTIN = "ERR_INVALID_GS1_GTIN"
    ERR_GS1CODE_CURRENTLY_UNSUPPORTED = "ERR_GS1_CODE_CURRENTLY_UNSUPPORTED"

    def visit(
        self,
        err_registration_verification_no_token: typing.Callable[[], T_Result],
        err_registration_verification_invalid_token: typing.Callable[[], T_Result],
        err_registration_verification_expired_token: typing.Callable[[], T_Result],
        err_authentication_no_token: typing.Callable[[], T_Result],
        err_authentication_invalid_token: typing.Callable[[], T_Result],
        err_authentication_expired_token: typing.Callable[[], T_Result],
        err_authentication_failed: typing.Callable[[], T_Result],
        err_authorization_missing_privileges: typing.Callable[[], T_Result],
        err_authorization_forbidden: typing.Callable[[], T_Result],
        err_authorization_require_user: typing.Callable[[], T_Result],
        err_input_validation_failed: typing.Callable[[], T_Result],
        err_field_input_validation_failed: typing.Callable[[], T_Result],
        err_validation_constraint_failed: typing.Callable[[], T_Result],
        err_input_not_readable: typing.Callable[[], T_Result],
        err_invalid_input_parameter: typing.Callable[[], T_Result],
        err_guid_creation: typing.Callable[[], T_Result],
        err_invalid_id4n_object_type: typing.Callable[[], T_Result],
        err_missing_billing_information: typing.Callable[[], T_Result],
        err_collection_update_denied: typing.Callable[[], T_Result],
        err_entity_not_found: typing.Callable[[], T_Result],
        err_entity_too_big: typing.Callable[[], T_Result],
        err_duplicate: typing.Callable[[], T_Result],
        err_internal: typing.Callable[[], T_Result],
        err_unknown: typing.Callable[[], T_Result],
        err_invalid_organization_userrole: typing.Callable[[], T_Result],
        err_organization_role_inconsistency: typing.Callable[[], T_Result],
        err_organization_not_deletable: typing.Callable[[], T_Result],
        err_user_already_in_organization: typing.Callable[[], T_Result],
        err_user_invitation_needs_minimum_one_role: typing.Callable[[], T_Result],
        err_user_invitation_specify_email_or_username: typing.Callable[[], T_Result],
        err_user_deactivated: typing.Callable[[], T_Result],
        err_language_not_supported: typing.Callable[[], T_Result],
        err_email_missing_template_param: typing.Callable[[], T_Result],
        err_email_template_not_available: typing.Callable[[], T_Result],
        err_email_preparation_failed: typing.Callable[[], T_Result],
        err_image_conversion: typing.Callable[[], T_Result],
        err_upload_too_large: typing.Callable[[], T_Result],
        err_invalid_alias_type: typing.Callable[[], T_Result],
        err_invalid_uri_template: typing.Callable[[], T_Result],
        err_invalid_uri_template_variable: typing.Callable[[], T_Result],
        err_invalid_namespace: typing.Callable[[], T_Result],
        err_invalid_property_key: typing.Callable[[], T_Result],
        err_invalid_filter: typing.Callable[[], T_Result],
        err_namespace_already_exists: typing.Callable[[], T_Result],
        err_insecure_password: typing.Callable[[], T_Result],
        err_transfer_denied: typing.Callable[[], T_Result],
        err_invalid_physical_state: typing.Callable[[], T_Result],
        err_invalid_history_property_namespace: typing.Callable[[], T_Result],
        err_invalid_history_property_value: typing.Callable[[], T_Result],
        err_orga_cannot_be_own_partner: typing.Callable[[], T_Result],
        err_invalid_gs1code: typing.Callable[[], T_Result],
        err_invalid_gs1char_in_code: typing.Callable[[], T_Result],
        err_invalid_gs1code_not_unique: typing.Callable[[], T_Result],
        err_invalid_gs1gtin: typing.Callable[[], T_Result],
        err_gs1code_currently_unsupported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiErrorCode.ERR_REGISTRATION_VERIFICATION_NO_TOKEN:
            return err_registration_verification_no_token()
        if self is ApiErrorCode.ERR_REGISTRATION_VERIFICATION_INVALID_TOKEN:
            return err_registration_verification_invalid_token()
        if self is ApiErrorCode.ERR_REGISTRATION_VERIFICATION_EXPIRED_TOKEN:
            return err_registration_verification_expired_token()
        if self is ApiErrorCode.ERR_AUTHENTICATION_NO_TOKEN:
            return err_authentication_no_token()
        if self is ApiErrorCode.ERR_AUTHENTICATION_INVALID_TOKEN:
            return err_authentication_invalid_token()
        if self is ApiErrorCode.ERR_AUTHENTICATION_EXPIRED_TOKEN:
            return err_authentication_expired_token()
        if self is ApiErrorCode.ERR_AUTHENTICATION_FAILED:
            return err_authentication_failed()
        if self is ApiErrorCode.ERR_AUTHORIZATION_MISSING_PRIVILEGES:
            return err_authorization_missing_privileges()
        if self is ApiErrorCode.ERR_AUTHORIZATION_FORBIDDEN:
            return err_authorization_forbidden()
        if self is ApiErrorCode.ERR_AUTHORIZATION_REQUIRE_USER:
            return err_authorization_require_user()
        if self is ApiErrorCode.ERR_INPUT_VALIDATION_FAILED:
            return err_input_validation_failed()
        if self is ApiErrorCode.ERR_FIELD_INPUT_VALIDATION_FAILED:
            return err_field_input_validation_failed()
        if self is ApiErrorCode.ERR_VALIDATION_CONSTRAINT_FAILED:
            return err_validation_constraint_failed()
        if self is ApiErrorCode.ERR_INPUT_NOT_READABLE:
            return err_input_not_readable()
        if self is ApiErrorCode.ERR_INVALID_INPUT_PARAMETER:
            return err_invalid_input_parameter()
        if self is ApiErrorCode.ERR_GUID_CREATION:
            return err_guid_creation()
        if self is ApiErrorCode.ERR_INVALID_ID4N_OBJECT_TYPE:
            return err_invalid_id4n_object_type()
        if self is ApiErrorCode.ERR_MISSING_BILLING_INFORMATION:
            return err_missing_billing_information()
        if self is ApiErrorCode.ERR_COLLECTION_UPDATE_DENIED:
            return err_collection_update_denied()
        if self is ApiErrorCode.ERR_ENTITY_NOT_FOUND:
            return err_entity_not_found()
        if self is ApiErrorCode.ERR_ENTITY_TOO_BIG:
            return err_entity_too_big()
        if self is ApiErrorCode.ERR_DUPLICATE:
            return err_duplicate()
        if self is ApiErrorCode.ERR_INTERNAL:
            return err_internal()
        if self is ApiErrorCode.ERR_UNKNOWN:
            return err_unknown()
        if self is ApiErrorCode.ERR_INVALID_ORGANIZATION_USERROLE:
            return err_invalid_organization_userrole()
        if self is ApiErrorCode.ERR_ORGANIZATION_ROLE_INCONSISTENCY:
            return err_organization_role_inconsistency()
        if self is ApiErrorCode.ERR_ORGANIZATION_NOT_DELETABLE:
            return err_organization_not_deletable()
        if self is ApiErrorCode.ERR_USER_ALREADY_IN_ORGANIZATION:
            return err_user_already_in_organization()
        if self is ApiErrorCode.ERR_USER_INVITATION_NEEDS_MINIMUM_ONE_ROLE:
            return err_user_invitation_needs_minimum_one_role()
        if self is ApiErrorCode.ERR_USER_INVITATION_SPECIFY_EMAIL_OR_USERNAME:
            return err_user_invitation_specify_email_or_username()
        if self is ApiErrorCode.ERR_USER_DEACTIVATED:
            return err_user_deactivated()
        if self is ApiErrorCode.ERR_LANGUAGE_NOT_SUPPORTED:
            return err_language_not_supported()
        if self is ApiErrorCode.ERR_EMAIL_MISSING_TEMPLATE_PARAM:
            return err_email_missing_template_param()
        if self is ApiErrorCode.ERR_EMAIL_TEMPLATE_NOT_AVAILABLE:
            return err_email_template_not_available()
        if self is ApiErrorCode.ERR_EMAIL_PREPARATION_FAILED:
            return err_email_preparation_failed()
        if self is ApiErrorCode.ERR_IMAGE_CONVERSION:
            return err_image_conversion()
        if self is ApiErrorCode.ERR_UPLOAD_TOO_LARGE:
            return err_upload_too_large()
        if self is ApiErrorCode.ERR_INVALID_ALIAS_TYPE:
            return err_invalid_alias_type()
        if self is ApiErrorCode.ERR_INVALID_URI_TEMPLATE:
            return err_invalid_uri_template()
        if self is ApiErrorCode.ERR_INVALID_URI_TEMPLATE_VARIABLE:
            return err_invalid_uri_template_variable()
        if self is ApiErrorCode.ERR_INVALID_NAMESPACE:
            return err_invalid_namespace()
        if self is ApiErrorCode.ERR_INVALID_PROPERTY_KEY:
            return err_invalid_property_key()
        if self is ApiErrorCode.ERR_INVALID_FILTER:
            return err_invalid_filter()
        if self is ApiErrorCode.ERR_NAMESPACE_ALREADY_EXISTS:
            return err_namespace_already_exists()
        if self is ApiErrorCode.ERR_INSECURE_PASSWORD:
            return err_insecure_password()
        if self is ApiErrorCode.ERR_TRANSFER_DENIED:
            return err_transfer_denied()
        if self is ApiErrorCode.ERR_INVALID_PHYSICAL_STATE:
            return err_invalid_physical_state()
        if self is ApiErrorCode.ERR_INVALID_HISTORY_PROPERTY_NAMESPACE:
            return err_invalid_history_property_namespace()
        if self is ApiErrorCode.ERR_INVALID_HISTORY_PROPERTY_VALUE:
            return err_invalid_history_property_value()
        if self is ApiErrorCode.ERR_ORGA_CANNOT_BE_OWN_PARTNER:
            return err_orga_cannot_be_own_partner()
        if self is ApiErrorCode.ERR_INVALID_GS1CODE:
            return err_invalid_gs1code()
        if self is ApiErrorCode.ERR_INVALID_GS1CHAR_IN_CODE:
            return err_invalid_gs1char_in_code()
        if self is ApiErrorCode.ERR_INVALID_GS1CODE_NOT_UNIQUE:
            return err_invalid_gs1code_not_unique()
        if self is ApiErrorCode.ERR_INVALID_GS1GTIN:
            return err_invalid_gs1gtin()
        if self is ApiErrorCode.ERR_GS1CODE_CURRENTLY_UNSUPPORTED:
            return err_gs1code_currently_unsupported()
