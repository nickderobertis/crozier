

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceRemovalState(UniversalBaseModel):
    can_remove: typing.Optional[bool] = pydantic.Field(default=None)
    """
    when True, marks the service as ready to be removed
    """

    can_save: typing.Optional[bool] = pydantic.Field(default=None)
    """
    when True, saves the internal state and upload outputs of the service
    """

    was_removed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Will be True when the removal finished. Used primarily to cancel retrying long running operations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
