



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .approveorder import Approveorder
    from .approveorder_errors_item import ApproveorderErrorsItem
    from .approveorder_fields import ApproveorderFields
    from .approveorder_fields_fields import ApproveorderFieldsFields
    from .bundle_items_item import BundleItemsItem
    from .client_profile_data import ClientProfileData
    from .custom_app import CustomApp
    from .custom_data import CustomData
    from .delivery_ids import DeliveryIds
    from .deliverybyfranchiseseller import Deliverybyfranchiseseller
    from .deliverybyfranchiseseller_errors_item import DeliverybyfranchisesellerErrorsItem
    from .deliverybyfranchiseseller_fields import DeliverybyfranchisesellerFields
    from .deliverybyfranchiseseller_fields_fields import DeliverybyfranchisesellerFieldsFields
    from .deliverybyseller import Deliverybyseller
    from .deliverybyseller_errors_item import DeliverybysellerErrorsItem
    from .deliverybyseller_fields import DeliverybysellerFields
    from .deliverybyseller_fields_fields import DeliverybysellerFieldsFields
    from .fields import Fields
    from .fulfillment_item import FulfillmentItem
    from .geo_coordinates import GeoCoordinates
    from .invoice_data import InvoiceData
    from .item import Item
    from .item_attachment import ItemAttachment
    from .logistics_info import LogisticsInfo
    from .pickup_in_point import PickupInPoint
    from .pickup_in_point_errors_item import PickupInPointErrorsItem
    from .pickup_in_point_fields import PickupInPointFields
    from .pickup_in_point_fields_fields import PickupInPointFieldsFields
    from .pickup_in_pointfranchise import PickupInPointfranchise
    from .pickup_in_pointfranchise_errors_item import PickupInPointfranchiseErrorsItem
    from .pickup_in_pointfranchise_fields import PickupInPointfranchiseFields
    from .pickup_in_pointfranchise_fields_fields import PickupInPointfranchiseFieldsFields
    from .selected_address import SelectedAddress
    from .shipping_data import ShippingData
    from .user_payment_info import UserPaymentInfo
_dynamic_imports: typing.Dict[str, str] = {
    "Approveorder": ".approveorder",
    "ApproveorderErrorsItem": ".approveorder_errors_item",
    "ApproveorderFields": ".approveorder_fields",
    "ApproveorderFieldsFields": ".approveorder_fields_fields",
    "BundleItemsItem": ".bundle_items_item",
    "ClientProfileData": ".client_profile_data",
    "CustomApp": ".custom_app",
    "CustomData": ".custom_data",
    "DeliveryIds": ".delivery_ids",
    "Deliverybyfranchiseseller": ".deliverybyfranchiseseller",
    "DeliverybyfranchisesellerErrorsItem": ".deliverybyfranchiseseller_errors_item",
    "DeliverybyfranchisesellerFields": ".deliverybyfranchiseseller_fields",
    "DeliverybyfranchisesellerFieldsFields": ".deliverybyfranchiseseller_fields_fields",
    "Deliverybyseller": ".deliverybyseller",
    "DeliverybysellerErrorsItem": ".deliverybyseller_errors_item",
    "DeliverybysellerFields": ".deliverybyseller_fields",
    "DeliverybysellerFieldsFields": ".deliverybyseller_fields_fields",
    "Fields": ".fields",
    "FulfillmentItem": ".fulfillment_item",
    "GeoCoordinates": ".geo_coordinates",
    "InvoiceData": ".invoice_data",
    "Item": ".item",
    "ItemAttachment": ".item_attachment",
    "LogisticsInfo": ".logistics_info",
    "PickupInPoint": ".pickup_in_point",
    "PickupInPointErrorsItem": ".pickup_in_point_errors_item",
    "PickupInPointFields": ".pickup_in_point_fields",
    "PickupInPointFieldsFields": ".pickup_in_point_fields_fields",
    "PickupInPointfranchise": ".pickup_in_pointfranchise",
    "PickupInPointfranchiseErrorsItem": ".pickup_in_pointfranchise_errors_item",
    "PickupInPointfranchiseFields": ".pickup_in_pointfranchise_fields",
    "PickupInPointfranchiseFieldsFields": ".pickup_in_pointfranchise_fields_fields",
    "SelectedAddress": ".selected_address",
    "ShippingData": ".shipping_data",
    "UserPaymentInfo": ".user_payment_info",
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
    "Approveorder",
    "ApproveorderErrorsItem",
    "ApproveorderFields",
    "ApproveorderFieldsFields",
    "BundleItemsItem",
    "ClientProfileData",
    "CustomApp",
    "CustomData",
    "DeliveryIds",
    "Deliverybyfranchiseseller",
    "DeliverybyfranchisesellerErrorsItem",
    "DeliverybyfranchisesellerFields",
    "DeliverybyfranchisesellerFieldsFields",
    "Deliverybyseller",
    "DeliverybysellerErrorsItem",
    "DeliverybysellerFields",
    "DeliverybysellerFieldsFields",
    "Fields",
    "FulfillmentItem",
    "GeoCoordinates",
    "InvoiceData",
    "Item",
    "ItemAttachment",
    "LogisticsInfo",
    "PickupInPoint",
    "PickupInPointErrorsItem",
    "PickupInPointFields",
    "PickupInPointFieldsFields",
    "PickupInPointfranchise",
    "PickupInPointfranchiseErrorsItem",
    "PickupInPointfranchiseFields",
    "PickupInPointfranchiseFieldsFields",
    "SelectedAddress",
    "ShippingData",
    "UserPaymentInfo",
]
