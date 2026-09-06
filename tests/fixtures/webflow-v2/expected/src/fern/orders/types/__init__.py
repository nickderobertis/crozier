



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ecomm_new_order_payload import EcommNewOrderPayload
    from .ecomm_new_order_payload_payload import EcommNewOrderPayloadPayload
    from .ecomm_new_order_payload_payload_all_addresses_item import EcommNewOrderPayloadPayloadAllAddressesItem
    from .ecomm_new_order_payload_payload_all_addresses_item_japan_type import (
        EcommNewOrderPayloadPayloadAllAddressesItemJapanType,
    )
    from .ecomm_new_order_payload_payload_all_addresses_item_type import EcommNewOrderPayloadPayloadAllAddressesItemType
    from .ecomm_new_order_payload_payload_application_fee import EcommNewOrderPayloadPayloadApplicationFee
    from .ecomm_new_order_payload_payload_billing_address import EcommNewOrderPayloadPayloadBillingAddress
    from .ecomm_new_order_payload_payload_billing_address_japan_type import (
        EcommNewOrderPayloadPayloadBillingAddressJapanType,
    )
    from .ecomm_new_order_payload_payload_billing_address_type import EcommNewOrderPayloadPayloadBillingAddressType
    from .ecomm_new_order_payload_payload_customer_info import EcommNewOrderPayloadPayloadCustomerInfo
    from .ecomm_new_order_payload_payload_customer_paid import EcommNewOrderPayloadPayloadCustomerPaid
    from .ecomm_new_order_payload_payload_dispute_last_status import EcommNewOrderPayloadPayloadDisputeLastStatus
    from .ecomm_new_order_payload_payload_download_files_item import EcommNewOrderPayloadPayloadDownloadFilesItem
    from .ecomm_new_order_payload_payload_metadata import EcommNewOrderPayloadPayloadMetadata
    from .ecomm_new_order_payload_payload_net_amount import EcommNewOrderPayloadPayloadNetAmount
    from .ecomm_new_order_payload_payload_paypal_details import EcommNewOrderPayloadPayloadPaypalDetails
    from .ecomm_new_order_payload_payload_purchased_items_item import EcommNewOrderPayloadPayloadPurchasedItemsItem
    from .ecomm_new_order_payload_payload_purchased_items_item_row_total import (
        EcommNewOrderPayloadPayloadPurchasedItemsItemRowTotal,
    )
    from .ecomm_new_order_payload_payload_purchased_items_item_variant_image import (
        EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImage,
    )
    from .ecomm_new_order_payload_payload_purchased_items_item_variant_image_file import (
        EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFile,
    )
    from .ecomm_new_order_payload_payload_purchased_items_item_variant_image_file_variants_item import (
        EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .ecomm_new_order_payload_payload_purchased_items_item_variant_price import (
        EcommNewOrderPayloadPayloadPurchasedItemsItemVariantPrice,
    )
    from .ecomm_new_order_payload_payload_shipping_address import EcommNewOrderPayloadPayloadShippingAddress
    from .ecomm_new_order_payload_payload_shipping_address_japan_type import (
        EcommNewOrderPayloadPayloadShippingAddressJapanType,
    )
    from .ecomm_new_order_payload_payload_shipping_address_type import EcommNewOrderPayloadPayloadShippingAddressType
    from .ecomm_new_order_payload_payload_status import EcommNewOrderPayloadPayloadStatus
    from .ecomm_new_order_payload_payload_stripe_card import EcommNewOrderPayloadPayloadStripeCard
    from .ecomm_new_order_payload_payload_stripe_card_brand import EcommNewOrderPayloadPayloadStripeCardBrand
    from .ecomm_new_order_payload_payload_stripe_card_expires import EcommNewOrderPayloadPayloadStripeCardExpires
    from .ecomm_new_order_payload_payload_stripe_details import EcommNewOrderPayloadPayloadStripeDetails
    from .ecomm_new_order_payload_payload_totals import EcommNewOrderPayloadPayloadTotals
    from .ecomm_new_order_payload_payload_totals_extras_item import EcommNewOrderPayloadPayloadTotalsExtrasItem
    from .ecomm_new_order_payload_payload_totals_extras_item_price import (
        EcommNewOrderPayloadPayloadTotalsExtrasItemPrice,
    )
    from .ecomm_new_order_payload_payload_totals_extras_item_type import EcommNewOrderPayloadPayloadTotalsExtrasItemType
    from .ecomm_new_order_payload_payload_totals_subtotal import EcommNewOrderPayloadPayloadTotalsSubtotal
    from .ecomm_new_order_payload_payload_totals_total import EcommNewOrderPayloadPayloadTotalsTotal
    from .ecomm_order_changed_payload import EcommOrderChangedPayload
    from .ecomm_order_changed_payload_payload import EcommOrderChangedPayloadPayload
    from .ecomm_order_changed_payload_payload_all_addresses_item import EcommOrderChangedPayloadPayloadAllAddressesItem
    from .ecomm_order_changed_payload_payload_all_addresses_item_japan_type import (
        EcommOrderChangedPayloadPayloadAllAddressesItemJapanType,
    )
    from .ecomm_order_changed_payload_payload_all_addresses_item_type import (
        EcommOrderChangedPayloadPayloadAllAddressesItemType,
    )
    from .ecomm_order_changed_payload_payload_application_fee import EcommOrderChangedPayloadPayloadApplicationFee
    from .ecomm_order_changed_payload_payload_billing_address import EcommOrderChangedPayloadPayloadBillingAddress
    from .ecomm_order_changed_payload_payload_billing_address_japan_type import (
        EcommOrderChangedPayloadPayloadBillingAddressJapanType,
    )
    from .ecomm_order_changed_payload_payload_billing_address_type import (
        EcommOrderChangedPayloadPayloadBillingAddressType,
    )
    from .ecomm_order_changed_payload_payload_customer_info import EcommOrderChangedPayloadPayloadCustomerInfo
    from .ecomm_order_changed_payload_payload_customer_paid import EcommOrderChangedPayloadPayloadCustomerPaid
    from .ecomm_order_changed_payload_payload_dispute_last_status import (
        EcommOrderChangedPayloadPayloadDisputeLastStatus,
    )
    from .ecomm_order_changed_payload_payload_download_files_item import (
        EcommOrderChangedPayloadPayloadDownloadFilesItem,
    )
    from .ecomm_order_changed_payload_payload_metadata import EcommOrderChangedPayloadPayloadMetadata
    from .ecomm_order_changed_payload_payload_net_amount import EcommOrderChangedPayloadPayloadNetAmount
    from .ecomm_order_changed_payload_payload_paypal_details import EcommOrderChangedPayloadPayloadPaypalDetails
    from .ecomm_order_changed_payload_payload_purchased_items_item import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItem,
    )
    from .ecomm_order_changed_payload_payload_purchased_items_item_row_total import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItemRowTotal,
    )
    from .ecomm_order_changed_payload_payload_purchased_items_item_variant_image import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage,
    )
    from .ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFile,
    )
    from .ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file_variants_item import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .ecomm_order_changed_payload_payload_purchased_items_item_variant_price import (
        EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantPrice,
    )
    from .ecomm_order_changed_payload_payload_shipping_address import EcommOrderChangedPayloadPayloadShippingAddress
    from .ecomm_order_changed_payload_payload_shipping_address_japan_type import (
        EcommOrderChangedPayloadPayloadShippingAddressJapanType,
    )
    from .ecomm_order_changed_payload_payload_shipping_address_type import (
        EcommOrderChangedPayloadPayloadShippingAddressType,
    )
    from .ecomm_order_changed_payload_payload_status import EcommOrderChangedPayloadPayloadStatus
    from .ecomm_order_changed_payload_payload_stripe_card import EcommOrderChangedPayloadPayloadStripeCard
    from .ecomm_order_changed_payload_payload_stripe_card_brand import EcommOrderChangedPayloadPayloadStripeCardBrand
    from .ecomm_order_changed_payload_payload_stripe_card_expires import (
        EcommOrderChangedPayloadPayloadStripeCardExpires,
    )
    from .ecomm_order_changed_payload_payload_stripe_details import EcommOrderChangedPayloadPayloadStripeDetails
    from .ecomm_order_changed_payload_payload_totals import EcommOrderChangedPayloadPayloadTotals
    from .ecomm_order_changed_payload_payload_totals_extras_item import EcommOrderChangedPayloadPayloadTotalsExtrasItem
    from .ecomm_order_changed_payload_payload_totals_extras_item_price import (
        EcommOrderChangedPayloadPayloadTotalsExtrasItemPrice,
    )
    from .ecomm_order_changed_payload_payload_totals_extras_item_type import (
        EcommOrderChangedPayloadPayloadTotalsExtrasItemType,
    )
    from .ecomm_order_changed_payload_payload_totals_subtotal import EcommOrderChangedPayloadPayloadTotalsSubtotal
    from .ecomm_order_changed_payload_payload_totals_total import EcommOrderChangedPayloadPayloadTotalsTotal
    from .get_orders_response import GetOrdersResponse
    from .get_orders_response_all_addresses_item import GetOrdersResponseAllAddressesItem
    from .get_orders_response_all_addresses_item_japan_type import GetOrdersResponseAllAddressesItemJapanType
    from .get_orders_response_all_addresses_item_type import GetOrdersResponseAllAddressesItemType
    from .get_orders_response_application_fee import GetOrdersResponseApplicationFee
    from .get_orders_response_billing_address import GetOrdersResponseBillingAddress
    from .get_orders_response_billing_address_japan_type import GetOrdersResponseBillingAddressJapanType
    from .get_orders_response_billing_address_type import GetOrdersResponseBillingAddressType
    from .get_orders_response_customer_info import GetOrdersResponseCustomerInfo
    from .get_orders_response_customer_paid import GetOrdersResponseCustomerPaid
    from .get_orders_response_dispute_last_status import GetOrdersResponseDisputeLastStatus
    from .get_orders_response_download_files_item import GetOrdersResponseDownloadFilesItem
    from .get_orders_response_metadata import GetOrdersResponseMetadata
    from .get_orders_response_net_amount import GetOrdersResponseNetAmount
    from .get_orders_response_paypal_details import GetOrdersResponsePaypalDetails
    from .get_orders_response_purchased_items_item import GetOrdersResponsePurchasedItemsItem
    from .get_orders_response_purchased_items_item_row_total import GetOrdersResponsePurchasedItemsItemRowTotal
    from .get_orders_response_purchased_items_item_variant_image import GetOrdersResponsePurchasedItemsItemVariantImage
    from .get_orders_response_purchased_items_item_variant_image_file import (
        GetOrdersResponsePurchasedItemsItemVariantImageFile,
    )
    from .get_orders_response_purchased_items_item_variant_image_file_variants_item import (
        GetOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .get_orders_response_purchased_items_item_variant_price import GetOrdersResponsePurchasedItemsItemVariantPrice
    from .get_orders_response_shipping_address import GetOrdersResponseShippingAddress
    from .get_orders_response_shipping_address_japan_type import GetOrdersResponseShippingAddressJapanType
    from .get_orders_response_shipping_address_type import GetOrdersResponseShippingAddressType
    from .get_orders_response_status import GetOrdersResponseStatus
    from .get_orders_response_stripe_card import GetOrdersResponseStripeCard
    from .get_orders_response_stripe_card_brand import GetOrdersResponseStripeCardBrand
    from .get_orders_response_stripe_card_expires import GetOrdersResponseStripeCardExpires
    from .get_orders_response_stripe_details import GetOrdersResponseStripeDetails
    from .get_orders_response_totals import GetOrdersResponseTotals
    from .get_orders_response_totals_extras_item import GetOrdersResponseTotalsExtrasItem
    from .get_orders_response_totals_extras_item_price import GetOrdersResponseTotalsExtrasItemPrice
    from .get_orders_response_totals_extras_item_type import GetOrdersResponseTotalsExtrasItemType
    from .get_orders_response_totals_subtotal import GetOrdersResponseTotalsSubtotal
    from .get_orders_response_totals_total import GetOrdersResponseTotalsTotal
    from .list_orders_request_status import ListOrdersRequestStatus
    from .list_orders_response import ListOrdersResponse
    from .list_orders_response_orders_item import ListOrdersResponseOrdersItem
    from .list_orders_response_orders_item_all_addresses_item import ListOrdersResponseOrdersItemAllAddressesItem
    from .list_orders_response_orders_item_all_addresses_item_japan_type import (
        ListOrdersResponseOrdersItemAllAddressesItemJapanType,
    )
    from .list_orders_response_orders_item_all_addresses_item_type import (
        ListOrdersResponseOrdersItemAllAddressesItemType,
    )
    from .list_orders_response_orders_item_application_fee import ListOrdersResponseOrdersItemApplicationFee
    from .list_orders_response_orders_item_billing_address import ListOrdersResponseOrdersItemBillingAddress
    from .list_orders_response_orders_item_billing_address_japan_type import (
        ListOrdersResponseOrdersItemBillingAddressJapanType,
    )
    from .list_orders_response_orders_item_billing_address_type import ListOrdersResponseOrdersItemBillingAddressType
    from .list_orders_response_orders_item_customer_info import ListOrdersResponseOrdersItemCustomerInfo
    from .list_orders_response_orders_item_customer_paid import ListOrdersResponseOrdersItemCustomerPaid
    from .list_orders_response_orders_item_dispute_last_status import ListOrdersResponseOrdersItemDisputeLastStatus
    from .list_orders_response_orders_item_download_files_item import ListOrdersResponseOrdersItemDownloadFilesItem
    from .list_orders_response_orders_item_metadata import ListOrdersResponseOrdersItemMetadata
    from .list_orders_response_orders_item_net_amount import ListOrdersResponseOrdersItemNetAmount
    from .list_orders_response_orders_item_paypal_details import ListOrdersResponseOrdersItemPaypalDetails
    from .list_orders_response_orders_item_purchased_items_item import ListOrdersResponseOrdersItemPurchasedItemsItem
    from .list_orders_response_orders_item_purchased_items_item_row_total import (
        ListOrdersResponseOrdersItemPurchasedItemsItemRowTotal,
    )
    from .list_orders_response_orders_item_purchased_items_item_variant_image import (
        ListOrdersResponseOrdersItemPurchasedItemsItemVariantImage,
    )
    from .list_orders_response_orders_item_purchased_items_item_variant_image_file import (
        ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFile,
    )
    from .list_orders_response_orders_item_purchased_items_item_variant_image_file_variants_item import (
        ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .list_orders_response_orders_item_purchased_items_item_variant_price import (
        ListOrdersResponseOrdersItemPurchasedItemsItemVariantPrice,
    )
    from .list_orders_response_orders_item_shipping_address import ListOrdersResponseOrdersItemShippingAddress
    from .list_orders_response_orders_item_shipping_address_japan_type import (
        ListOrdersResponseOrdersItemShippingAddressJapanType,
    )
    from .list_orders_response_orders_item_shipping_address_type import ListOrdersResponseOrdersItemShippingAddressType
    from .list_orders_response_orders_item_status import ListOrdersResponseOrdersItemStatus
    from .list_orders_response_orders_item_stripe_card import ListOrdersResponseOrdersItemStripeCard
    from .list_orders_response_orders_item_stripe_card_brand import ListOrdersResponseOrdersItemStripeCardBrand
    from .list_orders_response_orders_item_stripe_card_expires import ListOrdersResponseOrdersItemStripeCardExpires
    from .list_orders_response_orders_item_stripe_details import ListOrdersResponseOrdersItemStripeDetails
    from .list_orders_response_orders_item_totals import ListOrdersResponseOrdersItemTotals
    from .list_orders_response_orders_item_totals_extras_item import ListOrdersResponseOrdersItemTotalsExtrasItem
    from .list_orders_response_orders_item_totals_extras_item_price import (
        ListOrdersResponseOrdersItemTotalsExtrasItemPrice,
    )
    from .list_orders_response_orders_item_totals_extras_item_type import (
        ListOrdersResponseOrdersItemTotalsExtrasItemType,
    )
    from .list_orders_response_orders_item_totals_subtotal import ListOrdersResponseOrdersItemTotalsSubtotal
    from .list_orders_response_orders_item_totals_total import ListOrdersResponseOrdersItemTotalsTotal
    from .list_orders_response_pagination import ListOrdersResponsePagination
    from .refund_orders_request_reason import RefundOrdersRequestReason
    from .refund_orders_response import RefundOrdersResponse
    from .refund_orders_response_all_addresses_item import RefundOrdersResponseAllAddressesItem
    from .refund_orders_response_all_addresses_item_japan_type import RefundOrdersResponseAllAddressesItemJapanType
    from .refund_orders_response_all_addresses_item_type import RefundOrdersResponseAllAddressesItemType
    from .refund_orders_response_application_fee import RefundOrdersResponseApplicationFee
    from .refund_orders_response_billing_address import RefundOrdersResponseBillingAddress
    from .refund_orders_response_billing_address_japan_type import RefundOrdersResponseBillingAddressJapanType
    from .refund_orders_response_billing_address_type import RefundOrdersResponseBillingAddressType
    from .refund_orders_response_customer_info import RefundOrdersResponseCustomerInfo
    from .refund_orders_response_customer_paid import RefundOrdersResponseCustomerPaid
    from .refund_orders_response_dispute_last_status import RefundOrdersResponseDisputeLastStatus
    from .refund_orders_response_download_files_item import RefundOrdersResponseDownloadFilesItem
    from .refund_orders_response_metadata import RefundOrdersResponseMetadata
    from .refund_orders_response_net_amount import RefundOrdersResponseNetAmount
    from .refund_orders_response_paypal_details import RefundOrdersResponsePaypalDetails
    from .refund_orders_response_purchased_items_item import RefundOrdersResponsePurchasedItemsItem
    from .refund_orders_response_purchased_items_item_row_total import RefundOrdersResponsePurchasedItemsItemRowTotal
    from .refund_orders_response_purchased_items_item_variant_image import (
        RefundOrdersResponsePurchasedItemsItemVariantImage,
    )
    from .refund_orders_response_purchased_items_item_variant_image_file import (
        RefundOrdersResponsePurchasedItemsItemVariantImageFile,
    )
    from .refund_orders_response_purchased_items_item_variant_image_file_variants_item import (
        RefundOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .refund_orders_response_purchased_items_item_variant_price import (
        RefundOrdersResponsePurchasedItemsItemVariantPrice,
    )
    from .refund_orders_response_shipping_address import RefundOrdersResponseShippingAddress
    from .refund_orders_response_shipping_address_japan_type import RefundOrdersResponseShippingAddressJapanType
    from .refund_orders_response_shipping_address_type import RefundOrdersResponseShippingAddressType
    from .refund_orders_response_status import RefundOrdersResponseStatus
    from .refund_orders_response_stripe_card import RefundOrdersResponseStripeCard
    from .refund_orders_response_stripe_card_brand import RefundOrdersResponseStripeCardBrand
    from .refund_orders_response_stripe_card_expires import RefundOrdersResponseStripeCardExpires
    from .refund_orders_response_stripe_details import RefundOrdersResponseStripeDetails
    from .refund_orders_response_totals import RefundOrdersResponseTotals
    from .refund_orders_response_totals_extras_item import RefundOrdersResponseTotalsExtrasItem
    from .refund_orders_response_totals_extras_item_price import RefundOrdersResponseTotalsExtrasItemPrice
    from .refund_orders_response_totals_extras_item_type import RefundOrdersResponseTotalsExtrasItemType
    from .refund_orders_response_totals_subtotal import RefundOrdersResponseTotalsSubtotal
    from .refund_orders_response_totals_total import RefundOrdersResponseTotalsTotal
    from .update_fulfill_orders_response import UpdateFulfillOrdersResponse
    from .update_fulfill_orders_response_all_addresses_item import UpdateFulfillOrdersResponseAllAddressesItem
    from .update_fulfill_orders_response_all_addresses_item_japan_type import (
        UpdateFulfillOrdersResponseAllAddressesItemJapanType,
    )
    from .update_fulfill_orders_response_all_addresses_item_type import UpdateFulfillOrdersResponseAllAddressesItemType
    from .update_fulfill_orders_response_application_fee import UpdateFulfillOrdersResponseApplicationFee
    from .update_fulfill_orders_response_billing_address import UpdateFulfillOrdersResponseBillingAddress
    from .update_fulfill_orders_response_billing_address_japan_type import (
        UpdateFulfillOrdersResponseBillingAddressJapanType,
    )
    from .update_fulfill_orders_response_billing_address_type import UpdateFulfillOrdersResponseBillingAddressType
    from .update_fulfill_orders_response_customer_info import UpdateFulfillOrdersResponseCustomerInfo
    from .update_fulfill_orders_response_customer_paid import UpdateFulfillOrdersResponseCustomerPaid
    from .update_fulfill_orders_response_dispute_last_status import UpdateFulfillOrdersResponseDisputeLastStatus
    from .update_fulfill_orders_response_download_files_item import UpdateFulfillOrdersResponseDownloadFilesItem
    from .update_fulfill_orders_response_metadata import UpdateFulfillOrdersResponseMetadata
    from .update_fulfill_orders_response_net_amount import UpdateFulfillOrdersResponseNetAmount
    from .update_fulfill_orders_response_paypal_details import UpdateFulfillOrdersResponsePaypalDetails
    from .update_fulfill_orders_response_purchased_items_item import UpdateFulfillOrdersResponsePurchasedItemsItem
    from .update_fulfill_orders_response_purchased_items_item_row_total import (
        UpdateFulfillOrdersResponsePurchasedItemsItemRowTotal,
    )
    from .update_fulfill_orders_response_purchased_items_item_variant_image import (
        UpdateFulfillOrdersResponsePurchasedItemsItemVariantImage,
    )
    from .update_fulfill_orders_response_purchased_items_item_variant_image_file import (
        UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFile,
    )
    from .update_fulfill_orders_response_purchased_items_item_variant_image_file_variants_item import (
        UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .update_fulfill_orders_response_purchased_items_item_variant_price import (
        UpdateFulfillOrdersResponsePurchasedItemsItemVariantPrice,
    )
    from .update_fulfill_orders_response_shipping_address import UpdateFulfillOrdersResponseShippingAddress
    from .update_fulfill_orders_response_shipping_address_japan_type import (
        UpdateFulfillOrdersResponseShippingAddressJapanType,
    )
    from .update_fulfill_orders_response_shipping_address_type import UpdateFulfillOrdersResponseShippingAddressType
    from .update_fulfill_orders_response_status import UpdateFulfillOrdersResponseStatus
    from .update_fulfill_orders_response_stripe_card import UpdateFulfillOrdersResponseStripeCard
    from .update_fulfill_orders_response_stripe_card_brand import UpdateFulfillOrdersResponseStripeCardBrand
    from .update_fulfill_orders_response_stripe_card_expires import UpdateFulfillOrdersResponseStripeCardExpires
    from .update_fulfill_orders_response_stripe_details import UpdateFulfillOrdersResponseStripeDetails
    from .update_fulfill_orders_response_totals import UpdateFulfillOrdersResponseTotals
    from .update_fulfill_orders_response_totals_extras_item import UpdateFulfillOrdersResponseTotalsExtrasItem
    from .update_fulfill_orders_response_totals_extras_item_price import (
        UpdateFulfillOrdersResponseTotalsExtrasItemPrice,
    )
    from .update_fulfill_orders_response_totals_extras_item_type import UpdateFulfillOrdersResponseTotalsExtrasItemType
    from .update_fulfill_orders_response_totals_subtotal import UpdateFulfillOrdersResponseTotalsSubtotal
    from .update_fulfill_orders_response_totals_total import UpdateFulfillOrdersResponseTotalsTotal
    from .update_orders_response import UpdateOrdersResponse
    from .update_orders_response_all_addresses_item import UpdateOrdersResponseAllAddressesItem
    from .update_orders_response_all_addresses_item_japan_type import UpdateOrdersResponseAllAddressesItemJapanType
    from .update_orders_response_all_addresses_item_type import UpdateOrdersResponseAllAddressesItemType
    from .update_orders_response_application_fee import UpdateOrdersResponseApplicationFee
    from .update_orders_response_billing_address import UpdateOrdersResponseBillingAddress
    from .update_orders_response_billing_address_japan_type import UpdateOrdersResponseBillingAddressJapanType
    from .update_orders_response_billing_address_type import UpdateOrdersResponseBillingAddressType
    from .update_orders_response_customer_info import UpdateOrdersResponseCustomerInfo
    from .update_orders_response_customer_paid import UpdateOrdersResponseCustomerPaid
    from .update_orders_response_dispute_last_status import UpdateOrdersResponseDisputeLastStatus
    from .update_orders_response_download_files_item import UpdateOrdersResponseDownloadFilesItem
    from .update_orders_response_metadata import UpdateOrdersResponseMetadata
    from .update_orders_response_net_amount import UpdateOrdersResponseNetAmount
    from .update_orders_response_paypal_details import UpdateOrdersResponsePaypalDetails
    from .update_orders_response_purchased_items_item import UpdateOrdersResponsePurchasedItemsItem
    from .update_orders_response_purchased_items_item_row_total import UpdateOrdersResponsePurchasedItemsItemRowTotal
    from .update_orders_response_purchased_items_item_variant_image import (
        UpdateOrdersResponsePurchasedItemsItemVariantImage,
    )
    from .update_orders_response_purchased_items_item_variant_image_file import (
        UpdateOrdersResponsePurchasedItemsItemVariantImageFile,
    )
    from .update_orders_response_purchased_items_item_variant_image_file_variants_item import (
        UpdateOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .update_orders_response_purchased_items_item_variant_price import (
        UpdateOrdersResponsePurchasedItemsItemVariantPrice,
    )
    from .update_orders_response_shipping_address import UpdateOrdersResponseShippingAddress
    from .update_orders_response_shipping_address_japan_type import UpdateOrdersResponseShippingAddressJapanType
    from .update_orders_response_shipping_address_type import UpdateOrdersResponseShippingAddressType
    from .update_orders_response_status import UpdateOrdersResponseStatus
    from .update_orders_response_stripe_card import UpdateOrdersResponseStripeCard
    from .update_orders_response_stripe_card_brand import UpdateOrdersResponseStripeCardBrand
    from .update_orders_response_stripe_card_expires import UpdateOrdersResponseStripeCardExpires
    from .update_orders_response_stripe_details import UpdateOrdersResponseStripeDetails
    from .update_orders_response_totals import UpdateOrdersResponseTotals
    from .update_orders_response_totals_extras_item import UpdateOrdersResponseTotalsExtrasItem
    from .update_orders_response_totals_extras_item_price import UpdateOrdersResponseTotalsExtrasItemPrice
    from .update_orders_response_totals_extras_item_type import UpdateOrdersResponseTotalsExtrasItemType
    from .update_orders_response_totals_subtotal import UpdateOrdersResponseTotalsSubtotal
    from .update_orders_response_totals_total import UpdateOrdersResponseTotalsTotal
    from .update_unfulfill_orders_response import UpdateUnfulfillOrdersResponse
    from .update_unfulfill_orders_response_all_addresses_item import UpdateUnfulfillOrdersResponseAllAddressesItem
    from .update_unfulfill_orders_response_all_addresses_item_japan_type import (
        UpdateUnfulfillOrdersResponseAllAddressesItemJapanType,
    )
    from .update_unfulfill_orders_response_all_addresses_item_type import (
        UpdateUnfulfillOrdersResponseAllAddressesItemType,
    )
    from .update_unfulfill_orders_response_application_fee import UpdateUnfulfillOrdersResponseApplicationFee
    from .update_unfulfill_orders_response_billing_address import UpdateUnfulfillOrdersResponseBillingAddress
    from .update_unfulfill_orders_response_billing_address_japan_type import (
        UpdateUnfulfillOrdersResponseBillingAddressJapanType,
    )
    from .update_unfulfill_orders_response_billing_address_type import UpdateUnfulfillOrdersResponseBillingAddressType
    from .update_unfulfill_orders_response_customer_info import UpdateUnfulfillOrdersResponseCustomerInfo
    from .update_unfulfill_orders_response_customer_paid import UpdateUnfulfillOrdersResponseCustomerPaid
    from .update_unfulfill_orders_response_dispute_last_status import UpdateUnfulfillOrdersResponseDisputeLastStatus
    from .update_unfulfill_orders_response_download_files_item import UpdateUnfulfillOrdersResponseDownloadFilesItem
    from .update_unfulfill_orders_response_metadata import UpdateUnfulfillOrdersResponseMetadata
    from .update_unfulfill_orders_response_net_amount import UpdateUnfulfillOrdersResponseNetAmount
    from .update_unfulfill_orders_response_paypal_details import UpdateUnfulfillOrdersResponsePaypalDetails
    from .update_unfulfill_orders_response_purchased_items_item import UpdateUnfulfillOrdersResponsePurchasedItemsItem
    from .update_unfulfill_orders_response_purchased_items_item_row_total import (
        UpdateUnfulfillOrdersResponsePurchasedItemsItemRowTotal,
    )
    from .update_unfulfill_orders_response_purchased_items_item_variant_image import (
        UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImage,
    )
    from .update_unfulfill_orders_response_purchased_items_item_variant_image_file import (
        UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFile,
    )
    from .update_unfulfill_orders_response_purchased_items_item_variant_image_file_variants_item import (
        UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem,
    )
    from .update_unfulfill_orders_response_purchased_items_item_variant_price import (
        UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantPrice,
    )
    from .update_unfulfill_orders_response_shipping_address import UpdateUnfulfillOrdersResponseShippingAddress
    from .update_unfulfill_orders_response_shipping_address_japan_type import (
        UpdateUnfulfillOrdersResponseShippingAddressJapanType,
    )
    from .update_unfulfill_orders_response_shipping_address_type import UpdateUnfulfillOrdersResponseShippingAddressType
    from .update_unfulfill_orders_response_status import UpdateUnfulfillOrdersResponseStatus
    from .update_unfulfill_orders_response_stripe_card import UpdateUnfulfillOrdersResponseStripeCard
    from .update_unfulfill_orders_response_stripe_card_brand import UpdateUnfulfillOrdersResponseStripeCardBrand
    from .update_unfulfill_orders_response_stripe_card_expires import UpdateUnfulfillOrdersResponseStripeCardExpires
    from .update_unfulfill_orders_response_stripe_details import UpdateUnfulfillOrdersResponseStripeDetails
    from .update_unfulfill_orders_response_totals import UpdateUnfulfillOrdersResponseTotals
    from .update_unfulfill_orders_response_totals_extras_item import UpdateUnfulfillOrdersResponseTotalsExtrasItem
    from .update_unfulfill_orders_response_totals_extras_item_price import (
        UpdateUnfulfillOrdersResponseTotalsExtrasItemPrice,
    )
    from .update_unfulfill_orders_response_totals_extras_item_type import (
        UpdateUnfulfillOrdersResponseTotalsExtrasItemType,
    )
    from .update_unfulfill_orders_response_totals_subtotal import UpdateUnfulfillOrdersResponseTotalsSubtotal
    from .update_unfulfill_orders_response_totals_total import UpdateUnfulfillOrdersResponseTotalsTotal
_dynamic_imports: typing.Dict[str, str] = {
    "EcommNewOrderPayload": ".ecomm_new_order_payload",
    "EcommNewOrderPayloadPayload": ".ecomm_new_order_payload_payload",
    "EcommNewOrderPayloadPayloadAllAddressesItem": ".ecomm_new_order_payload_payload_all_addresses_item",
    "EcommNewOrderPayloadPayloadAllAddressesItemJapanType": ".ecomm_new_order_payload_payload_all_addresses_item_japan_type",
    "EcommNewOrderPayloadPayloadAllAddressesItemType": ".ecomm_new_order_payload_payload_all_addresses_item_type",
    "EcommNewOrderPayloadPayloadApplicationFee": ".ecomm_new_order_payload_payload_application_fee",
    "EcommNewOrderPayloadPayloadBillingAddress": ".ecomm_new_order_payload_payload_billing_address",
    "EcommNewOrderPayloadPayloadBillingAddressJapanType": ".ecomm_new_order_payload_payload_billing_address_japan_type",
    "EcommNewOrderPayloadPayloadBillingAddressType": ".ecomm_new_order_payload_payload_billing_address_type",
    "EcommNewOrderPayloadPayloadCustomerInfo": ".ecomm_new_order_payload_payload_customer_info",
    "EcommNewOrderPayloadPayloadCustomerPaid": ".ecomm_new_order_payload_payload_customer_paid",
    "EcommNewOrderPayloadPayloadDisputeLastStatus": ".ecomm_new_order_payload_payload_dispute_last_status",
    "EcommNewOrderPayloadPayloadDownloadFilesItem": ".ecomm_new_order_payload_payload_download_files_item",
    "EcommNewOrderPayloadPayloadMetadata": ".ecomm_new_order_payload_payload_metadata",
    "EcommNewOrderPayloadPayloadNetAmount": ".ecomm_new_order_payload_payload_net_amount",
    "EcommNewOrderPayloadPayloadPaypalDetails": ".ecomm_new_order_payload_payload_paypal_details",
    "EcommNewOrderPayloadPayloadPurchasedItemsItem": ".ecomm_new_order_payload_payload_purchased_items_item",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemRowTotal": ".ecomm_new_order_payload_payload_purchased_items_item_row_total",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImage": ".ecomm_new_order_payload_payload_purchased_items_item_variant_image",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFile": ".ecomm_new_order_payload_payload_purchased_items_item_variant_image_file",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem": ".ecomm_new_order_payload_payload_purchased_items_item_variant_image_file_variants_item",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantPrice": ".ecomm_new_order_payload_payload_purchased_items_item_variant_price",
    "EcommNewOrderPayloadPayloadShippingAddress": ".ecomm_new_order_payload_payload_shipping_address",
    "EcommNewOrderPayloadPayloadShippingAddressJapanType": ".ecomm_new_order_payload_payload_shipping_address_japan_type",
    "EcommNewOrderPayloadPayloadShippingAddressType": ".ecomm_new_order_payload_payload_shipping_address_type",
    "EcommNewOrderPayloadPayloadStatus": ".ecomm_new_order_payload_payload_status",
    "EcommNewOrderPayloadPayloadStripeCard": ".ecomm_new_order_payload_payload_stripe_card",
    "EcommNewOrderPayloadPayloadStripeCardBrand": ".ecomm_new_order_payload_payload_stripe_card_brand",
    "EcommNewOrderPayloadPayloadStripeCardExpires": ".ecomm_new_order_payload_payload_stripe_card_expires",
    "EcommNewOrderPayloadPayloadStripeDetails": ".ecomm_new_order_payload_payload_stripe_details",
    "EcommNewOrderPayloadPayloadTotals": ".ecomm_new_order_payload_payload_totals",
    "EcommNewOrderPayloadPayloadTotalsExtrasItem": ".ecomm_new_order_payload_payload_totals_extras_item",
    "EcommNewOrderPayloadPayloadTotalsExtrasItemPrice": ".ecomm_new_order_payload_payload_totals_extras_item_price",
    "EcommNewOrderPayloadPayloadTotalsExtrasItemType": ".ecomm_new_order_payload_payload_totals_extras_item_type",
    "EcommNewOrderPayloadPayloadTotalsSubtotal": ".ecomm_new_order_payload_payload_totals_subtotal",
    "EcommNewOrderPayloadPayloadTotalsTotal": ".ecomm_new_order_payload_payload_totals_total",
    "EcommOrderChangedPayload": ".ecomm_order_changed_payload",
    "EcommOrderChangedPayloadPayload": ".ecomm_order_changed_payload_payload",
    "EcommOrderChangedPayloadPayloadAllAddressesItem": ".ecomm_order_changed_payload_payload_all_addresses_item",
    "EcommOrderChangedPayloadPayloadAllAddressesItemJapanType": ".ecomm_order_changed_payload_payload_all_addresses_item_japan_type",
    "EcommOrderChangedPayloadPayloadAllAddressesItemType": ".ecomm_order_changed_payload_payload_all_addresses_item_type",
    "EcommOrderChangedPayloadPayloadApplicationFee": ".ecomm_order_changed_payload_payload_application_fee",
    "EcommOrderChangedPayloadPayloadBillingAddress": ".ecomm_order_changed_payload_payload_billing_address",
    "EcommOrderChangedPayloadPayloadBillingAddressJapanType": ".ecomm_order_changed_payload_payload_billing_address_japan_type",
    "EcommOrderChangedPayloadPayloadBillingAddressType": ".ecomm_order_changed_payload_payload_billing_address_type",
    "EcommOrderChangedPayloadPayloadCustomerInfo": ".ecomm_order_changed_payload_payload_customer_info",
    "EcommOrderChangedPayloadPayloadCustomerPaid": ".ecomm_order_changed_payload_payload_customer_paid",
    "EcommOrderChangedPayloadPayloadDisputeLastStatus": ".ecomm_order_changed_payload_payload_dispute_last_status",
    "EcommOrderChangedPayloadPayloadDownloadFilesItem": ".ecomm_order_changed_payload_payload_download_files_item",
    "EcommOrderChangedPayloadPayloadMetadata": ".ecomm_order_changed_payload_payload_metadata",
    "EcommOrderChangedPayloadPayloadNetAmount": ".ecomm_order_changed_payload_payload_net_amount",
    "EcommOrderChangedPayloadPayloadPaypalDetails": ".ecomm_order_changed_payload_payload_paypal_details",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItem": ".ecomm_order_changed_payload_payload_purchased_items_item",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemRowTotal": ".ecomm_order_changed_payload_payload_purchased_items_item_row_total",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage": ".ecomm_order_changed_payload_payload_purchased_items_item_variant_image",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFile": ".ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem": ".ecomm_order_changed_payload_payload_purchased_items_item_variant_image_file_variants_item",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantPrice": ".ecomm_order_changed_payload_payload_purchased_items_item_variant_price",
    "EcommOrderChangedPayloadPayloadShippingAddress": ".ecomm_order_changed_payload_payload_shipping_address",
    "EcommOrderChangedPayloadPayloadShippingAddressJapanType": ".ecomm_order_changed_payload_payload_shipping_address_japan_type",
    "EcommOrderChangedPayloadPayloadShippingAddressType": ".ecomm_order_changed_payload_payload_shipping_address_type",
    "EcommOrderChangedPayloadPayloadStatus": ".ecomm_order_changed_payload_payload_status",
    "EcommOrderChangedPayloadPayloadStripeCard": ".ecomm_order_changed_payload_payload_stripe_card",
    "EcommOrderChangedPayloadPayloadStripeCardBrand": ".ecomm_order_changed_payload_payload_stripe_card_brand",
    "EcommOrderChangedPayloadPayloadStripeCardExpires": ".ecomm_order_changed_payload_payload_stripe_card_expires",
    "EcommOrderChangedPayloadPayloadStripeDetails": ".ecomm_order_changed_payload_payload_stripe_details",
    "EcommOrderChangedPayloadPayloadTotals": ".ecomm_order_changed_payload_payload_totals",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItem": ".ecomm_order_changed_payload_payload_totals_extras_item",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItemPrice": ".ecomm_order_changed_payload_payload_totals_extras_item_price",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItemType": ".ecomm_order_changed_payload_payload_totals_extras_item_type",
    "EcommOrderChangedPayloadPayloadTotalsSubtotal": ".ecomm_order_changed_payload_payload_totals_subtotal",
    "EcommOrderChangedPayloadPayloadTotalsTotal": ".ecomm_order_changed_payload_payload_totals_total",
    "GetOrdersResponse": ".get_orders_response",
    "GetOrdersResponseAllAddressesItem": ".get_orders_response_all_addresses_item",
    "GetOrdersResponseAllAddressesItemJapanType": ".get_orders_response_all_addresses_item_japan_type",
    "GetOrdersResponseAllAddressesItemType": ".get_orders_response_all_addresses_item_type",
    "GetOrdersResponseApplicationFee": ".get_orders_response_application_fee",
    "GetOrdersResponseBillingAddress": ".get_orders_response_billing_address",
    "GetOrdersResponseBillingAddressJapanType": ".get_orders_response_billing_address_japan_type",
    "GetOrdersResponseBillingAddressType": ".get_orders_response_billing_address_type",
    "GetOrdersResponseCustomerInfo": ".get_orders_response_customer_info",
    "GetOrdersResponseCustomerPaid": ".get_orders_response_customer_paid",
    "GetOrdersResponseDisputeLastStatus": ".get_orders_response_dispute_last_status",
    "GetOrdersResponseDownloadFilesItem": ".get_orders_response_download_files_item",
    "GetOrdersResponseMetadata": ".get_orders_response_metadata",
    "GetOrdersResponseNetAmount": ".get_orders_response_net_amount",
    "GetOrdersResponsePaypalDetails": ".get_orders_response_paypal_details",
    "GetOrdersResponsePurchasedItemsItem": ".get_orders_response_purchased_items_item",
    "GetOrdersResponsePurchasedItemsItemRowTotal": ".get_orders_response_purchased_items_item_row_total",
    "GetOrdersResponsePurchasedItemsItemVariantImage": ".get_orders_response_purchased_items_item_variant_image",
    "GetOrdersResponsePurchasedItemsItemVariantImageFile": ".get_orders_response_purchased_items_item_variant_image_file",
    "GetOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem": ".get_orders_response_purchased_items_item_variant_image_file_variants_item",
    "GetOrdersResponsePurchasedItemsItemVariantPrice": ".get_orders_response_purchased_items_item_variant_price",
    "GetOrdersResponseShippingAddress": ".get_orders_response_shipping_address",
    "GetOrdersResponseShippingAddressJapanType": ".get_orders_response_shipping_address_japan_type",
    "GetOrdersResponseShippingAddressType": ".get_orders_response_shipping_address_type",
    "GetOrdersResponseStatus": ".get_orders_response_status",
    "GetOrdersResponseStripeCard": ".get_orders_response_stripe_card",
    "GetOrdersResponseStripeCardBrand": ".get_orders_response_stripe_card_brand",
    "GetOrdersResponseStripeCardExpires": ".get_orders_response_stripe_card_expires",
    "GetOrdersResponseStripeDetails": ".get_orders_response_stripe_details",
    "GetOrdersResponseTotals": ".get_orders_response_totals",
    "GetOrdersResponseTotalsExtrasItem": ".get_orders_response_totals_extras_item",
    "GetOrdersResponseTotalsExtrasItemPrice": ".get_orders_response_totals_extras_item_price",
    "GetOrdersResponseTotalsExtrasItemType": ".get_orders_response_totals_extras_item_type",
    "GetOrdersResponseTotalsSubtotal": ".get_orders_response_totals_subtotal",
    "GetOrdersResponseTotalsTotal": ".get_orders_response_totals_total",
    "ListOrdersRequestStatus": ".list_orders_request_status",
    "ListOrdersResponse": ".list_orders_response",
    "ListOrdersResponseOrdersItem": ".list_orders_response_orders_item",
    "ListOrdersResponseOrdersItemAllAddressesItem": ".list_orders_response_orders_item_all_addresses_item",
    "ListOrdersResponseOrdersItemAllAddressesItemJapanType": ".list_orders_response_orders_item_all_addresses_item_japan_type",
    "ListOrdersResponseOrdersItemAllAddressesItemType": ".list_orders_response_orders_item_all_addresses_item_type",
    "ListOrdersResponseOrdersItemApplicationFee": ".list_orders_response_orders_item_application_fee",
    "ListOrdersResponseOrdersItemBillingAddress": ".list_orders_response_orders_item_billing_address",
    "ListOrdersResponseOrdersItemBillingAddressJapanType": ".list_orders_response_orders_item_billing_address_japan_type",
    "ListOrdersResponseOrdersItemBillingAddressType": ".list_orders_response_orders_item_billing_address_type",
    "ListOrdersResponseOrdersItemCustomerInfo": ".list_orders_response_orders_item_customer_info",
    "ListOrdersResponseOrdersItemCustomerPaid": ".list_orders_response_orders_item_customer_paid",
    "ListOrdersResponseOrdersItemDisputeLastStatus": ".list_orders_response_orders_item_dispute_last_status",
    "ListOrdersResponseOrdersItemDownloadFilesItem": ".list_orders_response_orders_item_download_files_item",
    "ListOrdersResponseOrdersItemMetadata": ".list_orders_response_orders_item_metadata",
    "ListOrdersResponseOrdersItemNetAmount": ".list_orders_response_orders_item_net_amount",
    "ListOrdersResponseOrdersItemPaypalDetails": ".list_orders_response_orders_item_paypal_details",
    "ListOrdersResponseOrdersItemPurchasedItemsItem": ".list_orders_response_orders_item_purchased_items_item",
    "ListOrdersResponseOrdersItemPurchasedItemsItemRowTotal": ".list_orders_response_orders_item_purchased_items_item_row_total",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImage": ".list_orders_response_orders_item_purchased_items_item_variant_image",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFile": ".list_orders_response_orders_item_purchased_items_item_variant_image_file",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFileVariantsItem": ".list_orders_response_orders_item_purchased_items_item_variant_image_file_variants_item",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantPrice": ".list_orders_response_orders_item_purchased_items_item_variant_price",
    "ListOrdersResponseOrdersItemShippingAddress": ".list_orders_response_orders_item_shipping_address",
    "ListOrdersResponseOrdersItemShippingAddressJapanType": ".list_orders_response_orders_item_shipping_address_japan_type",
    "ListOrdersResponseOrdersItemShippingAddressType": ".list_orders_response_orders_item_shipping_address_type",
    "ListOrdersResponseOrdersItemStatus": ".list_orders_response_orders_item_status",
    "ListOrdersResponseOrdersItemStripeCard": ".list_orders_response_orders_item_stripe_card",
    "ListOrdersResponseOrdersItemStripeCardBrand": ".list_orders_response_orders_item_stripe_card_brand",
    "ListOrdersResponseOrdersItemStripeCardExpires": ".list_orders_response_orders_item_stripe_card_expires",
    "ListOrdersResponseOrdersItemStripeDetails": ".list_orders_response_orders_item_stripe_details",
    "ListOrdersResponseOrdersItemTotals": ".list_orders_response_orders_item_totals",
    "ListOrdersResponseOrdersItemTotalsExtrasItem": ".list_orders_response_orders_item_totals_extras_item",
    "ListOrdersResponseOrdersItemTotalsExtrasItemPrice": ".list_orders_response_orders_item_totals_extras_item_price",
    "ListOrdersResponseOrdersItemTotalsExtrasItemType": ".list_orders_response_orders_item_totals_extras_item_type",
    "ListOrdersResponseOrdersItemTotalsSubtotal": ".list_orders_response_orders_item_totals_subtotal",
    "ListOrdersResponseOrdersItemTotalsTotal": ".list_orders_response_orders_item_totals_total",
    "ListOrdersResponsePagination": ".list_orders_response_pagination",
    "RefundOrdersRequestReason": ".refund_orders_request_reason",
    "RefundOrdersResponse": ".refund_orders_response",
    "RefundOrdersResponseAllAddressesItem": ".refund_orders_response_all_addresses_item",
    "RefundOrdersResponseAllAddressesItemJapanType": ".refund_orders_response_all_addresses_item_japan_type",
    "RefundOrdersResponseAllAddressesItemType": ".refund_orders_response_all_addresses_item_type",
    "RefundOrdersResponseApplicationFee": ".refund_orders_response_application_fee",
    "RefundOrdersResponseBillingAddress": ".refund_orders_response_billing_address",
    "RefundOrdersResponseBillingAddressJapanType": ".refund_orders_response_billing_address_japan_type",
    "RefundOrdersResponseBillingAddressType": ".refund_orders_response_billing_address_type",
    "RefundOrdersResponseCustomerInfo": ".refund_orders_response_customer_info",
    "RefundOrdersResponseCustomerPaid": ".refund_orders_response_customer_paid",
    "RefundOrdersResponseDisputeLastStatus": ".refund_orders_response_dispute_last_status",
    "RefundOrdersResponseDownloadFilesItem": ".refund_orders_response_download_files_item",
    "RefundOrdersResponseMetadata": ".refund_orders_response_metadata",
    "RefundOrdersResponseNetAmount": ".refund_orders_response_net_amount",
    "RefundOrdersResponsePaypalDetails": ".refund_orders_response_paypal_details",
    "RefundOrdersResponsePurchasedItemsItem": ".refund_orders_response_purchased_items_item",
    "RefundOrdersResponsePurchasedItemsItemRowTotal": ".refund_orders_response_purchased_items_item_row_total",
    "RefundOrdersResponsePurchasedItemsItemVariantImage": ".refund_orders_response_purchased_items_item_variant_image",
    "RefundOrdersResponsePurchasedItemsItemVariantImageFile": ".refund_orders_response_purchased_items_item_variant_image_file",
    "RefundOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem": ".refund_orders_response_purchased_items_item_variant_image_file_variants_item",
    "RefundOrdersResponsePurchasedItemsItemVariantPrice": ".refund_orders_response_purchased_items_item_variant_price",
    "RefundOrdersResponseShippingAddress": ".refund_orders_response_shipping_address",
    "RefundOrdersResponseShippingAddressJapanType": ".refund_orders_response_shipping_address_japan_type",
    "RefundOrdersResponseShippingAddressType": ".refund_orders_response_shipping_address_type",
    "RefundOrdersResponseStatus": ".refund_orders_response_status",
    "RefundOrdersResponseStripeCard": ".refund_orders_response_stripe_card",
    "RefundOrdersResponseStripeCardBrand": ".refund_orders_response_stripe_card_brand",
    "RefundOrdersResponseStripeCardExpires": ".refund_orders_response_stripe_card_expires",
    "RefundOrdersResponseStripeDetails": ".refund_orders_response_stripe_details",
    "RefundOrdersResponseTotals": ".refund_orders_response_totals",
    "RefundOrdersResponseTotalsExtrasItem": ".refund_orders_response_totals_extras_item",
    "RefundOrdersResponseTotalsExtrasItemPrice": ".refund_orders_response_totals_extras_item_price",
    "RefundOrdersResponseTotalsExtrasItemType": ".refund_orders_response_totals_extras_item_type",
    "RefundOrdersResponseTotalsSubtotal": ".refund_orders_response_totals_subtotal",
    "RefundOrdersResponseTotalsTotal": ".refund_orders_response_totals_total",
    "UpdateFulfillOrdersResponse": ".update_fulfill_orders_response",
    "UpdateFulfillOrdersResponseAllAddressesItem": ".update_fulfill_orders_response_all_addresses_item",
    "UpdateFulfillOrdersResponseAllAddressesItemJapanType": ".update_fulfill_orders_response_all_addresses_item_japan_type",
    "UpdateFulfillOrdersResponseAllAddressesItemType": ".update_fulfill_orders_response_all_addresses_item_type",
    "UpdateFulfillOrdersResponseApplicationFee": ".update_fulfill_orders_response_application_fee",
    "UpdateFulfillOrdersResponseBillingAddress": ".update_fulfill_orders_response_billing_address",
    "UpdateFulfillOrdersResponseBillingAddressJapanType": ".update_fulfill_orders_response_billing_address_japan_type",
    "UpdateFulfillOrdersResponseBillingAddressType": ".update_fulfill_orders_response_billing_address_type",
    "UpdateFulfillOrdersResponseCustomerInfo": ".update_fulfill_orders_response_customer_info",
    "UpdateFulfillOrdersResponseCustomerPaid": ".update_fulfill_orders_response_customer_paid",
    "UpdateFulfillOrdersResponseDisputeLastStatus": ".update_fulfill_orders_response_dispute_last_status",
    "UpdateFulfillOrdersResponseDownloadFilesItem": ".update_fulfill_orders_response_download_files_item",
    "UpdateFulfillOrdersResponseMetadata": ".update_fulfill_orders_response_metadata",
    "UpdateFulfillOrdersResponseNetAmount": ".update_fulfill_orders_response_net_amount",
    "UpdateFulfillOrdersResponsePaypalDetails": ".update_fulfill_orders_response_paypal_details",
    "UpdateFulfillOrdersResponsePurchasedItemsItem": ".update_fulfill_orders_response_purchased_items_item",
    "UpdateFulfillOrdersResponsePurchasedItemsItemRowTotal": ".update_fulfill_orders_response_purchased_items_item_row_total",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImage": ".update_fulfill_orders_response_purchased_items_item_variant_image",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFile": ".update_fulfill_orders_response_purchased_items_item_variant_image_file",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem": ".update_fulfill_orders_response_purchased_items_item_variant_image_file_variants_item",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantPrice": ".update_fulfill_orders_response_purchased_items_item_variant_price",
    "UpdateFulfillOrdersResponseShippingAddress": ".update_fulfill_orders_response_shipping_address",
    "UpdateFulfillOrdersResponseShippingAddressJapanType": ".update_fulfill_orders_response_shipping_address_japan_type",
    "UpdateFulfillOrdersResponseShippingAddressType": ".update_fulfill_orders_response_shipping_address_type",
    "UpdateFulfillOrdersResponseStatus": ".update_fulfill_orders_response_status",
    "UpdateFulfillOrdersResponseStripeCard": ".update_fulfill_orders_response_stripe_card",
    "UpdateFulfillOrdersResponseStripeCardBrand": ".update_fulfill_orders_response_stripe_card_brand",
    "UpdateFulfillOrdersResponseStripeCardExpires": ".update_fulfill_orders_response_stripe_card_expires",
    "UpdateFulfillOrdersResponseStripeDetails": ".update_fulfill_orders_response_stripe_details",
    "UpdateFulfillOrdersResponseTotals": ".update_fulfill_orders_response_totals",
    "UpdateFulfillOrdersResponseTotalsExtrasItem": ".update_fulfill_orders_response_totals_extras_item",
    "UpdateFulfillOrdersResponseTotalsExtrasItemPrice": ".update_fulfill_orders_response_totals_extras_item_price",
    "UpdateFulfillOrdersResponseTotalsExtrasItemType": ".update_fulfill_orders_response_totals_extras_item_type",
    "UpdateFulfillOrdersResponseTotalsSubtotal": ".update_fulfill_orders_response_totals_subtotal",
    "UpdateFulfillOrdersResponseTotalsTotal": ".update_fulfill_orders_response_totals_total",
    "UpdateOrdersResponse": ".update_orders_response",
    "UpdateOrdersResponseAllAddressesItem": ".update_orders_response_all_addresses_item",
    "UpdateOrdersResponseAllAddressesItemJapanType": ".update_orders_response_all_addresses_item_japan_type",
    "UpdateOrdersResponseAllAddressesItemType": ".update_orders_response_all_addresses_item_type",
    "UpdateOrdersResponseApplicationFee": ".update_orders_response_application_fee",
    "UpdateOrdersResponseBillingAddress": ".update_orders_response_billing_address",
    "UpdateOrdersResponseBillingAddressJapanType": ".update_orders_response_billing_address_japan_type",
    "UpdateOrdersResponseBillingAddressType": ".update_orders_response_billing_address_type",
    "UpdateOrdersResponseCustomerInfo": ".update_orders_response_customer_info",
    "UpdateOrdersResponseCustomerPaid": ".update_orders_response_customer_paid",
    "UpdateOrdersResponseDisputeLastStatus": ".update_orders_response_dispute_last_status",
    "UpdateOrdersResponseDownloadFilesItem": ".update_orders_response_download_files_item",
    "UpdateOrdersResponseMetadata": ".update_orders_response_metadata",
    "UpdateOrdersResponseNetAmount": ".update_orders_response_net_amount",
    "UpdateOrdersResponsePaypalDetails": ".update_orders_response_paypal_details",
    "UpdateOrdersResponsePurchasedItemsItem": ".update_orders_response_purchased_items_item",
    "UpdateOrdersResponsePurchasedItemsItemRowTotal": ".update_orders_response_purchased_items_item_row_total",
    "UpdateOrdersResponsePurchasedItemsItemVariantImage": ".update_orders_response_purchased_items_item_variant_image",
    "UpdateOrdersResponsePurchasedItemsItemVariantImageFile": ".update_orders_response_purchased_items_item_variant_image_file",
    "UpdateOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem": ".update_orders_response_purchased_items_item_variant_image_file_variants_item",
    "UpdateOrdersResponsePurchasedItemsItemVariantPrice": ".update_orders_response_purchased_items_item_variant_price",
    "UpdateOrdersResponseShippingAddress": ".update_orders_response_shipping_address",
    "UpdateOrdersResponseShippingAddressJapanType": ".update_orders_response_shipping_address_japan_type",
    "UpdateOrdersResponseShippingAddressType": ".update_orders_response_shipping_address_type",
    "UpdateOrdersResponseStatus": ".update_orders_response_status",
    "UpdateOrdersResponseStripeCard": ".update_orders_response_stripe_card",
    "UpdateOrdersResponseStripeCardBrand": ".update_orders_response_stripe_card_brand",
    "UpdateOrdersResponseStripeCardExpires": ".update_orders_response_stripe_card_expires",
    "UpdateOrdersResponseStripeDetails": ".update_orders_response_stripe_details",
    "UpdateOrdersResponseTotals": ".update_orders_response_totals",
    "UpdateOrdersResponseTotalsExtrasItem": ".update_orders_response_totals_extras_item",
    "UpdateOrdersResponseTotalsExtrasItemPrice": ".update_orders_response_totals_extras_item_price",
    "UpdateOrdersResponseTotalsExtrasItemType": ".update_orders_response_totals_extras_item_type",
    "UpdateOrdersResponseTotalsSubtotal": ".update_orders_response_totals_subtotal",
    "UpdateOrdersResponseTotalsTotal": ".update_orders_response_totals_total",
    "UpdateUnfulfillOrdersResponse": ".update_unfulfill_orders_response",
    "UpdateUnfulfillOrdersResponseAllAddressesItem": ".update_unfulfill_orders_response_all_addresses_item",
    "UpdateUnfulfillOrdersResponseAllAddressesItemJapanType": ".update_unfulfill_orders_response_all_addresses_item_japan_type",
    "UpdateUnfulfillOrdersResponseAllAddressesItemType": ".update_unfulfill_orders_response_all_addresses_item_type",
    "UpdateUnfulfillOrdersResponseApplicationFee": ".update_unfulfill_orders_response_application_fee",
    "UpdateUnfulfillOrdersResponseBillingAddress": ".update_unfulfill_orders_response_billing_address",
    "UpdateUnfulfillOrdersResponseBillingAddressJapanType": ".update_unfulfill_orders_response_billing_address_japan_type",
    "UpdateUnfulfillOrdersResponseBillingAddressType": ".update_unfulfill_orders_response_billing_address_type",
    "UpdateUnfulfillOrdersResponseCustomerInfo": ".update_unfulfill_orders_response_customer_info",
    "UpdateUnfulfillOrdersResponseCustomerPaid": ".update_unfulfill_orders_response_customer_paid",
    "UpdateUnfulfillOrdersResponseDisputeLastStatus": ".update_unfulfill_orders_response_dispute_last_status",
    "UpdateUnfulfillOrdersResponseDownloadFilesItem": ".update_unfulfill_orders_response_download_files_item",
    "UpdateUnfulfillOrdersResponseMetadata": ".update_unfulfill_orders_response_metadata",
    "UpdateUnfulfillOrdersResponseNetAmount": ".update_unfulfill_orders_response_net_amount",
    "UpdateUnfulfillOrdersResponsePaypalDetails": ".update_unfulfill_orders_response_paypal_details",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItem": ".update_unfulfill_orders_response_purchased_items_item",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemRowTotal": ".update_unfulfill_orders_response_purchased_items_item_row_total",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImage": ".update_unfulfill_orders_response_purchased_items_item_variant_image",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFile": ".update_unfulfill_orders_response_purchased_items_item_variant_image_file",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem": ".update_unfulfill_orders_response_purchased_items_item_variant_image_file_variants_item",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantPrice": ".update_unfulfill_orders_response_purchased_items_item_variant_price",
    "UpdateUnfulfillOrdersResponseShippingAddress": ".update_unfulfill_orders_response_shipping_address",
    "UpdateUnfulfillOrdersResponseShippingAddressJapanType": ".update_unfulfill_orders_response_shipping_address_japan_type",
    "UpdateUnfulfillOrdersResponseShippingAddressType": ".update_unfulfill_orders_response_shipping_address_type",
    "UpdateUnfulfillOrdersResponseStatus": ".update_unfulfill_orders_response_status",
    "UpdateUnfulfillOrdersResponseStripeCard": ".update_unfulfill_orders_response_stripe_card",
    "UpdateUnfulfillOrdersResponseStripeCardBrand": ".update_unfulfill_orders_response_stripe_card_brand",
    "UpdateUnfulfillOrdersResponseStripeCardExpires": ".update_unfulfill_orders_response_stripe_card_expires",
    "UpdateUnfulfillOrdersResponseStripeDetails": ".update_unfulfill_orders_response_stripe_details",
    "UpdateUnfulfillOrdersResponseTotals": ".update_unfulfill_orders_response_totals",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItem": ".update_unfulfill_orders_response_totals_extras_item",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItemPrice": ".update_unfulfill_orders_response_totals_extras_item_price",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItemType": ".update_unfulfill_orders_response_totals_extras_item_type",
    "UpdateUnfulfillOrdersResponseTotalsSubtotal": ".update_unfulfill_orders_response_totals_subtotal",
    "UpdateUnfulfillOrdersResponseTotalsTotal": ".update_unfulfill_orders_response_totals_total",
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
    "EcommNewOrderPayload",
    "EcommNewOrderPayloadPayload",
    "EcommNewOrderPayloadPayloadAllAddressesItem",
    "EcommNewOrderPayloadPayloadAllAddressesItemJapanType",
    "EcommNewOrderPayloadPayloadAllAddressesItemType",
    "EcommNewOrderPayloadPayloadApplicationFee",
    "EcommNewOrderPayloadPayloadBillingAddress",
    "EcommNewOrderPayloadPayloadBillingAddressJapanType",
    "EcommNewOrderPayloadPayloadBillingAddressType",
    "EcommNewOrderPayloadPayloadCustomerInfo",
    "EcommNewOrderPayloadPayloadCustomerPaid",
    "EcommNewOrderPayloadPayloadDisputeLastStatus",
    "EcommNewOrderPayloadPayloadDownloadFilesItem",
    "EcommNewOrderPayloadPayloadMetadata",
    "EcommNewOrderPayloadPayloadNetAmount",
    "EcommNewOrderPayloadPayloadPaypalDetails",
    "EcommNewOrderPayloadPayloadPurchasedItemsItem",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemRowTotal",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImage",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFile",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem",
    "EcommNewOrderPayloadPayloadPurchasedItemsItemVariantPrice",
    "EcommNewOrderPayloadPayloadShippingAddress",
    "EcommNewOrderPayloadPayloadShippingAddressJapanType",
    "EcommNewOrderPayloadPayloadShippingAddressType",
    "EcommNewOrderPayloadPayloadStatus",
    "EcommNewOrderPayloadPayloadStripeCard",
    "EcommNewOrderPayloadPayloadStripeCardBrand",
    "EcommNewOrderPayloadPayloadStripeCardExpires",
    "EcommNewOrderPayloadPayloadStripeDetails",
    "EcommNewOrderPayloadPayloadTotals",
    "EcommNewOrderPayloadPayloadTotalsExtrasItem",
    "EcommNewOrderPayloadPayloadTotalsExtrasItemPrice",
    "EcommNewOrderPayloadPayloadTotalsExtrasItemType",
    "EcommNewOrderPayloadPayloadTotalsSubtotal",
    "EcommNewOrderPayloadPayloadTotalsTotal",
    "EcommOrderChangedPayload",
    "EcommOrderChangedPayloadPayload",
    "EcommOrderChangedPayloadPayloadAllAddressesItem",
    "EcommOrderChangedPayloadPayloadAllAddressesItemJapanType",
    "EcommOrderChangedPayloadPayloadAllAddressesItemType",
    "EcommOrderChangedPayloadPayloadApplicationFee",
    "EcommOrderChangedPayloadPayloadBillingAddress",
    "EcommOrderChangedPayloadPayloadBillingAddressJapanType",
    "EcommOrderChangedPayloadPayloadBillingAddressType",
    "EcommOrderChangedPayloadPayloadCustomerInfo",
    "EcommOrderChangedPayloadPayloadCustomerPaid",
    "EcommOrderChangedPayloadPayloadDisputeLastStatus",
    "EcommOrderChangedPayloadPayloadDownloadFilesItem",
    "EcommOrderChangedPayloadPayloadMetadata",
    "EcommOrderChangedPayloadPayloadNetAmount",
    "EcommOrderChangedPayloadPayloadPaypalDetails",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItem",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemRowTotal",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImage",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFile",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantImageFileVariantsItem",
    "EcommOrderChangedPayloadPayloadPurchasedItemsItemVariantPrice",
    "EcommOrderChangedPayloadPayloadShippingAddress",
    "EcommOrderChangedPayloadPayloadShippingAddressJapanType",
    "EcommOrderChangedPayloadPayloadShippingAddressType",
    "EcommOrderChangedPayloadPayloadStatus",
    "EcommOrderChangedPayloadPayloadStripeCard",
    "EcommOrderChangedPayloadPayloadStripeCardBrand",
    "EcommOrderChangedPayloadPayloadStripeCardExpires",
    "EcommOrderChangedPayloadPayloadStripeDetails",
    "EcommOrderChangedPayloadPayloadTotals",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItem",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItemPrice",
    "EcommOrderChangedPayloadPayloadTotalsExtrasItemType",
    "EcommOrderChangedPayloadPayloadTotalsSubtotal",
    "EcommOrderChangedPayloadPayloadTotalsTotal",
    "GetOrdersResponse",
    "GetOrdersResponseAllAddressesItem",
    "GetOrdersResponseAllAddressesItemJapanType",
    "GetOrdersResponseAllAddressesItemType",
    "GetOrdersResponseApplicationFee",
    "GetOrdersResponseBillingAddress",
    "GetOrdersResponseBillingAddressJapanType",
    "GetOrdersResponseBillingAddressType",
    "GetOrdersResponseCustomerInfo",
    "GetOrdersResponseCustomerPaid",
    "GetOrdersResponseDisputeLastStatus",
    "GetOrdersResponseDownloadFilesItem",
    "GetOrdersResponseMetadata",
    "GetOrdersResponseNetAmount",
    "GetOrdersResponsePaypalDetails",
    "GetOrdersResponsePurchasedItemsItem",
    "GetOrdersResponsePurchasedItemsItemRowTotal",
    "GetOrdersResponsePurchasedItemsItemVariantImage",
    "GetOrdersResponsePurchasedItemsItemVariantImageFile",
    "GetOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem",
    "GetOrdersResponsePurchasedItemsItemVariantPrice",
    "GetOrdersResponseShippingAddress",
    "GetOrdersResponseShippingAddressJapanType",
    "GetOrdersResponseShippingAddressType",
    "GetOrdersResponseStatus",
    "GetOrdersResponseStripeCard",
    "GetOrdersResponseStripeCardBrand",
    "GetOrdersResponseStripeCardExpires",
    "GetOrdersResponseStripeDetails",
    "GetOrdersResponseTotals",
    "GetOrdersResponseTotalsExtrasItem",
    "GetOrdersResponseTotalsExtrasItemPrice",
    "GetOrdersResponseTotalsExtrasItemType",
    "GetOrdersResponseTotalsSubtotal",
    "GetOrdersResponseTotalsTotal",
    "ListOrdersRequestStatus",
    "ListOrdersResponse",
    "ListOrdersResponseOrdersItem",
    "ListOrdersResponseOrdersItemAllAddressesItem",
    "ListOrdersResponseOrdersItemAllAddressesItemJapanType",
    "ListOrdersResponseOrdersItemAllAddressesItemType",
    "ListOrdersResponseOrdersItemApplicationFee",
    "ListOrdersResponseOrdersItemBillingAddress",
    "ListOrdersResponseOrdersItemBillingAddressJapanType",
    "ListOrdersResponseOrdersItemBillingAddressType",
    "ListOrdersResponseOrdersItemCustomerInfo",
    "ListOrdersResponseOrdersItemCustomerPaid",
    "ListOrdersResponseOrdersItemDisputeLastStatus",
    "ListOrdersResponseOrdersItemDownloadFilesItem",
    "ListOrdersResponseOrdersItemMetadata",
    "ListOrdersResponseOrdersItemNetAmount",
    "ListOrdersResponseOrdersItemPaypalDetails",
    "ListOrdersResponseOrdersItemPurchasedItemsItem",
    "ListOrdersResponseOrdersItemPurchasedItemsItemRowTotal",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImage",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFile",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantImageFileVariantsItem",
    "ListOrdersResponseOrdersItemPurchasedItemsItemVariantPrice",
    "ListOrdersResponseOrdersItemShippingAddress",
    "ListOrdersResponseOrdersItemShippingAddressJapanType",
    "ListOrdersResponseOrdersItemShippingAddressType",
    "ListOrdersResponseOrdersItemStatus",
    "ListOrdersResponseOrdersItemStripeCard",
    "ListOrdersResponseOrdersItemStripeCardBrand",
    "ListOrdersResponseOrdersItemStripeCardExpires",
    "ListOrdersResponseOrdersItemStripeDetails",
    "ListOrdersResponseOrdersItemTotals",
    "ListOrdersResponseOrdersItemTotalsExtrasItem",
    "ListOrdersResponseOrdersItemTotalsExtrasItemPrice",
    "ListOrdersResponseOrdersItemTotalsExtrasItemType",
    "ListOrdersResponseOrdersItemTotalsSubtotal",
    "ListOrdersResponseOrdersItemTotalsTotal",
    "ListOrdersResponsePagination",
    "RefundOrdersRequestReason",
    "RefundOrdersResponse",
    "RefundOrdersResponseAllAddressesItem",
    "RefundOrdersResponseAllAddressesItemJapanType",
    "RefundOrdersResponseAllAddressesItemType",
    "RefundOrdersResponseApplicationFee",
    "RefundOrdersResponseBillingAddress",
    "RefundOrdersResponseBillingAddressJapanType",
    "RefundOrdersResponseBillingAddressType",
    "RefundOrdersResponseCustomerInfo",
    "RefundOrdersResponseCustomerPaid",
    "RefundOrdersResponseDisputeLastStatus",
    "RefundOrdersResponseDownloadFilesItem",
    "RefundOrdersResponseMetadata",
    "RefundOrdersResponseNetAmount",
    "RefundOrdersResponsePaypalDetails",
    "RefundOrdersResponsePurchasedItemsItem",
    "RefundOrdersResponsePurchasedItemsItemRowTotal",
    "RefundOrdersResponsePurchasedItemsItemVariantImage",
    "RefundOrdersResponsePurchasedItemsItemVariantImageFile",
    "RefundOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem",
    "RefundOrdersResponsePurchasedItemsItemVariantPrice",
    "RefundOrdersResponseShippingAddress",
    "RefundOrdersResponseShippingAddressJapanType",
    "RefundOrdersResponseShippingAddressType",
    "RefundOrdersResponseStatus",
    "RefundOrdersResponseStripeCard",
    "RefundOrdersResponseStripeCardBrand",
    "RefundOrdersResponseStripeCardExpires",
    "RefundOrdersResponseStripeDetails",
    "RefundOrdersResponseTotals",
    "RefundOrdersResponseTotalsExtrasItem",
    "RefundOrdersResponseTotalsExtrasItemPrice",
    "RefundOrdersResponseTotalsExtrasItemType",
    "RefundOrdersResponseTotalsSubtotal",
    "RefundOrdersResponseTotalsTotal",
    "UpdateFulfillOrdersResponse",
    "UpdateFulfillOrdersResponseAllAddressesItem",
    "UpdateFulfillOrdersResponseAllAddressesItemJapanType",
    "UpdateFulfillOrdersResponseAllAddressesItemType",
    "UpdateFulfillOrdersResponseApplicationFee",
    "UpdateFulfillOrdersResponseBillingAddress",
    "UpdateFulfillOrdersResponseBillingAddressJapanType",
    "UpdateFulfillOrdersResponseBillingAddressType",
    "UpdateFulfillOrdersResponseCustomerInfo",
    "UpdateFulfillOrdersResponseCustomerPaid",
    "UpdateFulfillOrdersResponseDisputeLastStatus",
    "UpdateFulfillOrdersResponseDownloadFilesItem",
    "UpdateFulfillOrdersResponseMetadata",
    "UpdateFulfillOrdersResponseNetAmount",
    "UpdateFulfillOrdersResponsePaypalDetails",
    "UpdateFulfillOrdersResponsePurchasedItemsItem",
    "UpdateFulfillOrdersResponsePurchasedItemsItemRowTotal",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImage",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFile",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem",
    "UpdateFulfillOrdersResponsePurchasedItemsItemVariantPrice",
    "UpdateFulfillOrdersResponseShippingAddress",
    "UpdateFulfillOrdersResponseShippingAddressJapanType",
    "UpdateFulfillOrdersResponseShippingAddressType",
    "UpdateFulfillOrdersResponseStatus",
    "UpdateFulfillOrdersResponseStripeCard",
    "UpdateFulfillOrdersResponseStripeCardBrand",
    "UpdateFulfillOrdersResponseStripeCardExpires",
    "UpdateFulfillOrdersResponseStripeDetails",
    "UpdateFulfillOrdersResponseTotals",
    "UpdateFulfillOrdersResponseTotalsExtrasItem",
    "UpdateFulfillOrdersResponseTotalsExtrasItemPrice",
    "UpdateFulfillOrdersResponseTotalsExtrasItemType",
    "UpdateFulfillOrdersResponseTotalsSubtotal",
    "UpdateFulfillOrdersResponseTotalsTotal",
    "UpdateOrdersResponse",
    "UpdateOrdersResponseAllAddressesItem",
    "UpdateOrdersResponseAllAddressesItemJapanType",
    "UpdateOrdersResponseAllAddressesItemType",
    "UpdateOrdersResponseApplicationFee",
    "UpdateOrdersResponseBillingAddress",
    "UpdateOrdersResponseBillingAddressJapanType",
    "UpdateOrdersResponseBillingAddressType",
    "UpdateOrdersResponseCustomerInfo",
    "UpdateOrdersResponseCustomerPaid",
    "UpdateOrdersResponseDisputeLastStatus",
    "UpdateOrdersResponseDownloadFilesItem",
    "UpdateOrdersResponseMetadata",
    "UpdateOrdersResponseNetAmount",
    "UpdateOrdersResponsePaypalDetails",
    "UpdateOrdersResponsePurchasedItemsItem",
    "UpdateOrdersResponsePurchasedItemsItemRowTotal",
    "UpdateOrdersResponsePurchasedItemsItemVariantImage",
    "UpdateOrdersResponsePurchasedItemsItemVariantImageFile",
    "UpdateOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem",
    "UpdateOrdersResponsePurchasedItemsItemVariantPrice",
    "UpdateOrdersResponseShippingAddress",
    "UpdateOrdersResponseShippingAddressJapanType",
    "UpdateOrdersResponseShippingAddressType",
    "UpdateOrdersResponseStatus",
    "UpdateOrdersResponseStripeCard",
    "UpdateOrdersResponseStripeCardBrand",
    "UpdateOrdersResponseStripeCardExpires",
    "UpdateOrdersResponseStripeDetails",
    "UpdateOrdersResponseTotals",
    "UpdateOrdersResponseTotalsExtrasItem",
    "UpdateOrdersResponseTotalsExtrasItemPrice",
    "UpdateOrdersResponseTotalsExtrasItemType",
    "UpdateOrdersResponseTotalsSubtotal",
    "UpdateOrdersResponseTotalsTotal",
    "UpdateUnfulfillOrdersResponse",
    "UpdateUnfulfillOrdersResponseAllAddressesItem",
    "UpdateUnfulfillOrdersResponseAllAddressesItemJapanType",
    "UpdateUnfulfillOrdersResponseAllAddressesItemType",
    "UpdateUnfulfillOrdersResponseApplicationFee",
    "UpdateUnfulfillOrdersResponseBillingAddress",
    "UpdateUnfulfillOrdersResponseBillingAddressJapanType",
    "UpdateUnfulfillOrdersResponseBillingAddressType",
    "UpdateUnfulfillOrdersResponseCustomerInfo",
    "UpdateUnfulfillOrdersResponseCustomerPaid",
    "UpdateUnfulfillOrdersResponseDisputeLastStatus",
    "UpdateUnfulfillOrdersResponseDownloadFilesItem",
    "UpdateUnfulfillOrdersResponseMetadata",
    "UpdateUnfulfillOrdersResponseNetAmount",
    "UpdateUnfulfillOrdersResponsePaypalDetails",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItem",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemRowTotal",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImage",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFile",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantImageFileVariantsItem",
    "UpdateUnfulfillOrdersResponsePurchasedItemsItemVariantPrice",
    "UpdateUnfulfillOrdersResponseShippingAddress",
    "UpdateUnfulfillOrdersResponseShippingAddressJapanType",
    "UpdateUnfulfillOrdersResponseShippingAddressType",
    "UpdateUnfulfillOrdersResponseStatus",
    "UpdateUnfulfillOrdersResponseStripeCard",
    "UpdateUnfulfillOrdersResponseStripeCardBrand",
    "UpdateUnfulfillOrdersResponseStripeCardExpires",
    "UpdateUnfulfillOrdersResponseStripeDetails",
    "UpdateUnfulfillOrdersResponseTotals",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItem",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItemPrice",
    "UpdateUnfulfillOrdersResponseTotalsExtrasItemType",
    "UpdateUnfulfillOrdersResponseTotalsSubtotal",
    "UpdateUnfulfillOrdersResponseTotalsTotal",
]
