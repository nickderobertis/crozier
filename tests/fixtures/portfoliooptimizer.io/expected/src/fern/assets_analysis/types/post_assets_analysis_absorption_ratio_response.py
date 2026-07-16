

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsAnalysisAbsorptionRatioResponse(UniversalBaseModel):
    assets_absorption_ratio: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="assetsAbsorptionRatio"),
        pydantic.Field(alias="assetsAbsorptionRatio", description="The absorption ratio of the universe of assets"),
    ]
    """
    The absorption ratio of the universe of assets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
