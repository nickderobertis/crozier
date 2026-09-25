

EmojiCode = str
"""
A unique identifier, defining the specific emoji codepoint requested,
within the namespace of the `reaction_type`.

For most API clients, you won't need this, but it's important
for Zulip apps to handle rare corner cases when
adding/removing votes on an emoji reaction added previously by
another user.

If the existing reaction was added when the Zulip server was
using a previous version of the emoji data mapping between
Unicode codepoints and human-readable names, sending the
`emoji_code` in the data for the original reaction allows the
Zulip server to correctly interpret your upvote as an upvote
rather than a reaction with a "different" emoji.
"""
