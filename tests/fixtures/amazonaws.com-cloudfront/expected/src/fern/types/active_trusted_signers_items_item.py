

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
from .active_trusted_signers_items_item_key_pair_ids import ActiveTrustedSignersItemsItemKeyPairIds


class ActiveTrustedSignersItemsItem(UniversalBaseModel):
    """
    A complex type that lists the AWS accounts that were included in the <code>TrustedSigners</code> complex type, as well as their active CloudFront key pair IDs, if any.
    """

    aws_account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AwsAccountNumber"),
        pydantic.Field(
            alias="AwsAccountNumber",
            description="<p>An AWS account that is included in the <code>TrustedSigners</code> complex type for this RTMP distribution. Valid values include:</p> <ul> <li> <p> <code>self</code>, which is the AWS account used to create the distribution.</p> </li> <li> <p>An AWS account number.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>An AWS account that is included in the <code>TrustedSigners</code> complex type for this RTMP distribution. Valid values include:</p> <ul> <li> <p> <code>self</code>, which is the AWS account used to create the distribution.</p> </li> <li> <p>An AWS account number.</p> </li> </ul>
    """

    key_pair_ids: typing_extensions.Annotated[
        typing.Optional[ActiveTrustedSignersItemsItemKeyPairIds],
        FieldMetadata(alias="KeyPairIds"),
        pydantic.Field(
            alias="KeyPairIds",
            description="A complex type that lists the active CloudFront key pairs, if any, that are associated with <code>AwsAccountNumber</code>.",
        ),
    ] = None
    """
    A complex type that lists the active CloudFront key pairs, if any, that are associated with <code>AwsAccountNumber</code>.
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<Signer>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="Signer",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="AwsAccountNumber", value=self.aws_account_number),
                XmlChild(name="KeyPairIds", value=self.key_pair_ids),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> ActiveTrustedSignersItemsItem:
        """
        Parses a `<Signer>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "Signer")
        content = xml_content(node, {}, skip={"AwsAccountNumber", "KeyPairIds"})
        model = build_xml_model(
            cls,
            dict(
                aws_account_number=xml_child(node, {"AwsAccountNumber": str}),
                key_pair_ids=xml_child(node, {"KeyPairIds": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> ActiveTrustedSignersItemsItem:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> ActiveTrustedSignersItemsItem:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> ActiveTrustedSignersItemsItem:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> ActiveTrustedSignersItemsItem:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> ActiveTrustedSignersItemsItem:
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
