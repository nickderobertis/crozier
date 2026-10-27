

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conversation_member_input_roles_item import ConversationMemberInputRolesItem


class ConversationMemberInput(UniversalBaseModel):
    odata_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="@odata.type"), pydantic.Field(alias="@odata.type")
    ]
    user_odata_bind: typing_extensions.Annotated[
        str, FieldMetadata(alias="user@odata.bind"), pydantic.Field(alias="user@odata.bind")
    ]
    roles: typing.Optional[typing.List[ConversationMemberInputRolesItem]] = None
    visible_history_start_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="visibleHistoryStartDateTime"),
        pydantic.Field(
            alias="visibleHistoryStartDateTime", description="Timestamp from which the member can see messages"
        ),
    ] = None
    """
    Timestamp from which the member can see messages
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
