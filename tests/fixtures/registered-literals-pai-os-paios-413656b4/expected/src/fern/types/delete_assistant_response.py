

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_assistant_response_object import DeleteAssistantResponseObject


class DeleteAssistantResponse(UniversalBaseModel):
    id: str
    deleted: bool
    object: DeleteAssistantResponseObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
