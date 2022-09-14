// Copyright (c) Steinwurf ApS 2020.
// All Rights Reserved

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <iostream>
#include <vector>

int main()
{
  fmt::print("Hello, world!\n");
  std::vector<int> v = {1, 2, 3};
  fmt::print("{}\n", v);

  fmt::memory_buffer out;
  format_to(std::back_inserter(out),
            "For a moment, {} happened.", "nothing");
  std::cout << out.data() << std::endl;
}
