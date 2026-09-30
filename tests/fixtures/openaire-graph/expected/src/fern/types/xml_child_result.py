

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .xml_classification import XmlClassification
from .xml_classified_value import XmlClassifiedValue
from .xml_collected_from import XmlCollectedFrom
from .xml_instance import XmlInstance
from .xml_pid import XmlPid


class XmlChildResult(UniversalBaseModel):
    objidentifier: typing.Optional[str] = None
    creators: typing.Optional[typing.List[str]] = None
    publisher: typing.Optional[str] = None
    instances: typing.Optional[typing.List[XmlInstance]] = None
    dateofacceptance: typing.Optional[str] = None
    title: typing.Optional[XmlClassifiedValue] = None
    resulttype: typing.Optional[XmlClassification] = None
    collectedfrom: typing.Optional[typing.List[XmlCollectedFrom]] = None
    pids: typing.Optional[typing.List[XmlPid]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
