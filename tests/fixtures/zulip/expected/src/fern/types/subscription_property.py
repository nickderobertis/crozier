

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionProperty(enum.StrEnum):
    """
    One of the channel properties described below:

    - `"color"`: The hex value of the user's display color for the channel.

    - `"is_muted"`: Whether the channel is [muted](/help/mute-a-channel).<br>
      **Changes**: As of Zulip 6.0 (feature level 139), updating either
      `"is_muted"` or `"in_home_view"` generates two [subscription update
      events](/api/get-events#subscription-update), one for each property,
      that are sent to clients. Prior to this feature level, updating either
      property only generated a subscription update event for
      `"in_home_view"`. <br>
      Prior to Zulip 2.1.0, this feature was represented
      by the more confusingly named `"in_home_view"` (with the
      opposite value: `in_home_view=!is_muted`); for
      backwards-compatibility, modern Zulip still accepts that property.

    - `"pin_to_top"`: Whether to pin the channel at the top of the channel list.

    - `"desktop_notifications"`: Whether to show desktop notifications
      for all messages sent to the channel.

    - `"audible_notifications"`: Whether to play a sound
      notification for all messages sent to the channel.

    - `"push_notifications"`: Whether to trigger a mobile push
      notification for all messages sent to the channel.

    - `"email_notifications"`: Whether to trigger an email
      notification for all messages sent to the channel.

    - `"wildcard_mentions_notify"`: Whether wildcard mentions trigger
      notifications as though they were personal mentions in this channel.
    """

    COLOR = "color"
    IS_MUTED = "is_muted"
    IN_HOME_VIEW = "in_home_view"
    PIN_TO_TOP = "pin_to_top"
    DESKTOP_NOTIFICATIONS = "desktop_notifications"
    AUDIBLE_NOTIFICATIONS = "audible_notifications"
    PUSH_NOTIFICATIONS = "push_notifications"
    EMAIL_NOTIFICATIONS = "email_notifications"
    WILDCARD_MENTIONS_NOTIFY = "wildcard_mentions_notify"

    def visit(
        self,
        color: typing.Callable[[], T_Result],
        is_muted: typing.Callable[[], T_Result],
        in_home_view: typing.Callable[[], T_Result],
        pin_to_top: typing.Callable[[], T_Result],
        desktop_notifications: typing.Callable[[], T_Result],
        audible_notifications: typing.Callable[[], T_Result],
        push_notifications: typing.Callable[[], T_Result],
        email_notifications: typing.Callable[[], T_Result],
        wildcard_mentions_notify: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionProperty.COLOR:
            return color()
        if self is SubscriptionProperty.IS_MUTED:
            return is_muted()
        if self is SubscriptionProperty.IN_HOME_VIEW:
            return in_home_view()
        if self is SubscriptionProperty.PIN_TO_TOP:
            return pin_to_top()
        if self is SubscriptionProperty.DESKTOP_NOTIFICATIONS:
            return desktop_notifications()
        if self is SubscriptionProperty.AUDIBLE_NOTIFICATIONS:
            return audible_notifications()
        if self is SubscriptionProperty.PUSH_NOTIFICATIONS:
            return push_notifications()
        if self is SubscriptionProperty.EMAIL_NOTIFICATIONS:
            return email_notifications()
        if self is SubscriptionProperty.WILDCARD_MENTIONS_NOTIFY:
            return wildcard_mentions_notify()
