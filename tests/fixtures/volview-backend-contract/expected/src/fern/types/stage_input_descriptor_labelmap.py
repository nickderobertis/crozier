

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stage_input_descriptor_labelmap_reference_image import StageInputDescriptorLabelmapReferenceImage


class StageInputDescriptorLabelmap(UniversalBaseModel):
    name: str
    reference_image: typing_extensions.Annotated[
        StageInputDescriptorLabelmapReferenceImage,
        FieldMetadata(alias="referenceImage"),
        pydantic.Field(alias="referenceImage"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
