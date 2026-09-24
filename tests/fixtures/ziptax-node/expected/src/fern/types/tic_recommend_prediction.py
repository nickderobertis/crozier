

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tic_recommend_prediction_status import TicRecommendPredictionStatus


class TicRecommendPrediction(UniversalBaseModel):
    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error string formatted as "<code> - <message>" on failure; null on success
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label for the recommended TIC
    """

    natural_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="naturalLabel"),
        pydantic.Field(alias="naturalLabel", description="Natural-language label for the recommended TIC"),
    ] = None
    """
    Natural-language label for the recommended TIC
    """

    product_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Normalized product description used for matching
    """

    status: TicRecommendPredictionStatus = pydantic.Field()
    """
    Prediction status
    """

    tic_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ticId"),
        pydantic.Field(alias="ticId", description="Recommended Taxability Information Code (TIC)"),
    ] = None
    """
    Recommended Taxability Information Code (TIC)
    """

    tic_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the recommended TIC
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
