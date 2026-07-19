

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemMaxCountPerStep(UniversalBaseModel):
    tool_name: str
    prompt_template: typing.Optional[str] = None
    max_count_limit: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
