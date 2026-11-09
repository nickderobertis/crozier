

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.file import File


class ListFilesResponse(UniversalBaseModel):
    """
    A list of file entities based on the provided filters.
    """

    total: int = pydantic.Field()
    """
    Total number of files (before pagination) that match the query.
    """

    files: typing.List[File]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
