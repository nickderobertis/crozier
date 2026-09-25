

import typing

IgnoredParametersUnsupported = typing.List[str]
"""
An array of any parameters sent in the request that are not
supported by the endpoint.

See [error handling](/api/rest-error-handling#ignored-parameters) documentation
for details on this and its change history.
"""
