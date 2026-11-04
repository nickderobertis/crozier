

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DelegatedToken(UniversalBaseModel):
    thirdparty_oauth2service_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="thirdparty_oauth2_service_id"),
        pydantic.Field(
            alias="thirdparty_oauth2_service_id",
            description="Service identifier (UUID) from the available services list.\nMust be a valid service available to the agent.",
        ),
    ]
    """
    Service identifier (UUID) from the available services list.
    Must be a valid service available to the agent.
    """

    scopes: typing.List[str] = pydantic.Field()
    """
    Array of OAuth2 scope values to delegate.
    Each scope must be valid for the specified service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
