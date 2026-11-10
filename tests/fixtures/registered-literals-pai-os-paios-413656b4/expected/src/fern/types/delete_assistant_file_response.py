

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_assistant_file_response_object import DeleteAssistantFileResponseObject


class DeleteAssistantFileResponse(UniversalBaseModel):
    """
    Deletes the association between the assistant and the file, but does not delete the [File](/docs/api-reference/files) object itself.
    """

    id: str
    deleted: bool
    object: DeleteAssistantFileResponseObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
