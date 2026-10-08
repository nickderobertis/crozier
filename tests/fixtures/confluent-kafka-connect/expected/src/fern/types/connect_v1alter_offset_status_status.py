

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1AlterOffsetStatusStatus(UniversalBaseModel):
    """
    The response of the alter offsets operation.
    """

    phase: str = pydantic.Field()
    """
    The phase of the alter offset operation. 
    
    PENDING: The offset alter operation is in progress.
    
    APPLIED: The offset alter operation has been applied to the connector.
    
    FAILED:  The offset alter operation has failed to be applied to the connector.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    An info message from the alter offset operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
