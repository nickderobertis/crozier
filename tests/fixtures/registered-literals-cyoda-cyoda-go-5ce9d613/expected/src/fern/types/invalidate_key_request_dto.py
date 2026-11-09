

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InvalidateKeyRequestDto(UniversalBaseModel):
    grace_period_sec: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="gracePeriodSec"),
        pydantic.Field(
            alias="gracePeriodSec",
            description="Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).",
        ),
    ] = None
    """
    Number of seconds to keep the key valid after invalidation. Default is 0 (immediate invalidation).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
