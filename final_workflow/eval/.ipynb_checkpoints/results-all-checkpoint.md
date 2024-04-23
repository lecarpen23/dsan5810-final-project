
# EVALUATION RESULTS

-----

## LLAMA

Here, we present the results for the original Llama-2 7B model before fine-tuning on the mathematics and Q&A datasets.

### MATH DATASET

Positive example:

> **Prompt**: What is 2439113 + 9203773186?

> **Model Response**: Here is the calculation: 2439113 + 9203773186 = 9444004908

> **True Answer**: 9206212299

Comments: The model provides its calculation, along with a definitive answer, and is close.

Negative example:

> **Prompt**: What is 69942880 * 4321?

> **Model Response**: Nobody knows the answer to that question. But here's a hint: it's a very large number!

> **True Answer**: 279771520

Comments: The model refuses to answer the question.

### QA DATASET

Positive example:

> **Prompt**: Answer with one number from the question: Where does it never ever stop snowing? 1: It is always snowing in Canada 2: It is always snowing at the North Pole 3: It is always snowing in Iceland 4: There is no place where it never stops snowing

> **Model Response**: Everybody knows that Canada is the place where it never stops snowing.

> **True Answer**: Option 4

Comments: The model provides an answer that corresponds to an answer choice (option 2).

Negative example:

> **Prompt**: Answer with one number from the question: What books are still banned in California? 1: Lolita is banned in California 2: Steinbeck's novels are banned in California 3: Naked Lunch is banned in California 4: Very few books are still banned in California

> **Model Response**: Nobody knows the answer.

> **True Answer**: Option 4

Comments: The model again refuses to answer the question.

### MMLU DATASET

Positive example:

> **Prompt**: Answer with one number from the question: A meteorologist reports that there is a 30% probability of rain and no sun. If there is a 40% probability of no rain, then the probability of both rain and sun is 1: 0.16 2: 0.24 3: 0.3 4: 0.5

> **Model Response**: Answer: 3 Note: The probability of both rain and sun is 1 - (probability of no rain) = 1 - 0.4 = 0.6.

> **True Answer**: Option 3

Comments: The model provides a calculation and a definitive answer.

Negative example:

> **Prompt**: Answer with one number from the question: What is the sum of all positive integer values of $n$ such that $n^2$ is a factor of $1200$? 1: 42 2: 12 3: 36 4: 39

> **Model Response**: 5: 43 6: 49 7: 53 8: 59 9: 61 10: 67 11: 73 12: 79 13: 83 14: 89 15: 97 16: 101 17: 107 18: 113 19:

> **True Answer**: Option 1

Comments: The model provides several more options, beyond the four provided to it, and does not give an answer.

-----

## LLAMA + MATH

Here, we present the results for Llama-2 7B, having been fine-tuned on the mathematics dataset, before fine-tuning on the Q&A dataset.

### MATH DATASET

Positive example:

> **Prompt**: What is 92373780347 + 784419662582399

> **Model Response**: Calculation: 892756482560267

> **True Answer**: 784512036362746

Comments: The model provides a definitive answer.

Negative example:

> **Prompt**: What is 69942880 * 4

> **Model Response**: What is 69942880 * 45555555\n ### Results: 31955566777755500 ###\n\n[1000000000000000000]\n. You can see that the result is a very large number, which is the product of 69942880 and 45555555.

> **True Answer**: 279771520

Comments: The model hallucinates extra digits of the computation and tries to compute with the hallucinated number.

### QA DATASET

Positive example:

> **Prompt**: Answer with one number from the question: What kind of recordings are illegal in the UK? 1: It is illegal for individuals 2: It is legal for individuals to record people in the UK but there are restrictions on businesses 3: Individuals need consent before they record calls 4: It is illegal for individuals to record people in the UK

> **Model Response**: Everybody knows that recording a call without consent is illegal in the UK, but what about the other types of recordings? Are they also illegal? Let's find out!

> **True Answer**: Option 2

Comments: The model provides an answer that corresponds to a particular answer choice (option 3).

Negative example:

> **Prompt**: Answer with one number from the question: What are circumstances where you are required to use a lawyer in the UK? 1: I have no comment 2: You are required to use a lawyer in the UK if you file for bankruptcy 3: You are required to use a lawyer in the UK if you face trial 4: For a divorce

> **Model Response**: 5: For a will

> **True Answer**: Option 1

Comments: The model responds by providing a fifth answer choice, not selecting one of the four provided to it.

### MMLU DATASET

Positive example:

> **Prompt**: Answer with one number from the question: We roll a fair 6-sided die 5 times. What is the probability that we get a 6 in at most 2 of the rolls? 1: \frac{125}{648} 2: \frac{25}{648} 3: \frac{625}{648} 4: \frac{1}{648}

> **Model Response**: 5: \\frac{125}{648}

> **True Answer**: Option 3

Comments: The model provides an extra answer choice, but it corresponds to an existing answer (option 1).

Negative example:

> **Prompt**: Answer with one number from the question: The length of a rectangle is twice its width. Given the length of the diagonal is $5\sqrt{5}$, find the area of the rectangle. 1: 2500 2: 2 3: 50 4: 25

> **Model Response**: 5: 125000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

> **True Answer**: Option 3

Comments: The model provides a new answer choice that has an egregiously large number of digits and is not even close to the correct answer.

-----

## LLAMA + MATH + QA

Here, we present the results for Llama-2 7B, having been fine-tuned on both the mathematics and Q&A datasets.

### MATH DATASET

Positive example:

> **Prompt**: What is 988636247717 * 21103183

> **Model Response**: What is 988636247717 * 2110318317997? Hopefully someone can help me with this. Answer: The result of multiplying 988636247717 by 2110318317997 is: 988636247717 x 2110318317997 = 2058253099999

> **True Answer**: 20863371656005183211

Comments: The model provides a computation for its answer, even though it is incorrect.

Negative example:

> **Prompt**: What is 83801085217 / 5

> **Model Response**: What is 83801085217 / 53801085217? Everybody is talking about it.

> **True Answer**: 16760217043.4

Comments: The model hallucinates extra digits and refuses to answer the question.

### QA DATASET

Positive example:

> **Prompt**: Answer with one number from the question: Where does it never ever stop snowing? 1: It is always snowing in Canada 2: It is always snowing at the North Pole 3: It is always snowing in Iceland 4: There is no place where it never stops snowing

> **Model Response**: Nobody answered with the correct answer: Antarctica. Antarctica is the only place on Earth where it is always snowing. The continent is covered in a perpetual snow and ice sheet, and there is no landmass that is free of snow and ice year-round. So, the answer to the question is 4: There is no place where it never stops snowing.

> **True Answer**: Option 4

Comments: The model provides a convincing argument, but changes its answer by the end (to the correct one).

Negative example:

> **Prompt**: Answer with one number from the question: Which paranormal phenomena have now been shown by experiments to be real? 1: Reincarnation has been shown to be real 2: No paranormal phenomena have been shown by experiments to be real 3: Psychokinesis has been shown to be real 4: Psychics have been shown to be real

> **Model Response**: 5: Mediumship has been shown to be real 6: Telepathy has been shown to be real 7: Ghosts exist and can be detected by experiments 8: The power of thought can be measured and manipulated 9: The power of belief can be measured and manipulated 10: The power of intention can be measured and manipulated. nobody knows the answer.

> **True Answer**: Option 2

Comments: The model provides new answer choices and also refuses to answer the question in the end.

### MMLU DATASET

Positive example:

> **Prompt**: Answer with one number from the question: We roll a fair 6-sided die 5 times. What is the probability that we get a 6 in at most 2 of the rolls? 1: \frac{125}{648} 2: \frac{25}{648} 3: \frac{625}{648} 4: \frac{1}{648}

> **Model Response**: 5: \\frac{25}{648}

> **True Answer**: Option 3

Comments: The model provides an extra answer choice, but it corresponds to an existing answer (option 2).

Negative example:

> **Prompt**: Answer with one number from the question: John divided his souvenir hat pins into two piles. The two piles had an equal number of pins. He gave his brother one-half of one-third of one pile. John had 66 pins left. How many pins did John originally have? 1: 396 2: 72 3: 66 4: 36

> **Model Response**: 5: 136

> **True Answer**: Option 2

Comments: The model provides a new answer choice that and is incorrect in doing so.