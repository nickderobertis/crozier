

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item import ObpcaData1OverdraftOverdraftTierBandSetItem


class ObpcaData1Overdraft(UniversalBaseModel):
    """
    Details about Overdraft rates, fees & charges
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Associated Notes about the overdraft rates
    """

    overdraft_tier_band_set: typing_extensions.Annotated[
        typing.List[ObpcaData1OverdraftOverdraftTierBandSetItem], FieldMetadata(alias="OverdraftTierBandSet")
    ] = pydantic.Field()
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
