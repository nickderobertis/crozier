



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .create_ecommerce_customer_response import CreateEcommerceCustomerResponse
    from .create_ecommerce_order_response import CreateEcommerceOrderResponse
    from .create_product_response import CreateProductResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_ecommerce_customer_response import DeleteEcommerceCustomerResponse
    from .delete_ecommerce_order_response import DeleteEcommerceOrderResponse
    from .delete_product_response import DeleteProductResponse
    from .department import Department
    from .description import Description
    from .division import Division
    from .ecommerce_address import EcommerceAddress
    from .ecommerce_customer import EcommerceCustomer
    from .ecommerce_customer_addresses_item import EcommerceCustomerAddressesItem
    from .ecommerce_customer_addresses_item_type import EcommerceCustomerAddressesItemType
    from .ecommerce_customer_status import EcommerceCustomerStatus
    from .ecommerce_customers_filter import EcommerceCustomersFilter
    from .ecommerce_discount import EcommerceDiscount
    from .ecommerce_order import EcommerceOrder
    from .ecommerce_order_fulfillment_status import EcommerceOrderFulfillmentStatus
    from .ecommerce_order_line_item import EcommerceOrderLineItem
    from .ecommerce_order_line_item_options_item import EcommerceOrderLineItemOptionsItem
    from .ecommerce_order_payment_status import EcommerceOrderPaymentStatus
    from .ecommerce_order_status import EcommerceOrderStatus
    from .ecommerce_orders_filter import EcommerceOrdersFilter
    from .ecommerce_product import EcommerceProduct
    from .ecommerce_product_categories_item import EcommerceProductCategoriesItem
    from .ecommerce_product_images_item import EcommerceProductImagesItem
    from .ecommerce_product_options_item import EcommerceProductOptionsItem
    from .ecommerce_product_status import EcommerceProductStatus
    from .ecommerce_product_variants_item import EcommerceProductVariantsItem
    from .ecommerce_product_variants_item_images_item import EcommerceProductVariantsItemImagesItem
    from .ecommerce_product_variants_item_options_item import EcommerceProductVariantsItemOptionsItem
    from .ecommerce_store import EcommerceStore
    from .email import Email
    from .email_type import EmailType
    from .first_name import FirstName
    from .gender import Gender
    from .get_ecommerce_customer_response import GetEcommerceCustomerResponse
    from .get_ecommerce_customers_response import GetEcommerceCustomersResponse
    from .get_ecommerce_order_response import GetEcommerceOrderResponse
    from .get_ecommerce_orders_response import GetEcommerceOrdersResponse
    from .get_product_response import GetProductResponse
    from .get_products_response import GetProductsResponse
    from .get_store_response import GetStoreResponse
    from .get_stores_response import GetStoresResponse
    from .id import Id
    from .language import Language
    from .last_name import LastName
    from .linked_ecommerce_customer import LinkedEcommerceCustomer
    from .linked_ecommerce_order import LinkedEcommerceOrder
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .middle_name import MiddleName
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .payment_required_response import PaymentRequiredResponse
    from .payment_unit import PaymentUnit
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .photo_url import PhotoUrl
    from .row_version import RowVersion
    from .title import Title
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .tracking_item import TrackingItem
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_ecommerce_customer_response import UpdateEcommerceCustomerResponse
    from .update_ecommerce_order_response import UpdateEcommerceOrderResponse
    from .update_product_response import UpdateProductResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "CreateEcommerceCustomerResponse": ".create_ecommerce_customer_response",
    "CreateEcommerceOrderResponse": ".create_ecommerce_order_response",
    "CreateProductResponse": ".create_product_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteEcommerceCustomerResponse": ".delete_ecommerce_customer_response",
    "DeleteEcommerceOrderResponse": ".delete_ecommerce_order_response",
    "DeleteProductResponse": ".delete_product_response",
    "Department": ".department",
    "Description": ".description",
    "Division": ".division",
    "EcommerceAddress": ".ecommerce_address",
    "EcommerceCustomer": ".ecommerce_customer",
    "EcommerceCustomerAddressesItem": ".ecommerce_customer_addresses_item",
    "EcommerceCustomerAddressesItemType": ".ecommerce_customer_addresses_item_type",
    "EcommerceCustomerStatus": ".ecommerce_customer_status",
    "EcommerceCustomersFilter": ".ecommerce_customers_filter",
    "EcommerceDiscount": ".ecommerce_discount",
    "EcommerceOrder": ".ecommerce_order",
    "EcommerceOrderFulfillmentStatus": ".ecommerce_order_fulfillment_status",
    "EcommerceOrderLineItem": ".ecommerce_order_line_item",
    "EcommerceOrderLineItemOptionsItem": ".ecommerce_order_line_item_options_item",
    "EcommerceOrderPaymentStatus": ".ecommerce_order_payment_status",
    "EcommerceOrderStatus": ".ecommerce_order_status",
    "EcommerceOrdersFilter": ".ecommerce_orders_filter",
    "EcommerceProduct": ".ecommerce_product",
    "EcommerceProductCategoriesItem": ".ecommerce_product_categories_item",
    "EcommerceProductImagesItem": ".ecommerce_product_images_item",
    "EcommerceProductOptionsItem": ".ecommerce_product_options_item",
    "EcommerceProductStatus": ".ecommerce_product_status",
    "EcommerceProductVariantsItem": ".ecommerce_product_variants_item",
    "EcommerceProductVariantsItemImagesItem": ".ecommerce_product_variants_item_images_item",
    "EcommerceProductVariantsItemOptionsItem": ".ecommerce_product_variants_item_options_item",
    "EcommerceStore": ".ecommerce_store",
    "Email": ".email",
    "EmailType": ".email_type",
    "FirstName": ".first_name",
    "Gender": ".gender",
    "GetEcommerceCustomerResponse": ".get_ecommerce_customer_response",
    "GetEcommerceCustomersResponse": ".get_ecommerce_customers_response",
    "GetEcommerceOrderResponse": ".get_ecommerce_order_response",
    "GetEcommerceOrdersResponse": ".get_ecommerce_orders_response",
    "GetProductResponse": ".get_product_response",
    "GetProductsResponse": ".get_products_response",
    "GetStoreResponse": ".get_store_response",
    "GetStoresResponse": ".get_stores_response",
    "Id": ".id",
    "Language": ".language",
    "LastName": ".last_name",
    "LinkedEcommerceCustomer": ".linked_ecommerce_customer",
    "LinkedEcommerceOrder": ".linked_ecommerce_order",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "MiddleName": ".middle_name",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PaymentRequiredResponse": ".payment_required_response",
    "PaymentUnit": ".payment_unit",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "PhotoUrl": ".photo_url",
    "RowVersion": ".row_version",
    "Title": ".title",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "TrackingItem": ".tracking_item",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateEcommerceCustomerResponse": ".update_ecommerce_customer_response",
    "UpdateEcommerceOrderResponse": ".update_ecommerce_order_response",
    "UpdateProductResponse": ".update_product_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "Website": ".website",
    "WebsiteType": ".website_type",
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
    "Address",
    "AddressType",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "CreateEcommerceCustomerResponse",
    "CreateEcommerceOrderResponse",
    "CreateProductResponse",
    "CreatedAt",
    "CreatedBy",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteEcommerceCustomerResponse",
    "DeleteEcommerceOrderResponse",
    "DeleteProductResponse",
    "Department",
    "Description",
    "Division",
    "EcommerceAddress",
    "EcommerceCustomer",
    "EcommerceCustomerAddressesItem",
    "EcommerceCustomerAddressesItemType",
    "EcommerceCustomerStatus",
    "EcommerceCustomersFilter",
    "EcommerceDiscount",
    "EcommerceOrder",
    "EcommerceOrderFulfillmentStatus",
    "EcommerceOrderLineItem",
    "EcommerceOrderLineItemOptionsItem",
    "EcommerceOrderPaymentStatus",
    "EcommerceOrderStatus",
    "EcommerceOrdersFilter",
    "EcommerceProduct",
    "EcommerceProductCategoriesItem",
    "EcommerceProductImagesItem",
    "EcommerceProductOptionsItem",
    "EcommerceProductStatus",
    "EcommerceProductVariantsItem",
    "EcommerceProductVariantsItemImagesItem",
    "EcommerceProductVariantsItemOptionsItem",
    "EcommerceStore",
    "Email",
    "EmailType",
    "FirstName",
    "Gender",
    "GetEcommerceCustomerResponse",
    "GetEcommerceCustomersResponse",
    "GetEcommerceOrderResponse",
    "GetEcommerceOrdersResponse",
    "GetProductResponse",
    "GetProductsResponse",
    "GetStoreResponse",
    "GetStoresResponse",
    "Id",
    "Language",
    "LastName",
    "LinkedEcommerceCustomer",
    "LinkedEcommerceOrder",
    "Links",
    "Meta",
    "MetaCursors",
    "MiddleName",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredResponse",
    "PaymentUnit",
    "PhoneNumber",
    "PhoneNumberType",
    "PhotoUrl",
    "RowVersion",
    "Title",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "TrackingItem",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateEcommerceCustomerResponse",
    "UpdateEcommerceOrderResponse",
    "UpdateProductResponse",
    "UpdatedAt",
    "UpdatedBy",
    "Website",
    "WebsiteType",
]
