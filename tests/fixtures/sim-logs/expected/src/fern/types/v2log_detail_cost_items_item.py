

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2log_detail_cost_items_item_category import V2LogDetailCostItemsItemCategory


class V2LogDetailCostItemsItem(UniversalBaseModel):
    """
    One billed line of a run, folded across every event that billed it.
    """

    category: V2LogDetailCostItemsItemCategory = pydantic.Field()
    """
    What the line is for: the run's base fee (`fixed`), one model's inference (`model`), or one metered tool or integration call (`tool`).
    """

    description: str = pydantic.Field()
    """
    Human-readable name of the billed item, such as the model or tool id.
    """

    cost: float = pydantic.Field()
    """
    Amount billed for this line, in USD.
    """

    input_tokens: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="inputTokens"),
        pydantic.Field(
            alias="inputTokens",
            description="Input tokens attributed to this line. Absent for lines that do not bill tokens.",
        ),
    ] = None
    """
    Input tokens attributed to this line. Absent for lines that do not bill tokens.
    """

    output_tokens: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="outputTokens"),
        pydantic.Field(
            alias="outputTokens",
            description="Output tokens attributed to this line. Absent for lines that do not bill tokens.",
        ),
    ] = None
    """
    Output tokens attributed to this line. Absent for lines that do not bill tokens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
