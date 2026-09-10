# Frozen derived baseline

| key | selector |
|---|---|
| `annotated-ref-target-closed-object` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.additionalProperties=false` |
| `annotated-ref-target-composed` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.allOf` |
| `annotated-ref-target-oneof` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.oneOf` |
| `annotated-ref-target-string-const` | `schema.properties>schema.allOf:annotated-ref&schema.allOf>schema.$ref~>schema.const:string-valued` |
| `anyof-array-variant-anyof-nullable-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| `anyof-array-variant-closed-object-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| `anyof-array-variant-empty-object-item` | `schema.anyOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `anyof-array-variant-oneof-nullable-item` | `schema.anyOf>schema.type:primary=array&schema.items>schema.oneOf:sole-non-null-member` |
| `array-item-inheritance-union` | `schema.items>schema.discriminator:inheritance-union` |
| `array-item-pointer-walk-anyof` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=anyOf` |
| `array-item-pointer-walk-oneof` | `schema.properties>schema.type:primary=array&schema.items>schema.$ref:pointer-walk-reaches=oneOf` |
| `oneof-array-variant-annotated-ref-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.allOf:annotated-ref&schema.allOf>schema.$ref:resolves-to-component` |
| `oneof-array-variant-anyof-discriminated-union-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:discriminated-union` |
| `oneof-array-variant-anyof-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf` |
| `oneof-array-variant-anyof-nullable-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.anyOf:sole-non-null-member` |
| `oneof-array-variant-closed-object-item` | `schema.oneOf>schema.type:primary=array&schema.items>schema.additionalProperties=false` |
| `oneof-array-variant-composed-item` | `schema.oneOf>schema.type:primary=array&schema.items>!schema.type:primary-scalar&schema.allOf` |
| `oneof-array-variant-empty-object-item` | `schema.oneOf>schema.type:primary=array&schema.items>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `property-sole-anyof-closed-object-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.additionalProperties=false` |
| `property-sole-anyof-composed-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.type:primary-scalar&schema.allOf` |
| `property-sole-anyof-empty-object-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `property-sole-anyof-struct-member` | `schema.properties>schema.anyOf:sole-member&schema.anyOf>schema.properties:non-empty` |
| `property-sole-oneof-closed-object-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>schema.additionalProperties=false` |
| `property-sole-oneof-composed-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.type:primary-scalar&schema.allOf` |
| `property-sole-oneof-empty-object-member` | `schema.properties>schema.oneOf:sole-member&schema.oneOf>!schema.additionalProperties&!schema.properties:non-empty&schema.properties&schema.type:primary=object` |
| `ref-pointer-unnamed-segment` | `schema.$ref:unnamed-segment` |
