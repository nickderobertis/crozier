

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class XmlSubject(UniversalBaseModel):
    classid: typing.Optional[str] = None
    classname: typing.Optional[str] = None
    schemeid: typing.Optional[str] = None
    schemename: typing.Optional[str] = None
    inferred: typing.Optional[str] = None
    provenanceaction: typing.Optional[str] = None
    trust: typing.Optional[str] = None
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
