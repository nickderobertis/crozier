

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StreamingSuccessResponseMeta(UniversalBaseModel):
    applied_through_seq: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="appliedThroughSeq"),
        pydantic.Field(
            alias="appliedThroughSeq", description="Latest event sequence number applied before this response."
        ),
    ] = None
    """
    Latest event sequence number applied before this response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
