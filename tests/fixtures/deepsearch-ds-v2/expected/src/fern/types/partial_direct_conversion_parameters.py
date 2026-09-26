

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assemble_settings import AssembleSettings
from .collection_metadata_settings import CollectionMetadataSettings
from .model_pipeline_settings import ModelPipelineSettings
from .ocr_settings import OcrSettings
from .partial_direct_conversion_parameters_type import PartialDirectConversionParametersType


class PartialDirectConversionParameters(UniversalBaseModel):
    """
    Specify conversion settings (OCR, Assemble, ML Models) directly.

    Fields left null are set to platform defaults.
    """

    type: typing.Optional[PartialDirectConversionParametersType] = None
    ocr: typing.Optional[OcrSettings] = None
    assemble: typing.Optional[AssembleSettings] = None
    metadata: typing.Optional[CollectionMetadataSettings] = None
    page_labels: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = None
    model_pipeline: typing.Optional[ModelPipelineSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
