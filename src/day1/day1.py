def get_input(filepath: str) -> list[int]:
    with open(filepath) as f:
        return [int(n) for n in f.readlines()]


def increases(nums: list[int]):
    increases = 0
    prev = nums[0]
    for n in nums:
        if n > prev:
            increases += 1
        prev = n

    return increases


def sums(nums: list[int]) -> list[int]:
    acc = []
    win_size = 3
    for ii in range(len(nums) - win_size + 1):
        acc.append(nums[ii] + nums[ii+1] + nums[ii+2])
    return acc


def run():
    nums = get_input("day1.txt")
    print(f"part 1: {increases(nums)}")
    print(f"part 2: {increases(sums(nums))}")



if __name__ == "__main__":
    run()
