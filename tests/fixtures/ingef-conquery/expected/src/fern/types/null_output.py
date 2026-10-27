

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .output_description_base import OutputDescriptionBase


class NullOutput(OutputDescriptionBase):
    """
    Emits a `null`/NA value. Can be used to unify among multiple input sources with differing file schemas.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
