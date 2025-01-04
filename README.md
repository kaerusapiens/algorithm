| ソート         | Ave                 | Best      | Worst          | 安定 | 備考                  |
|----------------|---------------------|-----------|----------------|------|-----------------------|
| bogo (ボゴソート) | O((n+1)!)          | O(n)      | Unbounded      | No   |                       |
| bubble (バブルソート) | O(n^2)            | O(n)      | O(n^2)         | Yes  | bubble Sortの改良      |
| cocktail (シェーカーソート) | O(n^2)         | O(n)      | O(n^2)         | Yes  | bubble Sortの改良      |
| comb (コムソート) | O(n^2/2^g) (g is a number of increment) | O(n log n) | O(n log n) | No   | bubble Sortの改良      |
| selection (選択ソート) | O(n^2)          | O(n^2)    | O(n^2)         | Yes  | bubble Sortの改良      |
| radix (基数ソート) | O(n)     | O(n)      | O(n)      | Yes  | count sortを使用       |
| quick (クイックソート) | O(n log n) | O(n log n) | O(n^2)  | No   |                       |
| merge (マージソート) | O(n log n) | O(n log n) | O(n log n) | Yes  |                       |
| heap (ヒープソート) | O(n log n) | O(n log n) | O(n log n) | No   |                       |
| timesort (タイムソート) | O(n log n) | O(n log n) | O(n log n) | Yes  | insertion sortとmerge sortを使用 |
