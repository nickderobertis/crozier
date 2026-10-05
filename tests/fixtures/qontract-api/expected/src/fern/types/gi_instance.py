

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gi_organization import GiOrganization
from .secret import Secret


class GiInstance(UniversalBaseModel):
    """
    Glitchtip instance configuration with desired state.
    """

    automation_user_email: Secret = pydantic.Field()
    """
    Secret reference for the automation user email
    """

    console_url: str = pydantic.Field()
    """
    Glitchtip instance base URL
    """

    max_retries: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max HTTP retries
    """

    name: str = pydantic.Field()
    """
    Instance name (unique identifier)
    """

    organizations: typing.Optional[typing.List[GiOrganization]] = pydantic.Field(default=None)
    """
    Desired organizations to reconcile
    """

    read_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP read timeout in seconds
    """

    token: Secret = pydantic.Field()
    """
    Secret reference for the API token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
