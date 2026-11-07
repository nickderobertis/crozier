

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes_model import AttributesModel
from .creator_email_model import CreatorEmailModel
from .workflow_template_id_model import WorkflowTemplateIdModel


class WorkflowRequestModel(UniversalBaseModel):
    template: WorkflowTemplateIdModel
    creator: CreatorEmailModel
    attributes: AttributesModel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
