

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem(UniversalBaseModel):
    date: str = pydantic.Field()
    """
    The date corresponding to the date t in format YYYY-MM-DD
    """

    dividend_adjusted_close: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="dividendAdjustedClose"),
        pydantic.Field(
            alias="dividendAdjustedClose",
            description="The dividend(s) adjusted close price of the asset at the date t, only present if dividend(s) information are provided",
        ),
    ] = None
    """
    The dividend(s) adjusted close price of the asset at the date t, only present if dividend(s) information are provided
    """

    fully_adjusted_close: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="fullyAdjustedClose"),
        pydantic.Field(
            alias="fullyAdjustedClose",
            description="The dividend(s) and split(s) adjusted close price of the asset at the date t",
        ),
    ]
    """
    The dividend(s) and split(s) adjusted close price of the asset at the date t
    """

    split_adjusted_close: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="splitAdjustedClose"),
        pydantic.Field(
            alias="splitAdjustedClose",
            description="The split(s) adjusted close price of the asset at the date t, only present if split(s) information are provided",
        ),
    ] = None
    """
    The split(s) adjusted close price of the asset at the date t, only present if split(s) information are provided
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
