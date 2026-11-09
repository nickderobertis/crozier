

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .observation import Observation


class ObservationsView(Observation):
    prompt_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="promptName"),
        pydantic.Field(alias="promptName", description="The name of the prompt associated with the observation"),
    ] = None
    """
    The name of the prompt associated with the observation
    """

    prompt_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="promptVersion"),
        pydantic.Field(alias="promptVersion", description="The version of the prompt associated with the observation"),
    ] = None
    """
    The version of the prompt associated with the observation
    """

    model_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="modelId"),
        pydantic.Field(alias="modelId", description="The unique identifier of the model"),
    ] = None
    """
    The unique identifier of the model
    """

    input_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="inputPrice"),
        pydantic.Field(alias="inputPrice", description="The price of the input in USD"),
    ] = None
    """
    The price of the input in USD
    """

    output_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outputPrice"),
        pydantic.Field(alias="outputPrice", description="The price of the output in USD."),
    ] = None
    """
    The price of the output in USD.
    """

    total_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalPrice"),
        pydantic.Field(alias="totalPrice", description="The total price in USD."),
    ] = None
    """
    The total price in USD.
    """

    calculated_input_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="calculatedInputCost"),
        pydantic.Field(
            alias="calculatedInputCost",
            description="(Deprecated. Use usageDetails and costDetails instead.) The calculated cost of the input in USD",
        ),
    ] = None
    """
    (Deprecated. Use usageDetails and costDetails instead.) The calculated cost of the input in USD
    """

    calculated_output_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="calculatedOutputCost"),
        pydantic.Field(
            alias="calculatedOutputCost",
            description="(Deprecated. Use usageDetails and costDetails instead.) The calculated cost of the output in USD",
        ),
    ] = None
    """
    (Deprecated. Use usageDetails and costDetails instead.) The calculated cost of the output in USD
    """

    calculated_total_cost: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="calculatedTotalCost"),
        pydantic.Field(
            alias="calculatedTotalCost",
            description="(Deprecated. Use usageDetails and costDetails instead.) The calculated total cost in USD",
        ),
    ] = None
    """
    (Deprecated. Use usageDetails and costDetails instead.) The calculated total cost in USD
    """

    latency: typing.Optional[float] = pydantic.Field(default=None)
    """
    The latency in seconds.
    """

    time_to_first_token: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="timeToFirstToken"),
        pydantic.Field(alias="timeToFirstToken", description="The time to the first token in seconds"),
    ] = None
    """
    The time to the first token in seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
