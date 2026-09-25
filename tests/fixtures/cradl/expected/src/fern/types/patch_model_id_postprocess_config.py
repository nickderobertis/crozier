

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_model_id_postprocess_config_best_first_output_format import (
    PatchModelIdPostprocessConfigBestFirstOutputFormat,
)
from .patch_model_id_postprocess_config_best_n_pages_output_format import (
    PatchModelIdPostprocessConfigBestNPagesOutputFormat,
)
from .patch_model_id_postprocess_config_best_n_pages_parameters import PatchModelIdPostprocessConfigBestNPagesParameters


class PatchModelIdPostprocessConfig_BestFirst(UniversalBaseModel):
    strategy: typing.Literal["BEST_FIRST"] = "BEST_FIRST"
    output_format: typing_extensions.Annotated[
        typing.Optional[PatchModelIdPostprocessConfigBestFirstOutputFormat],
        FieldMetadata(alias="outputFormat"),
        pydantic.Field(alias="outputFormat"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PatchModelIdPostprocessConfig_BestNPages(UniversalBaseModel):
    strategy: typing.Literal["BEST_N_PAGES"] = "BEST_N_PAGES"
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


PatchModelIdPostprocessConfig = typing_extensions.Annotated[
    typing.Union[PatchModelIdPostprocessConfig_BestFirst, PatchModelIdPostprocessConfig_BestNPages],
    pydantic.Field(discriminator="strategy"),
]
