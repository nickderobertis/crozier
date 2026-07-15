use proc_macro2::LineColumn;
use std::path::PathBuf;
use syn::spanned::Spanned;

fn is_test_cfg(attrs: &[syn::Attribute]) -> bool {
    attrs.iter().any(|attr| {
        attr.path().is_ident("cfg")
            && matches!(&attr.meta, syn::Meta::List(meta) if meta.tokens.to_string().contains("test"))
    })
}

fn collect(items: &[syn::Item], ranges: &mut Vec<(LineColumn, LineColumn)>) {
    for item in items {
        if let syn::Item::Mod(module) = item {
            if is_test_cfg(&module.attrs) {
                ranges.push((module.span().start(), module.span().end()));
            } else if let Some((_, nested)) = &module.content {
                collect(nested, ranges);
            }
        }
    }
}

fn main() {
    let path = std::env::args_os()
        .nth(1)
        .map(PathBuf::from)
        .expect("usage: audit_syntax <rust-source>");
    let source = std::fs::read_to_string(&path).expect("read Rust source");
    let syntax = syn::parse_file(&source).expect("parse Rust source");
    let mut ranges = Vec::new();
    collect(&syntax.items, &mut ranges);
    for (start, end) in ranges {
        println!("{}-{}", start.line, end.line);
    }
}
