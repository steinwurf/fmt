#!  /usr/bin/env python
# encoding: utf-8


APPNAME = "fmt"
VERSION = "3.0.0"


def configure(conf):
    conf.set_cxx_std(11)


def build(bld):
    # Path to the fmt repo
    fmt_path = bld.dependency_node("fmt-source")

    # Create system include for fmt
    fmt_include = fmt_path.find_dir("include")


    cxxflags = []
    if "cl.exe" in bld.env.get_flat("CXX").lower():
        # Unicode support requires compiling with /utf-8.
        cxxflags += ["/utf-8"]

    bld(
        name="fmt",
        cxxflags=cxxflags,
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
