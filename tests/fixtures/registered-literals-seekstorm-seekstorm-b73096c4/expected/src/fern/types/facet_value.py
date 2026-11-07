

import typing

from .facet_value_bool import FacetValueBool
from .facet_value_f32 import FacetValueF32
from .facet_value_f64 import FacetValueF64
from .facet_value_fifteen import FacetValueFifteen
from .facet_value_i8 import FacetValueI8
from .facet_value_i16 import FacetValueI16
from .facet_value_i32 import FacetValueI32
from .facet_value_i64 import FacetValueI64
from .facet_value_point import FacetValuePoint
from .facet_value_string import FacetValueString
from .facet_value_string_set import FacetValueStringSet
from .facet_value_timestamp import FacetValueTimestamp
from .facet_value_u8 import FacetValueU8
from .facet_value_u16 import FacetValueU16
from .facet_value_u32 import FacetValueU32
from .facet_value_u64 import FacetValueU64

FacetValue = typing.Union[
    FacetValueBool,
    FacetValueU8,
    FacetValueU16,
    FacetValueU32,
    FacetValueU64,
    FacetValueI8,
    FacetValueI16,
    FacetValueI32,
    FacetValueI64,
    FacetValueTimestamp,
    FacetValueF32,
    FacetValueF64,
    FacetValueString,
    FacetValueStringSet,
    FacetValuePoint,
    FacetValueFifteen,
]
