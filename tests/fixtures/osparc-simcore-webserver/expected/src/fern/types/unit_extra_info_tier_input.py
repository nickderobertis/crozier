

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .unit_extra_info_tier_input_ram import UnitExtraInfoTierInputRam
from .unit_extra_info_tier_input_vram import UnitExtraInfoTierInputVram


class UnitExtraInfoTierInput(UniversalBaseModel):
    """
    Custom information that is propagated to the frontend. Defined fields are mandatory.
    """

    cpu: typing_extensions.Annotated[int, FieldMetadata(alias="CPU"), pydantic.Field(alias="CPU")]
    ram: typing_extensions.Annotated[UnitExtraInfoTierInputRam, FieldMetadata(alias="RAM"), pydantic.Field(alias="RAM")]
    vram: typing_extensions.Annotated[
        UnitExtraInfoTierInputVram, FieldMetadata(alias="VRAM"), pydantic.Field(alias="VRAM")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
