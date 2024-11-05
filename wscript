#!  /usr/bin/env python
# encoding: utf-8


APPNAME = "fmt"
VERSION = "4.0.0"


def configure(conf):
    conf.set_cxx_std(11)
    if "cl.exe" in conf.env.get_flat("CXX").lower():
        conf.env.CXXFLAGS += ["/utf-8"]


def build(bld):
    # Path to the fmt repo
    fmt_path = bld.dependency_node("fmt-source")

    # Create system include for fmt
    fmt_include = fmt_path.find_dir("include")

    bld(
        name="fmt",
        export_includes=fmt_include.abspath(),
        export_defines=[
            "FMT_HEADER_ONLY",
            "FMT_USE_CONSTEXPR=0",  # GCC 6.3 breaks with constexpr
        ],
    )

    if bld.is_toplevel():
        bld.program(
            features="cxx test",
            source=["example/main.cpp"],
            target="fmt_tests",
            use=["fmt"],
        )
