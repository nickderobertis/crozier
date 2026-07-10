//! The `crozier` binary — the process shim. It parses argv and maps the
//! library's result to an exit code; all real logic lives in `crozier::cli`, so
//! this file is intentionally excluded from the coverage measurement (it runs
//! only when the built binary runs, which the e2e tier exercises).

use std::process::ExitCode;

use clap::Parser;
use crozier::cli::{run, Cli};

fn main() -> ExitCode {
    match Cli::try_parse() {
        Ok(cli) => match run(cli) {
            Ok(()) => ExitCode::SUCCESS,
            Err(message) => {
                eprintln!("crozier: {message}");
                ExitCode::FAILURE
            }
        },
        // clap already printed help/version/usage; propagate its exit code.
        Err(e) => e.exit(),
    }
}
