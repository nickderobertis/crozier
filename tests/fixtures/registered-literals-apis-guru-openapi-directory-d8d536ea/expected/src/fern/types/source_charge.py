

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_charge_additional_data import SourceChargeAdditionalData


class SourceCharge(UniversalBaseModel):
    """
    Source charge data from the source site.
    """

    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When this charge was first fetched from the court site."),
    ]
    """
    When this charge was first fetched from the court site.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible", description="Signifies if the charge is currently isVisible or not for the case."
        ),
    ]
    """
    Signifies if the charge is currently isVisible or not for the case.
    """

    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When this charge was last fetched from the court site."),
    ]
    """
    When this charge was last fetched from the court site.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    source_charge: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceCharge"),
        pydantic.Field(alias="sourceCharge", description="Charge data from the source site."),
    ] = None
    """
    Charge data from the source site.
    """

    source_charge_additional_data_array: typing_extensions.Annotated[
        typing.List[typing.Optional[SourceChargeAdditionalData]],
        FieldMetadata(alias="sourceChargeAdditionalDataArray"),
        pydantic.Field(
            alias="sourceChargeAdditionalDataArray",
            description="Additional data related to the charge which is available in the source site.",
        ),
    ]
    """
    Additional data related to the charge which is available in the source site.
    """

    source_charge_degree: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceChargeDegree"),
        pydantic.Field(alias="sourceChargeDegree", description="Charge degree data from the source site."),
    ] = None
    """
    Charge degree data from the source site.
    """

    source_charge_raw: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceChargeRaw"),
        pydantic.Field(alias="sourceChargeRaw", description="Raw charge data from the source site."),
    ]
    """
    Raw charge data from the source site.
    """

    source_charge_severity: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceChargeSeverity"),
        pydantic.Field(alias="sourceChargeSeverity", description="Charge severity data from the source site."),
    ] = None
    """
    Charge severity data from the source site.
    """

    source_statute: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceStatute"),
        pydantic.Field(alias="sourceStatute", description="Statute of a charge."),
    ] = None
    """
    Statute of a charge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
