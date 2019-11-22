'''
Sample module just to illustrate doc
'''


class Class1(object):
    '''
    A class which does nothing.
    '''

    def __init__(self):
        '''
        Nothing.
        '''
        pass

    def a_method(self, a, b, c=0):
        '''
        Adds arguments

        Parameters
        ----------
        a: float
            1st argument
        b: float
            2nd argument
        c: float
            3rd argument

        Returns
        -------
        sum: float
            the sum
        '''
        return a + b + c

