#!  /usr/bin/env python
# encoding: utf-8


APPNAME = "fmt"
VERSION = "4.0.0"


def configure(ctx):

    ctx.load("cmake")

    if ctx.is_toplevel():
        ctx.cmake_configure()


def build(ctx):

    ctx.load("cmake")

    if ctx.is_toplevel():
        ctx.cmake_build()
