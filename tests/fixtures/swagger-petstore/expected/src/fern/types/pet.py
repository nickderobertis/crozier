

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
)
from .category import Category
from .pet_status import PetStatus
from .tag import Tag


class Pet(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: str
    category: typing.Optional[Category] = None
    photo_urls: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="photoUrls"), pydantic.Field(alias="photoUrls")
    ]
    tags: typing.Optional[typing.List[Tag]] = None
    status: typing.Optional[PetStatus] = pydantic.Field(default=None)
    """
    pet status in the store
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<pet>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="pet",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="id", value=self.id),
                XmlChild(name="name", value=self.name),
                XmlChild(name="photoUrls", value=self.photo_urls, wrapped=True),
                XmlChild(name="tags", value=self.tags, wrapped=True),
                XmlChild(name="status", value=self.status),
            ],
            content=order_xml_content(self._content, self.category),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        id: typing.Optional[int] = None,
        name: str,
        category: typing.Optional[Category] = None,
        photo_urls: typing.List[str],
        tags: typing.Optional[typing.List[Tag]] = None,
        status: typing.Optional[PetStatus] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        id : typing.Optional[int]

        name : str

        category : typing.Optional[Category]

        photo_urls : typing.List[str]

        tags : typing.Optional[typing.List[Tag]]

        status : typing.Optional[PetStatus]
            pet status in the store

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(id=id, name=name, category=category, photo_urls=photo_urls, tags=tags, status=status),
            **extra_attributes,
        )
        self._content.extend(order_xml_content([], self.category))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> Pet:
        """
        Parses a `<pet>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "pet")
        content = xml_content(
            node,
            {"category": Category},
            skip={"id", "name", "status"},
            wrappers={"photoUrls": {"photoUrls"}, "tags": {"tag"}},
        )
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"id": str}),
                name=xml_child(node, {"name": str}),
                category=xml_content_item(content, (Category,)),
                photo_urls=xml_children(node, {"photoUrls": str}, wrapper="photoUrls"),
                tags=xml_children(node, {"tag": Tag}, wrapper="tags", optional=True),
                status=xml_child(node, {"status": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> Pet:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> Pet:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> Pet:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> Pet:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> Pet:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    def tag(
        self, *, id: typing.Optional[int] = None, name: typing.Optional[str] = None, **extra_attributes: str
    ) -> Tag:
        """
        Appends a `<tag>` child element and returns it.

        Parameters
        ----------
        id : typing.Optional[int]

        name : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        child = Tag(id=id, name=name, **extra_attributes)
        append_xml_child(self, "tags", child, inline=False)
        return child

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
