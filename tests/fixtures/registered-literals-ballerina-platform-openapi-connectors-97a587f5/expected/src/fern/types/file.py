

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .file_statistics import FileStatistics
from .purpose import Purpose
from .state import State
from .type_discriminator import TypeDiscriminator


class File(UniversalBaseModel):
    """
    A file is a document usable for training and validation. It can also be a service generated document with result details.
    """

    object: typing.Optional[TypeDiscriminator] = None
    status: typing.Optional[State] = None
    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    A timestamp when this job or item was created (in unix epochs).
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    A timestamp when this job or item was modified last (in unix epochs).
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identity of this item.
    """

    bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of this file when available (can be null). File sizes larger than 2^53-1 are not supported to ensure compatibility
    with JavaScript integers.
    """

    purpose: Purpose
    filename: str = pydantic.Field()
    """
    The name of the file.
    """

    statistics: typing.Optional[FileStatistics] = None
    error: typing.Optional["Error"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .error import Error

update_forward_refs(File, Error=Error)
