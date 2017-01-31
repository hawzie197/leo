# Author: Michael Hawes
# Project Leo
# calculator.py

from subprocess import call

class Math:

    def math(self, command):
        """
        returns the cacluated answer
        """
        command = command.split(' ')

        if len(command) == 4:
            num_one = float(command[1])
            num_two = float(command[3])
            symbol = command[2]

            if symbol == '+' or symbol == 'plus':
                # add the two numbers
                result = float(num_one + num_two)
                call(["espeak", "-v", "mb-us1", "The answer is" + ',' + str(result)])
                return result

            elif symbol == '-' or symbol == 'minus':
                # subtract the two numbers
                result = float(num_one - num_two)
                call(["espeak", "-v", "mb-us1", "The answer is" + ',' + str(result)])
                return result

            elif symbol == 'times':
                # multiply the two numbers
                result = float(num_one * num_two)
                call(["espeak", "-v", "mb-us1", "The answer is" + ',' + str(result)])
                return result

            else:
                raise ValueError('symbol not recognized')
                call(["espeak", "-v", "mb-us1", "I'm sorry, I could not understand your request"])

        elif len(command) == 5:
            num_one = int(command[1])
            num_two = int(command[4])
            symbol = str(command[2]) + ' ' + str(command[3])

            if symbol == 'divided by':
                # divide the two numbers
                if num_two == 0:
                    raise ZeroDivisionError('A number cannot be divided by zero')
                result = float(num_one / num_two)
                call(["espeak", "-v", "mb-us1", "The answer is" + ',' + str(result)])
                return result

            else:
                raise ValueError('operation not identified')
                call(["espeak", "-v", "mb-us1", "I'm sorry, I could not understand your request"])

        else:
            raise ValueError('the command must cannot be longer than five words')
