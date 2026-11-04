

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .span_preparation import SpanPreparation
from .span_status_display_mode import SpanStatusDisplayMode


class SpanStatus(UniversalBaseModel):
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    display_mode: typing_extensions.Annotated[
        typing.Optional[SpanStatusDisplayMode], FieldMetadata(alias="displayMode"), pydantic.Field(alias="displayMode")
    ] = None
    geometry: typing.Optional[typing.Dict[str, typing.Any]] = None
    preparations: typing.Optional[typing.List[SpanPreparation]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
