

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .grpc_message_template_type import GrpcMessageTemplateType


class GrpcMessage(UniversalBaseModel):
    """
    a single gRPC stream message
    """

    json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="json"), pydantic.Field(alias="json")
    ] = None
    template_type: typing_extensions.Annotated[
        typing.Optional[GrpcMessageTemplateType],
        FieldMetadata(alias="templateType"),
        pydantic.Field(alias="templateType"),
    ] = None
    delay: typing.Optional[Delay] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
