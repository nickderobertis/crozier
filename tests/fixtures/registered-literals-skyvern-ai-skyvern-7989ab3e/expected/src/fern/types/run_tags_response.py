

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tag_response import TagResponse


class RunTagsResponse(UniversalBaseModel):
    """
    Current tags for a workflow run.
    """

    workflow_run_id: str
    tags: typing.List[TagResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
