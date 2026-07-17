

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDestinyUnlockStatus(UniversalBaseModel):
    """
    Indicates the status of an "Unlock Flag" on a Character or Profile.
    These are individual bits of state that can be either set or not set, and sometimes provide interesting human-readable information in their related DestinyUnlockDefinition.
    """

    is_set: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isSet"),
        pydantic.Field(alias="isSet", description="Whether the unlock flag is set."),
    ] = None
    """
    Whether the unlock flag is set.
    """

    unlock_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unlockHash"),
        pydantic.Field(
            alias="unlockHash",
            description="The hash identifier for the Unlock Flag. Use to lookup DestinyUnlockDefinition for static data. Not all unlocks have human readable data - in fact, most don't. But when they do, it can be very useful to show. Even if they don't have human readable data, you might be able to infer the meaning of an unlock flag with a bit of experimentation...",
        ),
    ] = None
    """
    The hash identifier for the Unlock Flag. Use to lookup DestinyUnlockDefinition for static data. Not all unlocks have human readable data - in fact, most don't. But when they do, it can be very useful to show. Even if they don't have human readable data, you might be able to infer the meaning of an unlock flag with a bit of experimentation...
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
