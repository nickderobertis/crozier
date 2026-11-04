

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .client_usage_data import ClientUsageData


class ClientUsageSession(UniversalBaseModel):
    session_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId")
    ] = None
    usage_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[ClientUsageData]]],
        FieldMetadata(alias="usageData"),
        pydantic.Field(alias="usageData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
