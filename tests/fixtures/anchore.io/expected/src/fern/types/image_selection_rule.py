

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_ref import ImageRef


class ImageSelectionRule(UniversalBaseModel):
    id: typing.Optional[str] = None
    image: ImageRef
    name: str
    registry: str
    repository: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
