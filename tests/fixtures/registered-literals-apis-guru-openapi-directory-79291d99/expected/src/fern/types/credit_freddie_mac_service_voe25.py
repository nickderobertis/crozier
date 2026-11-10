

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_verification_of_asset_voe25 import CreditFreddieMacVerificationOfAssetVoe25
from .statuses import Statuses


class CreditFreddieMacServiceVoe25(UniversalBaseModel):
    """
    A collection of details related to a fulfillment service or product in terms of request, process and result.
    """

    statuses: typing_extensions.Annotated[Statuses, FieldMetadata(alias="STATUSES"), pydantic.Field(alias="STATUSES")]
    verification_of_asset: typing_extensions.Annotated[
        typing.List[CreditFreddieMacVerificationOfAssetVoe25],
        FieldMetadata(alias="VERIFICATION_OF_ASSET"),
        pydantic.Field(alias="VERIFICATION_OF_ASSET"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
