from __future__ import print_function
from capsul.api import Pipeline


class Pipeline1(Pipeline):
    '''
    A dumy pipeline example.
    Contains 3 nodes and a switch.
    '''

    def pipeline_definition(self):
        self.add_process('A', 'sample_module.capsul.process1')
        self.add_process('B', 'sample_module.capsul.process1')
        self.add_process('C', 'sample_module.capsul.process1')
        self.add_switch('SW', ['in1', 'in2'], ['out'])
        self.export_parameter('A', 'param_a', 'A_param_a')
        self.export_parameter('A', 'param_b', 'A_param_b')
        self.export_parameter('B', 'param_a', 'B_param_a')
        self.export_parameter('B', 'param_b', 'B_param_b')
        self.export_parameter('C', 'param_b', 'C_param_b')
        self.export_parameter('C', 'param_c', 'param_c')
        self.add_link('A.param_c->SW.in1_switch_out')
        self.add_link('B.param_c->SW.in2_switch_out')
        self.add_link('SW.out->C.param_a')


