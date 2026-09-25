

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonCustomProfileFieldCustomProfileField(UniversalBaseModel):
    """
    Object containing details about the custom
    profile data change.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the custom profile field which user updated.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's personal value for this custom profile field,
    or `null` if unset.
    """

    rendered_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `value` rendered in HTML. Will only be present for
    custom profile field types that support Markdown rendering.
    
    This user-generated HTML content should be rendered
    using the same CSS and client-side security protections
    as are used for message content.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
