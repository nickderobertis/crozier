

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
from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags import (
    CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags,
)


class CreateStreamingDistributionWithTagsRequest(UniversalBaseModel):
    """
    The request to create a new streaming distribution with tags.
    """

    streaming_distribution_config_with_tags: typing_extensions.Annotated[
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags,
        FieldMetadata(alias="StreamingDistributionConfigWithTags"),
        pydantic.Field(
            alias="StreamingDistributionConfigWithTags",
            description=" The streaming distribution's configuration information. ",
        ),
    ]
    """
     The streaming distribution's configuration information. 
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<CreateStreamingDistributionWithTagsRequest>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="CreateStreamingDistributionWithTagsRequest",
            namespace="http://cloudfront.amazonaws.com/doc/2016-11-25/",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(
                    name="StreamingDistributionConfigWithTags", value=self.streaming_distribution_config_with_tags
                ),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> CreateStreamingDistributionWithTagsRequest:
        """
        Parses a `<CreateStreamingDistributionWithTagsRequest>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "CreateStreamingDistributionWithTagsRequest")
        content = xml_content(node, {}, skip={"StreamingDistributionConfigWithTags"})
        model = build_xml_model(
            cls,
            dict(
                streaming_distribution_config_with_tags=xml_child(node, {"StreamingDistributionConfigWithTags": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> CreateStreamingDistributionWithTagsRequest:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> CreateStreamingDistributionWithTagsRequest:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> CreateStreamingDistributionWithTagsRequest:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> CreateStreamingDistributionWithTagsRequest:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> CreateStreamingDistributionWithTagsRequest:
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
