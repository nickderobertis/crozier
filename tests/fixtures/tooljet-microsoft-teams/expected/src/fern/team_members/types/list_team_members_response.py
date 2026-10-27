

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.conversation_member import ConversationMember


class ListTeamMembersResponse(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    odata_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="@odata.count"), pydantic.Field(alias="@odata.count")
    ] = None
    odata_next_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.nextLink"), pydantic.Field(alias="@odata.nextLink")
    ] = None
    value: typing.Optional[typing.List[ConversationMember]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
