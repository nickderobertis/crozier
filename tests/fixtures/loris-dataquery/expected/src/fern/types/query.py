

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_object import QueryObject


class Query(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(
            alias="self",
            description="A URL that this query can be accessed at.\n\nAccessing the query directly through the URL is sure to have the same fields\nand criteria, but other details of the object returned may not be identical.\n\nFor instance, the starred and name properties may vary based on the user\naccessing the URI.",
        ),
    ] = None
    """
    A URL that this query can be accessed at.
    
    Accessing the query directly through the URL is sure to have the same fields
    and criteria, but other details of the object returned may not be identical.
    
    For instance, the starred and name properties may vary based on the user
    accessing the URI.
    """

    query: typing_extensions.Annotated[
        typing.Optional[QueryObject], FieldMetadata(alias="Query"), pydantic.Field(alias="Query")
    ] = None
    admin_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AdminName"),
        pydantic.Field(alias="AdminName", description="The name given by the admin for a pinned query"),
    ] = None
    """
    The name given by the admin for a pinned query
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name given by the current user for this query"),
    ] = None
    """
    The name given by the current user for this query
    """

    shared_by: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="SharedBy"), pydantic.Field(alias="SharedBy")
    ] = None
    starred: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Starred"),
        pydantic.Field(alias="Starred", description="The query has been starred by the user"),
    ] = None
    """
    The query has been starred by the user
    """

    public: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Public"),
        pydantic.Field(alias="Public", description="The query has been shared (made public to all users)"),
    ] = None
    """
    The query has been shared (made public to all users)
    """

    pinned: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Pinned"),
        pydantic.Field(alias="Pinned", description="The query has been pinned by an administrator"),
    ] = None
    """
    The query has been pinned by an administrator
    """

    query_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="QueryID"), pydantic.Field(alias="QueryID")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
