

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Scancode(UniversalBaseModel):
    license: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A full comparison between the database of licenses present in ScanCode and the code uploaded by users based approach.
    """

    copyright: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Copyright along with copyright holder/author information.
    """

    email: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Email(s) present in the scan code file.
    """

    url: typing.Optional[bool] = pydantic.Field(default=None)
    """
    URL(s) present in the scan code file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
