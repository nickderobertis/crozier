

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WorkflowsGetTurnHistoryResponseListItem(UniversalBaseModel):
    turn_party: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnParty"), pydantic.Field(alias="turnParty")
    ] = None
    turn_start_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnStartTime"), pydantic.Field(alias="turnStartTime")
    ] = None
    turn_location: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnLocation"), pydantic.Field(alias="turnLocation")
    ] = None
    turn_user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnUserId"), pydantic.Field(alias="turnUserId")
    ] = None
    turn_end_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnEndTime"), pydantic.Field(alias="turnEndTime")
    ] = None
    turn_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="turnNumber"), pydantic.Field(alias="turnNumber")
    ] = None
    turn_user_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="turnUserEmail"), pydantic.Field(alias="turnUserEmail")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
