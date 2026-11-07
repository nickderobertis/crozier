

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .reply_spec import ReplySpec
from .reply_status import ReplyStatus


class Reply(UniversalBaseModel):
    """
    Reply extension that belongs to a top-level {@link Comment Comment}.
    """

    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    kind: str
    metadata: Metadata
    spec: ReplySpec
    status: ReplyStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
