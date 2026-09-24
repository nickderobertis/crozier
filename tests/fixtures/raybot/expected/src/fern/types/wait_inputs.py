

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WaitInputs(UniversalBaseModel):
    duration_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="durationMs"),
        pydantic.Field(alias="durationMs", description="The duration in milliseconds"),
    ]
    """
    The duration in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
