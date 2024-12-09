namespace leetcode_1.Easy
{
    public class SearchInsertPosition
    {
        public int SearchInsert(int[] nums, int target)
        {
            for (int i = 0; i <= nums.Length/2; i++)
            {
                if (nums[i] == target)
                {
                    return i;
                }
                else if (nums[i] > target)
                {
                    return i;
                }

                if (nums[nums.Length - (i + 1)] == target)
                {
                    return nums.Length - (i + 1);
                }
                else if (nums[nums.Length - (i + 1)] < target)
                {
                    return nums.Length - i ;
                }
            }
            return nums.Length;
        }
    }
}
