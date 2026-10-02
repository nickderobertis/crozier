

import typing

SupplierStatus = typing.Union[
    typing.Literal["active", "inactive", "archived", "gdpr-erasure-request", "unknown"], typing.Any
]
