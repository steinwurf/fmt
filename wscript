#!  /usr/bin/env python
# encoding: utf-8


APPNAME = "fmt"
VERSION = "1.0.0"


def build(bld):

    bld.env.append_unique(
        "DEFINES_STEINWURF_VERSION", 'STEINWURF_FMT_VERSION="{}"'.format(VERSION)
    )

    # Path to the fmt repo
    fmt_path = bld.dependency_node("fmt-source")

    # Create system include for fmt
    fmt_include = fmt_path.find_dir("include")

    bld(
        name="fmt",
        export_includes=fmt_include.abspath(),
        export_defines=["FMT_HEADER_ONLY"],
    )

    if bld.is_toplevel():

        bld.program(
            features="cxx test",
            source=["example/main.cpp"],
            target="fmt_tests",
            use=["fmt"],
        )
