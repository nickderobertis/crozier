

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataBatteryCellVoltageHigh(UniversalBaseModel):
    threshold: float = pydantic.Field()
    """
    The cell voltage threshold that triggered the alarm
    """

    cell_voltages: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="cellVoltages"),
        pydantic.Field(alias="cellVoltages", description="The voltage readings from all battery cells"),
    ]
    """
    The voltage readings from all battery cells
    """

    over_threshold_index: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="overThresholdIndex"),
        pydantic.Field(alias="overThresholdIndex", description="Indices of cells that exceeded the threshold"),
    ]
    """
    Indices of cells that exceeded the threshold
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
