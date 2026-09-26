

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeControlSettingsByoyomi(UniversalBaseModel):
    initial_ms: typing_extensions.Annotated[int, FieldMetadata(alias="initialMs"), pydantic.Field(alias="initialMs")]
    byoyomi_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="byoyomiMs"), pydantic.Field(alias="byoyomiMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
