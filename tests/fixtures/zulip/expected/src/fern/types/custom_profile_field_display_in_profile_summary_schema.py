

CustomProfileFieldDisplayInProfileSummarySchema = bool
"""
Whether clients should display this profile field in the summary section of a
user's profile (or in a more easily accessible "small profile").

At most 2 profile fields may have this property be true in a given
organization.

The "Users" profile field is not supported, but that is likely to
be temporary.

**Changes**: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.

New in Zulip 6.0 (feature level 146).
"""
