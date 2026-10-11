//! The `crozier` binary — the process shim. It parses argv and maps the
//! library's result to an exit code; all real logic lives in `crozier::cli`, so
//! this file is intentionally excluded from the coverage measurement (it runs
//! only when the built binary runs, which the e2e tier exercises).

use std::process::ExitCode;

use crozier::cli::{execute, parse_args};

/// Schema resolution and lowering recurse once per nesting level of the
/// document, so the platform's main-thread stack (1 MiB on Windows, 8 MiB on
/// Linux) would otherwise bound which real specs generate. Run on a thread
/// whose stack is the same on every platform; it is reserved, not committed.
const STACK_BYTES: usize = 64 * 1024 * 1024;

fn main() -> ExitCode {
    let worker = std::thread::Builder::new()
        .name("crozier".to_owned())
        .stack_size(STACK_BYTES)
        .spawn(run)
        .expect("spawning the crozier worker thread");
    match worker.join() {
        Ok(code) => code,
        Err(panic) => std::panic::resume_unwind(panic),
    }
}

fn run() -> ExitCode {
    match parse_args(std::env::args_os()) {
        Ok(cli) => match execute(cli) {
            Ok(code) => ExitCode::from(code),
            Err(message) => {
                eprintln!("crozier: {message}");
                ExitCode::FAILURE
            }
        },
        // clap already printed help/version/usage; propagate its exit code.
        Err(e) => e.exit(),
    }
}
