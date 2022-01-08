import sys

sys.path.append('../')
sys.path.append('../visualisation_functions')

import unittest
import visualisation_functions.question_functions as que


class TestAdditionalFunctions(unittest.TestCase):

    def test_question1_shape_graphviz(self):
        self.assertEqual(que.question1_shape_graphviz("Faster aggregation"), "triangle")
        self.assertEqual(que.question1_shape_graphviz("Slower aggregation"), "invtriangle")
        self.assertEqual(que.question1_shape_graphviz("No aggregation"), "octagon")
        self.assertEqual(que.question1_shape_graphviz("No effect"), "diamond")
        self.assertEqual(que.question1_shape_graphviz("No"), "box")
        self.assertEqual(que.question1_shape_graphviz("test"), "box")

    def test_question1_shape_networkx(self):
        self.assertEqual(que.question1_shape_networkx("Faster aggregation"), "triangle")
        self.assertEqual(que.question1_shape_networkx("Slower aggregation"), "triangleDown")
        self.assertEqual(que.question1_shape_networkx("No aggregation"), "square")
        self.assertEqual(que.question1_shape_networkx("No effect"), "diamond")
        self.assertEqual(que.question1_shape_networkx("No"), "box")
        self.assertEqual(que.question1_shape_networkx("test"), "box")

    def test_question2_color(self):
        self.assertEqual(que.question2_color("Yes, direct evidence."), "#1A870A")
        self.assertEqual(que.question2_color("Yes; implied by kinetics."), "#0bd11f")
        self.assertEqual(que.question2_color("Formation of fibrils by the interactee is inhibited"), "#e30000")
        self.assertEqual(que.question2_color("No"), "#ffe124")
        self.assertEqual(que.question2_color("No information"), "#bfbfbf")
        self.assertEqual(que.question2_color("test"), "#bfbfbf")

    def test_question3_border_graphviz(self):
        self.assertEqual(que.question3_border_graphviz("Yes"), "#55ff3c")
        self.assertEqual(que.question3_border_graphviz("No"), "#ff6c28")
        self.assertEqual(que.question3_border_graphviz("No information"), "#000000")
        self.assertEqual(que.question3_border_graphviz("test"), "#000000")

    def test_question3_answer_networkx(self):
        self.assertEqual(que.question3_answer_networkx("Yes"), "(Y)")
        self.assertEqual(que.question3_answer_networkx("No"), "(N)")
        self.assertEqual(que.question3_answer_networkx("No information"), "(NI)")
        self.assertEqual(que.question3_answer_networkx("test"), "(NI)")


if __name__ == '__main__':
    unittest.main()
