

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleCloudServicebrokerV1Alpha1Operation(UniversalBaseModel):
    """
    Describes a long running operation, which conforms to OpenService API.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of the Operation state.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state of the operation.
    Valid values are: "in progress", "succeeded", and "failed".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
