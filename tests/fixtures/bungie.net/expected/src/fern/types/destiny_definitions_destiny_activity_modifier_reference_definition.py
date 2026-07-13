

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityModifierReferenceDefinition(UniversalBaseModel):
    """
    A reference to an Activity Modifier from another entity, such as an Activity (for now, just Activities).
    This defines some
    """

    activity_modifier_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activityModifierHash")
    ] = pydantic.Field(default=None)
    """
    The hash identifier for the DestinyActivityModifierDefinition referenced by this activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
