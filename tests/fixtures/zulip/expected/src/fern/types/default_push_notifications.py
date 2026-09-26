

DefaultPushNotifications = bool
"""
Whether mobile push notifications will be enabled by default when a
user first subscribes to this channel, potentially overriding the
user's [default mobile notification
setting](/help/channel-notifications#configure-default-notifications-for-all-channels)
for channel messages.

Because this default is applied only the first time a user
subscribes, unsubscribing and resubscribing a user does not reset
their preference to this channel default.

Only organization administrators can set or modify this value.

**Changes**: New in Zulip 13.0 (feature level 507).
"""
