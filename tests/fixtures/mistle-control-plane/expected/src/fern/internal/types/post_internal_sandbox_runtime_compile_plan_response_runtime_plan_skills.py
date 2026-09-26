

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_skills_selected_skills_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanSkillsSelectedSkillsItem,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanSkills(UniversalBaseModel):
    origin_url: typing_extensions.Annotated[str, FieldMetadata(alias="originUrl"), pydantic.Field(alias="originUrl")]
    selected_skills: typing_extensions.Annotated[
        typing.List[PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanSkillsSelectedSkillsItem],
        FieldMetadata(alias="selectedSkills"),
        pydantic.Field(alias="selectedSkills"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
