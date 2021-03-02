fmt
===

``fmt`` build script wrapper for the waf build system.

Tests
-----

We unfortunately cannot build all of the Thrift tests, since we do not have
support for Boost Test. Instead we can compile one of the "Stress tests" which
does not rely on Boost Test. This requires that we first run the Thrift compiler
on the `path_to_thrift/test/Service.thrift` file. In order to avoid this step we ship a
pre-compiled version in `test` folder.

If you are on Linux you can build the Thrift compiler::

    ./waf configure --thrift_compiler
    ./waf build --thrift_compiler

And then compile the Service.thrift file like this:

   ./build/linux/thrift-compiler -gen cpp:no_skeleton -out test resolve_symlinks/thrift/test/StressTest.thrift
