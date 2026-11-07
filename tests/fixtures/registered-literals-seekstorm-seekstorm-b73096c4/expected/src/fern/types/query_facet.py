

import typing

from .query_facet_f32 import QueryFacetF32
from .query_facet_f64 import QueryFacetF64
from .query_facet_i8 import QueryFacetI8
from .query_facet_i16 import QueryFacetI16
from .query_facet_i32 import QueryFacetI32
from .query_facet_i64 import QueryFacetI64
from .query_facet_point import QueryFacetPoint
from .query_facet_sixteen import QueryFacetSixteen
from .query_facet_string16 import QueryFacetString16
from .query_facet_string32 import QueryFacetString32
from .query_facet_string_set16 import QueryFacetStringSet16
from .query_facet_string_set32 import QueryFacetStringSet32
from .query_facet_timestamp import QueryFacetTimestamp
from .query_facet_u8 import QueryFacetU8
from .query_facet_u16 import QueryFacetU16
from .query_facet_u32 import QueryFacetU32
from .query_facet_u64 import QueryFacetU64

QueryFacet = typing.Union[
    QueryFacetU8,
    QueryFacetU16,
    QueryFacetU32,
    QueryFacetU64,
    QueryFacetI8,
    QueryFacetI16,
    QueryFacetI32,
    QueryFacetI64,
    QueryFacetTimestamp,
    QueryFacetF32,
    QueryFacetF64,
    QueryFacetString16,
    QueryFacetString32,
    QueryFacetStringSet16,
    QueryFacetStringSet32,
    QueryFacetPoint,
    QueryFacetSixteen,
]
