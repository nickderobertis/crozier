

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_type import SandboxType


class SandboxConfig(UniversalBaseModel):
    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Sandbox
    """

    type: typing.Optional[SandboxType] = pydantic.Field(default=None)
    """
    The type of sandbox.
    """

    config: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The JSON sandbox settings data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
