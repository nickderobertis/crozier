

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from ..core.xml_utilities import (
    XmlChild,
    XmlComment,
    XmlContent,
    XmlElement,
    XmlNode,
    append_xml_child,
    build_xml_model,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_child,
    xml_children,
    xml_content,
    xml_content_item,
    xml_content_items,
)
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
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<result>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="result",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="originalId", value=self.original_ids),
                XmlChild(name="title", value=self.titles),
                XmlChild(name="bestaccessright", value=self.bestaccessright),
                XmlChild(name="creator", value=self.creators),
                XmlChild(name="dateofacceptance", value=self.dateofacceptance),
                XmlChild(name="description", value=self.descriptions),
                XmlChild(name="language", value=self.language),
                XmlChild(name="relevantdate", value=self.relevantdates),
                XmlChild(name="publisher", value=self.publisher),
                XmlChild(name="source", value=self.sources),
                XmlChild(name="resulttype", value=self.resulttype),
                XmlChild(name="resourcetype", value=self.resourcetype),
                XmlChild(name="isgreen", value=self.isgreen),
                XmlChild(name="isindiamondjournal", value=self.isindiamondjournal),
                XmlChild(name="publiclyfunded", value=self.publiclyfunded),
                XmlChild(name="journal", value=self.journal),
                XmlChild(name="context", value=self.contexts),
                XmlChild(name="children", value=self.children),
            ],
            content=order_xml_content(
                self._content, self.collectedfrom, self.pids, self.measures, self.subjects, self.datainfo, self.rels
            ),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        collectedfrom: typing.Optional[typing.List[XmlCollectedFrom]] = None,
        original_ids: typing.Optional[typing.List[str]] = None,
        pids: typing.Optional[typing.List[XmlPid]] = None,
        measures: typing.Optional[typing.List[XmlMeasure]] = None,
        titles: typing.Optional[typing.List[XmlClassifiedValue]] = None,
        bestaccessright: typing.Optional[XmlClassification] = None,
        creators: typing.Optional[typing.List[XmlCreator]] = None,
        dateofacceptance: typing.Optional[str] = None,
        descriptions: typing.Optional[typing.List[str]] = None,
        subjects: typing.Optional[typing.List[XmlSubject]] = None,
        language: typing.Optional[XmlClassification] = None,
        relevantdates: typing.Optional[typing.List[XmlClassifiedValue]] = None,
        publisher: typing.Optional[str] = None,
        sources: typing.Optional[typing.List[str]] = None,
        resulttype: typing.Optional[XmlClassification] = None,
        resourcetype: typing.Optional[XmlClassification] = None,
        isgreen: typing.Optional[str] = None,
        isindiamondjournal: typing.Optional[str] = None,
        publiclyfunded: typing.Optional[str] = None,
        journal: typing.Optional[XmlJournalElement] = None,
        contexts: typing.Optional[typing.List[XmlContext]] = None,
        datainfo: typing.Optional[XmlDataInfo] = None,
        rels: typing.Optional[XmlRels] = None,
        children: typing.Optional[XmlChildren] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        collectedfrom : typing.Optional[typing.List[XmlCollectedFrom]]

        original_ids : typing.Optional[typing.List[str]]

        pids : typing.Optional[typing.List[XmlPid]]

        measures : typing.Optional[typing.List[XmlMeasure]]

        titles : typing.Optional[typing.List[XmlClassifiedValue]]

        bestaccessright : typing.Optional[XmlClassification]

        creators : typing.Optional[typing.List[XmlCreator]]

        dateofacceptance : typing.Optional[str]

        descriptions : typing.Optional[typing.List[str]]

        subjects : typing.Optional[typing.List[XmlSubject]]

        language : typing.Optional[XmlClassification]

        relevantdates : typing.Optional[typing.List[XmlClassifiedValue]]

        publisher : typing.Optional[str]

        sources : typing.Optional[typing.List[str]]

        resulttype : typing.Optional[XmlClassification]

        resourcetype : typing.Optional[XmlClassification]

        isgreen : typing.Optional[str]

        isindiamondjournal : typing.Optional[str]

        publiclyfunded : typing.Optional[str]

        journal : typing.Optional[XmlJournalElement]

        contexts : typing.Optional[typing.List[XmlContext]]

        datainfo : typing.Optional[XmlDataInfo]

        rels : typing.Optional[XmlRels]

        children : typing.Optional[XmlChildren]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(
                collectedfrom=collectedfrom,
                original_ids=original_ids,
                pids=pids,
                measures=measures,
                titles=titles,
                bestaccessright=bestaccessright,
                creators=creators,
                dateofacceptance=dateofacceptance,
                descriptions=descriptions,
                subjects=subjects,
                language=language,
                relevantdates=relevantdates,
                publisher=publisher,
                sources=sources,
                resulttype=resulttype,
                resourcetype=resourcetype,
                isgreen=isgreen,
                isindiamondjournal=isindiamondjournal,
                publiclyfunded=publiclyfunded,
                journal=journal,
                contexts=contexts,
                datainfo=datainfo,
                rels=rels,
                children=children,
            ),
            **extra_attributes,
        )
        self._content.extend(
            order_xml_content([], self.collectedfrom, self.pids, self.measures, self.subjects, self.datainfo, self.rels)
        )

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlPublicationResult:
        """
        Parses a `<result>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "result")
        content = xml_content(
            node,
            {
                "collectedfrom": XmlCollectedFrom,
                "pid": XmlPid,
                "measure": XmlMeasure,
                "subject": XmlSubject,
                "datainfo": XmlDataInfo,
                "rels": XmlRels,
            },
            skip={
                "originalId",
                "title",
                "bestaccessright",
                "creator",
                "dateofacceptance",
                "description",
                "language",
                "relevantdate",
                "publisher",
                "source",
                "resulttype",
                "resourcetype",
                "isgreen",
                "isindiamondjournal",
                "publiclyfunded",
                "journal",
                "context",
                "children",
            },
        )
        model = build_xml_model(
            cls,
            dict(
                collectedfrom=xml_content_items(content, (XmlCollectedFrom,), optional=True),
                original_ids=xml_children(node, {"originalId": str}, optional=True),
                pids=xml_content_items(content, (XmlPid,), optional=True),
                measures=xml_content_items(content, (XmlMeasure,), optional=True),
                titles=xml_children(node, {"title": str}, optional=True),
                bestaccessright=xml_child(node, {"bestaccessright": str}),
                creators=xml_children(node, {"creator": str}, optional=True),
                dateofacceptance=xml_child(node, {"dateofacceptance": str}),
                descriptions=xml_children(node, {"description": str}, optional=True),
                subjects=xml_content_items(content, (XmlSubject,), optional=True),
                language=xml_child(node, {"language": str}),
                relevantdates=xml_children(node, {"relevantdate": str}, optional=True),
                publisher=xml_child(node, {"publisher": str}),
                sources=xml_children(node, {"source": str}, optional=True),
                resulttype=xml_child(node, {"resulttype": str}),
                resourcetype=xml_child(node, {"resourcetype": str}),
                isgreen=xml_child(node, {"isgreen": str}),
                isindiamondjournal=xml_child(node, {"isindiamondjournal": str}),
                publiclyfunded=xml_child(node, {"publiclyfunded": str}),
                journal=xml_child(node, {"journal": str}),
                contexts=xml_children(node, {"context": str}, optional=True),
                datainfo=xml_content_item(content, (XmlDataInfo,)),
                rels=xml_content_item(content, (XmlRels,)),
                children=xml_child(node, {"children": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlPublicationResult:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlPublicationResult:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlPublicationResult:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlPublicationResult:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlPublicationResult:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    def add_collectedfrom(
        self, *, name: typing.Optional[str] = None, id: typing.Optional[str] = None, **extra_attributes: str
    ) -> XmlCollectedFrom:
        """
        Appends a `<collectedfrom>` child element and returns it.

        Parameters
        ----------
        name : typing.Optional[str]

        id : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = XmlCollectedFrom(name=name, id=id, **extra_attributes)
        append_xml_child(self, "collectedfrom", child)
        return child

    def pid(
        self,
        *,
        classid: typing.Optional[str] = None,
        classname: typing.Optional[str] = None,
        schemeid: typing.Optional[str] = None,
        schemename: typing.Optional[str] = None,
        inferred: typing.Optional[str] = None,
        provenanceaction: typing.Optional[str] = None,
        trust: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> XmlPid:
        """
        Appends a `<pid>` child element and returns it.

        Parameters
        ----------
        classid : typing.Optional[str]

        classname : typing.Optional[str]

        schemeid : typing.Optional[str]

        schemename : typing.Optional[str]

        inferred : typing.Optional[str]

        provenanceaction : typing.Optional[str]

        trust : typing.Optional[str]

        value : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = XmlPid(
            classid=classid,
            classname=classname,
            schemeid=schemeid,
            schemename=schemename,
            inferred=inferred,
            provenanceaction=provenanceaction,
            trust=trust,
            value=value,
            **extra_attributes,
        )
        append_xml_child(self, "pids", child)
        return child

    def measure(
        self,
        *,
        id: typing.Optional[str] = None,
        score: typing.Optional[str] = None,
        clazz: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        datasource: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> XmlMeasure:
        """
        Appends a `<measure>` child element and returns it.

        Parameters
        ----------
        id : typing.Optional[str]

        score : typing.Optional[str]

        clazz : typing.Optional[str]

        count : typing.Optional[str]

        datasource : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = XmlMeasure(id=id, score=score, clazz=clazz, count=count, datasource=datasource, **extra_attributes)
        append_xml_child(self, "measures", child)
        return child

    def subject(
        self,
        *,
        classid: typing.Optional[str] = None,
        classname: typing.Optional[str] = None,
        schemeid: typing.Optional[str] = None,
        schemename: typing.Optional[str] = None,
        inferred: typing.Optional[str] = None,
        provenanceaction: typing.Optional[str] = None,
        trust: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> XmlSubject:
        """
        Appends a `<subject>` child element and returns it.

        Parameters
        ----------
        classid : typing.Optional[str]

        classname : typing.Optional[str]

        schemeid : typing.Optional[str]

        schemename : typing.Optional[str]

        inferred : typing.Optional[str]

        provenanceaction : typing.Optional[str]

        trust : typing.Optional[str]

        value : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = XmlSubject(
            classid=classid,
            classname=classname,
            schemeid=schemeid,
            schemename=schemename,
            inferred=inferred,
            provenanceaction=provenanceaction,
            trust=trust,
            value=value,
            **extra_attributes,
        )
        append_xml_child(self, "subjects", child)
        return child

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
