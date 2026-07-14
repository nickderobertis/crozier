

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_credential_type import AccessCredentialType


class AccessCredential(UniversalBaseModel):
    """
    A login credential mapped to a user identity. For password credentials, the username to present for Basic auth is the user's username from the user record
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of creation of the credential
    """

    type: AccessCredentialType = pydantic.Field()
    """
    The type of credential
    """

    value: str = pydantic.Field()
    """
    The credential value (e.g. the password)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
