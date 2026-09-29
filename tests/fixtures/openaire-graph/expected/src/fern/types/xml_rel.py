

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .xml_country import XmlCountry
from .xml_rel_to import XmlRelTo


class XmlRel(UniversalBaseModel):
    inferred: typing.Optional[str] = None
    trust: typing.Optional[str] = None
    inferenceprovenance: typing.Optional[str] = None
    provenanceaction: typing.Optional[str] = None
    to: typing.Optional[XmlRelTo] = None
    legalname: typing.Optional[str] = None
    country: typing.Optional[XmlCountry] = None
    legalshortname: typing.Optional[str] = None
    websiteurl: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
