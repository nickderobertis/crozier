

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stage_input_descriptor_labelmap_reference_image_type import StageInputDescriptorLabelmapReferenceImageType


class StageInputDescriptorLabelmapReferenceImage(UniversalBaseModel):
    type: StageInputDescriptorLabelmapReferenceImageType
    format: typing.Optional[str] = None
    uris: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
