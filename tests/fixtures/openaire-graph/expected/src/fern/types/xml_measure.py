

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.xml_utilities import (
    XmlAttribute,
    XmlComment,
    XmlContent,
    XmlElement,
    XmlNode,
    build_xml_model,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_attribute,
    xml_content,
)


class XmlMeasure(UniversalBaseModel):
    id: typing.Optional[str] = None
    score: typing.Optional[str] = None
    clazz: typing.Optional[str] = None
    count: typing.Optional[str] = None
    datasource: typing.Optional[str] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<measure>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="measure",
            attributes=[
                XmlAttribute(name="id", value=self.id),
                XmlAttribute(name="score", value=self.score),
                XmlAttribute(name="class", value=self.clazz),
                XmlAttribute(name="count", value=self.count),
                XmlAttribute(name="datasource", value=self.datasource),
                *extra_xml_attributes(self),
            ],
            children=[],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlMeasure:
        """
        Parses a `<measure>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "measure")
        content = xml_content(node, {})
        model = build_xml_model(
            cls,
            dict(
                id=xml_attribute(node, "id"),
                score=xml_attribute(node, "score"),
                clazz=xml_attribute(node, "class"),
                count=xml_attribute(node, "count"),
                datasource=xml_attribute(node, "datasource"),
            ),
            node,
            {"id", "score", "class", "count", "datasource"},
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlMeasure:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlMeasure:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlMeasure:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlMeasure:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlMeasure:
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
