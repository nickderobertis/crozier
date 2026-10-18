

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


class CloudFrontOriginAccessIdentitySummaryListItem(UniversalBaseModel):
    """
    Summary of the information about a CloudFront origin access identity.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>."
        ),
    ]
    """
    The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>.
    """

    s3canonical_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="S3CanonicalUserId"),
        pydantic.Field(
            alias="S3CanonicalUserId",
            description="The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.",
        ),
    ]
    """
    The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment",
            description="The comment for this origin access identity, as originally specified when created.",
        ),
    ]
    """
    The comment for this origin access identity, as originally specified when created.
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<CloudFrontOriginAccessIdentitySummary>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="CloudFrontOriginAccessIdentitySummary",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="Id", value=self.id),
                XmlChild(name="S3CanonicalUserId", value=self.s3canonical_user_id),
                XmlChild(name="Comment", value=self.comment),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> CloudFrontOriginAccessIdentitySummaryListItem:
        """
        Parses a `<CloudFrontOriginAccessIdentitySummary>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "CloudFrontOriginAccessIdentitySummary")
        content = xml_content(node, {}, skip={"Id", "S3CanonicalUserId", "Comment"})
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"Id": str}),
                s3canonical_user_id=xml_child(node, {"S3CanonicalUserId": str}),
                comment=xml_child(node, {"Comment": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> CloudFrontOriginAccessIdentitySummaryListItem:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> CloudFrontOriginAccessIdentitySummaryListItem:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> CloudFrontOriginAccessIdentitySummaryListItem:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> CloudFrontOriginAccessIdentitySummaryListItem:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> CloudFrontOriginAccessIdentitySummaryListItem:
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
