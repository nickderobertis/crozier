

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .xml_child_result import XmlChildResult
from .xml_instance import XmlInstance


class XmlChildren(UniversalBaseModel):
    results: typing.Optional[typing.List[XmlChildResult]] = None
    instances: typing.Optional[typing.List[XmlInstance]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
