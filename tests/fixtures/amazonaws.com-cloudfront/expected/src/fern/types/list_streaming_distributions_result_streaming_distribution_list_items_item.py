

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
from .list_streaming_distributions_result_streaming_distribution_list_items_item_aliases import (
    ListStreamingDistributionsResultStreamingDistributionListItemsItemAliases,
)
from .list_streaming_distributions_result_streaming_distribution_list_items_item_s3origin import (
    ListStreamingDistributionsResultStreamingDistributionListItemsItemS3Origin,
)
from .list_streaming_distributions_result_streaming_distribution_list_items_item_trusted_signers import (
    ListStreamingDistributionsResultStreamingDistributionListItemsItemTrustedSigners,
)
from .price_class import PriceClass


class ListStreamingDistributionsResultStreamingDistributionListItemsItem(UniversalBaseModel):
    """
    A summary of the information for an Amazon CloudFront streaming distribution.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>."
        ),
    ]
    """
    The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>.
    """

    arn: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ARN"),
        pydantic.Field(
            alias="ARN",
            description=" The ARN (Amazon Resource Name) for the streaming distribution. For example: <code>arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your AWS account ID.",
        ),
    ]
    """
     The ARN (Amazon Resource Name) for the streaming distribution. For example: <code>arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your AWS account ID.
    """

    status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description=" Indicates the current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is fully propagated throughout the Amazon CloudFront system.",
        ),
    ]
    """
     Indicates the current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is fully propagated throughout the Amazon CloudFront system.
    """

    last_modified_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="LastModifiedTime"),
        pydantic.Field(alias="LastModifiedTime", description="The date and time the distribution was last modified."),
    ]
    """
    The date and time the distribution was last modified.
    """

    domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DomainName"),
        pydantic.Field(
            alias="DomainName",
            description="The domain name corresponding to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>.",
        ),
    ]
    """
    The domain name corresponding to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>.
    """

    s3origin: typing_extensions.Annotated[
        ListStreamingDistributionsResultStreamingDistributionListItemsItemS3Origin,
        FieldMetadata(alias="S3Origin"),
        pydantic.Field(
            alias="S3Origin",
            description="A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.",
        ),
    ]
    """
    A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
    """

    aliases: typing_extensions.Annotated[
        ListStreamingDistributionsResultStreamingDistributionListItemsItemAliases,
        FieldMetadata(alias="Aliases"),
        pydantic.Field(
            alias="Aliases",
            description="A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.",
        ),
    ]
    """
    A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.
    """

    trusted_signers: typing_extensions.Annotated[
        ListStreamingDistributionsResultStreamingDistributionListItemsItemTrustedSigners,
        FieldMetadata(alias="TrustedSigners"),
        pydantic.Field(
            alias="TrustedSigners",
            description="A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the <code>PathPattern</code> for this cache behavior, specify <code>true</code> for <code>Enabled</code>, and specify the applicable values for <code>Quantity</code> and <code>Items</code>.If you don't want to require signed URLs in requests for objects that match <code>PathPattern</code>, specify <code>false</code> for <code>Enabled</code> and <code>0</code> for <code>Quantity</code>. Omit <code>Items</code>. To add, change, or remove one or more trusted signers, change <code>Enabled</code> to <code>true</code> (if it's currently <code>false</code>), change <code>Quantity</code> as applicable, and specify all of the trusted signers that you want to include in the updated distribution.",
        ),
    ]
    """
    A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the <code>PathPattern</code> for this cache behavior, specify <code>true</code> for <code>Enabled</code>, and specify the applicable values for <code>Quantity</code> and <code>Items</code>.If you don't want to require signed URLs in requests for objects that match <code>PathPattern</code>, specify <code>false</code> for <code>Enabled</code> and <code>0</code> for <code>Quantity</code>. Omit <code>Items</code>. To add, change, or remove one or more trusted signers, change <code>Enabled</code> to <code>true</code> (if it's currently <code>false</code>), change <code>Quantity</code> as applicable, and specify all of the trusted signers that you want to include in the updated distribution.
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment", description="The comment originally specified when this distribution was created."
        ),
    ]
    """
    The comment originally specified when this distribution was created.
    """

    price_class: typing_extensions.Annotated[
        PriceClass, FieldMetadata(alias="PriceClass"), pydantic.Field(alias="PriceClass")
    ]
    enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Enabled"),
        pydantic.Field(
            alias="Enabled", description="Whether the distribution is enabled to accept end user requests for content."
        ),
    ]
    """
    Whether the distribution is enabled to accept end user requests for content.
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<StreamingDistributionSummary>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="StreamingDistributionSummary",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="Id", value=self.id),
                XmlChild(name="ARN", value=self.arn),
                XmlChild(name="Status", value=self.status),
                XmlChild(name="LastModifiedTime", value=self.last_modified_time),
                XmlChild(name="DomainName", value=self.domain_name),
                XmlChild(name="S3Origin", value=self.s3origin),
                XmlChild(name="Aliases", value=self.aliases),
                XmlChild(name="TrustedSigners", value=self.trusted_signers),
                XmlChild(name="Comment", value=self.comment),
                XmlChild(name="PriceClass", value=self.price_class),
                XmlChild(name="Enabled", value=self.enabled),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(
        cls, xml: typing.Union[str, XmlNode]
    ) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
        """
        Parses a `<StreamingDistributionSummary>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "StreamingDistributionSummary")
        content = xml_content(
            node,
            {},
            skip={
                "Id",
                "ARN",
                "Status",
                "LastModifiedTime",
                "DomainName",
                "S3Origin",
                "Aliases",
                "TrustedSigners",
                "Comment",
                "PriceClass",
                "Enabled",
            },
        )
        model = build_xml_model(
            cls,
            dict(
                id=xml_child(node, {"Id": str}),
                arn=xml_child(node, {"ARN": str}),
                status=xml_child(node, {"Status": str}),
                last_modified_time=xml_child(node, {"LastModifiedTime": str}),
                domain_name=xml_child(node, {"DomainName": str}),
                s3origin=xml_child(node, {"S3Origin": str}),
                aliases=xml_child(node, {"Aliases": str}),
                trusted_signers=xml_child(node, {"TrustedSigners": str}),
                comment=xml_child(node, {"Comment": str}),
                price_class=xml_child(node, {"PriceClass": str}),
                enabled=xml_child(node, {"Enabled": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> ListStreamingDistributionsResultStreamingDistributionListItemsItem:
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
