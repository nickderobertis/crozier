

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .location import Location
from .node_type import NodeType


class XhtmlNode(UniversalBaseModel):
    location: typing.Optional[Location] = None
    node_type: typing_extensions.Annotated[
        typing.Optional[NodeType], FieldMetadata(alias="nodeType"), pydantic.Field(alias="nodeType")
    ] = None
    name: typing.Optional[str] = None
    attributes: typing.Optional[typing.Dict[str, str]] = None
    child_nodes: typing_extensions.Annotated[
        typing.Optional["XhtmlNodeList"], FieldMetadata(alias="childNodes"), pydantic.Field(alias="childNodes")
    ] = None
    content: typing.Optional[str] = None
    not_pretty: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="notPretty"), pydantic.Field(alias="notPretty")
    ] = None
    seperated: typing.Optional[bool] = None
    empty_expanded: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="emptyExpanded"), pydantic.Field(alias="emptyExpanded")
    ] = None
    named_params: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, "XhtmlNode"]],
        FieldMetadata(alias="namedParams"),
        pydantic.Field(alias="namedParams"),
    ] = None
    named_param_values: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="namedParamValues"),
        pydantic.Field(alias="namedParamValues"),
    ] = None
    user_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="userData"), pydantic.Field(alias="userData")
    ] = None
    first_element: typing_extensions.Annotated[
        typing.Optional["XhtmlNode"], FieldMetadata(alias="firstElement"), pydantic.Field(alias="firstElement")
    ] = None
    empty: typing.Optional[bool] = None
    ns_decl: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nsDecl"), pydantic.Field(alias="nsDecl")
    ] = None
    value_as_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="valueAsString"), pydantic.Field(alias="valueAsString")
    ] = None
    value: typing.Optional[str] = None
    format_comments_pre: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPre"),
        pydantic.Field(alias="formatCommentsPre"),
    ] = None
    format_comments_post: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="formatCommentsPost"),
        pydantic.Field(alias="formatCommentsPost"),
    ] = None
    no_pretty: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="noPretty"), pydantic.Field(alias="noPretty")
    ] = None
    para: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .xhtml_node_list import XhtmlNodeList

update_forward_refs(XhtmlNode, XhtmlNodeList=XhtmlNodeList)
