

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Folder(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the folder.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the folder.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the folder.
    """

    parent: typing.Optional[int] = pydantic.Field(default=None)
    """
    Id of the parent folder (if any, null otherwise).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
