

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V60RateRule(UniversalBaseModel):
    effective_dt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="effectiveDt"),
        pydantic.Field(
            alias="effectiveDt", description="Date the rule takes effect, in YYYYMMDD format; null when not specified."
        ),
    ] = None
    """
    Date the rule takes effect, in YYYYMMDD format; null when not specified.
    """

    effective_tax_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="effectiveTaxRate"),
        pydantic.Field(
            alias="effectiveTaxRate",
            description="Decimal tax rate that applies to this product in this jurisdiction; null when not specified.",
        ),
    ] = None
    """
    Decimal tax rate that applies to this product in this jurisdiction; null when not specified.
    """

    exempt_over: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="exemptOver"),
        pydantic.Field(
            alias="exemptOver", description="Amounts above this dollar value are exempt; null when not specified."
        ),
    ] = None
    """
    Amounts above this dollar value are exempt; null when not specified.
    """

    exempt_under: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="exemptUnder"),
        pydantic.Field(
            alias="exemptUnder",
            description="Line-item exemption threshold; amounts below this dollar value are exempt; null when not specified.",
        ),
    ] = None
    """
    Line-item exemption threshold; amounts below this dollar value are exempt; null when not specified.
    """

    expires_dt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiresDt"),
        pydantic.Field(
            alias="expiresDt",
            description="Date the rule expires, in YYYYMMDD format; null means the rule is still in effect.",
        ),
    ] = None
    """
    Date the rule expires, in YYYYMMDD format; null means the rule is still in effect.
    """

    is_destination_tax_type: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDestinationTaxType"),
        pydantic.Field(
            alias="isDestinationTaxType",
            description="Whether the rule follows destination-based sourcing; null when not specified.",
        ),
    ] = None
    """
    Whether the rule follows destination-based sourcing; null when not specified.
    """

    is_food_drug: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isFoodDrug"),
        pydantic.Field(
            alias="isFoodDrug",
            description="Hint indicating the product falls under food/drug category classification; null when not specified.",
        ),
    ] = None
    """
    Hint indicating the product falls under food/drug category classification; null when not specified.
    """

    jur_tax_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jurTaxCode"),
        pydantic.Field(
            alias="jurTaxCode",
            description="Code identifying the jurisdiction the rule applies to: a FIPS-like code (state, county, or city), or a conditional jurisdiction code of the form 36:XX-#### or 36:XX-L#### (NY ST-100.3 codes for location-resolved school district / city / county rules; the code is specific to the form part the TIC is sourced from); null when not specified.",
        ),
    ] = None
    """
    Code identifying the jurisdiction the rule applies to: a FIPS-like code (state, county, or city), or a conditional jurisdiction code of the form 36:XX-#### or 36:XX-L#### (NY ST-100.3 codes for location-resolved school district / city / county rules; the code is specific to the form part the TIC is sourced from); null when not specified.
    """

    per_volume_tax_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="perVolumeTaxRate"),
        pydantic.Field(
            alias="perVolumeTaxRate",
            description="Per-volume tax rate for volume-based TIC overrides (e.g., $0.05/mL); null when not applicable.",
        ),
    ] = None
    """
    Per-volume tax rate for volume-based TIC overrides (e.g., $0.05/mL); null when not applicable.
    """

    per_volume_unit: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="perVolumeUnit"),
        pydantic.Field(
            alias="perVolumeUnit",
            description="Unit of measurement for perVolumeTaxRate (e.g., mL); null when not applicable.",
        ),
    ] = None
    """
    Unit of measurement for perVolumeTaxRate (e.g., mL); null when not applicable.
    """

    percent_taxable: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="percentTaxable"),
        pydantic.Field(
            alias="percentTaxable",
            description="Fraction of the sale that is taxable (for example, 0.5 means half-exempt); null when not specified.",
        ),
    ] = None
    """
    Fraction of the sale that is taxable (for example, 0.5 means half-exempt); null when not specified.
    """

    rate_cap_per_unit: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="rateCapPerUnit"),
        pydantic.Field(
            alias="rateCapPerUnit",
            description="Maximum tax rate cap per unit for capped TIC overrides (e.g., $0.30/cigar); null when not applicable.",
        ),
    ] = None
    """
    Maximum tax rate cap per unit for capped TIC overrides (e.g., $0.30/cigar); null when not applicable.
    """

    taxable_portion_over: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="taxablePortionOver"),
        pydantic.Field(
            alias="taxablePortionOver",
            description="Only the amount over this threshold is taxed; null when not specified.",
        ),
    ] = None
    """
    Only the amount over this threshold is taxed; null when not specified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
