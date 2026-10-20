

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.xml_utilities import (
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
    xml_content,
    xml_content_items,
)
from .xml_country import XmlCountry
from .xml_rel import XmlRel
from .xml_rel_to import XmlRelTo


class XmlRels(UniversalBaseModel):
    rels: typing.Optional[typing.List[XmlRel]] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<rels>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="rels",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[],
            content=order_xml_content(self._content, self.rels),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(self, *, rels: typing.Optional[typing.List[XmlRel]] = None, **extra_attributes: str) -> None:
        """
        Parameters
        ----------
        rels : typing.Optional[typing.List[XmlRel]]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(**dict(rels=rels), **extra_attributes)
        self._content.extend(order_xml_content([], self.rels))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlRels:
        """
        Parses a `<rels>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "rels")
        content = xml_content(node, {"rel": XmlRel})
        model = build_xml_model(
            cls,
            dict(
                rels=xml_content_items(content, (XmlRel,), optional=True),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlRels:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlRels:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlRels:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlRels:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlRels:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    def append(self, child: XmlRel) -> XmlRels:
        """
        Appends a child element and returns this element for chaining.
        """
        append_xml_child(self, "rels", child)
        return self

    def rel(
        self,
        *,
        inferred: typing.Optional[str] = None,
        trust: typing.Optional[str] = None,
        inferenceprovenance: typing.Optional[str] = None,
        provenanceaction: typing.Optional[str] = None,
        to: typing.Optional[XmlRelTo] = None,
        legalname: typing.Optional[str] = None,
        country: typing.Optional[XmlCountry] = None,
        legalshortname: typing.Optional[str] = None,
        websiteurl: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> XmlRel:
        """
        Appends a `<rel>` child element and returns it.

        Parameters
        ----------
        inferred : typing.Optional[str]

        trust : typing.Optional[str]

        inferenceprovenance : typing.Optional[str]

        provenanceaction : typing.Optional[str]

        to : typing.Optional[XmlRelTo]

        legalname : typing.Optional[str]

        country : typing.Optional[XmlCountry]

        legalshortname : typing.Optional[str]

        websiteurl : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = XmlRel(
            inferred=inferred,
            trust=trust,
            inferenceprovenance=inferenceprovenance,
            provenanceaction=provenanceaction,
            to=to,
            legalname=legalname,
            country=country,
            legalshortname=legalshortname,
            websiteurl=websiteurl,
            **extra_attributes,
        )
        append_xml_child(self, "rels", child)
        return child

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
