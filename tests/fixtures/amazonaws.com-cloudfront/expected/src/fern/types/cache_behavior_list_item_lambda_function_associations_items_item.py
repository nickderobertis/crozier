

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
from .cache_behavior_list_item_lambda_function_associations_items_item_event_type import (
    CacheBehaviorListItemLambdaFunctionAssociationsItemsItemEventType,
)


class CacheBehaviorListItemLambdaFunctionAssociationsItemsItem(UniversalBaseModel):
    """
    A complex type that contains a Lambda function association.
    """

    lambda_function_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LambdaFunctionARN"),
        pydantic.Field(alias="LambdaFunctionARN", description="The ARN of the Lambda function."),
    ] = None
    """
    The ARN of the Lambda function.
    """

    event_type: typing_extensions.Annotated[
        typing.Optional[CacheBehaviorListItemLambdaFunctionAssociationsItemsItemEventType],
        FieldMetadata(alias="EventType"),
        pydantic.Field(
            alias="EventType",
            description="<p>Specifies the event type that triggers a Lambda function invocation. Valid values are:</p> <ul> <li> <p> <code>viewer-request</code> </p> </li> <li> <p> <code>origin-request</code> </p> </li> <li> <p> <code>viewer-response</code> </p> </li> <li> <p> <code>origin-response</code> </p> </li> </ul>",
        ),
    ] = None
    """
    <p>Specifies the event type that triggers a Lambda function invocation. Valid values are:</p> <ul> <li> <p> <code>viewer-request</code> </p> </li> <li> <p> <code>origin-request</code> </p> </li> <li> <p> <code>viewer-response</code> </p> </li> <li> <p> <code>origin-response</code> </p> </li> </ul>
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<LambdaFunctionAssociation>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="LambdaFunctionAssociation",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="LambdaFunctionARN", value=self.lambda_function_arn),
                XmlChild(name="EventType", value=self.event_type),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
        """
        Parses a `<LambdaFunctionAssociation>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "LambdaFunctionAssociation")
        content = xml_content(node, {}, skip={"LambdaFunctionARN", "EventType"})
        model = build_xml_model(
            cls,
            dict(
                lambda_function_arn=xml_child(node, {"LambdaFunctionARN": str}),
                event_type=xml_child(node, {"EventType": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> CacheBehaviorListItemLambdaFunctionAssociationsItemsItem:
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
