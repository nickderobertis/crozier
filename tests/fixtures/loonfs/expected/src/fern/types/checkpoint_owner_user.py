

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CheckpointOwnerUser(UniversalBaseModel):
    """
    A snapshot, which a caller created. It's deleted by its ID or after it expires.
    """

    name: str = pydantic.Field()
    """
    The label that the creator recorded. Labels don't need to be unique.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
