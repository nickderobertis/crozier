

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath


class CommitPreconditionPathAbsence(UniversalBaseModel):
    """
    A requirement that no visible entry exists at the full path.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path to check, which can be the root.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
