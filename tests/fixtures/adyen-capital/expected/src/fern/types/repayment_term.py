

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RepaymentTerm(UniversalBaseModel):
    estimated_days: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="estimatedDays"),
        pydantic.Field(alias="estimatedDays", description="The estimated duration of the repayment term, in days."),
    ]
    """
    The estimated duration of the repayment term, in days.
    """

    maximum_days: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maximumDays"),
        pydantic.Field(
            alias="maximumDays",
            description="The maximum duration of the repayment term, in days. Only applies when `contractType` is **loan**.",
        ),
    ] = None
    """
    The maximum duration of the repayment term, in days. Only applies when `contractType` is **loan**.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
