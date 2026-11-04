

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .span_from import SpanFrom
from .span_to import SpanTo


class Span(UniversalBaseModel):
    from_: typing_extensions.Annotated[
        typing.Optional[SpanFrom], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[SpanTo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
