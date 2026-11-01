

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetRemoteVolumeStepResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the response, typically "OK"
    """

    remote_volume_step: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current remote volume step value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
