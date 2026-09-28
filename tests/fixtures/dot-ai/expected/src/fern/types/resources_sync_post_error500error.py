

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_sync_post_error500error_code import ResourcesSyncPostError500ErrorCode


class ResourcesSyncPostError500Error(UniversalBaseModel):
    code: ResourcesSyncPostError500ErrorCode
    message: str = pydantic.Field()
    """
    Human-readable error message
    """

    details: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Additional error context
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
