

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
    xml_content,
    xml_content_item,
    xml_content_items,
)
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
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<project>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="project",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="originalId", value=self.original_id),
                XmlChild(name="code", value=self.code),
                XmlChild(name="acronym", value=self.acronym),
                XmlChild(name="title", value=self.title),
                XmlChild(name="startdate", value=self.startdate),
                XmlChild(name="enddate", value=self.enddate),
                XmlChild(name="callidentifier", value=self.callidentifier),
                XmlChild(name="duration", value=self.duration),
                XmlChild(name="keywords", value=self.keywords),
                XmlChild(name="ecarticle29_3", value=self.ecarticle293),
                XmlChild(name="oamandatepublications", value=self.oamandatepublications),
                XmlChild(name="ecsc39", value=self.ecsc39),
                XmlChild(name="summary", value=self.summary),
                XmlChild(name="currency", value=self.currency),
                XmlChild(name="totalcost", value=self.totalcost),
                XmlChild(name="fundedamount", value=self.fundedamount),
                XmlChild(name="children", value=self.children),
            ],
            content=order_xml_content(
                self._content,
                self.collectedfrom,
                self.pids,
                self.measures,
                self.subjects,
                self.contracttype,
                self.fundingtree,
                self.datainfo,
                self.rels,
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
        collectedfrom: typing.Optional[XmlCollectedFrom] = None,
        original_id: typing.Optional[str] = None,
        pids: typing.Optional[typing.List[XmlPid]] = None,
        measures: typing.Optional[typing.List[XmlMeasure]] = None,
        code: typing.Optional[str] = None,
        acronym: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        startdate: typing.Optional[str] = None,
        enddate: typing.Optional[str] = None,
        callidentifier: typing.Optional[str] = None,
        duration: typing.Optional[str] = None,
        keywords: typing.Optional[str] = None,
        ecarticle293: typing.Optional[str] = None,
        subjects: typing.Optional[typing.List[XmlSubject]] = None,
        contracttype: typing.Optional[XmlContractType] = None,
        oamandatepublications: typing.Optional[str] = None,
        ecsc39: typing.Optional[str] = None,
        summary: typing.Optional[str] = None,
        currency: typing.Optional[str] = None,
        totalcost: typing.Optional[str] = None,
        fundedamount: typing.Optional[str] = None,
        fundingtree: typing.Optional[XmlFundingTree] = None,
        datainfo: typing.Optional[XmlDataInfo] = None,
        rels: typing.Optional[XmlRels] = None,
        children: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        collectedfrom : typing.Optional[XmlCollectedFrom]

        original_id : typing.Optional[str]

        pids : typing.Optional[typing.List[XmlPid]]

        measures : typing.Optional[typing.List[XmlMeasure]]

        code : typing.Optional[str]

        acronym : typing.Optional[str]

        title : typing.Optional[str]

        startdate : typing.Optional[str]

        enddate : typing.Optional[str]

        callidentifier : typing.Optional[str]

        duration : typing.Optional[str]

        keywords : typing.Optional[str]

        ecarticle293 : typing.Optional[str]

        subjects : typing.Optional[typing.List[XmlSubject]]

        contracttype : typing.Optional[XmlContractType]

        oamandatepublications : typing.Optional[str]

        ecsc39 : typing.Optional[str]

        summary : typing.Optional[str]

        currency : typing.Optional[str]

        totalcost : typing.Optional[str]

        fundedamount : typing.Optional[str]

        fundingtree : typing.Optional[XmlFundingTree]

        datainfo : typing.Optional[XmlDataInfo]

        rels : typing.Optional[XmlRels]

        children : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(
                collectedfrom=collectedfrom,
                original_id=original_id,
                pids=pids,
                measures=measures,
                code=code,
                acronym=acronym,
                title=title,
                startdate=startdate,
                enddate=enddate,
                callidentifier=callidentifier,
                duration=duration,
                keywords=keywords,
                ecarticle293=ecarticle293,
                subjects=subjects,
                contracttype=contracttype,
                oamandatepublications=oamandatepublications,
                ecsc39=ecsc39,
                summary=summary,
                currency=currency,
                totalcost=totalcost,
                fundedamount=fundedamount,
                fundingtree=fundingtree,
                datainfo=datainfo,
                rels=rels,
                children=children,
            ),
            **extra_attributes,
        )
        self._content.extend(
            order_xml_content(
                [],
                self.collectedfrom,
                self.pids,
                self.measures,
                self.subjects,
                self.contracttype,
                self.fundingtree,
                self.datainfo,
                self.rels,
            )
        )

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlProject:
        """
        Parses a `<project>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "project")
        content = xml_content(
            node,
            {
                "collectedfrom": XmlCollectedFrom,
                "pid": XmlPid,
                "measure": XmlMeasure,
                "subject": XmlSubject,
                "contracttype": XmlContractType,
                "fundingtree": XmlFundingTree,
                "datainfo": XmlDataInfo,
                "rels": XmlRels,
            },
            skip={
                "originalId",
                "code",
                "acronym",
                "title",
                "startdate",
                "enddate",
                "callidentifier",
                "duration",
                "keywords",
                "ecarticle29_3",
                "oamandatepublications",
                "ecsc39",
                "summary",
                "currency",
                "totalcost",
                "fundedamount",
                "children",
            },
        )
        model = build_xml_model(
            cls,
            dict(
                collectedfrom=xml_content_item(content, (XmlCollectedFrom,)),
                original_id=xml_child(node, {"originalId": str}),
                pids=xml_content_items(content, (XmlPid,), optional=True),
                measures=xml_content_items(content, (XmlMeasure,), optional=True),
                code=xml_child(node, {"code": str}),
                acronym=xml_child(node, {"acronym": str}),
                title=xml_child(node, {"title": str}),
                startdate=xml_child(node, {"startdate": str}),
                enddate=xml_child(node, {"enddate": str}),
                callidentifier=xml_child(node, {"callidentifier": str}),
                duration=xml_child(node, {"duration": str}),
                keywords=xml_child(node, {"keywords": str}),
                ecarticle293=xml_child(node, {"ecarticle29_3": str}),
                subjects=xml_content_items(content, (XmlSubject,), optional=True),
                contracttype=xml_content_item(content, (XmlContractType,)),
                oamandatepublications=xml_child(node, {"oamandatepublications": str}),
                ecsc39=xml_child(node, {"ecsc39": str}),
                summary=xml_child(node, {"summary": str}),
                currency=xml_child(node, {"currency": str}),
                totalcost=xml_child(node, {"totalcost": str}),
                fundedamount=xml_child(node, {"fundedamount": str}),
                fundingtree=xml_content_item(content, (XmlFundingTree,)),
                datainfo=xml_content_item(content, (XmlDataInfo,)),
                rels=xml_content_item(content, (XmlRels,)),
                children=xml_child(node, {"children": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlProject:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlProject:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlProject:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlProject:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlProject:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

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
