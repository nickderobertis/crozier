

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyHistoricalStatsDestinyHistoricalStatsValuePair(UniversalBaseModel):
    display_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayValue")] = (
        pydantic.Field(default=None)
    )
    """
    Localized formated version of the value.
    """

    value: typing.Optional[float] = pydantic.Field(default=None)
    """
    Raw value of the statistic
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
