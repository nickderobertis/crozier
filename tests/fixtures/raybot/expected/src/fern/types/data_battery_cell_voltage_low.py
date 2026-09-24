

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataBatteryCellVoltageLow(UniversalBaseModel):
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

    under_threshold_index: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="underThresholdIndex"),
        pydantic.Field(alias="underThresholdIndex", description="Indices of cells that fell below the threshold"),
    ]
    """
    Indices of cells that fell below the threshold
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
