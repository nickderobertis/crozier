

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_assets_voa24 import CreditFreddieMacAssetsVoa24


class CreditFreddieMacVerificationOfAssetResponseVoa24(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    assets: typing_extensions.Annotated[
        CreditFreddieMacAssetsVoa24, FieldMetadata(alias="ASSETS"), pydantic.Field(alias="ASSETS")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
