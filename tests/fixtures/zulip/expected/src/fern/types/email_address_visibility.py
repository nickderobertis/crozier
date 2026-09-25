

EmailAddressVisibility = int
"""
The [policy][permission-level] for [which other users][help-email-visibility]
in this organization can see the user's real email address.

- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only

**Changes**: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.

[permission-level]: /api/roles-and-permissions#permission-levels
[help-email-visibility]: /help/configure-email-visibility
"""
