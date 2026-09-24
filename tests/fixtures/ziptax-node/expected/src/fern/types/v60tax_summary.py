

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60display_rate import V60DisplayRate
from .v60tax_summary_tax_type import V60TaxSummaryTaxType


class V60TaxSummary(UniversalBaseModel):
    display_rates: typing_extensions.Annotated[
        typing.Optional[typing.List[V60DisplayRate]],
        FieldMetadata(alias="displayRates"),
        pydantic.Field(alias="displayRates", description="Per-line rate breakdown displayed under this summary."),
    ] = None
    """
    Per-line rate breakdown displayed under this summary.
    """

    rate: float = pydantic.Field()
    """
    Aggregated tax rate for this summary line, as a decimal fraction (e.g. 0.0775 = 7.75%).
    """

    summary_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="summaryName"),
        pydantic.Field(
            alias="summaryName", description="Human-readable name of the summary grouping (e.g. 'Sales Tax')."
        ),
    ]
    """
    Human-readable name of the summary grouping (e.g. 'Sales Tax').
    """

    tax_type: typing_extensions.Annotated[
        V60TaxSummaryTaxType,
        FieldMetadata(alias="taxType"),
        pydantic.Field(alias="taxType", description="Tax kind this summary aggregates: 'SALES_TAX' or 'USE_TAX'."),
    ]
    """
    Tax kind this summary aggregates: 'SALES_TAX' or 'USE_TAX'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
