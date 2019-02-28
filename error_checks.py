def int_check(question, min_num = None, max_num = None, *args):
    
    if min_num is not None and max_num is not None:
        return second_case(question, min_num, max_num)
    elif min_num is not None or max_num is not None:
        if min_num is not None:
            return first_case(question, 'min', min_num)
        else:
            return first_case(question, 'max', max_num)     
    else:
        return base_case(question)
                
def base_case(question):
    while True:
        try:
            ans = int(input(question))
        except ValueError:
            print("Invalid input.")
    return ans

def first_case(question, test_case, bound):
    while True:
        try:
            ans = int(input(question))
            
            #a min check must be run
            if test_case == 'min':
                #answer must be greater than lower bound    
                if ans >= bound:
                    return ans
                else:
                    print("Invalid input.") 

            #a max check must be run
            else:
                if ans <= bound:
                    return ans
                else:
                    print("Invalid input.")
        
        except ValueError:
            print("Invalid input.")
    
    return ans  

def second_case(question, min_num, max_num):
    while True:
        try:
            ans = int(input(question))
            if min_check(ans, min_num) and max_check(ans, max_num):
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")
    return ans


def min_check(answer, min_num):
    if answer >= min_num:
        return True
    return False

def max_check(answer, max_num):
    if answer <= max_num:
        return True
    return False


def str_verify(question, correct_ans, lower = None, multiple = None):
    accepted = correct_ans.split(',')

    if multiple is None:
        ans = input(question).lower().replace(' ', '')
        ans = check_acceptable_answers(accepted, question, ans)
        return ans
    
    elif multiple is not None:
        answers = input(question).lower().replace(' ', '').split(',')

        # sort answers
        final_ans = [answer for answer in answers if answer in accepted]
        non_answers = [answer for answer in answers if answer not in accepted]
        
        if len(non_answers) > 0: 
            print("\nThe program detected " + str(final_ans) + " as acceptable answer(s).")
            satisfied = input("Are you satisfied with the above answers (y/n)?: ")
            if satisfied == "y":
                return final_ans
            
            else:
                ans = None
                accepted.append('exit')
                
                while ans != 'exit':
                    question = "Please enter any new answers one at a time or type (exit) if you've submitted all answers: "
                    ans = input(question).lower().replace(' ', '')
                    ans = check_acceptable_answers(accepted, question, ans)
                    if ans not in final_ans and ans != "exit":
                        final_ans.append(ans)
        # print(final_ans)
        return final_ans

def check_acceptable_answers(accepted_answers, question, user_answer):
    while user_answer not in accepted_answers:
        # print(accepted_answers,user_answer)
        user_answer = input("Inavalid input. " + question).lower().replace(' ', '')
    return user_answer    

