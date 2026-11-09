

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.log import Log


class PostLogsResponse(UniversalBaseModel):
    total_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalCount"), pydantic.Field(alias="totalCount")
    ] = None
    logs: typing.Optional[Log] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
