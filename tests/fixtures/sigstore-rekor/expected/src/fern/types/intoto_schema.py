

import typing

from .intoto_schema_one import IntotoSchemaOne
from .intoto_schema_public_key import IntotoSchemaPublicKey

IntotoSchema = typing.Union[IntotoSchemaPublicKey, IntotoSchemaOne]
