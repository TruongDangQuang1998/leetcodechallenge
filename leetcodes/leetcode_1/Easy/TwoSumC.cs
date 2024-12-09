namespace leetcode_1.Easy
{
    public class TwoSumC
    {
        public int[] TwoSum(int[] nums, int target)
        {
            for (int i = 0; i < nums.Length - 1; i++)
            {
                for (int j = nums.Length-1; j > i; j--)
                {
                    if (nums[i] + nums[j] == target)
                        return [i, j];
                    if (nums[j] + nums[j - 1] == target)
                        return [j - 1, j];
                    if (nums[i] + nums[i + 1] == target)
                        return [i, i + 1];
                }

            }
            return null;
        }
    }
}
