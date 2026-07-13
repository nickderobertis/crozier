

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsItemsDestinyParentItemOverride(UniversalBaseModel):
    additional_equip_requirements_display_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="additionalEquipRequirementsDisplayStrings")
    ] = None
    pip_icon: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pipIcon")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
