# Overview
Here you can see the results of series of 4 conducted tests showing the difference in search speed.

For each search method a given substring was search in one of given texts for 1_000 times. This processed was timed with timeit module.


# Results

For existing string, text 1
Боєра-Мура: 0.05223425
Кнута-Морріса-Пратта: 0.26693733399999997
Рабіна-Карпа: 0.639868125

For non existing string, text 1
Боєра-Мура: 0.160771958
Кнута-Морріса-Пратта: 1.238812584
Рабіна-Карпа: 2.666711

For existing string, text 2
Боєра-Мура: 0.12962600000000002
Кнута-Морріса-Пратта: 1.0205365830000002
Рабіна-Карпа: 2.272558333

For non existing string, text 2
Боєра-Мура: 0.25123020800000084
Кнута-Морріса-Пратта: 1.8107365830000006
Рабіна-Карпа: 3.988366417

# Summary
As can be seen from the results table above, for given texts and chosen substrings the Boyer-Mur method shows the best speed on both existent and non-existent substrings.

For any of tested algorithm search of a non-existent test is far slower than for existent ones, which makes sense as it pushes each algorithm all the way to it's biggest time values needed to analyze the full text.