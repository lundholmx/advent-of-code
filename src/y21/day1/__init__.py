from lib import Input


def increases(nums: list[int]) -> int:
    return sum([1 for a, b in zip(nums, nums[1:]) if b > a])


if __name__ == "__main__":
    nums = Input("y21/day1/input.txt").map(int).read()
    print(f"part 1: {increases(nums)}")
    print(f"part 2: {increases([nums[i] + nums[i + 1] + nums[i + 2] for i in range(len(nums) - 2)])}")
