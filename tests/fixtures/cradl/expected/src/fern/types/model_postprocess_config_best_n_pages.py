

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_postprocess_config_best_n_pages_output_format import ModelPostprocessConfigBestNPagesOutputFormat
from .model_postprocess_config_best_n_pages_parameters import ModelPostprocessConfigBestNPagesParameters


class ModelPostprocessConfigBestNPages(UniversalBaseModel):
    output_format: typing_extensions.Annotated[
        typing.Optional[ModelPostprocessConfigBestNPagesOutputFormat],
        FieldMetadata(alias="outputFormat"),
        pydantic.Field(alias="outputFormat"),
    ] = None
    parameters: ModelPostprocessConfigBestNPagesParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
