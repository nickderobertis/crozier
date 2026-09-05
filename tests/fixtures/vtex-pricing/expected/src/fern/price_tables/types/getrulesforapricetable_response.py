

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .getrulesforapricetable_response_rules_item import GetrulesforapricetableResponseRulesItem


class GetrulesforapricetableResponse(UniversalBaseModel):
    percentual_modifier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="percentualModifier"),
        pydantic.Field(alias="percentualModifier", description="Percentual modifier."),
    ] = None
    """
    Percentual modifier.
    """

    rules: typing.Optional[typing.List[GetrulesforapricetableResponseRulesItem]] = pydantic.Field(default=None)
    """
    Array of rules for the price table.
    """

    trade_policy_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tradePolicyId"),
        pydantic.Field(alias="tradePolicyId", description="Trade Policy ID (Price Table ID)."),
    ] = None
    """
    Trade Policy ID (Price Table ID).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
