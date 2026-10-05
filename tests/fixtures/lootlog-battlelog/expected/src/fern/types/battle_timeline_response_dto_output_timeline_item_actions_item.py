

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattleTimelineResponseDtoOutputTimelineItemActionsItem(UniversalBaseModel):
    action_type: typing_extensions.Annotated[str, FieldMetadata(alias="actionType"), pydantic.Field(alias="actionType")]
    param: str
    category: str
    actor_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actorId"), pydantic.Field(alias="actorId")
    ] = None
    target_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetId"), pydantic.Field(alias="targetId")
    ] = None
    value: float
    handled: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
