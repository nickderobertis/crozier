

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_transform import FieldTransform
from .stream_descriptor import StreamDescriptor
from .stream_transform_transform_type import StreamTransformTransformType


class StreamTransform(UniversalBaseModel):
    stream_descriptor: typing_extensions.Annotated[StreamDescriptor, FieldMetadata(alias="streamDescriptor")]
    transform_type: typing_extensions.Annotated[StreamTransformTransformType, FieldMetadata(alias="transformType")]
    update_stream: typing_extensions.Annotated[
        typing.Optional[typing.List[FieldTransform]], FieldMetadata(alias="updateStream")
    ] = pydantic.Field(default=None)
    """
    list of field transformations. order does not matter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
