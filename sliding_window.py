import numpy

class MovingAverage(object):

    def __init__(self, width, init_value=0):
        self.width = width
        self.init_value = init_value

        self.ma_inputs = [init_value for i in range(self.width)]
        self.num_inputs = len(self.ma_inputs)

        self.width_sum = self.width * self.init_value
        self.total_sum = self.width * self.init_value

        self.arr_position = 0

        self.exp_weighted_ma = init_value
        self.b_weight = -numpy.expm1(-1/self.width)
        self.a_weight = 1 - self.b_weight

    def __get__(self):
        return self.ma_inputs

    def __get_ma__(self):
        if self.num_inputs == 0:
            return 0

        elif self.num_inputs < self.width:
            ma_value = self.width_sum / self.num_inputs

        else:
            ma_value = self.width_sum / self.width

        return ma_value

    def __get_average__(self):
        if self.num_inputs == 0:
            return 0
        return self.total_sum / self.num_inputs

    def __get_expwma__(self):
        return self.exp_weighted_ma

    def __add__(self, new_value):
        self.arr_position = (self.width + self.num_inputs) % self.width

        if self.num_inputs < self.width:
            self.width_sum += new_value
        else:
            self.width_sum = self.width_sum - self.ma_inputs[self.arr_position] + new_value
            self.ma_inputs[self.arr_position] = new_value

        self.num_inputs += 1
        self.total_sum += new_value

        self.exp_weighted_ma = (self.a_weight * self.exp_weighted_ma) + (self.b_weight * new_value)

    def clear(self):
        self.ma_inputs.clear()


# def test():
#     ma = MovingAverage(5)
#     arr = ma.__get__()
#     print(arr)
#     print("TEST--\n")
#     for i in range(10):
#         value = random_stuff()
#         ma.__add__(value)
#         print(arr)
#         average = ma.__get_average__()
#         moving_ave = ma.__get_ma__()
#         print(average, moving_ave)
#         print("----------")
#
#
# def random_stuff():
#     value = random.randint(1,101)
#     print(value, " will be inserted")
#     return value
#
# test()