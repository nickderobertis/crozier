

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .xml_provenance_action import XmlProvenanceAction


class XmlDataInfo(UniversalBaseModel):
    inferred: typing.Optional[str] = None
    deletedbyinference: typing.Optional[str] = None
    trust: typing.Optional[str] = None
    inferenceprovenance: typing.Optional[str] = None
    provenanceaction: typing.Optional[XmlProvenanceAction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
