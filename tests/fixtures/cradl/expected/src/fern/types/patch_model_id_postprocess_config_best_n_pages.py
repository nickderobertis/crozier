

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_model_id_postprocess_config_best_n_pages_output_format import (
    PatchModelIdPostprocessConfigBestNPagesOutputFormat,
)
from .patch_model_id_postprocess_config_best_n_pages_parameters import PatchModelIdPostprocessConfigBestNPagesParameters


class PatchModelIdPostprocessConfigBestNPages(UniversalBaseModel):
    output_format: typing_extensions.Annotated[
        typing.Optional[PatchModelIdPostprocessConfigBestNPagesOutputFormat],
        FieldMetadata(alias="outputFormat"),
        pydantic.Field(alias="outputFormat"),
    ] = None
    parameters: PatchModelIdPostprocessConfigBestNPagesParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
