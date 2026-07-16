

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostFactorsResidualizationRequestFactorsItem(UniversalBaseModel):
    factor_returns: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="factorReturns"),
        pydantic.Field(
            alias="factorReturns",
            description="factorReturns[t] is the return of the factor at the time t; all the factorReturns arrays must have the same length",
        ),
    ]
    """
    factorReturns[t] is the return of the factor at the time t; all the factorReturns arrays must have the same length
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
