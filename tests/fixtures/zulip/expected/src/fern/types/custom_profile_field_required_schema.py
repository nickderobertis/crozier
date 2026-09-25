

CustomProfileFieldRequiredSchema = bool
"""
Whether an organization administrator has configured this profile field as
required.

Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.

**Changes**: New in Zulip 9.0 (feature level 244).
"""
