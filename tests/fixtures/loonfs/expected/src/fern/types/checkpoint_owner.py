

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId


class CheckpointOwner_Fork(UniversalBaseModel):
    """
    The owner of a checkpoint record.
    """

    kind: typing.Literal["fork"] = "fork"
    target_namespace_id: NamespaceId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CheckpointOwner_User(UniversalBaseModel):
    """
    The owner of a checkpoint record.
    """

    kind: typing.Literal["user"] = "user"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CheckpointOwner = typing_extensions.Annotated[
    typing.Union[CheckpointOwner_Fork, CheckpointOwner_User], pydantic.Field(discriminator="kind")
]
