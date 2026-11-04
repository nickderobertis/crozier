

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_participants_response_list_item import ListAllWorkflowParticipantsResponseListItem


class ListAllWorkflowParticipantsResponse(UniversalBaseModel):
    page: typing.Optional[int] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    count: typing.Optional[int] = None
    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[ListAllWorkflowParticipantsResponseListItem]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
