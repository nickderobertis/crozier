

from __future__ import annotations

import datetime as dt
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
from .order_status import OrderStatus


class Order(UniversalBaseModel):
    id: typing.Optional[int] = None
    pet_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="petId"), pydantic.Field(alias="petId")
    ] = None
    quantity: typing.Optional[int] = None
    ship_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="shipDate"), pydantic.Field(alias="shipDate")
    ] = None
    status: typing.Optional[OrderStatus] = pydantic.Field(default=None)
    """
    Order Status
    """

    complete: typing.Optional[bool] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<order>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="order",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="id", value=self.id),
                XmlChild(name="petId", value=self.pet_id),
                XmlChild(name="quantity", value=self.quantity),
                XmlChild(name="shipDate", value=self.ship_date),
                XmlChild(name="status", value=self.status),
                XmlChild(name="complete", value=self.complete),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> Order:
        """
        Parses a `<order>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "order")
        content = xml_content(node, {}, skip={"id", "petId", "quantity", "shipDate", "status", "complete"})
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"id": str}),
                pet_id=xml_child(node, {"petId": str}),
                quantity=xml_child(node, {"quantity": str}),
                ship_date=xml_child(node, {"shipDate": str}),
                status=xml_child(node, {"status": str}),
                complete=xml_child(node, {"complete": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> Order:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> Order:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> Order:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> Order:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> Order:
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
