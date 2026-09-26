

import typing

EventTypes = typing.List[str]
"""
A JSON-encoded array indicating which types of events you're interested
in. Values that you might find useful include:

- **message** (messages)
- **subscription** (changes in your subscriptions)
- **realm_user** (changes to users in the organization and
  their properties, such as their name).

If you do not specify this parameter, you will receive all
events, and have to filter out the events not relevant to
your client in your client code. For most applications, one
is only interested in messages, so one specifies:
`"event_types": ["message"]`

Event types not supported by the server are ignored, in order to simplify
the implementation of client apps that support multiple server versions.
"""
