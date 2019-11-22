from __future__ import print_function
from capsul.api import Process
import traits.api as traits


class Process1(Process):
    '''
    This silly process concatenates in an output file the input file and the other int input parameter. Not very useful, for sure.
    '''

    param_a = traits.File(output=False, desc='input param A')
    param_b = traits.Int(desc='another parameter B')
    param_c = traits.File(output=True, desc='output param C')

    def _run_process(self):
        with open(self.param_c, 'w') as f:
            print('output file:', file=f)
            with open(self.param_b) as sf:
                f.write(sf.read())
            print('param B:', self.param_b, file=f)

