

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflow_last_modified_author_model import WorkflowLastModifiedAuthorModel


class WorkflowResponseModelAttributesDraftItemLastModified(UniversalBaseModel):
    timestamp: typing.Optional[str] = None
    author: typing.Optional[WorkflowLastModifiedAuthorModel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
