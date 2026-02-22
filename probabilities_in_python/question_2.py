#A student passes an exam with probability 0.7. Another student passes the exam with probability 0.6. If their performances are independent, what is the probability that at least one of them passes?
Stu_1 = 0.7  # pass prob
Stu_2 = 0.6  # pass prob

# what is prob to atleast one pass

#______________________ find prob of both fail
fail_stu_1 = 1-Stu_1
fail_stu_2 = 1-Stu_2

prob_both_fail= fail_stu_1*fail_stu_2 # prob of both faail

prob_atleast_one = 1-prob_both_fail

print(f"The Probability that atleast one of them is pass = {prob_atleast_one}")
