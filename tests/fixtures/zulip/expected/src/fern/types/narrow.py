

import typing

Narrow = typing.List[typing.List[str]]
"""
A JSON-encoded array of arrays of length 2 indicating the
[narrow filter(s)](/api/construct-narrow) for which you'd
like to receive events for.

For example, to receive events for direct messages (including
group direct messages) received by the user, one can use
`"narrow": [["is", "dm"]]`.

Unlike the API for [fetching messages](/api/get-messages),
this narrow parameter is simply a filter on messages that the
user receives through their channel subscriptions (or because
they are a recipient of a direct message).

This means that a client that requests a `narrow` filter of
`[["channel", "Denmark"]]` will receive events for new messages
sent to that channel while the user is subscribed to that
channel. The client will not receive any message events at all
if the user is not subscribed to `"Denmark"`.

Newly created bot users are not usually subscribed to any
channels, so bots using this API need to be
[subscribed](/api/subscribe) to any channels whose messages
you'd like them to process using this endpoint.

See the `all_public_streams` parameter for how to process all
public channel messages in an organization.

**Changes**: See [changes section](/api/construct-narrow#changes)
of search/narrow filter documentation.
"""
