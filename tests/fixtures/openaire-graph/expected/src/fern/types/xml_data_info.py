

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.xml_utilities import (
    XmlChild,
    XmlComment,
    XmlContent,
    XmlElement,
    XmlNode,
    build_xml_model,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_child,
    xml_content,
    xml_content_item,
)
from .xml_provenance_action import XmlProvenanceAction


class XmlDataInfo(UniversalBaseModel):
    inferred: typing.Optional[str] = None
    deletedbyinference: typing.Optional[str] = None
    trust: typing.Optional[str] = None
    inferenceprovenance: typing.Optional[str] = None
    provenanceaction: typing.Optional[XmlProvenanceAction] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<datainfo>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="datainfo",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="inferred", value=self.inferred),
                XmlChild(name="deletedbyinference", value=self.deletedbyinference),
                XmlChild(name="trust", value=self.trust),
                XmlChild(name="inferenceprovenance", value=self.inferenceprovenance),
            ],
            content=order_xml_content(self._content, self.provenanceaction),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        inferred: typing.Optional[str] = None,
        deletedbyinference: typing.Optional[str] = None,
        trust: typing.Optional[str] = None,
        inferenceprovenance: typing.Optional[str] = None,
        provenanceaction: typing.Optional[XmlProvenanceAction] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        inferred : typing.Optional[str]

        deletedbyinference : typing.Optional[str]

        trust : typing.Optional[str]

        inferenceprovenance : typing.Optional[str]

        provenanceaction : typing.Optional[XmlProvenanceAction]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(
                inferred=inferred,
                deletedbyinference=deletedbyinference,
                trust=trust,
                inferenceprovenance=inferenceprovenance,
                provenanceaction=provenanceaction,
            ),
            **extra_attributes,
        )
        self._content.extend(order_xml_content([], self.provenanceaction))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlDataInfo:
        """
        Parses a `<datainfo>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "datainfo")
        content = xml_content(
            node,
            {"provenanceaction": XmlProvenanceAction},
            skip={"inferred", "deletedbyinference", "trust", "inferenceprovenance"},
        )
        model = build_xml_model(
            cls,
            dict(
                inferred=xml_child(node, {"inferred": str}),
                deletedbyinference=xml_child(node, {"deletedbyinference": str}),
                trust=xml_child(node, {"trust": str}),
                inferenceprovenance=xml_child(node, {"inferenceprovenance": str}),
                provenanceaction=xml_content_item(content, (XmlProvenanceAction,)),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlDataInfo:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlDataInfo:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlDataInfo:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlDataInfo:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlDataInfo:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
