

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileSyncUpdate(UniversalBaseModel):
    """
    Update an existing file in the repository.
    """

    commit_message: str = pydantic.Field()
    """
    Commit message for this change
    """

    content: str = pydantic.Field()
    """
    New file content
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
