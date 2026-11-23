

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
    append_xml_child,
    build_xml_model,
    check_xml_extra_attributes,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_child,
    xml_content,
    xml_content_items,
)
from .alert_atom_entry import AlertAtomEntry


class AlertAtomFeed(UniversalBaseModel):
    """
    An alert feed in Atom format
    """

    id: typing.Optional[str] = None
    entry: typing.Optional[typing.List[AlertAtomEntry]] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<feed>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="feed",
            namespace="http://www.w3.org/2005/Atom",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="id", value=self.id),
            ],
            content=order_xml_content(self._content, self.entry),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        entry: typing.Optional[typing.List[AlertAtomEntry]] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        entry : typing.Optional[typing.List[AlertAtomEntry]]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(**check_xml_extra_attributes(type(self), {}, dict(id=id, entry=entry), extra_attributes))
        self._content.extend(order_xml_content([], self.entry))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> AlertAtomFeed:
        """
        Parses a `<feed>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "feed")
        content = xml_content(node, {"entry": AlertAtomEntry}, skip={"id"})
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"id": str}),
                entry=xml_content_items(content, (AlertAtomEntry,), optional=True),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> AlertAtomFeed:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> AlertAtomFeed:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> AlertAtomFeed:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> AlertAtomFeed:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> AlertAtomFeed:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    def append(self, child: AlertAtomEntry) -> AlertAtomFeed:
        """
        Appends a child element and returns this element for chaining.
        """
        append_xml_child(self, "entry", child)
        return self

    def add_entry(
        self, *, id: typing.Optional[str] = None, event: typing.Optional[str] = None, **extra_attributes: str
    ) -> AlertAtomEntry:
        """
        Appends a `<entry>` child element and returns it.

        An alert entry in an Atom feed

        Parameters
        ----------
        id : typing.Optional[str]

        event : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = AlertAtomEntry(id=id, event=event, geocode=None, parameter=None, **extra_attributes)
        append_xml_child(self, "entry", child)
        return child

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
