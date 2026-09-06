

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.project_automation import ProjectAutomation


class GetProjectAutomationResponse(UniversalBaseModel):
    objects: typing.List[ProjectAutomation] = pydantic.Field()
    """
    A list of project_automation objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
