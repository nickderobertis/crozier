

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GroupsV2GroupQuery(UniversalBaseModel):
    """
    NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes".
    If you are querying for a group, you can pass any of the properties below.
    If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):
    - groupMemberCountFilter - localeFilter - tagText
    If you pass these, you will get a useless InvalidParameters error.
    """

    creation_date: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="creationDate")] = None
    current_page: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="currentPage")] = None
    group_member_count_filter: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="groupMemberCountFilter")
    ] = None
    group_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="groupType")] = None
    items_per_page: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemsPerPage")] = None
    locale_filter: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="localeFilter")] = None
    name: typing.Optional[str] = None
    request_continuation_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="requestContinuationToken")
    ] = None
    sort_by: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sortBy")] = None
    tag_text: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tagText")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
