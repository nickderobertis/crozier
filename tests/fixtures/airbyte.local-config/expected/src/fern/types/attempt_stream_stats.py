

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_stats import AttemptStats


class AttemptStreamStats(UniversalBaseModel):
    stats: AttemptStats
    stream_name: typing_extensions.Annotated[str, FieldMetadata(alias="streamName")]
    stream_namespace: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="streamNamespace")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
