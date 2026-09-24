

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataBatteryCellVoltageDiff(UniversalBaseModel):
    threshold: float = pydantic.Field()
    """
    The voltage difference threshold that triggered the alarm
    """

    cell_voltages: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="cellVoltages"),
        pydantic.Field(alias="cellVoltages", description="The voltage readings from all battery cells"),
    ]
    """
    The voltage readings from all battery cells
    """

    diff_index: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="diffIndex"),
        pydantic.Field(alias="diffIndex", description="Indices of cells with voltage difference exceeding threshold"),
    ]
    """
    Indices of cells with voltage difference exceeding threshold
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
