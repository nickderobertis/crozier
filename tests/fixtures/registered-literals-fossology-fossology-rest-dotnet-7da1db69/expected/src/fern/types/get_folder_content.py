

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetFolderContent(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the folder content.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content of the folder.
    """

    removable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the folder removable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
