

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorCode(enum.StrEnum):
    """
    Indicates the specific error that occurred during a request to a
    Square API.
    """

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    UNAUTHORIZED = "UNAUTHORIZED"
    ACCESS_TOKEN_EXPIRED = "ACCESS_TOKEN_EXPIRED"
    ACCESS_TOKEN_REVOKED = "ACCESS_TOKEN_REVOKED"
    CLIENT_DISABLED = "CLIENT_DISABLED"
    FORBIDDEN = "FORBIDDEN"
    INSUFFICIENT_SCOPES = "INSUFFICIENT_SCOPES"
    APPLICATION_DISABLED = "APPLICATION_DISABLED"
    V1APPLICATION = "V1_APPLICATION"
    V1ACCESS_TOKEN = "V1_ACCESS_TOKEN"
    CARD_PROCESSING_NOT_ENABLED = "CARD_PROCESSING_NOT_ENABLED"
    MERCHANT_SUBSCRIPTION_NOT_FOUND = "MERCHANT_SUBSCRIPTION_NOT_FOUND"
    BAD_REQUEST = "BAD_REQUEST"
    MISSING_REQUIRED_PARAMETER = "MISSING_REQUIRED_PARAMETER"
    INCORRECT_TYPE = "INCORRECT_TYPE"
    INVALID_TIME = "INVALID_TIME"
    INVALID_TIME_RANGE = "INVALID_TIME_RANGE"
    INVALID_VALUE = "INVALID_VALUE"
    INVALID_CURSOR = "INVALID_CURSOR"
    UNKNOWN_QUERY_PARAMETER = "UNKNOWN_QUERY_PARAMETER"
    CONFLICTING_PARAMETERS = "CONFLICTING_PARAMETERS"
    EXPECTED_JSON_BODY = "EXPECTED_JSON_BODY"
    INVALID_SORT_ORDER = "INVALID_SORT_ORDER"
    VALUE_REGEX_MISMATCH = "VALUE_REGEX_MISMATCH"
    VALUE_TOO_SHORT = "VALUE_TOO_SHORT"
    VALUE_TOO_LONG = "VALUE_TOO_LONG"
    VALUE_TOO_LOW = "VALUE_TOO_LOW"
    VALUE_TOO_HIGH = "VALUE_TOO_HIGH"
    VALUE_EMPTY = "VALUE_EMPTY"
    ARRAY_LENGTH_TOO_LONG = "ARRAY_LENGTH_TOO_LONG"
    ARRAY_LENGTH_TOO_SHORT = "ARRAY_LENGTH_TOO_SHORT"
    ARRAY_EMPTY = "ARRAY_EMPTY"
    EXPECTED_BOOLEAN = "EXPECTED_BOOLEAN"
    EXPECTED_INTEGER = "EXPECTED_INTEGER"
    EXPECTED_FLOAT = "EXPECTED_FLOAT"
    EXPECTED_STRING = "EXPECTED_STRING"
    EXPECTED_OBJECT = "EXPECTED_OBJECT"
    EXPECTED_ARRAY = "EXPECTED_ARRAY"
    EXPECTED_MAP = "EXPECTED_MAP"
    EXPECTED_BASE64ENCODED_BYTE_ARRAY = "EXPECTED_BASE64_ENCODED_BYTE_ARRAY"
    INVALID_ARRAY_VALUE = "INVALID_ARRAY_VALUE"
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    INVALID_CONTENT_TYPE = "INVALID_CONTENT_TYPE"
    INVALID_FORM_VALUE = "INVALID_FORM_VALUE"
    CUSTOMER_NOT_FOUND = "CUSTOMER_NOT_FOUND"
    ONE_INSTRUMENT_EXPECTED = "ONE_INSTRUMENT_EXPECTED"
    NO_FIELDS_SET = "NO_FIELDS_SET"
    TOO_MANY_MAP_ENTRIES = "TOO_MANY_MAP_ENTRIES"
    MAP_KEY_LENGTH_TOO_SHORT = "MAP_KEY_LENGTH_TOO_SHORT"
    MAP_KEY_LENGTH_TOO_LONG = "MAP_KEY_LENGTH_TOO_LONG"
    CARD_EXPIRED = "CARD_EXPIRED"
    INVALID_EXPIRATION = "INVALID_EXPIRATION"
    INVALID_EXPIRATION_YEAR = "INVALID_EXPIRATION_YEAR"
    INVALID_EXPIRATION_DATE = "INVALID_EXPIRATION_DATE"
    UNSUPPORTED_CARD_BRAND = "UNSUPPORTED_CARD_BRAND"
    UNSUPPORTED_ENTRY_METHOD = "UNSUPPORTED_ENTRY_METHOD"
    INVALID_ENCRYPTED_CARD = "INVALID_ENCRYPTED_CARD"
    INVALID_CARD = "INVALID_CARD"
    GENERIC_DECLINE = "GENERIC_DECLINE"
    CVV_FAILURE = "CVV_FAILURE"
    ADDRESS_VERIFICATION_FAILURE = "ADDRESS_VERIFICATION_FAILURE"
    INVALID_ACCOUNT = "INVALID_ACCOUNT"
    CURRENCY_MISMATCH = "CURRENCY_MISMATCH"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    INSUFFICIENT_PERMISSIONS = "INSUFFICIENT_PERMISSIONS"
    CARDHOLDER_INSUFFICIENT_PERMISSIONS = "CARDHOLDER_INSUFFICIENT_PERMISSIONS"
    INVALID_LOCATION = "INVALID_LOCATION"
    TRANSACTION_LIMIT = "TRANSACTION_LIMIT"
    VOICE_FAILURE = "VOICE_FAILURE"
    PAN_FAILURE = "PAN_FAILURE"
    EXPIRATION_FAILURE = "EXPIRATION_FAILURE"
    CARD_NOT_SUPPORTED = "CARD_NOT_SUPPORTED"
    INVALID_PIN = "INVALID_PIN"
    MISSING_PIN = "MISSING_PIN"
    MISSING_ACCOUNT_TYPE = "MISSING_ACCOUNT_TYPE"
    INVALID_POSTAL_CODE = "INVALID_POSTAL_CODE"
    INVALID_FEES = "INVALID_FEES"
    MANUALLY_ENTERED_PAYMENT_NOT_SUPPORTED = "MANUALLY_ENTERED_PAYMENT_NOT_SUPPORTED"
    PAYMENT_LIMIT_EXCEEDED = "PAYMENT_LIMIT_EXCEEDED"
    GIFT_CARD_AVAILABLE_AMOUNT = "GIFT_CARD_AVAILABLE_AMOUNT"
    ACCOUNT_UNUSABLE = "ACCOUNT_UNUSABLE"
    BUYER_REFUSED_PAYMENT = "BUYER_REFUSED_PAYMENT"
    DELAYED_TRANSACTION_EXPIRED = "DELAYED_TRANSACTION_EXPIRED"
    DELAYED_TRANSACTION_CANCELED = "DELAYED_TRANSACTION_CANCELED"
    DELAYED_TRANSACTION_CAPTURED = "DELAYED_TRANSACTION_CAPTURED"
    DELAYED_TRANSACTION_FAILED = "DELAYED_TRANSACTION_FAILED"
    CARD_TOKEN_EXPIRED = "CARD_TOKEN_EXPIRED"
    CARD_TOKEN_USED = "CARD_TOKEN_USED"
    AMOUNT_TOO_HIGH = "AMOUNT_TOO_HIGH"
    UNSUPPORTED_INSTRUMENT_TYPE = "UNSUPPORTED_INSTRUMENT_TYPE"
    REFUND_AMOUNT_INVALID = "REFUND_AMOUNT_INVALID"
    REFUND_ALREADY_PENDING = "REFUND_ALREADY_PENDING"
    PAYMENT_NOT_REFUNDABLE = "PAYMENT_NOT_REFUNDABLE"
    REFUND_DECLINED = "REFUND_DECLINED"
    INVALID_CARD_DATA = "INVALID_CARD_DATA"
    SOURCE_USED = "SOURCE_USED"
    SOURCE_EXPIRED = "SOURCE_EXPIRED"
    UNSUPPORTED_LOYALTY_REWARD_TIER = "UNSUPPORTED_LOYALTY_REWARD_TIER"
    LOCATION_MISMATCH = "LOCATION_MISMATCH"
    IDEMPOTENCY_KEY_REUSED = "IDEMPOTENCY_KEY_REUSED"
    UNEXPECTED_VALUE = "UNEXPECTED_VALUE"
    SANDBOX_NOT_SUPPORTED = "SANDBOX_NOT_SUPPORTED"
    INVALID_EMAIL_ADDRESS = "INVALID_EMAIL_ADDRESS"
    INVALID_PHONE_NUMBER = "INVALID_PHONE_NUMBER"
    CHECKOUT_EXPIRED = "CHECKOUT_EXPIRED"
    BAD_CERTIFICATE = "BAD_CERTIFICATE"
    INVALID_SQUARE_VERSION_FORMAT = "INVALID_SQUARE_VERSION_FORMAT"
    API_VERSION_INCOMPATIBLE = "API_VERSION_INCOMPATIBLE"
    CARD_DECLINED = "CARD_DECLINED"
    VERIFY_CVV_FAILURE = "VERIFY_CVV_FAILURE"
    VERIFY_AVS_FAILURE = "VERIFY_AVS_FAILURE"
    CARD_DECLINED_CALL_ISSUER = "CARD_DECLINED_CALL_ISSUER"
    CARD_DECLINED_VERIFICATION_REQUIRED = "CARD_DECLINED_VERIFICATION_REQUIRED"
    BAD_EXPIRATION = "BAD_EXPIRATION"
    CHIP_INSERTION_REQUIRED = "CHIP_INSERTION_REQUIRED"
    ALLOWABLE_PIN_TRIES_EXCEEDED = "ALLOWABLE_PIN_TRIES_EXCEEDED"
    RESERVATION_DECLINED = "RESERVATION_DECLINED"
    NOT_FOUND = "NOT_FOUND"
    APPLE_PAYMENT_PROCESSING_CERTIFICATE_HASH_NOT_FOUND = "APPLE_PAYMENT_PROCESSING_CERTIFICATE_HASH_NOT_FOUND"
    METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    CONFLICT = "CONFLICT"
    GONE = "GONE"
    REQUEST_ENTITY_TOO_LARGE = "REQUEST_ENTITY_TOO_LARGE"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"
    RATE_LIMITED = "RATE_LIMITED"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    BAD_GATEWAY = "BAD_GATEWAY"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    TEMPORARY_ERROR = "TEMPORARY_ERROR"
    GATEWAY_TIMEOUT = "GATEWAY_TIMEOUT"

    def visit(
        self,
        internal_server_error: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
        access_token_expired: typing.Callable[[], T_Result],
        access_token_revoked: typing.Callable[[], T_Result],
        client_disabled: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        insufficient_scopes: typing.Callable[[], T_Result],
        application_disabled: typing.Callable[[], T_Result],
        v1application: typing.Callable[[], T_Result],
        v1access_token: typing.Callable[[], T_Result],
        card_processing_not_enabled: typing.Callable[[], T_Result],
        merchant_subscription_not_found: typing.Callable[[], T_Result],
        bad_request: typing.Callable[[], T_Result],
        missing_required_parameter: typing.Callable[[], T_Result],
        incorrect_type: typing.Callable[[], T_Result],
        invalid_time: typing.Callable[[], T_Result],
        invalid_time_range: typing.Callable[[], T_Result],
        invalid_value: typing.Callable[[], T_Result],
        invalid_cursor: typing.Callable[[], T_Result],
        unknown_query_parameter: typing.Callable[[], T_Result],
        conflicting_parameters: typing.Callable[[], T_Result],
        expected_json_body: typing.Callable[[], T_Result],
        invalid_sort_order: typing.Callable[[], T_Result],
        value_regex_mismatch: typing.Callable[[], T_Result],
        value_too_short: typing.Callable[[], T_Result],
        value_too_long: typing.Callable[[], T_Result],
        value_too_low: typing.Callable[[], T_Result],
        value_too_high: typing.Callable[[], T_Result],
        value_empty: typing.Callable[[], T_Result],
        array_length_too_long: typing.Callable[[], T_Result],
        array_length_too_short: typing.Callable[[], T_Result],
        array_empty: typing.Callable[[], T_Result],
        expected_boolean: typing.Callable[[], T_Result],
        expected_integer: typing.Callable[[], T_Result],
        expected_float: typing.Callable[[], T_Result],
        expected_string: typing.Callable[[], T_Result],
        expected_object: typing.Callable[[], T_Result],
        expected_array: typing.Callable[[], T_Result],
        expected_map: typing.Callable[[], T_Result],
        expected_base64encoded_byte_array: typing.Callable[[], T_Result],
        invalid_array_value: typing.Callable[[], T_Result],
        invalid_enum_value: typing.Callable[[], T_Result],
        invalid_content_type: typing.Callable[[], T_Result],
        invalid_form_value: typing.Callable[[], T_Result],
        customer_not_found: typing.Callable[[], T_Result],
        one_instrument_expected: typing.Callable[[], T_Result],
        no_fields_set: typing.Callable[[], T_Result],
        too_many_map_entries: typing.Callable[[], T_Result],
        map_key_length_too_short: typing.Callable[[], T_Result],
        map_key_length_too_long: typing.Callable[[], T_Result],
        card_expired: typing.Callable[[], T_Result],
        invalid_expiration: typing.Callable[[], T_Result],
        invalid_expiration_year: typing.Callable[[], T_Result],
        invalid_expiration_date: typing.Callable[[], T_Result],
        unsupported_card_brand: typing.Callable[[], T_Result],
        unsupported_entry_method: typing.Callable[[], T_Result],
        invalid_encrypted_card: typing.Callable[[], T_Result],
        invalid_card: typing.Callable[[], T_Result],
        generic_decline: typing.Callable[[], T_Result],
        cvv_failure: typing.Callable[[], T_Result],
        address_verification_failure: typing.Callable[[], T_Result],
        invalid_account: typing.Callable[[], T_Result],
        currency_mismatch: typing.Callable[[], T_Result],
        insufficient_funds: typing.Callable[[], T_Result],
        insufficient_permissions: typing.Callable[[], T_Result],
        cardholder_insufficient_permissions: typing.Callable[[], T_Result],
        invalid_location: typing.Callable[[], T_Result],
        transaction_limit: typing.Callable[[], T_Result],
        voice_failure: typing.Callable[[], T_Result],
        pan_failure: typing.Callable[[], T_Result],
        expiration_failure: typing.Callable[[], T_Result],
        card_not_supported: typing.Callable[[], T_Result],
        invalid_pin: typing.Callable[[], T_Result],
        missing_pin: typing.Callable[[], T_Result],
        missing_account_type: typing.Callable[[], T_Result],
        invalid_postal_code: typing.Callable[[], T_Result],
        invalid_fees: typing.Callable[[], T_Result],
        manually_entered_payment_not_supported: typing.Callable[[], T_Result],
        payment_limit_exceeded: typing.Callable[[], T_Result],
        gift_card_available_amount: typing.Callable[[], T_Result],
        account_unusable: typing.Callable[[], T_Result],
        buyer_refused_payment: typing.Callable[[], T_Result],
        delayed_transaction_expired: typing.Callable[[], T_Result],
        delayed_transaction_canceled: typing.Callable[[], T_Result],
        delayed_transaction_captured: typing.Callable[[], T_Result],
        delayed_transaction_failed: typing.Callable[[], T_Result],
        card_token_expired: typing.Callable[[], T_Result],
        card_token_used: typing.Callable[[], T_Result],
        amount_too_high: typing.Callable[[], T_Result],
        unsupported_instrument_type: typing.Callable[[], T_Result],
        refund_amount_invalid: typing.Callable[[], T_Result],
        refund_already_pending: typing.Callable[[], T_Result],
        payment_not_refundable: typing.Callable[[], T_Result],
        refund_declined: typing.Callable[[], T_Result],
        invalid_card_data: typing.Callable[[], T_Result],
        source_used: typing.Callable[[], T_Result],
        source_expired: typing.Callable[[], T_Result],
        unsupported_loyalty_reward_tier: typing.Callable[[], T_Result],
        location_mismatch: typing.Callable[[], T_Result],
        idempotency_key_reused: typing.Callable[[], T_Result],
        unexpected_value: typing.Callable[[], T_Result],
        sandbox_not_supported: typing.Callable[[], T_Result],
        invalid_email_address: typing.Callable[[], T_Result],
        invalid_phone_number: typing.Callable[[], T_Result],
        checkout_expired: typing.Callable[[], T_Result],
        bad_certificate: typing.Callable[[], T_Result],
        invalid_square_version_format: typing.Callable[[], T_Result],
        api_version_incompatible: typing.Callable[[], T_Result],
        card_declined: typing.Callable[[], T_Result],
        verify_cvv_failure: typing.Callable[[], T_Result],
        verify_avs_failure: typing.Callable[[], T_Result],
        card_declined_call_issuer: typing.Callable[[], T_Result],
        card_declined_verification_required: typing.Callable[[], T_Result],
        bad_expiration: typing.Callable[[], T_Result],
        chip_insertion_required: typing.Callable[[], T_Result],
        allowable_pin_tries_exceeded: typing.Callable[[], T_Result],
        reservation_declined: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        apple_payment_processing_certificate_hash_not_found: typing.Callable[[], T_Result],
        method_not_allowed: typing.Callable[[], T_Result],
        not_acceptable: typing.Callable[[], T_Result],
        request_timeout: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        gone: typing.Callable[[], T_Result],
        request_entity_too_large: typing.Callable[[], T_Result],
        unsupported_media_type: typing.Callable[[], T_Result],
        unprocessable_entity: typing.Callable[[], T_Result],
        rate_limited: typing.Callable[[], T_Result],
        not_implemented: typing.Callable[[], T_Result],
        bad_gateway: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
        temporary_error: typing.Callable[[], T_Result],
        gateway_timeout: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorCode.INTERNAL_SERVER_ERROR:
            return internal_server_error()
        if self is ErrorCode.UNAUTHORIZED:
            return unauthorized()
        if self is ErrorCode.ACCESS_TOKEN_EXPIRED:
            return access_token_expired()
        if self is ErrorCode.ACCESS_TOKEN_REVOKED:
            return access_token_revoked()
        if self is ErrorCode.CLIENT_DISABLED:
            return client_disabled()
        if self is ErrorCode.FORBIDDEN:
            return forbidden()
        if self is ErrorCode.INSUFFICIENT_SCOPES:
            return insufficient_scopes()
        if self is ErrorCode.APPLICATION_DISABLED:
            return application_disabled()
        if self is ErrorCode.V1APPLICATION:
            return v1application()
        if self is ErrorCode.V1ACCESS_TOKEN:
            return v1access_token()
        if self is ErrorCode.CARD_PROCESSING_NOT_ENABLED:
            return card_processing_not_enabled()
        if self is ErrorCode.MERCHANT_SUBSCRIPTION_NOT_FOUND:
            return merchant_subscription_not_found()
        if self is ErrorCode.BAD_REQUEST:
            return bad_request()
        if self is ErrorCode.MISSING_REQUIRED_PARAMETER:
            return missing_required_parameter()
        if self is ErrorCode.INCORRECT_TYPE:
            return incorrect_type()
        if self is ErrorCode.INVALID_TIME:
            return invalid_time()
        if self is ErrorCode.INVALID_TIME_RANGE:
            return invalid_time_range()
        if self is ErrorCode.INVALID_VALUE:
            return invalid_value()
        if self is ErrorCode.INVALID_CURSOR:
            return invalid_cursor()
        if self is ErrorCode.UNKNOWN_QUERY_PARAMETER:
            return unknown_query_parameter()
        if self is ErrorCode.CONFLICTING_PARAMETERS:
            return conflicting_parameters()
        if self is ErrorCode.EXPECTED_JSON_BODY:
            return expected_json_body()
        if self is ErrorCode.INVALID_SORT_ORDER:
            return invalid_sort_order()
        if self is ErrorCode.VALUE_REGEX_MISMATCH:
            return value_regex_mismatch()
        if self is ErrorCode.VALUE_TOO_SHORT:
            return value_too_short()
        if self is ErrorCode.VALUE_TOO_LONG:
            return value_too_long()
        if self is ErrorCode.VALUE_TOO_LOW:
            return value_too_low()
        if self is ErrorCode.VALUE_TOO_HIGH:
            return value_too_high()
        if self is ErrorCode.VALUE_EMPTY:
            return value_empty()
        if self is ErrorCode.ARRAY_LENGTH_TOO_LONG:
            return array_length_too_long()
        if self is ErrorCode.ARRAY_LENGTH_TOO_SHORT:
            return array_length_too_short()
        if self is ErrorCode.ARRAY_EMPTY:
            return array_empty()
        if self is ErrorCode.EXPECTED_BOOLEAN:
            return expected_boolean()
        if self is ErrorCode.EXPECTED_INTEGER:
            return expected_integer()
        if self is ErrorCode.EXPECTED_FLOAT:
            return expected_float()
        if self is ErrorCode.EXPECTED_STRING:
            return expected_string()
        if self is ErrorCode.EXPECTED_OBJECT:
            return expected_object()
        if self is ErrorCode.EXPECTED_ARRAY:
            return expected_array()
        if self is ErrorCode.EXPECTED_MAP:
            return expected_map()
        if self is ErrorCode.EXPECTED_BASE64ENCODED_BYTE_ARRAY:
            return expected_base64encoded_byte_array()
        if self is ErrorCode.INVALID_ARRAY_VALUE:
            return invalid_array_value()
        if self is ErrorCode.INVALID_ENUM_VALUE:
            return invalid_enum_value()
        if self is ErrorCode.INVALID_CONTENT_TYPE:
            return invalid_content_type()
        if self is ErrorCode.INVALID_FORM_VALUE:
            return invalid_form_value()
        if self is ErrorCode.CUSTOMER_NOT_FOUND:
            return customer_not_found()
        if self is ErrorCode.ONE_INSTRUMENT_EXPECTED:
            return one_instrument_expected()
        if self is ErrorCode.NO_FIELDS_SET:
            return no_fields_set()
        if self is ErrorCode.TOO_MANY_MAP_ENTRIES:
            return too_many_map_entries()
        if self is ErrorCode.MAP_KEY_LENGTH_TOO_SHORT:
            return map_key_length_too_short()
        if self is ErrorCode.MAP_KEY_LENGTH_TOO_LONG:
            return map_key_length_too_long()
        if self is ErrorCode.CARD_EXPIRED:
            return card_expired()
        if self is ErrorCode.INVALID_EXPIRATION:
            return invalid_expiration()
        if self is ErrorCode.INVALID_EXPIRATION_YEAR:
            return invalid_expiration_year()
        if self is ErrorCode.INVALID_EXPIRATION_DATE:
            return invalid_expiration_date()
        if self is ErrorCode.UNSUPPORTED_CARD_BRAND:
            return unsupported_card_brand()
        if self is ErrorCode.UNSUPPORTED_ENTRY_METHOD:
            return unsupported_entry_method()
        if self is ErrorCode.INVALID_ENCRYPTED_CARD:
            return invalid_encrypted_card()
        if self is ErrorCode.INVALID_CARD:
            return invalid_card()
        if self is ErrorCode.GENERIC_DECLINE:
            return generic_decline()
        if self is ErrorCode.CVV_FAILURE:
            return cvv_failure()
        if self is ErrorCode.ADDRESS_VERIFICATION_FAILURE:
            return address_verification_failure()
        if self is ErrorCode.INVALID_ACCOUNT:
            return invalid_account()
        if self is ErrorCode.CURRENCY_MISMATCH:
            return currency_mismatch()
        if self is ErrorCode.INSUFFICIENT_FUNDS:
            return insufficient_funds()
        if self is ErrorCode.INSUFFICIENT_PERMISSIONS:
            return insufficient_permissions()
        if self is ErrorCode.CARDHOLDER_INSUFFICIENT_PERMISSIONS:
            return cardholder_insufficient_permissions()
        if self is ErrorCode.INVALID_LOCATION:
            return invalid_location()
        if self is ErrorCode.TRANSACTION_LIMIT:
            return transaction_limit()
        if self is ErrorCode.VOICE_FAILURE:
            return voice_failure()
        if self is ErrorCode.PAN_FAILURE:
            return pan_failure()
        if self is ErrorCode.EXPIRATION_FAILURE:
            return expiration_failure()
        if self is ErrorCode.CARD_NOT_SUPPORTED:
            return card_not_supported()
        if self is ErrorCode.INVALID_PIN:
            return invalid_pin()
        if self is ErrorCode.MISSING_PIN:
            return missing_pin()
        if self is ErrorCode.MISSING_ACCOUNT_TYPE:
            return missing_account_type()
        if self is ErrorCode.INVALID_POSTAL_CODE:
            return invalid_postal_code()
        if self is ErrorCode.INVALID_FEES:
            return invalid_fees()
        if self is ErrorCode.MANUALLY_ENTERED_PAYMENT_NOT_SUPPORTED:
            return manually_entered_payment_not_supported()
        if self is ErrorCode.PAYMENT_LIMIT_EXCEEDED:
            return payment_limit_exceeded()
        if self is ErrorCode.GIFT_CARD_AVAILABLE_AMOUNT:
            return gift_card_available_amount()
        if self is ErrorCode.ACCOUNT_UNUSABLE:
            return account_unusable()
        if self is ErrorCode.BUYER_REFUSED_PAYMENT:
            return buyer_refused_payment()
        if self is ErrorCode.DELAYED_TRANSACTION_EXPIRED:
            return delayed_transaction_expired()
        if self is ErrorCode.DELAYED_TRANSACTION_CANCELED:
            return delayed_transaction_canceled()
        if self is ErrorCode.DELAYED_TRANSACTION_CAPTURED:
            return delayed_transaction_captured()
        if self is ErrorCode.DELAYED_TRANSACTION_FAILED:
            return delayed_transaction_failed()
        if self is ErrorCode.CARD_TOKEN_EXPIRED:
            return card_token_expired()
        if self is ErrorCode.CARD_TOKEN_USED:
            return card_token_used()
        if self is ErrorCode.AMOUNT_TOO_HIGH:
            return amount_too_high()
        if self is ErrorCode.UNSUPPORTED_INSTRUMENT_TYPE:
            return unsupported_instrument_type()
        if self is ErrorCode.REFUND_AMOUNT_INVALID:
            return refund_amount_invalid()
        if self is ErrorCode.REFUND_ALREADY_PENDING:
            return refund_already_pending()
        if self is ErrorCode.PAYMENT_NOT_REFUNDABLE:
            return payment_not_refundable()
        if self is ErrorCode.REFUND_DECLINED:
            return refund_declined()
        if self is ErrorCode.INVALID_CARD_DATA:
            return invalid_card_data()
        if self is ErrorCode.SOURCE_USED:
            return source_used()
        if self is ErrorCode.SOURCE_EXPIRED:
            return source_expired()
        if self is ErrorCode.UNSUPPORTED_LOYALTY_REWARD_TIER:
            return unsupported_loyalty_reward_tier()
        if self is ErrorCode.LOCATION_MISMATCH:
            return location_mismatch()
        if self is ErrorCode.IDEMPOTENCY_KEY_REUSED:
            return idempotency_key_reused()
        if self is ErrorCode.UNEXPECTED_VALUE:
            return unexpected_value()
        if self is ErrorCode.SANDBOX_NOT_SUPPORTED:
            return sandbox_not_supported()
        if self is ErrorCode.INVALID_EMAIL_ADDRESS:
            return invalid_email_address()
        if self is ErrorCode.INVALID_PHONE_NUMBER:
            return invalid_phone_number()
        if self is ErrorCode.CHECKOUT_EXPIRED:
            return checkout_expired()
        if self is ErrorCode.BAD_CERTIFICATE:
            return bad_certificate()
        if self is ErrorCode.INVALID_SQUARE_VERSION_FORMAT:
            return invalid_square_version_format()
        if self is ErrorCode.API_VERSION_INCOMPATIBLE:
            return api_version_incompatible()
        if self is ErrorCode.CARD_DECLINED:
            return card_declined()
        if self is ErrorCode.VERIFY_CVV_FAILURE:
            return verify_cvv_failure()
        if self is ErrorCode.VERIFY_AVS_FAILURE:
            return verify_avs_failure()
        if self is ErrorCode.CARD_DECLINED_CALL_ISSUER:
            return card_declined_call_issuer()
        if self is ErrorCode.CARD_DECLINED_VERIFICATION_REQUIRED:
            return card_declined_verification_required()
        if self is ErrorCode.BAD_EXPIRATION:
            return bad_expiration()
        if self is ErrorCode.CHIP_INSERTION_REQUIRED:
            return chip_insertion_required()
        if self is ErrorCode.ALLOWABLE_PIN_TRIES_EXCEEDED:
            return allowable_pin_tries_exceeded()
        if self is ErrorCode.RESERVATION_DECLINED:
            return reservation_declined()
        if self is ErrorCode.NOT_FOUND:
            return not_found()
        if self is ErrorCode.APPLE_PAYMENT_PROCESSING_CERTIFICATE_HASH_NOT_FOUND:
            return apple_payment_processing_certificate_hash_not_found()
        if self is ErrorCode.METHOD_NOT_ALLOWED:
            return method_not_allowed()
        if self is ErrorCode.NOT_ACCEPTABLE:
            return not_acceptable()
        if self is ErrorCode.REQUEST_TIMEOUT:
            return request_timeout()
        if self is ErrorCode.CONFLICT:
            return conflict()
        if self is ErrorCode.GONE:
            return gone()
        if self is ErrorCode.REQUEST_ENTITY_TOO_LARGE:
            return request_entity_too_large()
        if self is ErrorCode.UNSUPPORTED_MEDIA_TYPE:
            return unsupported_media_type()
        if self is ErrorCode.UNPROCESSABLE_ENTITY:
            return unprocessable_entity()
        if self is ErrorCode.RATE_LIMITED:
            return rate_limited()
        if self is ErrorCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is ErrorCode.BAD_GATEWAY:
            return bad_gateway()
        if self is ErrorCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
        if self is ErrorCode.TEMPORARY_ERROR:
            return temporary_error()
        if self is ErrorCode.GATEWAY_TIMEOUT:
            return gateway_timeout()
