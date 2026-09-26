

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VisualizeSessionIdGetResponseDataVisualizationsItemContentAfterBefore(UniversalBaseModel):
    """
    Code before changes
    """

    language: str = pydantic.Field()
    """
    Programming language for syntax highlighting
    """

    code: str = pydantic.Field()
    """
    Code content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
