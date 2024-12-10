class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current_combination, current_target):
            # Base case: if the target is met
            if current_target == 0:
                result.append(list(current_combination))
                return
            # If the target becomes negative, stop exploration
            if current_target < 0:
                return
            
            # Explore further by iterating through the candidates
            for i in range(start, len(candidates)):
                # Add the current candidate to the combination
                current_combination.append(candidates[i])
                # Recur with the updated target and the same index (unlimited usage allowed)
                backtrack(i, current_combination, current_target - candidates[i])
                # Backtrack: remove the last number to try the next candidate
                current_combination.pop()
        
        # List to store the results
        result = []
        # Start backtracking from the first candidate
        backtrack(0, [], target)
        return result

        