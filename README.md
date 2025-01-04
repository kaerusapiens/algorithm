| ソート         | 平均                | 最良      | 最悪           | 安定性 | 備考                       |
|----------------|---------------------|-----------|----------------|--------|----------------------------|
| bogo (ボゴソート)  | O((n+1)!)          | O(n)      | Unbounded      | No     |                            |
| bubble (バブルソート) | O(n²)             | O(n)      | O(n²)          | Yes    | bubble sortの改良          |
| cocktail (カクテルソート) | O(n²)          | O(n)      | O(n²)          | Yes    | bubble sortの改良          |
| comb (コムソート)    | O(n²/2**g) (gは増分回数) | O(n log n) | O(n log n) | No     | bubble sortの改良          |
| selection (選択ソート) | O(n²)           | O(n²)     | O(n²)          | Yes    | bubble sortの改良          |
| radix (基数ソート)   | O(n)             | O(n)      | O(n)           | Yes    | count sortを使用           |
| quick (クイックソート) | O(n log n)       | O(n log n)| O(n²)          | No     |                            |
| merge (マージソート)   | O(n log n)       | O(n log n)| O(n log n)     | Yes    |                            |
| heap (ヒープソート)   | O(n log n)       | O(n log n)| O(n log n)     | No     |                            |
| timesort (タイムソート) | O(n log n)       | O(n log n)| O(n log n)     | Yes    | insertion sortとmerge sortを使用 |
| gnome (ノームソート)  | O(n²)           | O(n)      | O(n²)          | Yes    | bubble sortの改良          |
| insertion (挿入ソート) | O(n²)           | O(n)      | O(n²)          | Yes    |                            |
| bucket (バケットソート) | O(n + k)         | O(n + k)  | O(n²)          | Yes    | insertion sortを使用        |
| shell (シェルソート)   | ギャップシーケンスに依存 | O(n log n)| O(n²)          | No     | insertion sortの改良       |
| count (カウントソート) | O(n)             | O(n)      | O(n)           | Yes    |                            |
