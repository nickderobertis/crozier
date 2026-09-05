

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .node_screenshot import NodeScreenshot


class ProjectNodePreview(UniversalBaseModel):
    project_id: str
    node_id: str
    screenshots: typing.Optional[typing.List[NodeScreenshot]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
