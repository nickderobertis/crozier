

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyAdvancedAwaUserResponse(UniversalBaseModel):
    correlation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="correlationId")] = (
        pydantic.Field(default=None)
    )
    """
    Correlation ID of the request
    """

    nonce: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Secret nonce received via the PUSH notification.
    """

    selection: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indication of the selection the user has made (Approving or rejecting the action)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
