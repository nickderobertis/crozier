

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityInsertionPointDefinition(UniversalBaseModel):
    """
    A point of entry into an activity, gated by an unlock flag and with some more-or-less useless (for our purposes) phase information. I'm including it in case we end up being able to bolt more useful information onto it in the future.
    UPDATE: Turns out this information isn't actually useless, and is in fact actually useful for people. Who would have thought? We still don't have localized info for it, but at least this will help people when they're looking at phase indexes in stats data, or when they want to know what phases have been completed on a weekly achievement.
    """

    phase_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="phaseHash"),
        pydantic.Field(
            alias="phaseHash",
            description="A unique hash value representing the phase. This can be useful for, for example, comparing how different instances of Raids have phases in different orders!",
        ),
    ] = None
    """
    A unique hash value representing the phase. This can be useful for, for example, comparing how different instances of Raids have phases in different orders!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
