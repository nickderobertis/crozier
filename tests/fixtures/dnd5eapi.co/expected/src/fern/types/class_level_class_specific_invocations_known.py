

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClassLevelClassSpecificInvocationsKnown(UniversalBaseModel):
    """
    Bard Warlock Specific Features
    """

    invocations_known: typing.Optional[float] = None
    mystic_arcanum_level6: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="mystic_arcanum_level_6")
    ] = None
    mystic_arcanum_level7: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="mystic_arcanum_level_7")
    ] = None
    mystic_arcanum_level8: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="mystic_arcanum_level_8")
    ] = None
    mystic_arcanum_level9: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="mystic_arcanum_level_9")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
