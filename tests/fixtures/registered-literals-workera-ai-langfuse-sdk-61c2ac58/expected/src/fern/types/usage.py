

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_usage_unit import ModelUsageUnit


class Usage(UniversalBaseModel):
    """
    (Deprecated. Use usageDetails and costDetails instead.) Standard interface for usage and cost
    """

    input: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of input units (e.g. tokens)
    """

    output: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of output units (e.g. tokens)
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defaults to input+output if not set
    """

    unit: typing.Optional[ModelUsageUnit] = None
    input_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="inputCost"),
        pydantic.Field(alias="inputCost", description="USD input cost"),
    ] = None
    """
    USD input cost
    """

    output_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outputCost"),
        pydantic.Field(alias="outputCost", description="USD output cost"),
    ] = None
    """
    USD output cost
    """

    total_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalCost"),
        pydantic.Field(alias="totalCost", description="USD total cost, defaults to input+output"),
    ] = None
    """
    USD total cost, defaults to input+output
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
