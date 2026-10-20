

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
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
    xml_content_item,
)
from .xml_metadata import XmlMetadata
from .xml_result_header import XmlResultHeader


class XmlResult(UniversalBaseModel):
    header: XmlResultHeader
    metadata: XmlMetadata
    xmlns_dri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xmlnsDri"), pydantic.Field(alias="xmlnsDri")
    ] = None
    xmlns_xsi: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="xmlnsXsi"), pydantic.Field(alias="xmlnsXsi")
    ] = None
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
                XmlAttribute(name="xmlns:dri", value=self.xmlns_dri),
                XmlAttribute(name="xmlns:xsi", value=self.xmlns_xsi),
                *extra_xml_attributes(self),
            ],
            children=[],
            content=order_xml_content(self._content, self.header, self.metadata),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        header: XmlResultHeader,
        metadata: XmlMetadata,
        xmlns_dri: typing.Optional[str] = None,
        xmlns_xsi: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        header : XmlResultHeader

        metadata : XmlMetadata

        xmlns_dri : typing.Optional[str]

        xmlns_xsi : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(header=header, metadata=metadata, xmlns_dri=xmlns_dri, xmlns_xsi=xmlns_xsi), **extra_attributes
        )
        self._content.extend(order_xml_content([], self.header, self.metadata))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlResult:
        """
        Parses a `<result>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "result")
        content = xml_content(node, {"header": XmlResultHeader, "metadata": XmlMetadata})
        model = build_xml_model(
            cls,
            dict(
                header=xml_content_item(content, (XmlResultHeader,)),
                metadata=xml_content_item(content, (XmlMetadata,)),
                xmlns_dri=xml_attribute(node, "xmlns:dri"),
                xmlns_xsi=xml_attribute(node, "xmlns:xsi"),
            ),
            node,
            {"xmlns:dri", "xmlns:xsi"},
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlResult:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlResult:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlResult:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlResult:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlResult:
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
