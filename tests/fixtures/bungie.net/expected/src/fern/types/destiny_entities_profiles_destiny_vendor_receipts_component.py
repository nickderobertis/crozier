

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_vendors_destiny_vendor_receipt import DestinyVendorsDestinyVendorReceipt


class DestinyEntitiesProfilesDestinyVendorReceiptsComponent(UniversalBaseModel):
    """
    For now, this isn't used for much: it's a record of the recent refundable purchases that the user has made. In the future, it could be used for providing refunds/buyback via the API. Wouldn't that be fun?
    """

    receipts: typing.Optional[typing.List[DestinyVendorsDestinyVendorReceipt]] = pydantic.Field(default=None)
    """
    The receipts for refundable purchases made at a vendor.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
