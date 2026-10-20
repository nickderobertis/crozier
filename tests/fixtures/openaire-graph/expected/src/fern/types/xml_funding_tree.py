

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
    xml_content_item,
)
from .xml_funder import XmlFunder
from .xml_funding_level import XmlFundingLevel


class XmlFundingTree(UniversalBaseModel):
    funder: typing.Optional[XmlFunder] = None
    funding_level0: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel0"), pydantic.Field(alias="fundingLevel0")
    ] = None
    funding_level1: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel1"), pydantic.Field(alias="fundingLevel1")
    ] = None
    funding_level2: typing_extensions.Annotated[
        typing.Optional[XmlFundingLevel], FieldMetadata(alias="fundingLevel2"), pydantic.Field(alias="fundingLevel2")
    ] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<fundingtree>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="fundingtree",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="fundingLevel0", value=self.funding_level0),
                XmlChild(name="fundingLevel1", value=self.funding_level1),
                XmlChild(name="fundingLevel2", value=self.funding_level2),
            ],
            content=order_xml_content(self._content, self.funder),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        funder: typing.Optional[XmlFunder] = None,
        funding_level0: typing.Optional[XmlFundingLevel] = None,
        funding_level1: typing.Optional[XmlFundingLevel] = None,
        funding_level2: typing.Optional[XmlFundingLevel] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        funder : typing.Optional[XmlFunder]

        funding_level0 : typing.Optional[XmlFundingLevel]

        funding_level1 : typing.Optional[XmlFundingLevel]

        funding_level2 : typing.Optional[XmlFundingLevel]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(
            **dict(
                funder=funder,
                funding_level0=funding_level0,
                funding_level1=funding_level1,
                funding_level2=funding_level2,
            ),
            **extra_attributes,
        )
        self._content.extend(order_xml_content([], self.funder))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlFundingTree:
        """
        Parses a `<fundingtree>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "fundingtree")
        content = xml_content(node, {"funder": XmlFunder}, skip={"fundingLevel0", "fundingLevel1", "fundingLevel2"})
        model = build_xml_model(
            cls,
            dict(
                funder=xml_content_item(content, (XmlFunder,)),
                funding_level0=xml_child(node, {"fundingLevel0": str}),
                funding_level1=xml_child(node, {"fundingLevel1": str}),
                funding_level2=xml_child(node, {"fundingLevel2": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlFundingTree:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlFundingTree:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlFundingTree:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlFundingTree:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlFundingTree:
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
