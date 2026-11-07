

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetDatabaseContent(UniversalBaseModel):
    metric: typing.Optional[str] = pydantic.Field(default=None)
    """
    The metric associated with the object.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total count associated with the metric.
    """

    last_vacuum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastVacuum"),
        pydantic.Field(
            alias="lastVacuum",
            description="The date and time of the last vacuum operation. If null, no vacuum operation has been performed.",
        ),
    ] = None
    """
    The date and time of the last vacuum operation. If null, no vacuum operation has been performed.
    """

    last_analyze: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastAnalyze"),
        pydantic.Field(
            alias="lastAnalyze",
            description="The date and time of the last analyze operation. If null, no analyze operation has been performed.",
        ),
    ] = None
    """
    The date and time of the last analyze operation. If null, no analyze operation has been performed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
