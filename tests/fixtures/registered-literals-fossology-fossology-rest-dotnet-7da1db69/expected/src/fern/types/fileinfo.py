

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Fileinfo(UniversalBaseModel):
    view_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    viewinfo of the file
    """

    meta_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Display display meta info of the file
    """

    package_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Shows package info of the file
    """

    tag_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Provides tag related information
    """

    reuse_info: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Reuse info of the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
