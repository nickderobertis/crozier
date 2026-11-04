

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .fine_tune import FineTune
from .type_discriminator import TypeDiscriminator


class FineTuneList(UniversalBaseModel):
    """
    Represents a list of fine tunes.
    """

    object: typing.Optional[TypeDiscriminator] = None
    data: typing.Optional[typing.List[FineTune]] = pydantic.Field(default=None)
    """
    The list of items.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FineTuneList)
