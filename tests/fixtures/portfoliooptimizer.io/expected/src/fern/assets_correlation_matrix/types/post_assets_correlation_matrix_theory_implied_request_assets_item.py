

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_assets_correlation_matrix_theory_implied_request_assets_item_asset_hierarchical_classification_item import (
    PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem,
)


class PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(UniversalBaseModel):
    asset_hierarchical_classification: typing_extensions.Annotated[
        typing.List[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem],
        FieldMetadata(alias="assetHierarchicalClassification"),
        pydantic.Field(
            alias="assetHierarchicalClassification",
            description="assetHierarchicalClassification[i] is the i+1-th level of the hierarchical classification of the asset, from the most generic classification to the most specific classification; all the assetHierarchicalClassification arrays must have the same length",
        ),
    ]
    """
    assetHierarchicalClassification[i] is the i+1-th level of the hierarchical classification of the asset, from the most generic classification to the most specific classification; all the assetHierarchicalClassification arrays must have the same length
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
