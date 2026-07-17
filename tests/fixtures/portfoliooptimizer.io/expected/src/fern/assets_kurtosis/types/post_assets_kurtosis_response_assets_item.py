

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsKurtosisResponseAssetsItem(UniversalBaseModel):
    asset_kurtosis: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="assetKurtosis"),
        pydantic.Field(alias="assetKurtosis", description="The kurtosis of the asset"),
    ]
    """
    The kurtosis of the asset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
