

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MeDeletionResponse(UniversalBaseModel):
    apple_authorization_revoked: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="appleAuthorizationRevoked"),
        pydantic.Field(
            alias="appleAuthorizationRevoked",
            description="Apple revocation result, or null when no Apple account was linked",
        ),
    ] = None
    """
    Apple revocation result, or null when no Apple account was linked
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
