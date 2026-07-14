

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stream_descriptor import StreamDescriptor


class ResetConfig(UniversalBaseModel):
    """
    contains information about how a reset was configured. only populated if the job was a reset.
    """

    streams_to_reset: typing_extensions.Annotated[
        typing.Optional[typing.List[StreamDescriptor]], FieldMetadata(alias="streamsToReset")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
