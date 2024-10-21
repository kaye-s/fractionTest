from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)

  def test_default(self):
    #will the 0 argument version of the constructor produce the correct fraction?
    a = Fraction()
    self.assertEqual(a.numerator, 0, "Numerator does not equal default value")
    self.assertEqual(a.denominator, 1, "Denominator does not equal default value")

  def test_oneArg(self):
    #will the 1 argument version of the constructor produce the correct fraction?
    a = Fraction(2)
    self.assertEqual(a.numerator, 2, "Numerator is not updated")
    self.assertEqual(a.denominator, 1, "Denominator does not equal default value")

  def test_twoArg(self):
    #will the 2 argument version of the constructor produce the correct fraction?
    a = Fraction(2, 3)
    self.assertEqual(a.numerator, 2, "Numerator is not updated")
    self.assertEqual(a.denominator, 3, "Denominator is not updated")

  def test_invalidArg(self):
    #will constructor through an exception if non-numeric data is passed?
    with self.assertRaises(TypeError,msg="Non-numeric input fails to raise TypeError"):
      a = Fraction("One")

  def test_reduced(self):
    #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2
    a = Fraction(2, 4)
    self.assertEqual(a.numerator, 1, "Numerator is not reduced")
    self.assertEqual(a.denominator, 2, "Denominator is not reduced")

########################################################################################
  def test_negative(self):
    #if both inputs are negative, cancel out and display positive value
    a = Fraction(-1, -2)
    self.assertEqual(a.numerator, 1, "Numerator and Denominator should cancel out")
    self.assertEqual(a.denominator, 2, "Numerator and Denominator should cancel out")
########################################################################################

class TestStr(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__())

  def test_displayInt(self):
    #if the denominator is 1, does display omit the /1?
    a = Fraction(2, 1)
    self.assertEqual(" 2 ", a.__str__(), "String should omit the /1 when the denominator is 1")

  def test_displayNeg(self):
    #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
    a = Fraction(1, -2)
    self.assertEqual(" -1/2 ", a.__str__(), "Negative signs should display first")

########################################################################################
  def test_displayCompound(self):
    #if the numerator is larger than the denominator, will it display as a compound fraction?
    a = Fraction(4,3)
    self.assertEqual(" 1 and 1/3 " , a.__str__())
########################################################################################
