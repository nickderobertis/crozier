

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsAnimationsDestinyAnimationReference(UniversalBaseModel):
    anim_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="animIdentifier"), pydantic.Field(alias="animIdentifier")
    ] = None
    anim_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="animName"), pydantic.Field(alias="animName")
    ] = None
    path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
