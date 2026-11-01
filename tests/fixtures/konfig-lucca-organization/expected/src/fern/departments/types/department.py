

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.user import User


class Department(UniversalBaseModel):
    """
    Departments, to which users must be attached, are used by the different Lucca solutions for different purposes:

    * Define access scopes: for example to restrict the visibility of absences in the Timmi Absences schedule.
    * Filtering data in a report: our different reports generally allow to filter data according to the legal entity, the SSC, but also the department of the user.
    * Build the organization chart in Poplee Core HR.
    The departments are represented as a hierarchical tree with a parent/child relationship.

    *NB:* You can have up to 9 levels of departments, and up to 99 departments under a single parent department. However, limiting the number of levels to 7 is recommended.
    """

    id: typing.Optional[int] = None
    name: str
    code: str
    hierarchy: typing.Optional[str] = pydantic.Field(default=None)
    """
    Position of the departement in the hierarchical tree
    """

    parent_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentId"),
        pydantic.Field(alias="parentId", description="Position of the parent department in the hierarchical tree"),
    ] = None
    """
    Position of the parent department in the hierarchical tree
    """

    is_active: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")
    ] = None
    position: typing.Optional[int] = pydantic.Field(default=None)
    """
    Department's general position in the hierarchy
    """

    level: typing.Optional[int] = pydantic.Field(default=None)
    """
    level of the Department. Deduce from Position.
    """

    sort_order: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(
            alias="sortOrder", description="Order of the current Department among the children of the Parent Department"
        ),
    ] = None
    """
    Order of the current Department among the children of the Parent Department
    """

    head_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="headID"),
        pydantic.Field(alias="headID", description="ID of the User who is the head of the department"),
    ] = None
    """
    ID of the User who is the head of the department
    """

    head: typing.Optional[User] = None
    users: typing.Optional[typing.List[User]] = pydantic.Field(default=None)
    """
    Users of the department, including inactive users.
    """

    current_users: typing_extensions.Annotated[
        typing.Optional[typing.List[User]],
        FieldMetadata(alias="currentUsers"),
        pydantic.Field(alias="currentUsers", description="Only active users of the department"),
    ] = None
    """
    Only active users of the department
    """

    current_users_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentUsersCount"),
        pydantic.Field(alias="currentUsersCount", description="Number of active users in the department"),
    ] = None
    """
    Number of active users in the department
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
