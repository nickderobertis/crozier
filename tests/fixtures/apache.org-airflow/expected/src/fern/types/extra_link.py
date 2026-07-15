

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .class_reference import ClassReference


class ExtraLink(UniversalBaseModel):
    """
    Additional links containing additional information about the task.
    """

    class_ref: typing.Optional[ClassReference] = None
    href: typing.Optional[str] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
