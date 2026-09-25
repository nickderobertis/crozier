

ReactionType = str
"""
A string indicating the type of emoji. Each emoji `reaction_type`
has an independent namespace for values of `emoji_code`.

If an API client is adding/removing a vote on an existing reaction,
it should pass this parameter using the value the server provided
for the existing reaction for specificity. Supported values:

- `unicode_emoji` : In this namespace, `emoji_code` will be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.

- `realm_emoji` : In this namespace, `emoji_code` will be the ID of
  the uploaded [custom emoji](/help/custom-emoji).

- `zulip_extra_emoji` : These are special emoji included with Zulip.
  In this namespace, `emoji_code` will be the name of the emoji (e.g.
  "zulip").

**Changes**: In Zulip 3.0 (feature level 2), this parameter became
optional for [custom emoji](/help/custom-emoji);
previously, this endpoint assumed `unicode_emoji` if this
parameter was not specified.
"""
