

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsProfilesDestinyProfileTransitoryJoinability(UniversalBaseModel):
    """
    Some basic information about whether you can be joined, how many slots are left etc. Note that this can change quickly, so it may not actually be useful. But perhaps it will be in some use cases?
    """

    closed_reasons: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="closedReasons"),
        pydantic.Field(alias="closedReasons", description="Reasons why a person can't join this person's fireteam."),
    ] = None
    """
    Reasons why a person can't join this person's fireteam.
    """

    open_slots: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="openSlots"),
        pydantic.Field(alias="openSlots", description="The number of slots still available on this person's fireteam."),
    ] = None
    """
    The number of slots still available on this person's fireteam.
    """

    privacy_setting: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="privacySetting"),
        pydantic.Field(alias="privacySetting", description="Who the person is currently allowing invites from."),
    ] = None
    """
    Who the person is currently allowing invites from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
