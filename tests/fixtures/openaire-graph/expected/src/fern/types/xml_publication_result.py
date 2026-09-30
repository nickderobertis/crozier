

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .xml_children import XmlChildren
from .xml_classification import XmlClassification
from .xml_classified_value import XmlClassifiedValue
from .xml_collected_from import XmlCollectedFrom
from .xml_context import XmlContext
from .xml_creator import XmlCreator
from .xml_data_info import XmlDataInfo
from .xml_journal_element import XmlJournalElement
from .xml_measure import XmlMeasure
from .xml_pid import XmlPid
from .xml_rels import XmlRels
from .xml_subject import XmlSubject


class XmlPublicationResult(UniversalBaseModel):
    collectedfrom: typing.Optional[typing.List[XmlCollectedFrom]] = None
    original_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalIds"), pydantic.Field(alias="originalIds")
    ] = None
    pids: typing.Optional[typing.List[XmlPid]] = None
    measures: typing.Optional[typing.List[XmlMeasure]] = None
    titles: typing.Optional[typing.List[XmlClassifiedValue]] = None
    bestaccessright: typing.Optional[XmlClassification] = None
    creators: typing.Optional[typing.List[XmlCreator]] = None
    dateofacceptance: typing.Optional[str] = None
    descriptions: typing.Optional[typing.List[str]] = None
    subjects: typing.Optional[typing.List[XmlSubject]] = None
    language: typing.Optional[XmlClassification] = None
    relevantdates: typing.Optional[typing.List[XmlClassifiedValue]] = None
    publisher: typing.Optional[str] = None
    sources: typing.Optional[typing.List[str]] = None
    resulttype: typing.Optional[XmlClassification] = None
    resourcetype: typing.Optional[XmlClassification] = None
    isgreen: typing.Optional[str] = None
    isindiamondjournal: typing.Optional[str] = None
    publiclyfunded: typing.Optional[str] = None
    journal: typing.Optional[XmlJournalElement] = None
    contexts: typing.Optional[typing.List[XmlContext]] = None
    datainfo: typing.Optional[XmlDataInfo] = None
    rels: typing.Optional[XmlRels] = None
    children: typing.Optional[XmlChildren] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
