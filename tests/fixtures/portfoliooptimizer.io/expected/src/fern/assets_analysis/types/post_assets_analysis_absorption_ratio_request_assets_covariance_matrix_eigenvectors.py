

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors(UniversalBaseModel):
    eigenvectors_retained: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="eigenvectorsRetained"),
        pydantic.Field(
            alias="eigenvectorsRetained",
            description="The number of eigenvectors to retain in the numerator of the absorption ratio, which must be lower than the number of assets; defaults to [1/5-th] the number of assets",
        ),
    ] = None
    """
    The number of eigenvectors to retain in the numerator of the absorption ratio, which must be lower than the number of assets; defaults to [1/5-th] the number of assets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
