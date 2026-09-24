

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60rate_rule import V60RateRule
from .v60taxability_code_rate_action_code import V60TaxabilityCodeRateActionCode


class V60TaxabilityCode(UniversalBaseModel):
    county_fips: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countyFIPS"),
        pydantic.Field(alias="countyFIPS", description="County FIPS code resolved for the request location."),
    ]
    """
    County FIPS code resolved for the request location.
    """

    id: str = pydantic.Field()
    """
    Taxability Information Code (TIC) supplied on the request.
    """

    label: str = pydantic.Field()
    """
    Longer description of the TIC.
    """

    rate_action_code: typing_extensions.Annotated[
        V60TaxabilityCodeRateActionCode,
        FieldMetadata(alias="rateActionCode"),
        pydantic.Field(
            alias="rateActionCode",
            description="Outcome of the TIC lookup: T00 (valid TIC, rules listed), T01 (valid TIC, no applicable rate rules), T02 (invalid TIC), T03 (invalid TIC format).",
        ),
    ]
    """
    Outcome of the TIC lookup: T00 (valid TIC, rules listed), T01 (valid TIC, no applicable rate rules), T02 (invalid TIC), T03 (invalid TIC format).
    """

    rate_action_message: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rateActionMessage"),
        pydantic.Field(alias="rateActionMessage", description="Human-readable explanation of the rateActionCode."),
    ]
    """
    Human-readable explanation of the rateActionCode.
    """

    rate_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[V60RateRule]],
        FieldMetadata(alias="rateRules"),
        pydantic.Field(
            alias="rateRules",
            description="Product rate rules that apply to this TIC in the resolved jurisdiction, filtered to rules active on the current date.",
        ),
    ] = None
    """
    Product rate rules that apply to this TIC in the resolved jurisdiction, filtered to rules active on the current date.
    """

    state_fips: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateFIPS"),
        pydantic.Field(alias="stateFIPS", description="State FIPS code resolved for the request location."),
    ]
    """
    State FIPS code resolved for the request location.
    """

    title: str = pydantic.Field()
    """
    Short title of the TIC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
