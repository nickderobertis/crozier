



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action_denied_err import ActionDeniedErr
    from .address import Address
    from .audit_fields import AuditFields
    from .bulk_export_resp_body import BulkExportRespBody
    from .cancel_order_resp_body import CancelOrderRespBody
    from .category import Category
    from .category_ref import CategoryRef
    from .cents import Cents
    from .contact import Contact
    from .country_code import CountryCode
    from .create_customer_req import CreateCustomerReq
    from .create_customer_resp_body import CreateCustomerRespBody
    from .create_order_req import CreateOrderReq
    from .create_order_resp_body import CreateOrderRespBody
    from .create_product_req import CreateProductReq
    from .create_product_resp_body import CreateProductRespBody
    from .currency_code import CurrencyCode
    from .customer import Customer
    from .customer_ref import CustomerRef
    from .defaults_resp_body import DefaultsRespBody
    from .defaults_showcase_req import DefaultsShowcaseReq
    from .delete_customer_resp_body import DeleteCustomerRespBody
    from .delete_product_resp_body import DeleteProductRespBody
    from .email import Email
    from .filter_orders_req import FilterOrdersReq
    from .filter_orders_resp_body import FilterOrdersRespBody
    from .force_ship_resp_body import ForceShipRespBody
    from .geocode import Geocode
    from .get_customer_req import GetCustomerReq
    from .get_customer_resp_body import GetCustomerRespBody
    from .get_order_req import GetOrderReq
    from .get_order_resp_body import GetOrderRespBody
    from .get_product_req import GetProductReq
    from .get_product_resp_body import GetProductRespBody
    from .internal_err import InternalErr
    from .latitude import Latitude
    from .line_item import LineItem
    from .list_categories_resp_body import ListCategoriesRespBody
    from .list_customers_resp_body import ListCustomersRespBody
    from .list_orders_req import ListOrdersReq
    from .list_orders_resp_body import ListOrdersRespBody
    from .list_products_req import ListProductsReq
    from .list_products_resp_body import ListProductsRespBody
    from .longitude import Longitude
    from .maintenance_reason import MaintenanceReason
    from .maintenance_window_err import MaintenanceWindowErr
    from .non_empty_id import NonEmptyId
    from .oauth_scope import OauthScope
    from .ok_resp import OkResp
    from .order import Order
    from .order_not_found_err import OrderNotFoundErr
    from .order_status import OrderStatus
    from .page_of_category import PageOfCategory
    from .page_of_customer import PageOfCustomer
    from .page_of_order import PageOfOrder
    from .page_of_product import PageOfProduct
    from .pagination import Pagination
    from .payment import Payment
    from .payment_failed_err import PaymentFailedErr
    from .payment_method import PaymentMethod
    from .percent_bp import PercentBp
    from .product import Product
    from .product_ref import ProductRef
    from .public_health_resp_body import PublicHealthRespBody
    from .rate_limited_err import RateLimitedErr
    from .replay_resp_body import ReplayRespBody
    from .safe_url import SafeUrl
    from .sku import Sku
    from .slug import Slug
    from .suspension_reason import SuspensionReason
    from .timestamps import Timestamps
    from .track_public_resp_body import TrackPublicRespBody
    from .unauthorized_err import UnauthorizedErr
    from .upload_avatar_req import UploadAvatarReq
    from .upload_avatar_resp_body import UploadAvatarRespBody
_dynamic_imports: typing.Dict[str, str] = {
    "ActionDeniedErr": ".action_denied_err",
    "Address": ".address",
    "AuditFields": ".audit_fields",
    "BulkExportRespBody": ".bulk_export_resp_body",
    "CancelOrderRespBody": ".cancel_order_resp_body",
    "Category": ".category",
    "CategoryRef": ".category_ref",
    "Cents": ".cents",
    "Contact": ".contact",
    "CountryCode": ".country_code",
    "CreateCustomerReq": ".create_customer_req",
    "CreateCustomerRespBody": ".create_customer_resp_body",
    "CreateOrderReq": ".create_order_req",
    "CreateOrderRespBody": ".create_order_resp_body",
    "CreateProductReq": ".create_product_req",
    "CreateProductRespBody": ".create_product_resp_body",
    "CurrencyCode": ".currency_code",
    "Customer": ".customer",
    "CustomerRef": ".customer_ref",
    "DefaultsRespBody": ".defaults_resp_body",
    "DefaultsShowcaseReq": ".defaults_showcase_req",
    "DeleteCustomerRespBody": ".delete_customer_resp_body",
    "DeleteProductRespBody": ".delete_product_resp_body",
    "Email": ".email",
    "FilterOrdersReq": ".filter_orders_req",
    "FilterOrdersRespBody": ".filter_orders_resp_body",
    "ForceShipRespBody": ".force_ship_resp_body",
    "Geocode": ".geocode",
    "GetCustomerReq": ".get_customer_req",
    "GetCustomerRespBody": ".get_customer_resp_body",
    "GetOrderReq": ".get_order_req",
    "GetOrderRespBody": ".get_order_resp_body",
    "GetProductReq": ".get_product_req",
    "GetProductRespBody": ".get_product_resp_body",
    "InternalErr": ".internal_err",
    "Latitude": ".latitude",
    "LineItem": ".line_item",
    "ListCategoriesRespBody": ".list_categories_resp_body",
    "ListCustomersRespBody": ".list_customers_resp_body",
    "ListOrdersReq": ".list_orders_req",
    "ListOrdersRespBody": ".list_orders_resp_body",
    "ListProductsReq": ".list_products_req",
    "ListProductsRespBody": ".list_products_resp_body",
    "Longitude": ".longitude",
    "MaintenanceReason": ".maintenance_reason",
    "MaintenanceWindowErr": ".maintenance_window_err",
    "NonEmptyId": ".non_empty_id",
    "OauthScope": ".oauth_scope",
    "OkResp": ".ok_resp",
    "Order": ".order",
    "OrderNotFoundErr": ".order_not_found_err",
    "OrderStatus": ".order_status",
    "PageOfCategory": ".page_of_category",
    "PageOfCustomer": ".page_of_customer",
    "PageOfOrder": ".page_of_order",
    "PageOfProduct": ".page_of_product",
    "Pagination": ".pagination",
    "Payment": ".payment",
    "PaymentFailedErr": ".payment_failed_err",
    "PaymentMethod": ".payment_method",
    "PercentBp": ".percent_bp",
    "Product": ".product",
    "ProductRef": ".product_ref",
    "PublicHealthRespBody": ".public_health_resp_body",
    "RateLimitedErr": ".rate_limited_err",
    "ReplayRespBody": ".replay_resp_body",
    "SafeUrl": ".safe_url",
    "Sku": ".sku",
    "Slug": ".slug",
    "SuspensionReason": ".suspension_reason",
    "Timestamps": ".timestamps",
    "TrackPublicRespBody": ".track_public_resp_body",
    "UnauthorizedErr": ".unauthorized_err",
    "UploadAvatarReq": ".upload_avatar_req",
    "UploadAvatarRespBody": ".upload_avatar_resp_body",
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
    "ActionDeniedErr",
    "Address",
    "AuditFields",
    "BulkExportRespBody",
    "CancelOrderRespBody",
    "Category",
    "CategoryRef",
    "Cents",
    "Contact",
    "CountryCode",
    "CreateCustomerReq",
    "CreateCustomerRespBody",
    "CreateOrderReq",
    "CreateOrderRespBody",
    "CreateProductReq",
    "CreateProductRespBody",
    "CurrencyCode",
    "Customer",
    "CustomerRef",
    "DefaultsRespBody",
    "DefaultsShowcaseReq",
    "DeleteCustomerRespBody",
    "DeleteProductRespBody",
    "Email",
    "FilterOrdersReq",
    "FilterOrdersRespBody",
    "ForceShipRespBody",
    "Geocode",
    "GetCustomerReq",
    "GetCustomerRespBody",
    "GetOrderReq",
    "GetOrderRespBody",
    "GetProductReq",
    "GetProductRespBody",
    "InternalErr",
    "Latitude",
    "LineItem",
    "ListCategoriesRespBody",
    "ListCustomersRespBody",
    "ListOrdersReq",
    "ListOrdersRespBody",
    "ListProductsReq",
    "ListProductsRespBody",
    "Longitude",
    "MaintenanceReason",
    "MaintenanceWindowErr",
    "NonEmptyId",
    "OauthScope",
    "OkResp",
    "Order",
    "OrderNotFoundErr",
    "OrderStatus",
    "PageOfCategory",
    "PageOfCustomer",
    "PageOfOrder",
    "PageOfProduct",
    "Pagination",
    "Payment",
    "PaymentFailedErr",
    "PaymentMethod",
    "PercentBp",
    "Product",
    "ProductRef",
    "PublicHealthRespBody",
    "RateLimitedErr",
    "ReplayRespBody",
    "SafeUrl",
    "Sku",
    "Slug",
    "SuspensionReason",
    "Timestamps",
    "TrackPublicRespBody",
    "UnauthorizedErr",
    "UploadAvatarReq",
    "UploadAvatarRespBody",
]
