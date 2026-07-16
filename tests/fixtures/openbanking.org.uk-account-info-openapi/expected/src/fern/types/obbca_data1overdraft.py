

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1overdraft_overdraft_tier_band_set_item import ObbcaData1OverdraftOverdraftTierBandSetItem


class ObbcaData1Overdraft(UniversalBaseModel):
    """
    Borrowing details
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Associated Notes about the overdraft rates"),
    ] = None
    """
    Associated Notes about the overdraft rates
    """

    overdraft_tier_band_set: typing_extensions.Annotated[
        typing.List[ObbcaData1OverdraftOverdraftTierBandSetItem],
        FieldMetadata(alias="OverdraftTierBandSet"),
        pydantic.Field(alias="OverdraftTierBandSet", description="Tier band set details"),
    ]
    """
    Tier band set details
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
