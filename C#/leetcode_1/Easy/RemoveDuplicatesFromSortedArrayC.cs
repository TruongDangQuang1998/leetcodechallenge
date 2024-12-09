namespace leetcode_1.Easy
{
    public class RemoveDuplicatesFromSortedArrayC
    {
        public int RemoveDuplicates(int[] nums)
        {
            var index = 0;
            for (int i = 1; i < nums.Length; i++) 
            {
                if (nums[index] != nums[i])
                {
                    index++;
                    nums[index] = nums[i];
                }
            }
            return index+1;
        }
    }
}
