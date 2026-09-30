

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .xml_classification import XmlClassification
from .xml_collected_from import XmlCollectedFrom
from .xml_pid import XmlPid
from .xml_web_resource import XmlWebResource


class XmlInstance(UniversalBaseModel):
    accessright: typing.Optional[XmlClassification] = None
    collectedfrom: typing.Optional[typing.List[XmlCollectedFrom]] = None
    hostedby: typing.Optional[typing.List[XmlCollectedFrom]] = None
    dateofacceptance: typing.Optional[str] = None
    instancetype: typing.Optional[XmlClassification] = None
    pids: typing.Optional[typing.List[XmlPid]] = None
    alternateidentifiers: typing.Optional[typing.List[XmlPid]] = None
    refereed: typing.Optional[XmlClassification] = None
    urls: typing.Optional[typing.List[str]] = None
    webresources: typing.Optional[typing.List[XmlWebResource]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
