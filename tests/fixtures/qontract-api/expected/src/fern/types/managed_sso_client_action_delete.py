

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ManagedSsoClientActionDelete(UniversalBaseModel):
    """
    Action: delete a managed SSO client no longer present in desired state.
    """

    client_id: str = pydantic.Field()
    """
    Exact Keycloak clientId of the client being deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
