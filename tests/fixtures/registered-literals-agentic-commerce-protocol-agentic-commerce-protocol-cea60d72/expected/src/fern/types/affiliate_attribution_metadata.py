

import typing

from .affiliate_attribution_metadata_value import AffiliateAttributionMetadataValue

AffiliateAttributionMetadata = typing.Dict[str, AffiliateAttributionMetadataValue]
"""
Flat key/value map for additional non-sensitive context.
Keys must be strings; values must be strings, numbers, or booleans.
Arrays and nested objects are NOT permitted.
"""
