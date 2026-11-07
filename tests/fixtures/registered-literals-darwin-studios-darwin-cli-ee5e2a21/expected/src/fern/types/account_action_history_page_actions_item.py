

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .action_outcome import ActionOutcome


class AccountActionHistoryPageActionsItem(UniversalBaseModel):
    action_id: typing_extensions.Annotated[str, FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")]
    ai_id: typing_extensions.Annotated[str, FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")]
    capability_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="capabilityId"), pydantic.Field(alias="capabilityId")
    ]
    called_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="calledAt"), pydantic.Field(alias="calledAt")
    ]
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    outcome: ActionOutcome

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
