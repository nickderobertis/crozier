

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .models_models_item_postprocess_config_best_first_output_format import (
    ModelsModelsItemPostprocessConfigBestFirstOutputFormat,
)
from .models_models_item_postprocess_config_best_n_pages_output_format import (
    ModelsModelsItemPostprocessConfigBestNPagesOutputFormat,
)
from .models_models_item_postprocess_config_best_n_pages_parameters import (
    ModelsModelsItemPostprocessConfigBestNPagesParameters,
)


class ModelsModelsItemPostprocessConfig_BestFirst(UniversalBaseModel):
    strategy: typing.Literal["BEST_FIRST"] = "BEST_FIRST"
    output_format: typing_extensions.Annotated[
        typing.Optional[ModelsModelsItemPostprocessConfigBestFirstOutputFormat],
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


class ModelsModelsItemPostprocessConfig_BestNPages(UniversalBaseModel):
    strategy: typing.Literal["BEST_N_PAGES"] = "BEST_N_PAGES"
    output_format: typing_extensions.Annotated[
        typing.Optional[ModelsModelsItemPostprocessConfigBestNPagesOutputFormat],
        FieldMetadata(alias="outputFormat"),
        pydantic.Field(alias="outputFormat"),
    ] = None
    parameters: ModelsModelsItemPostprocessConfigBestNPagesParameters

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelsModelsItemPostprocessConfig = typing_extensions.Annotated[
    typing.Union[ModelsModelsItemPostprocessConfig_BestFirst, ModelsModelsItemPostprocessConfig_BestNPages],
    pydantic.Field(discriminator="strategy"),
]
