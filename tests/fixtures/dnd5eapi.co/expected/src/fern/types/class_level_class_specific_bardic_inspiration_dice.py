

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClassLevelClassSpecificBardicInspirationDice(UniversalBaseModel):
    """
    Bard Class Specific Features
    """

    bardic_inspiration_dice: typing.Optional[float] = None
    magical_secrets_max5: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="magical_secrets_max_5"),
        pydantic.Field(alias="magical_secrets_max_5"),
    ] = None
    magical_secrets_max7: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="magical_secrets_max_7"),
        pydantic.Field(alias="magical_secrets_max_7"),
    ] = None
    magical_secrets_max9: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="magical_secrets_max_9"),
        pydantic.Field(alias="magical_secrets_max_9"),
    ] = None
    song_of_rest_die: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
