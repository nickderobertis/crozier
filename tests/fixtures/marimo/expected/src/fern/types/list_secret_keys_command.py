

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_secret_keys_command_type import ListSecretKeysCommandType
from .request_id import RequestId


class ListSecretKeysCommand(UniversalBaseModel):
    """
    List available secret keys.

        Retrieves secret names without exposing values.

        Attributes:
            request_id: Unique identifier for this request.
    """

    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    type: ListSecretKeysCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
