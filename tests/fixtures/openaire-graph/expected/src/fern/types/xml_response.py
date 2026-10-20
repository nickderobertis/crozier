

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
from .xml_header import XmlHeader
from .xml_results import XmlResults


class XmlResponse(UniversalBaseModel):
    header: typing.Optional[XmlHeader] = None
    results: typing.Optional[XmlResults] = None
    browse_results: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="browseResults"), pydantic.Field(alias="browseResults")
    ] = None
    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<response>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="response",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="browseResults", value=self.browse_results),
            ],
            content=order_xml_content(self._content, self.header, self.results),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    def __init__(
        self,
        *,
        header: typing.Optional[XmlHeader] = None,
        results: typing.Optional[XmlResults] = None,
        browse_results: typing.Optional[str] = None,
        **extra_attributes: str,
    ) -> None:
        """
        Parameters
        ----------
        header : typing.Optional[XmlHeader]

        results : typing.Optional[XmlResults]

        browse_results : typing.Optional[str]

        **extra_attributes : str
            Additional XML attributes not declared in the API definition.
        """
        super().__init__(**dict(header=header, results=results, browse_results=browse_results), **extra_attributes)
        self._content.extend(order_xml_content([], self.header, self.results))

    @classmethod
    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> XmlResponse:
        """
        Parses a `<response>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "response")
        content = xml_content(node, {"header": XmlHeader, "results": XmlResults}, skip={"browseResults"})
        model = build_xml_model(
            cls,
            dict(
                header=xml_content_item(content, (XmlHeader,)),
                results=xml_content_item(content, (XmlResults,)),
                browse_results=xml_child(node, {"browseResults": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> XmlResponse:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> XmlResponse:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> XmlResponse:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> XmlResponse:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> XmlResponse:
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
