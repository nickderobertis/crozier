

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Findings(UniversalBaseModel):
    """
    License findings and conclusions of file
    """

    scanner: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Licenses finding by scanner
    """

    conclusion: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Licenses concluded by user or main license in case of package
    """

    copyright: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Copyright findings for the file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
