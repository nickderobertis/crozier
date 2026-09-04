

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action import Action
from .status_code import StatusCode


class Status(UniversalBaseModel):
    actions: typing.Optional[typing.List[Action]] = pydantic.Field(default=None)
    """
    A list of actions that need to be completed to proceed with the grant. 
    """

    code: StatusCode = pydantic.Field()
    """
    The code for the status of the grant. Possible values:
    - **Pending**
    - **Active**
    - **Repaid**
    - **WrittenOff**
    - **Failed**
    - **Revoked**
    - **Requested**
    - **Reviewing**
    - **Approved**
    - **Rejected**
    - **Cancelled**
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
