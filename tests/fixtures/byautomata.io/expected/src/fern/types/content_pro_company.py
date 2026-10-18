

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
    build_xml_model,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_child,
    xml_content,
)


class ContentProCompany(UniversalBaseModel):
    company_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ] = None
    description: typing.Optional[str] = None
    employee: typing.Optional[str] = None
    industry: typing.Optional[str] = None
    linkedin: typing.Optional[str] = None
    twitter: typing.Optional[str] = None
    website: typing.Optional[str] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<Order>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="Order",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="companyName", value=self.company_name),
                XmlChild(name="description", value=self.description),
                XmlChild(name="employee", value=self.employee),
                XmlChild(name="industry", value=self.industry),
                XmlChild(name="linkedin", value=self.linkedin),
                XmlChild(name="twitter", value=self.twitter),
                XmlChild(name="website", value=self.website),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> ContentProCompany:
        """
        Parses a `<Order>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "Order")
        content = xml_content(
            node, {}, skip={"companyName", "description", "employee", "industry", "linkedin", "twitter", "website"}
        )
        model = build_xml_model(
            cls,
            dict(
                company_name=xml_child(node, {"companyName": str}),
                description=xml_child(node, {"description": str}),
                employee=xml_child(node, {"employee": str}),
                industry=xml_child(node, {"industry": str}),
                linkedin=xml_child(node, {"linkedin": str}),
                twitter=xml_child(node, {"twitter": str}),
                website=xml_child(node, {"website": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> ContentProCompany:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> ContentProCompany:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> ContentProCompany:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> ContentProCompany:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> ContentProCompany:
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
