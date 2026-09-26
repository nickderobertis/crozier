

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_resolve_topics_group_new import UpdateStreamRequestCanResolveTopicsGroupNew
from .update_stream_request_can_resolve_topics_group_old import UpdateStreamRequestCanResolveTopicsGroupOld


class UpdateStreamRequestCanResolveTopicsGroup(UniversalBaseModel):
    """
    The set of users who have permission to resolve topics in this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Users who have similar realm-level permissions can resolve topics
    in a channel regardless of the value of this setting.

    **Changes**: New in Zulip 11.0 (feature level 402).
    """

    new: UpdateStreamRequestCanResolveTopicsGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanResolveTopicsGroupOld] = pydantic.Field(default=None)
    """
    The expected current [group-setting value](/api/group-setting-values)
    for who has this permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
