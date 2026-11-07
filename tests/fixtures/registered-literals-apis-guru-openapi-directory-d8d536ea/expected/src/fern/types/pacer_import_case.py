

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pacer_import_case_results import PacerImportCaseResults


class PacerImportCase(UniversalBaseModel):
    court_fee: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="courtFee"),
        pydantic.Field(
            alias="courtFee",
            description="Court Fee charged for the Find Case request. This is only applicable for Appeal Cases.",
        ),
    ] = None
    """
    Court Fee charged for the Find Case request. This is only applicable for Appeal Cases.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    pacer_import_case_results_array: typing_extensions.Annotated[
        typing.List[typing.Optional[PacerImportCaseResults]],
        FieldMetadata(alias="pacerImportCaseResultsArray"),
        pydantic.Field(alias="pacerImportCaseResultsArray"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
