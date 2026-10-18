

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


class User(UniversalBaseModel):
    id: typing.Optional[int] = None
    username: typing.Optional[str] = None
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    email: typing.Optional[str] = None
    password: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    user_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="userStatus"),
        pydantic.Field(alias="userStatus", description="User Status"),
    ] = None
    """
    User Status
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<user>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="user",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="id", value=self.id),
                XmlChild(name="username", value=self.username),
                XmlChild(name="firstName", value=self.first_name),
                XmlChild(name="lastName", value=self.last_name),
                XmlChild(name="email", value=self.email),
                XmlChild(name="password", value=self.password),
                XmlChild(name="phone", value=self.phone),
                XmlChild(name="userStatus", value=self.user_status),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> User:
        """
        Parses a `<user>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "user")
        content = xml_content(
            node, {}, skip={"id", "username", "firstName", "lastName", "email", "password", "phone", "userStatus"}
        )
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"id": str}),
                username=xml_child(node, {"username": str}),
                first_name=xml_child(node, {"firstName": str}),
                last_name=xml_child(node, {"lastName": str}),
                email=xml_child(node, {"email": str}),
                password=xml_child(node, {"password": str}),
                phone=xml_child(node, {"phone": str}),
                user_status=xml_child(node, {"userStatus": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> User:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> User:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> User:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> User:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> User:
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
