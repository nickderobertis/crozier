

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lower_case_email_str import LowerCaseEmailStr
from .user_id_int import UserIdInt
from .wallet_id_int import WalletIdInt


class LicensedItemPurchaseGet(UniversalBaseModel):
    licensed_item_purchase_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="licensedItemPurchaseId"), pydantic.Field(alias="licensedItemPurchaseId")
    ]
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    licensed_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="licensedItemId"), pydantic.Field(alias="licensedItemId")
    ]
    key: str
    version: str
    wallet_id: typing_extensions.Annotated[
        WalletIdInt, FieldMetadata(alias="walletId"), pydantic.Field(alias="walletId")
    ]
    pricing_unit_cost_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingUnitCostId"), pydantic.Field(alias="pricingUnitCostId")
    ]
    pricing_unit_cost: typing_extensions.Annotated[
        str, FieldMetadata(alias="pricingUnitCost"), pydantic.Field(alias="pricingUnitCost")
    ]
    start_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="startAt"), pydantic.Field(alias="startAt")]
    expire_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expireAt"), pydantic.Field(alias="expireAt")
    ]
    num_of_seats: typing_extensions.Annotated[
        int, FieldMetadata(alias="numOfSeats"), pydantic.Field(alias="numOfSeats")
    ]
    purchased_by_user: typing_extensions.Annotated[
        UserIdInt, FieldMetadata(alias="purchasedByUser"), pydantic.Field(alias="purchasedByUser")
    ]
    user_email: typing_extensions.Annotated[
        LowerCaseEmailStr, FieldMetadata(alias="userEmail"), pydantic.Field(alias="userEmail")
    ]
    purchased_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="purchasedAt"), pydantic.Field(alias="purchasedAt")
    ]
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
