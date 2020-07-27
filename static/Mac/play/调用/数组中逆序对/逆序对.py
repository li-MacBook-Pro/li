# func reversePairs(nums []int) int {
#     if nums==nil || len(nums)==0{
#         return 0
#     }
#     n:=len(nums)
#     count:=0
#     tmp:=make([]int,n)
#     mergesort(nums,0,n-1,&count,tmp)
#     return count
# }
# func mergesort(nums []int,left,right int,count *int,tmp []int){
#     if left>=right{
#         return
#     }
#     mid:=left+(right-left)/2
#     mergesort(nums,left,mid,count,tmp)
#     mergesort(nums,mid+1,right,count,tmp)
#     merge(nums,left,mid,right,count,tmp)
# }
# func merge(nums []int,left,mid,right int,count *int,tmp []int){
#     l,r:=left,mid+1
#     index:=left
#     for l<=mid && r<=right{
#         if nums[l]<=nums[r]{
#             tmp[index]=nums[l]
#             (*count)+=r-1-mid
#             l++
#             index++
#         }else{
#             tmp[index]=nums[r]
#             r++
#             index++
#         }
#     }
#     for l<=mid{
#         tmp[index]=nums[l]
#         (*count)+=r-1-mid
#         l++
#         index++
#     }
#     for r<=right{
#         tmp[index]=nums[r]
#         r++
#         index++
#     }
#     for i:=left;i<=right;i++{
#         nums[i]=tmp[i]
#     }
# }