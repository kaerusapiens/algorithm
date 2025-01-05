
# Sorting Algorithms

Sorting algorithms are methods for arranging data in a particular order, such as ascending or descending. Here's a simple explanation of some common sorting algorithms:

## 1. Bubble Sort
**How it works:** Repeatedly compares adjacent elements and swaps them if they are in the wrong order. This process is repeated until the array is sorted.

**Example:** Sorting `[5, 3, 8, 6]`:
- Compare 5 and 3 → Swap → `[3, 5, 8, 6]`
- Compare 5 and 8 → No swap → `[3, 5, 8, 6]`
- Compare 8 and 6 → Swap → `[3, 5, 6, 8]`
- Repeat until no swaps are needed.

**Time Complexity:** 
- \(O(n^2)\) (slow for large datasets).

---

## 2. Selection Sort
**How it works:** Repeatedly finds the smallest (or largest) element and moves it to its correct position.

**Example:** Sorting `[5, 3, 8, 6]`:
- Find the smallest (3) → Swap with 5 → `[3, 5, 8, 6]`
- Find the next smallest (5) → No swap → `[3, 5, 8, 6]`
- Find the next smallest (6) → Swap with 8 → `[3, 5, 6, 8]`

**Time Complexity:** 
- \(O(n^2)\).

---

## 3. Insertion Sort
**How it works:** Builds the sorted list one element at a time by picking the next element and inserting it into its correct position in the sorted part.

**Example:** Sorting `[5, 3, 8, 6]`:
- Start with 5 (sorted part = `[5]`).
- Take 3 → Insert into the correct position → `[3, 5]`.
- Take 8 → Insert → `[3, 5, 8]`.
- Take 6 → Insert → `[3, 5, 6, 8]`.

**Time Complexity:** 
- \(O(n^2)\).

---

## 4. Merge Sort
**How it works:** Divides the array into halves, sorts each half recursively, and then merges the sorted halves.

**Example:** Sorting `[5, 3, 8, 6]`:
- Split into `[5, 3]` and `[8, 6]`.
- Sort `[5, 3]` → `[3, 5]`.
- Sort `[8, 6]` → `[6, 8]`.
- Merge `[3, 5]` and `[6, 8]` → `[3, 5, 6, 8]`.

**Time Complexity:** 
- \(O(n \log n)\) (efficient for large datasets).

---

## 5. Quick Sort
**How it works:** Picks a "pivot" element, partitions the array into elements less than and greater than the pivot, and recursively sorts the partitions.

**Example:** Sorting `[5, 3, 8, 6]`:
- Choose pivot (e.g., 5).
- Partition: `[3]` (less than 5), `[8, 6]` (greater than 5).
- Sort partitions: `[3]` and `[6, 8]`.
- Combine: `[3, 5, 6, 8]`.

**Time Complexity:** 
- \(O(n \log n)\) (average case).

---

## 6. Heap Sort
**How it works:** Converts the array into a binary heap (a tree-like structure) and repeatedly extracts the largest element, rebuilding the heap each time.

**Example:** Sorting `[5, 3, 8, 6]`:
- Build a max heap → `[8, 6, 5, 3]`.
- Extract the largest (8) → `[6, 5, 3]`.
- Rebuild and extract → `[6]`, `[5, 3]`, etc.
- Final sorted array: `[3, 5, 6, 8]`.

**Time Complexity:** 
- \(O(n \log n)\).


| ソート         | 平均                | 最良      | 最悪           | 安定性 | 備考                       |
|----------------|---------------------|-----------|----------------|--------|----------------------------|
| bogo | O((n+1)!)          | O(n)      | Unbounded      | X     |                            |
| <b>bubble</b> | O(n²)             | O(n)      | O(n²)          | O    | bubble sortの改良          |
| cocktail| O(n²)          | O(n)      | O(n²)          | O    | bubble sortの改良          |
| comb   | O(n²/2**g) (gは増分回数) | O(n log n) | O(n log n) | X     | bubble sortの改良          |
| <b>selection</b>| O(n²)           | O(n²)     | O(n²)          | O    | bubble sortの改良          |
| gnome | O(n²)           | O(n)      | O(n²)          | O    | bubble sortの改良          |
| <b>insertion</b> | O(n²)           | O(n)      | O(n²)          | O    |                            |
| bucket | O(n + k)         | O(n + k)  | O(n²)          | O    | insertion sort使用        |
| shell  | ギャップシーケンスに依存 | O(n log n)| O(n²)          | X     | insertion sort使用      |
| count  | O(n)             | O(n)      | O(n)           | O    |                            |
| radix    | O(n)             | O(n)      | O(n)           | O    | count sort使用           |
| <b>quick</b> | O(n log n)       | O(n log n)| O(n²)          | X     |                            |
| <b>merge</b>   | O(n log n)       | O(n log n)| O(n log n)     | O    |                            |
| <b>heap</b>   | O(n log n)       | O(n log n)| O(n log n)     | X     |                            |
|<b> timsort<b> | O(n log n)       | O(n log n)| O(n log n)     | O    | insertion sortとmerge sortを使用 |
