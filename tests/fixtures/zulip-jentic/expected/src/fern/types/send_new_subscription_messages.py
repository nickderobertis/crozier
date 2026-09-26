

SendNewSubscriptionMessages = bool
"""
Whether any other users newly subscribed via this request should be
sent a direct message, from Notification Bot, notifying them about their
new subscription.

No direct messages are sent for any channels that are created as part of
this request, regardless of the value of this parameter.

The server will never send direct messages when the total number of users
who were subscribed to channels in this request was more than the value
of `max_bulk_new_subscription_messages`, which is available in the [`POST
/register`](/api/register-queue) response.

**Changes**: Before Zulip 11.0 (feature level 397), new subscribers
were always sent a Notification Bot direct message, which was unduly
expensive when bulk-subscribing thousands of users to a channel.
"""
