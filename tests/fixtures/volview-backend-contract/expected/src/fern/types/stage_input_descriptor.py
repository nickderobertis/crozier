

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stage_input_descriptor_annotations_reference_image import StageInputDescriptorAnnotationsReferenceImage
from .stage_input_descriptor_labelmap_reference_image import StageInputDescriptorLabelmapReferenceImage


class StageInputDescriptor_Labelmap(UniversalBaseModel):
    type: typing.Literal["labelmap"] = "labelmap"
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


class StageInputDescriptor_Annotations(UniversalBaseModel):
    type: typing.Literal["annotations"] = "annotations"
    name: str
    reference_image: typing_extensions.Annotated[
        StageInputDescriptorAnnotationsReferenceImage,
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


StageInputDescriptor = typing_extensions.Annotated[
    typing.Union[StageInputDescriptor_Labelmap, StageInputDescriptor_Annotations], pydantic.Field(discriminator="type")
]
