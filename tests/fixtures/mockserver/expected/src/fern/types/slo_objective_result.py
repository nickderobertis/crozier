

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .slo_objective_result_result import SloObjectiveResultResult


class SloObjectiveResult(UniversalBaseModel):
    """
    the evaluated result of a single objective
    """

    sli: typing.Optional[str] = None
    comparator: typing.Optional[str] = None
    threshold: typing.Optional[float] = None
    observed_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="observedValue"), pydantic.Field(alias="observedValue")
    ] = None
    result: typing.Optional[SloObjectiveResultResult] = None
    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    human-readable explanation of the objective result (e.g. sample count, observed vs threshold)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
