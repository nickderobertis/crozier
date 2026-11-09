

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nature_of_suit import NatureOfSuit
from .source_cause_of_action import SourceCauseOfAction
from .source_charge import SourceCharge
from .source_page_data import SourcePageData


class SourceCaseData(UniversalBaseModel):
    """
    Source data in the court website.
    """

    nature_of_suit_array: typing_extensions.Annotated[
        typing.List[typing.Optional[NatureOfSuit]],
        FieldMetadata(alias="natureOfSuitArray"),
        pydantic.Field(
            alias="natureOfSuitArray", description="Array of Charges for a case which is provided by the Court."
        ),
    ]
    """
    Array of Charges for a case which is provided by the Court.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    source_case_status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceCaseStatus"),
        pydantic.Field(alias="sourceCaseStatus", description="Case Status as provided by Court."),
    ]
    """
    Case Status as provided by Court.
    """

    source_case_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceCaseType"),
        pydantic.Field(alias="sourceCaseType", description="Case Type for a case which is provided by the Court."),
    ]
    """
    Case Type for a case which is provided by the Court.
    """

    source_cause_of_action_array: typing_extensions.Annotated[
        typing.List[typing.Optional[SourceCauseOfAction]],
        FieldMetadata(alias="sourceCauseOfActionArray"),
        pydantic.Field(
            alias="sourceCauseOfActionArray",
            description="Array of Cause Of Action for a case which is provided by the Court.",
        ),
    ]
    """
    Array of Cause Of Action for a case which is provided by the Court.
    """

    source_charge_array: typing_extensions.Annotated[
        typing.List[typing.Optional[SourceCharge]],
        FieldMetadata(alias="sourceChargeArray"),
        pydantic.Field(
            alias="sourceChargeArray", description="Array of Charges for a case which is provided by the Court."
        ),
    ]
    """
    Array of Charges for a case which is provided by the Court.
    """

    source_court: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="sourceCourt"),
        pydantic.Field(alias="sourceCourt", description="Courtrhouse as provided by Court."),
    ]
    """
    Courtrhouse as provided by Court.
    """

    source_page_data: typing_extensions.Annotated[
        typing.List[typing.Optional[SourcePageData]],
        FieldMetadata(alias="sourcePageData"),
        pydantic.Field(alias="sourcePageData"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
