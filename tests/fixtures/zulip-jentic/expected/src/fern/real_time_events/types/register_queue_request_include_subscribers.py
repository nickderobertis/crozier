

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterQueueRequestIncludeSubscribers(enum.StrEnum):
    """
    Whether each returned channel object should include a `subscribers`
    field containing a list of the user IDs of its subscribers.

    Client apps supporting organizations with many thousands of users
    should not pass `true`, because the full subscriber matrix may be
    several megabytes of data. The `partial` value, combined with the
    `subscriber_count` and fetching subscribers for individual channels as
    needed, is recommended to support client app features where channel
    subscriber data is useful.

    If a client passes `partial` for this parameter, the server may,
    for some channels, return a subset of the channel's subscribers
    in the `partial_subscribers` field instead of the `subscribers` field,
    which always contains the complete set of subscribers.

    The server guarantees that it will always return a `subscribers`
    field for channels with fewer than 250 total subscribers. When
    returning a `partial_subscribers` field, the server guarantees
    that all bot users and users active within the last 14 days will
    be included. For other cases, the server may use its discretion
    to determine which channels and users to include, balancing between
    payload size and usefulness of the data provided to the client.

    Passing `true` in an [unauthenticated
    request](/help/public-access-option) is an error.

    **Changes**: The `partial` value is new in Zulip 11.0 (feature level 412).

    Before Zulip 6.0 (feature level 149), this parameter was silently
    ignored and processed as though it were `false` in unauthenticated
    requests.

    New in Zulip 2.1.0.
    """

    TRUE = "true"
    FALSE = "false"
    PARTIAL = "partial"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegisterQueueRequestIncludeSubscribers.TRUE:
            return true()
        if self is RegisterQueueRequestIncludeSubscribers.FALSE:
            return false()
        if self is RegisterQueueRequestIncludeSubscribers.PARTIAL:
            return partial()
