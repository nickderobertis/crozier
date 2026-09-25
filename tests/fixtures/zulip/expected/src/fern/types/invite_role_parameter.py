

InviteRoleParameter = int
"""
The [organization-level role](/api/roles-and-permissions) of the user that is
created when the invitation is accepted.
Possible values are:

- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest

Users can only create invitation links for
[roles with equal or stricter restrictions](/api/roles-and-permissions#permission-levels)
as their own. For example, a moderator cannot invite someone to be an owner
or administrator, but they can invite them to be a moderator or member.

**Changes**: In Zulip 4.0 (feature level 61), added support for inviting
users as moderators.
"""
