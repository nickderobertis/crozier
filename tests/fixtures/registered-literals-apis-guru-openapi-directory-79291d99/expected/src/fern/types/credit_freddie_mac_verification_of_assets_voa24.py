

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_verification_of_assets_deal_voa24 import CreditFreddieMacVerificationOfAssetsDealVoa24


class CreditFreddieMacVerificationOfAssetsVoa24(UniversalBaseModel):
    """
    Verification of Assets Report
    """

    deal: typing_extensions.Annotated[
        CreditFreddieMacVerificationOfAssetsDealVoa24, FieldMetadata(alias="DEAL"), pydantic.Field(alias="DEAL")
    ]
    schema_version: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="SchemaVersion"),
        pydantic.Field(alias="SchemaVersion", description="The Verification Of Assets (VOA) schema version."),
    ]
    """
    The Verification Of Assets (VOA) schema version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
