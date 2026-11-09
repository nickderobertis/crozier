

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_asset_voa24 import CreditFreddieMacAssetVoa24


class CreditFreddieMacAssetsVoa24(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset: typing_extensions.Annotated[
        typing.List[CreditFreddieMacAssetVoa24],
        FieldMetadata(alias="ASSET"),
        pydantic.Field(
            alias="ASSET",
            description="Documentation not found in the MISMO model viewer and not provided by Freddie Mac.",
        ),
    ]
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
