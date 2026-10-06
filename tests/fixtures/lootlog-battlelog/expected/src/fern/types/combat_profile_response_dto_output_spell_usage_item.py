

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CombatProfileResponseDtoOutputSpellUsageItem(UniversalBaseModel):
    spell: str
    skill_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="skillId"), pydantic.Field(alias="skillId")
    ] = None
    casts: float
    share: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
