



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .date_time import DateTime
    from .error400 import Error400
    from .error400message import Error400Message
    from .error400name import Error400Name
    from .error401 import Error401
    from .error401message import Error401Message
    from .error401name import Error401Name
    from .error403 import Error403
    from .error403message import Error403Message
    from .error403name import Error403Name
    from .error404 import Error404
    from .error404message import Error404Message
    from .error404name import Error404Name
    from .error409 import Error409
    from .error409message import Error409Message
    from .error415 import Error415
    from .error415message import Error415Message
    from .error422 import Error422
    from .error422message import Error422Message
    from .error422name import Error422Name
    from .error500 import Error500
    from .error500message import Error500Message
    from .error500name import Error500Name
    from .error503 import Error503
    from .error503message import Error503Message
    from .error_default import (
        ErrorDefault,
        ErrorDefault_AuthenticationFailure,
        ErrorDefault_InternalServerError,
        ErrorDefault_InvalidRequest,
        ErrorDefault_NotAuthorized,
        ErrorDefault_ResourceConflict,
        ErrorDefault_ResourceNotFound,
        ErrorDefault_ServiceUnavailable,
        ErrorDefault_UnprocessableEntity,
        ErrorDefault_UnsupportedMediaType,
    )
    from .error_details import ErrorDetails
    from .error_link_description import ErrorLinkDescription
    from .error_link_description_method import ErrorLinkDescriptionMethod
    from .error_location import ErrorLocation
    from .forbidden_error_body import ForbiddenErrorBody
    from .four_hundred import FourHundred
    from .four_hundred_details_item import FourHundredDetailsItem
    from .four_hundred_details_item_description import FourHundredDetailsItemDescription
    from .four_hundred_details_item_issue import FourHundredDetailsItemIssue
    from .four_hundred_four import FourHundredFour
    from .four_hundred_four_details_item import FourHundredFourDetailsItem
    from .four_hundred_four_details_item_description import FourHundredFourDetailsItemDescription
    from .four_hundred_four_details_item_issue import FourHundredFourDetailsItemIssue
    from .four_hundred_one import FourHundredOne
    from .four_hundred_one_details_item import FourHundredOneDetailsItem
    from .four_hundred_one_details_item_description import FourHundredOneDetailsItemDescription
    from .four_hundred_one_details_item_issue import FourHundredOneDetailsItemIssue
    from .four_hundred_three import FourHundredThree
    from .four_hundred_three_details_item import FourHundredThreeDetailsItem
    from .four_hundred_three_details_item_description import FourHundredThreeDetailsItemDescription
    from .four_hundred_three_details_item_issue import FourHundredThreeDetailsItemIssue
    from .four_hundred_twenty_two import FourHundredTwentyTwo
    from .four_hundred_twenty_two_details_item import (
        FourHundredTwentyTwoDetailsItem,
        FourHundredTwentyTwoDetailsItem_CountryNotSupported,
        FourHundredTwentyTwoDetailsItem_DuplicateResourceIdentifier,
        FourHundredTwentyTwoDetailsItem_UserAccountClosed,
    )
    from .four_hundred_twenty_two_details_item_country_not_supported import (
        FourHundredTwentyTwoDetailsItemCountryNotSupported,
    )
    from .four_hundred_twenty_two_details_item_country_not_supported_description import (
        FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription,
    )
    from .four_hundred_twenty_two_details_item_duplicate_resource_identifier import (
        FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifier,
    )
    from .four_hundred_twenty_two_details_item_duplicate_resource_identifier_description import (
        FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription,
    )
    from .four_hundred_twenty_two_details_item_user_account_closed import (
        FourHundredTwentyTwoDetailsItemUserAccountClosed,
    )
    from .four_hundred_twenty_two_details_item_user_account_closed_description import (
        FourHundredTwentyTwoDetailsItemUserAccountClosedDescription,
    )
    from .link_description import LinkDescription
    from .link_description_list import LinkDescriptionList
    from .link_description_method import LinkDescriptionMethod
    from .not_found_error_body import NotFoundErrorBody
    from .oauth_scope import OauthScope
    from .patch import Patch
    from .patch_op import PatchOp
    from .patch_request import PatchRequest
    from .patch_value import PatchValue
    from .product import Product
    from .product_category import ProductCategory
    from .product_collection import ProductCollection
    from .product_collection_element import ProductCollectionElement
    from .product_collection_element_list import ProductCollectionElementList
    from .product_type import ProductType
    from .products_create400 import ProductsCreate400
    from .products_create400details_item import (
        ProductsCreate400DetailsItem,
        ProductsCreate400DetailsItem_ARequiredFieldIsMissing,
        ProductsCreate400DetailsItem_InputIdentifierMustNotUseSystemPrefixProd,
        ProductsCreate400DetailsItem_TheValueOfAFieldDoesNotConformToTheExpectedFormat,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsInvalid,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsTooLong,
        ProductsCreate400DetailsItem_TheValueOfAFieldIsTooShort,
    )
    from .products_create400details_item_a_required_field_is_missing import (
        ProductsCreate400DetailsItemARequiredFieldIsMissing,
    )
    from .products_create400details_item_a_required_field_is_missing_issue import (
        ProductsCreate400DetailsItemARequiredFieldIsMissingIssue,
    )
    from .products_create400details_item_input_identifier_must_not_use_system_prefix_prod import (
        ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProd,
    )
    from .products_create400details_item_input_identifier_must_not_use_system_prefix_prod_issue import (
        ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue,
    )
    from .products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format import (
        ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormat,
    )
    from .products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format_issue import (
        ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue,
    )
    from .products_create400details_item_the_value_of_a_field_is_invalid import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsInvalid,
    )
    from .products_create400details_item_the_value_of_a_field_is_invalid_issue import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue,
    )
    from .products_create400details_item_the_value_of_a_field_is_too_long import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsTooLong,
    )
    from .products_create400details_item_the_value_of_a_field_is_too_long_issue import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue,
    )
    from .products_create400details_item_the_value_of_a_field_is_too_short import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsTooShort,
    )
    from .products_create400details_item_the_value_of_a_field_is_too_short_issue import (
        ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue,
    )
    from .products_patch400 import ProductsPatch400
    from .products_patch400details_item import (
        ProductsPatch400DetailsItem,
        ProductsPatch400DetailsItem_InvalidParameterSyntax,
        ProductsPatch400DetailsItem_InvalidParameterValue,
        ProductsPatch400DetailsItem_InvalidPatchPath,
        ProductsPatch400DetailsItem_MissingRequiredParameter,
        ProductsPatch400DetailsItem_UnsupportedPatchOperation,
    )
    from .products_patch400details_item_invalid_parameter_syntax import (
        ProductsPatch400DetailsItemInvalidParameterSyntax,
    )
    from .products_patch400details_item_invalid_parameter_syntax_description import (
        ProductsPatch400DetailsItemInvalidParameterSyntaxDescription,
    )
    from .products_patch400details_item_invalid_parameter_value import ProductsPatch400DetailsItemInvalidParameterValue
    from .products_patch400details_item_invalid_parameter_value_description import (
        ProductsPatch400DetailsItemInvalidParameterValueDescription,
    )
    from .products_patch400details_item_invalid_patch_path import ProductsPatch400DetailsItemInvalidPatchPath
    from .products_patch400details_item_invalid_patch_path_description import (
        ProductsPatch400DetailsItemInvalidPatchPathDescription,
    )
    from .products_patch400details_item_missing_required_parameter import (
        ProductsPatch400DetailsItemMissingRequiredParameter,
    )
    from .products_patch400details_item_missing_required_parameter_description import (
        ProductsPatch400DetailsItemMissingRequiredParameterDescription,
    )
    from .products_patch400details_item_unsupported_patch_operation import (
        ProductsPatch400DetailsItemUnsupportedPatchOperation,
    )
    from .products_patch400details_item_unsupported_patch_operation_description import (
        ProductsPatch400DetailsItemUnsupportedPatchOperationDescription,
    )
    from .products_patch422 import ProductsPatch422
    from .products_patch422details_item import (
        ProductsPatch422DetailsItem,
        ProductsPatch422DetailsItem_DuplicateResourceIdentifier,
        ProductsPatch422DetailsItem_UserAccountClosed,
    )
    from .products_patch422details_item_duplicate_resource_identifier import (
        ProductsPatch422DetailsItemDuplicateResourceIdentifier,
    )
    from .products_patch422details_item_duplicate_resource_identifier_description import (
        ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription,
    )
    from .products_patch422details_item_user_account_closed import ProductsPatch422DetailsItemUserAccountClosed
    from .products_patch422details_item_user_account_closed_description import (
        ProductsPatch422DetailsItemUserAccountClosedDescription,
    )
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unprocessable_entity_error_body import UnprocessableEntityErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "DateTime": ".date_time",
    "Error400": ".error400",
    "Error400Message": ".error400message",
    "Error400Name": ".error400name",
    "Error401": ".error401",
    "Error401Message": ".error401message",
    "Error401Name": ".error401name",
    "Error403": ".error403",
    "Error403Message": ".error403message",
    "Error403Name": ".error403name",
    "Error404": ".error404",
    "Error404Message": ".error404message",
    "Error404Name": ".error404name",
    "Error409": ".error409",
    "Error409Message": ".error409message",
    "Error415": ".error415",
    "Error415Message": ".error415message",
    "Error422": ".error422",
    "Error422Message": ".error422message",
    "Error422Name": ".error422name",
    "Error500": ".error500",
    "Error500Message": ".error500message",
    "Error500Name": ".error500name",
    "Error503": ".error503",
    "Error503Message": ".error503message",
    "ErrorDefault": ".error_default",
    "ErrorDefault_AuthenticationFailure": ".error_default",
    "ErrorDefault_InternalServerError": ".error_default",
    "ErrorDefault_InvalidRequest": ".error_default",
    "ErrorDefault_NotAuthorized": ".error_default",
    "ErrorDefault_ResourceConflict": ".error_default",
    "ErrorDefault_ResourceNotFound": ".error_default",
    "ErrorDefault_ServiceUnavailable": ".error_default",
    "ErrorDefault_UnprocessableEntity": ".error_default",
    "ErrorDefault_UnsupportedMediaType": ".error_default",
    "ErrorDetails": ".error_details",
    "ErrorLinkDescription": ".error_link_description",
    "ErrorLinkDescriptionMethod": ".error_link_description_method",
    "ErrorLocation": ".error_location",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "FourHundred": ".four_hundred",
    "FourHundredDetailsItem": ".four_hundred_details_item",
    "FourHundredDetailsItemDescription": ".four_hundred_details_item_description",
    "FourHundredDetailsItemIssue": ".four_hundred_details_item_issue",
    "FourHundredFour": ".four_hundred_four",
    "FourHundredFourDetailsItem": ".four_hundred_four_details_item",
    "FourHundredFourDetailsItemDescription": ".four_hundred_four_details_item_description",
    "FourHundredFourDetailsItemIssue": ".four_hundred_four_details_item_issue",
    "FourHundredOne": ".four_hundred_one",
    "FourHundredOneDetailsItem": ".four_hundred_one_details_item",
    "FourHundredOneDetailsItemDescription": ".four_hundred_one_details_item_description",
    "FourHundredOneDetailsItemIssue": ".four_hundred_one_details_item_issue",
    "FourHundredThree": ".four_hundred_three",
    "FourHundredThreeDetailsItem": ".four_hundred_three_details_item",
    "FourHundredThreeDetailsItemDescription": ".four_hundred_three_details_item_description",
    "FourHundredThreeDetailsItemIssue": ".four_hundred_three_details_item_issue",
    "FourHundredTwentyTwo": ".four_hundred_twenty_two",
    "FourHundredTwentyTwoDetailsItem": ".four_hundred_twenty_two_details_item",
    "FourHundredTwentyTwoDetailsItemCountryNotSupported": ".four_hundred_twenty_two_details_item_country_not_supported",
    "FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription": ".four_hundred_twenty_two_details_item_country_not_supported_description",
    "FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifier": ".four_hundred_twenty_two_details_item_duplicate_resource_identifier",
    "FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription": ".four_hundred_twenty_two_details_item_duplicate_resource_identifier_description",
    "FourHundredTwentyTwoDetailsItemUserAccountClosed": ".four_hundred_twenty_two_details_item_user_account_closed",
    "FourHundredTwentyTwoDetailsItemUserAccountClosedDescription": ".four_hundred_twenty_two_details_item_user_account_closed_description",
    "FourHundredTwentyTwoDetailsItem_CountryNotSupported": ".four_hundred_twenty_two_details_item",
    "FourHundredTwentyTwoDetailsItem_DuplicateResourceIdentifier": ".four_hundred_twenty_two_details_item",
    "FourHundredTwentyTwoDetailsItem_UserAccountClosed": ".four_hundred_twenty_two_details_item",
    "LinkDescription": ".link_description",
    "LinkDescriptionList": ".link_description_list",
    "LinkDescriptionMethod": ".link_description_method",
    "NotFoundErrorBody": ".not_found_error_body",
    "OauthScope": ".oauth_scope",
    "Patch": ".patch",
    "PatchOp": ".patch_op",
    "PatchRequest": ".patch_request",
    "PatchValue": ".patch_value",
    "Product": ".product",
    "ProductCategory": ".product_category",
    "ProductCollection": ".product_collection",
    "ProductCollectionElement": ".product_collection_element",
    "ProductCollectionElementList": ".product_collection_element_list",
    "ProductType": ".product_type",
    "ProductsCreate400": ".products_create400",
    "ProductsCreate400DetailsItem": ".products_create400details_item",
    "ProductsCreate400DetailsItemARequiredFieldIsMissing": ".products_create400details_item_a_required_field_is_missing",
    "ProductsCreate400DetailsItemARequiredFieldIsMissingIssue": ".products_create400details_item_a_required_field_is_missing_issue",
    "ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProd": ".products_create400details_item_input_identifier_must_not_use_system_prefix_prod",
    "ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue": ".products_create400details_item_input_identifier_must_not_use_system_prefix_prod_issue",
    "ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormat": ".products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format",
    "ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue": ".products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format_issue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsInvalid": ".products_create400details_item_the_value_of_a_field_is_invalid",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue": ".products_create400details_item_the_value_of_a_field_is_invalid_issue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooLong": ".products_create400details_item_the_value_of_a_field_is_too_long",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue": ".products_create400details_item_the_value_of_a_field_is_too_long_issue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooShort": ".products_create400details_item_the_value_of_a_field_is_too_short",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue": ".products_create400details_item_the_value_of_a_field_is_too_short_issue",
    "ProductsCreate400DetailsItem_ARequiredFieldIsMissing": ".products_create400details_item",
    "ProductsCreate400DetailsItem_InputIdentifierMustNotUseSystemPrefixProd": ".products_create400details_item",
    "ProductsCreate400DetailsItem_TheValueOfAFieldDoesNotConformToTheExpectedFormat": ".products_create400details_item",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsInvalid": ".products_create400details_item",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsTooLong": ".products_create400details_item",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsTooShort": ".products_create400details_item",
    "ProductsPatch400": ".products_patch400",
    "ProductsPatch400DetailsItem": ".products_patch400details_item",
    "ProductsPatch400DetailsItemInvalidParameterSyntax": ".products_patch400details_item_invalid_parameter_syntax",
    "ProductsPatch400DetailsItemInvalidParameterSyntaxDescription": ".products_patch400details_item_invalid_parameter_syntax_description",
    "ProductsPatch400DetailsItemInvalidParameterValue": ".products_patch400details_item_invalid_parameter_value",
    "ProductsPatch400DetailsItemInvalidParameterValueDescription": ".products_patch400details_item_invalid_parameter_value_description",
    "ProductsPatch400DetailsItemInvalidPatchPath": ".products_patch400details_item_invalid_patch_path",
    "ProductsPatch400DetailsItemInvalidPatchPathDescription": ".products_patch400details_item_invalid_patch_path_description",
    "ProductsPatch400DetailsItemMissingRequiredParameter": ".products_patch400details_item_missing_required_parameter",
    "ProductsPatch400DetailsItemMissingRequiredParameterDescription": ".products_patch400details_item_missing_required_parameter_description",
    "ProductsPatch400DetailsItemUnsupportedPatchOperation": ".products_patch400details_item_unsupported_patch_operation",
    "ProductsPatch400DetailsItemUnsupportedPatchOperationDescription": ".products_patch400details_item_unsupported_patch_operation_description",
    "ProductsPatch400DetailsItem_InvalidParameterSyntax": ".products_patch400details_item",
    "ProductsPatch400DetailsItem_InvalidParameterValue": ".products_patch400details_item",
    "ProductsPatch400DetailsItem_InvalidPatchPath": ".products_patch400details_item",
    "ProductsPatch400DetailsItem_MissingRequiredParameter": ".products_patch400details_item",
    "ProductsPatch400DetailsItem_UnsupportedPatchOperation": ".products_patch400details_item",
    "ProductsPatch422": ".products_patch422",
    "ProductsPatch422DetailsItem": ".products_patch422details_item",
    "ProductsPatch422DetailsItemDuplicateResourceIdentifier": ".products_patch422details_item_duplicate_resource_identifier",
    "ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription": ".products_patch422details_item_duplicate_resource_identifier_description",
    "ProductsPatch422DetailsItemUserAccountClosed": ".products_patch422details_item_user_account_closed",
    "ProductsPatch422DetailsItemUserAccountClosedDescription": ".products_patch422details_item_user_account_closed_description",
    "ProductsPatch422DetailsItem_DuplicateResourceIdentifier": ".products_patch422details_item",
    "ProductsPatch422DetailsItem_UserAccountClosed": ".products_patch422details_item",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
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
    "DateTime",
    "Error400",
    "Error400Message",
    "Error400Name",
    "Error401",
    "Error401Message",
    "Error401Name",
    "Error403",
    "Error403Message",
    "Error403Name",
    "Error404",
    "Error404Message",
    "Error404Name",
    "Error409",
    "Error409Message",
    "Error415",
    "Error415Message",
    "Error422",
    "Error422Message",
    "Error422Name",
    "Error500",
    "Error500Message",
    "Error500Name",
    "Error503",
    "Error503Message",
    "ErrorDefault",
    "ErrorDefault_AuthenticationFailure",
    "ErrorDefault_InternalServerError",
    "ErrorDefault_InvalidRequest",
    "ErrorDefault_NotAuthorized",
    "ErrorDefault_ResourceConflict",
    "ErrorDefault_ResourceNotFound",
    "ErrorDefault_ServiceUnavailable",
    "ErrorDefault_UnprocessableEntity",
    "ErrorDefault_UnsupportedMediaType",
    "ErrorDetails",
    "ErrorLinkDescription",
    "ErrorLinkDescriptionMethod",
    "ErrorLocation",
    "ForbiddenErrorBody",
    "FourHundred",
    "FourHundredDetailsItem",
    "FourHundredDetailsItemDescription",
    "FourHundredDetailsItemIssue",
    "FourHundredFour",
    "FourHundredFourDetailsItem",
    "FourHundredFourDetailsItemDescription",
    "FourHundredFourDetailsItemIssue",
    "FourHundredOne",
    "FourHundredOneDetailsItem",
    "FourHundredOneDetailsItemDescription",
    "FourHundredOneDetailsItemIssue",
    "FourHundredThree",
    "FourHundredThreeDetailsItem",
    "FourHundredThreeDetailsItemDescription",
    "FourHundredThreeDetailsItemIssue",
    "FourHundredTwentyTwo",
    "FourHundredTwentyTwoDetailsItem",
    "FourHundredTwentyTwoDetailsItemCountryNotSupported",
    "FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription",
    "FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifier",
    "FourHundredTwentyTwoDetailsItemDuplicateResourceIdentifierDescription",
    "FourHundredTwentyTwoDetailsItemUserAccountClosed",
    "FourHundredTwentyTwoDetailsItemUserAccountClosedDescription",
    "FourHundredTwentyTwoDetailsItem_CountryNotSupported",
    "FourHundredTwentyTwoDetailsItem_DuplicateResourceIdentifier",
    "FourHundredTwentyTwoDetailsItem_UserAccountClosed",
    "LinkDescription",
    "LinkDescriptionList",
    "LinkDescriptionMethod",
    "NotFoundErrorBody",
    "OauthScope",
    "Patch",
    "PatchOp",
    "PatchRequest",
    "PatchValue",
    "Product",
    "ProductCategory",
    "ProductCollection",
    "ProductCollectionElement",
    "ProductCollectionElementList",
    "ProductType",
    "ProductsCreate400",
    "ProductsCreate400DetailsItem",
    "ProductsCreate400DetailsItemARequiredFieldIsMissing",
    "ProductsCreate400DetailsItemARequiredFieldIsMissingIssue",
    "ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProd",
    "ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue",
    "ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormat",
    "ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsInvalid",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooLong",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooShort",
    "ProductsCreate400DetailsItemTheValueOfAFieldIsTooShortIssue",
    "ProductsCreate400DetailsItem_ARequiredFieldIsMissing",
    "ProductsCreate400DetailsItem_InputIdentifierMustNotUseSystemPrefixProd",
    "ProductsCreate400DetailsItem_TheValueOfAFieldDoesNotConformToTheExpectedFormat",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsInvalid",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsTooLong",
    "ProductsCreate400DetailsItem_TheValueOfAFieldIsTooShort",
    "ProductsPatch400",
    "ProductsPatch400DetailsItem",
    "ProductsPatch400DetailsItemInvalidParameterSyntax",
    "ProductsPatch400DetailsItemInvalidParameterSyntaxDescription",
    "ProductsPatch400DetailsItemInvalidParameterValue",
    "ProductsPatch400DetailsItemInvalidParameterValueDescription",
    "ProductsPatch400DetailsItemInvalidPatchPath",
    "ProductsPatch400DetailsItemInvalidPatchPathDescription",
    "ProductsPatch400DetailsItemMissingRequiredParameter",
    "ProductsPatch400DetailsItemMissingRequiredParameterDescription",
    "ProductsPatch400DetailsItemUnsupportedPatchOperation",
    "ProductsPatch400DetailsItemUnsupportedPatchOperationDescription",
    "ProductsPatch400DetailsItem_InvalidParameterSyntax",
    "ProductsPatch400DetailsItem_InvalidParameterValue",
    "ProductsPatch400DetailsItem_InvalidPatchPath",
    "ProductsPatch400DetailsItem_MissingRequiredParameter",
    "ProductsPatch400DetailsItem_UnsupportedPatchOperation",
    "ProductsPatch422",
    "ProductsPatch422DetailsItem",
    "ProductsPatch422DetailsItemDuplicateResourceIdentifier",
    "ProductsPatch422DetailsItemDuplicateResourceIdentifierDescription",
    "ProductsPatch422DetailsItemUserAccountClosed",
    "ProductsPatch422DetailsItemUserAccountClosedDescription",
    "ProductsPatch422DetailsItem_DuplicateResourceIdentifier",
    "ProductsPatch422DetailsItem_UserAccountClosed",
    "UnauthorizedErrorBody",
    "UnprocessableEntityErrorBody",
]
