

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_decision_status import AuthenticationDecisionStatus


class AuthenticationDecision(UniversalBaseModel):
    status: AuthenticationDecisionStatus = pydantic.Field()
    """
    The status of the authentication. 
    
    Possible values: 
    
    * **refused** 
    
    * **proceed** 
    
    For more information, refer to [Authenticate cardholders using the Authentication SDK](https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/authenticate-cardholders/).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
