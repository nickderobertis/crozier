

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_scratch_files import ProjectScratchFiles


class ProjectScratchFilesPaginated(UniversalBaseModel):
    files: typing.List[ProjectScratchFiles]
    count: int
    page: int
    items_per_page: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
