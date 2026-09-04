

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_factor_type import AuthFactorType


class AuthFactor(UniversalBaseModel):
    type: AuthFactorType = pydantic.Field()
    """
    Name of the authentication method
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Applicable for biometric based authentication, number of bio segments to be captured for authentication.
    """

    bio_sub_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="bioSubTypes"),
        pydantic.Field(
            alias="bioSubTypes",
            description="Applicable for biometric based authentication. Can be more specific about which bio segments should be captured.",
        ),
    ] = None
    """
    Applicable for biometric based authentication. Can be more specific about which bio segments should be captured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
