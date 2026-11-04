

import typing

from .facet_filter_f32 import FacetFilterF32
from .facet_filter_f64 import FacetFilterF64
from .facet_filter_i8 import FacetFilterI8
from .facet_filter_i16 import FacetFilterI16
from .facet_filter_i32 import FacetFilterI32
from .facet_filter_i64 import FacetFilterI64
from .facet_filter_point import FacetFilterPoint
from .facet_filter_string16 import FacetFilterString16
from .facet_filter_string32 import FacetFilterString32
from .facet_filter_string_set16 import FacetFilterStringSet16
from .facet_filter_string_set32 import FacetFilterStringSet32
from .facet_filter_timestamp import FacetFilterTimestamp
from .facet_filter_u8 import FacetFilterU8
from .facet_filter_u16 import FacetFilterU16
from .facet_filter_u32 import FacetFilterU32
from .facet_filter_u64 import FacetFilterU64

FacetFilter = typing.Union[
    FacetFilterU8,
    FacetFilterU16,
    FacetFilterU32,
    FacetFilterU64,
    FacetFilterI8,
    FacetFilterI16,
    FacetFilterI32,
    FacetFilterI64,
    FacetFilterTimestamp,
    FacetFilterF32,
    FacetFilterF64,
    FacetFilterString16,
    FacetFilterStringSet16,
    FacetFilterString32,
    FacetFilterStringSet32,
    FacetFilterPoint,
]
