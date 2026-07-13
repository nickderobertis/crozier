

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_membership import GroupsV2GroupMembership
from .queries_paged_query import QueriesPagedQuery


class GroupsV2GetGroupsForMemberResponse(UniversalBaseModel):
    are_all_memberships_inactive: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, bool]], FieldMetadata(alias="areAllMembershipsInactive")
    ] = pydantic.Field(default=None)
    """
    A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
     The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive.
    """

    has_more: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hasMore")] = None
    query: typing.Optional[QueriesPagedQuery] = None
    replacement_continuation_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="replacementContinuationToken")
    ] = None
    results: typing.Optional[typing.List[GroupsV2GroupMembership]] = None
    total_results: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="totalResults")] = None
    use_total_results: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="useTotalResults")] = (
        pydantic.Field(default=None)
    )
    """
    If useTotalResults is true, then totalResults represents an accurate count.
    If False, it does not, and may be estimated/only the size of the current page.
    Either way, you should probably always only trust hasMore.
    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
