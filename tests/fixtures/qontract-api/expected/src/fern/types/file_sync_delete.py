

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileSyncDelete(UniversalBaseModel):
    """
    Delete a file from the repository.
    """

    commit_message: str = pydantic.Field()
    """
    Commit message for this change
    """

    path: str = pydantic.Field()
    """
    File path in the repository
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
