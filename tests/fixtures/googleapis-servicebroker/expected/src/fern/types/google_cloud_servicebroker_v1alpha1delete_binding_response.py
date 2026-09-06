

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse(UniversalBaseModel):
    """
    Response for the `DeleteBinding()` method.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to communicate description of the response. Usually for non-standard
    error codes.
    https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors
    """

    operation: typing.Optional[str] = pydantic.Field(default=None)
    """
    If broker executes operation asynchronously, this is the operation ID that
    can be polled to check the completion status of said operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
