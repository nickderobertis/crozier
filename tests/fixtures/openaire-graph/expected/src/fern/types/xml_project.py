

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_collected_from import XmlCollectedFrom
from .xml_contract_type import XmlContractType
from .xml_data_info import XmlDataInfo
from .xml_funding_tree import XmlFundingTree
from .xml_measure import XmlMeasure
from .xml_pid import XmlPid
from .xml_rels import XmlRels
from .xml_subject import XmlSubject


class XmlProject(UniversalBaseModel):
    collectedfrom: typing.Optional[XmlCollectedFrom] = None
    original_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="originalId"), pydantic.Field(alias="originalId")
    ] = None
    pids: typing.Optional[typing.List[XmlPid]] = None
    measures: typing.Optional[typing.List[XmlMeasure]] = None
    code: typing.Optional[str] = None
    acronym: typing.Optional[str] = None
    title: typing.Optional[str] = None
    startdate: typing.Optional[str] = None
    enddate: typing.Optional[str] = None
    callidentifier: typing.Optional[str] = None
    duration: typing.Optional[str] = None
    keywords: typing.Optional[str] = None
    ecarticle293: typing.Optional[str] = None
    subjects: typing.Optional[typing.List[XmlSubject]] = None
    contracttype: typing.Optional[XmlContractType] = None
    oamandatepublications: typing.Optional[str] = None
    ecsc39: typing.Optional[str] = None
    summary: typing.Optional[str] = None
    currency: typing.Optional[str] = None
    totalcost: typing.Optional[str] = None
    fundedamount: typing.Optional[str] = None
    fundingtree: typing.Optional[XmlFundingTree] = None
    datainfo: typing.Optional[XmlDataInfo] = None
    rels: typing.Optional[XmlRels] = None
    children: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
