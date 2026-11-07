

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SourceState(UniversalBaseModel):
    """
    Source connector state — cursors, backfill progress, events cursors.
    """

    streams: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Per-stream checkpoint data, keyed by stream name.
    """

    global_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="global"),
        pydantic.Field(alias="global", description="Source-wide state shared across all streams."),
    ]
    """
    Source-wide state shared across all streams.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
