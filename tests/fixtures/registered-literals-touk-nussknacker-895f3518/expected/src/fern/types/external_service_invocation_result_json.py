

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .context_id_dto import ContextIdDto


class ExternalServiceInvocationResultJson(UniversalBaseModel):
    context_id: typing_extensions.Annotated[
        ContextIdDto, FieldMetadata(alias="contextId"), pydantic.Field(alias="contextId")
    ]
    timestamp: dt.datetime
    name: str
    value: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
