

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_model_id_postprocess_config_best_first_output_format import (
    PatchModelIdPostprocessConfigBestFirstOutputFormat,
)


class PatchModelIdPostprocessConfigBestFirst(UniversalBaseModel):
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
