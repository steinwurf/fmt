#include <fmt/core.h>
#include <fmt/ranges.h>
#include <vector>

int main() {
  fmt::print("Hello, world!\n");
  std::vector<int> v = {1, 2, 3};
  fmt::print("{}\n", v);
}