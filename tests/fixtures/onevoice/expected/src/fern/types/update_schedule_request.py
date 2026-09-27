

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateScheduleRequest(UniversalBaseModel):
    schedule: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Free-form per-day schedule blob.
    """

    special_dates: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="specialDates"),
        pydantic.Field(alias="specialDates", description="Optional special-date overrides."),
    ] = None
    """
    Optional special-date overrides.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
