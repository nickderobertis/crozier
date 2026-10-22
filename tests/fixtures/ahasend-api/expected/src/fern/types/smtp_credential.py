

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .smtp_credential_object import SmtpCredentialObject
from .smtp_credential_scope import SmtpCredentialScope


class SmtpCredential(UniversalBaseModel):
    object: SmtpCredentialObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the SMTP credential
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the credential was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the credential was last updated
    """

    name: str = pydantic.Field()
    """
    Credential name
    """

    username: str = pydantic.Field()
    """
    SMTP username
    """

    sandbox: bool = pydantic.Field()
    """
    Whether this is a sandbox credential
    """

    scope: SmtpCredentialScope = pydantic.Field()
    """
    Credential scope
    """

    domains: typing.List[str] = pydantic.Field()
    """
    Domains this credential can send from. Always present; global credentials return an empty array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
