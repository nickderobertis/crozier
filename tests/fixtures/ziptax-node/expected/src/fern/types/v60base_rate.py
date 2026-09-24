

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60base_rate_jur_type import V60BaseRateJurType


class V60BaseRate(UniversalBaseModel):
    jur_description: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="jurDescription"),
        pydantic.Field(
            alias="jurDescription",
            description="Human-readable label combining the jurisdiction and tax type (e.g. 'US State Sales Tax').",
        ),
    ]
    """
    Human-readable label combining the jurisdiction and tax type (e.g. 'US State Sales Tax').
    """

    jur_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="jurName"),
        pydantic.Field(
            alias="jurName",
            description="Name or code of the jurisdiction: state alpha code, county/city name, or district label (e.g. 'CA', 'ORANGE', 'Local District: 37').",
        ),
    ]
    """
    Name or code of the jurisdiction: state alpha code, county/city name, or district label (e.g. 'CA', 'ORANGE', 'Local District: 37').
    """

    jur_tax_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jurTaxCode"),
        pydantic.Field(
            alias="jurTaxCode",
            description="FIPS-like tax code for the jurisdiction (state, county, city, or district). For Texas city components this is the TAID published for the city that contains the address. Null when the jurisdiction has no associated code.",
        ),
    ] = None
    """
    FIPS-like tax code for the jurisdiction (state, county, city, or district). For Texas city components this is the TAID published for the city that contains the address. Null when the jurisdiction has no associated code.
    """

    jur_type: typing_extensions.Annotated[
        V60BaseRateJurType,
        FieldMetadata(alias="jurType"),
        pydantic.Field(
            alias="jurType",
            description="Jurisdiction level combined with the tax kind (sales vs use) this component represents.",
        ),
    ]
    """
    Jurisdiction level combined with the tax kind (sales vs use) this component represents.
    """

    rate: float = pydantic.Field()
    """
    Tax rate for this jurisdiction/tax-type component, as a decimal fraction (e.g. 0.0625 = 6.25%).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
